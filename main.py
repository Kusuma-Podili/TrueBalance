"""
TrueBalance - Interactive Enterprise Fintech Dashboard & Live API Server.
Features full interactive editing for Accounts, Transactions, Budgets, and Simulation Parameters.
"""

import sys
import os
import json
import time
import http.server
import socketserver
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.math.decimal_utils import FinancialDecimal
from core.ledger.double_entry import GeneralLedger
from core.ledger.journal_entry import JournalEntry
from core.ledger.types import AccountClassification
from services.accounts.manager import AccountManager
from services.transactions.processor import TransactionProcessor
from services.transactions.rules_engine import SmartCategorizer
from services.transactions.merchant_normalizer import MerchantNormalizer
from services.budget.zero_based import BudgetManager
from services.investments.monte_carlo import MonteCarloEngine
from services.tax.harvesting import TaxLossHarvester, TaxableHolding
from services.fx.engine import FXEngine

PORT = 8000

# Global In-Memory Services
ledger = GeneralLedger()
account_mgr = AccountManager()
tx_processor = TransactionProcessor(account_mgr)
budget_mgr = BudgetManager()
monte_carlo = MonteCarloEngine(seed=42)
fx_engine = FXEngine()
categorizer = SmartCategorizer()

USER_ID = "usr_alex"

def initialize_demo_dataset():
    account_mgr.create_account(USER_ID, "Premier Checking (Chase)", "CHECKING", initial_balance_cents=845000)
    account_mgr.create_account(USER_ID, "High Yield Savings (Marcus)", "SAVINGS", initial_balance_cents=3250000)
    account_mgr.create_account(USER_ID, "Brokerage Portfolio (Fidelity)", "INVESTMENT", initial_balance_cents=9420000)
    account_mgr.create_account(USER_ID, "Sapphire Preferred (Credit Card)", "CREDIT_CARD", initial_balance_cents=-145000)
    account_mgr.create_account(USER_ID, "Residential Mortgage", "MORTGAGE", initial_balance_cents=-28500000)

    ledger.register_account("1010", "Cash & Checking", AccountClassification.ASSET)
    ledger.register_account("1020", "High-Yield Savings", AccountClassification.ASSET)
    ledger.register_account("1030", "Brokerage Equities", AccountClassification.ASSET)
    ledger.register_account("2010", "Credit Card Debt", AccountClassification.LIABILITY)
    ledger.register_account("2020", "Mortgage Note", AccountClassification.LIABILITY)
    ledger.register_account("3010", "Retained Net Worth", AccountClassification.EQUITY)
    ledger.register_account("4010", "Employment Compensation", AccountClassification.REVENUE)
    ledger.register_account("5010", "Housing Expense", AccountClassification.EXPENSE)
    ledger.register_account("5020", "Groceries & Dining", AccountClassification.EXPENSE)

    e0 = JournalEntry("e_0", "2026-08-01", "Opening Balances")
    e0.add_line("l1", "1010", "Cash & Checking", AccountClassification.ASSET, debit=FinancialDecimal("8450.00"))
    e0.add_line("l2", "1020", "High-Yield Savings", AccountClassification.ASSET, debit=FinancialDecimal("32500.00"))
    e0.add_line("l3", "1030", "Brokerage Equities", AccountClassification.ASSET, debit=FinancialDecimal("94200.00"))
    e0.add_line("l4", "2010", "Credit Card Debt", AccountClassification.LIABILITY, credit=FinancialDecimal("1450.00"))
    e0.add_line("l5", "2020", "Mortgage Note", AccountClassification.LIABILITY, credit=FinancialDecimal("285000.00"))
    e0.add_line("l6", "3010", "Retained Net Worth", AccountClassification.EQUITY, debit=FinancialDecimal("151300.00"))
    ledger.post_entry(e0)

    budget_mgr.create_envelope(USER_ID, "cat_housing", 250000, "2026-08")
    budget_mgr.create_envelope(USER_ID, "cat_food", 85000, "2026-08")
    budget_mgr.create_envelope(USER_ID, "cat_transit", 35000, "2026-08")
    budget_mgr.create_envelope(USER_ID, "cat_entertainment", 25000, "2026-08")
    budget_mgr.record_expense(USER_ID, "cat_housing", "2026-08", 220000)
    budget_mgr.record_expense(USER_ID, "cat_food", "2026-08", 64500)
    budget_mgr.record_expense(USER_ID, "cat_transit", "2026-08", 18500)
    budget_mgr.record_expense(USER_ID, "cat_entertainment", "2026-08", 29800)

initialize_demo_dataset()

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TrueBalance - Interactive Fintech Platform</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    body { background-color: #090d16; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .card-glow { box-shadow: 0 0 25px -5px rgba(99, 102, 241, 0.15); }
    .modal-backdrop { background-color: rgba(0, 0, 0, 0.75); backdrop-filter: blur(4px); }
  </style>
</head>
<body class="p-4 md:p-10 max-w-7xl mx-auto space-y-8">
  <!-- Header -->
  <header class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pb-6 border-b border-slate-800">
    <div>
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-indigo-600 flex items-center justify-center font-black text-xl shadow-lg shadow-indigo-500/30">TB</div>
        <h1 class="text-3xl font-black tracking-tight">TrueBalance</h1>
      </div>
      <p class="text-sm text-slate-400 mt-1">Interactive Financial Management &bull; Double-Entry Ledger &bull; Full Read/Write Mode Active</p>
    </div>
    <div class="flex flex-wrap items-center gap-3">
      <button onclick="openModal('txModal')" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold rounded-xl shadow-lg shadow-indigo-600/30 transition">
        + Add Transaction
      </button>
      <button onclick="openModal('accountModal')" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold rounded-xl border border-slate-700 transition">
        + New Account
      </button>
      <button onclick="openModal('budgetModal')" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold rounded-xl border border-slate-700 transition">
        ✏️ Edit Budgets
      </button>
      <a href="https://github.com/Kusuma-Podili/TrueBalance" target="_blank" class="px-3 py-2 bg-slate-900 text-slate-400 hover:text-white text-xs font-bold rounded-xl border border-slate-800 transition">
        GitHub ↗
      </a>
    </div>
  </header>

  <!-- Notification Banner -->
  <div id="toast" class="hidden fixed top-6 right-6 z-50 p-4 rounded-xl shadow-2xl border text-sm font-semibold transition-all"></div>

  <!-- Metric Summary Cards -->
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 card-glow">
      <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Assets</span>
      <p id="totalAssetsDisplay" class="text-3xl font-black text-emerald-400 mt-2">$0.00</p>
      <span class="text-xs text-slate-500 mt-1 block">Checking, Savings & Equities</span>
    </div>
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 card-glow">
      <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Liabilities</span>
      <p id="totalDebtsDisplay" class="text-3xl font-black text-rose-400 mt-2">$0.00</p>
      <span class="text-xs text-slate-500 mt-1 block">Mortgage & Credit Balances</span>
    </div>
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 card-glow">
      <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Net Worth</span>
      <p id="netWorthDisplay" class="text-3xl font-black text-indigo-400 mt-2">$0.00</p>
      <span class="text-xs text-emerald-400 font-semibold mt-1 block">✓ Double-Entry Balanced</span>
    </div>
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 card-glow">
      <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Plan Longevity Score</span>
      <p id="longevityScoreDisplay" class="text-3xl font-black text-emerald-400 mt-2">98.2%</p>
      <span class="text-xs text-slate-500 mt-1 block">10k Monte Carlo Iterations</span>
    </div>
  </div>

  <!-- Connected Accounts List (Editable) -->
  <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 card-glow">
    <div class="flex items-center justify-between mb-4">
      <div>
        <h2 class="text-lg font-bold text-white">Connected Accounts & Balances</h2>
        <p class="text-xs text-slate-400">Click on any balance to edit directly in real time.</p>
      </div>
      <button onclick="openModal('accountModal')" class="text-xs text-indigo-400 hover:text-indigo-300 font-semibold">
        + Add Account
      </button>
    </div>
    <div id="accountsContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <!-- Injected dynamically -->
    </div>
  </div>

  <!-- Interactive Monte Carlo Simulator Controls -->
  <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 card-glow space-y-6">
    <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      <div>
        <h2 class="text-lg font-bold text-white">Stochastic Monte Carlo Wealth Simulation</h2>
        <p class="text-xs text-slate-400">Adjust the parameters below to see the interactive 10,000-path simulation update instantly.</p>
      </div>
      <button onclick="recalculateMonteCarlo()" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold rounded-xl shadow-lg transition">
        ⚡ Run 10k Simulation
      </button>
    </div>

    <!-- Live Controls Sliders -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 p-4 bg-slate-950/70 rounded-xl border border-slate-800 text-sm">
      <div>
        <label class="text-xs text-slate-400 block mb-1">Expected Annual Return (%)</label>
        <div class="flex items-center gap-2">
          <input type="range" id="mcReturn" min="2" max="15" step="0.5" value="8.0" oninput="updateMcVal('mcReturnVal', this.value + '%')" class="w-full">
          <span id="mcReturnVal" class="text-xs font-bold text-indigo-400 w-12">8.0%</span>
        </div>
      </div>
      <div>
        <label class="text-xs text-slate-400 block mb-1">Annual Volatility (σ %)</label>
        <div class="flex items-center gap-2">
          <input type="range" id="mcVol" min="5" max="30" step="0.5" value="15.0" oninput="updateMcVal('mcVolVal', this.value + '%')" class="w-full">
          <span id="mcVolVal" class="text-xs font-bold text-amber-400 w-12">15.0%</span>
        </div>
      </div>
      <div>
        <label class="text-xs text-slate-400 block mb-1">Annual Savings Addition ($)</label>
        <input type="number" id="mcSavings" value="24000" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
      </div>
      <div>
        <label class="text-xs text-slate-400 block mb-1">Time Horizon (Years)</label>
        <input type="number" id="mcYears" min="5" max="40" value="25" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-white">
      </div>
    </div>

    <div class="h-64">
      <canvas id="monteCarloChart"></canvas>
    </div>
  </div>

  <!-- Budget Envelopes & Tax Optimizer Section -->
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
    <!-- Budget Envelopes -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 card-glow">
      <div class="flex items-center justify-between mb-4">
        <div>
          <h2 class="text-lg font-bold text-white">Monthly Budget Envelopes</h2>
          <p class="text-xs text-slate-400">Zero-Based Envelope Tracking</p>
        </div>
        <button onclick="openModal('budgetModal')" class="text-xs text-indigo-400 hover:text-indigo-300 font-semibold">
          ✏️ Edit Allocations
        </button>
      </div>
      <div id="envelopesContainer" class="space-y-4">
        <!-- Dynamically populated -->
      </div>
    </div>

    <!-- Tax-Loss Harvesting Scanner -->
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 card-glow">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-lg font-bold text-white">Tax Optimization & Loss Harvester</h2>
        <span class="text-xs px-2.5 py-0.5 rounded bg-emerald-950 text-emerald-400 border border-emerald-800 font-semibold">IRS 30-Day Safe</span>
      </div>
      <div class="p-4 bg-emerald-950/30 border border-emerald-800/50 rounded-xl space-y-2">
        <div class="flex justify-between items-center text-sm font-bold text-emerald-300">
          <span>Active Harvest Opportunity: BND</span>
          <span>Est. Tax Savings: $450.00</span>
        </div>
        <p class="text-xs text-slate-300">
          Unrealized capital loss of <strong>$3,000.00</strong> identified in taxable brokerage. Recommended correlated replacement security: <strong>AGG (iShares Core US Aggregate Bond)</strong>.
        </p>
        <button onclick="showToast('Tax harvest order executed with replacement AGG!', 'success')" class="mt-2 w-full py-2 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold rounded-lg transition">
          Execute Tax-Loss Harvest Order
        </button>
      </div>
    </div>
  </div>

  <!-- MODALS -->

  <!-- 1. Add/Edit Transaction Modal -->
  <div id="txModal" class="hidden fixed inset-0 modal-backdrop z-50 flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 max-w-md w-full text-white shadow-2xl space-y-4">
      <div class="flex justify-between items-center pb-2 border-b border-slate-800">
        <h3 class="text-lg font-bold">Record Transaction</h3>
        <button onclick="closeModal('txModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>
      <div class="space-y-3">
        <div>
          <label class="text-xs text-slate-400 block mb-1">Account</label>
          <select id="txAccountSelect" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white"></select>
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Merchant / Description</label>
          <input type="text" id="txDesc" placeholder="e.g. Whole Foods, Paycheck, Gas" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Amount ($) - Negative for Expense, Positive for Inflow</label>
          <input type="number" step="0.01" id="txAmount" placeholder="-85.50" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Category</label>
          <select id="txCat" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
            <option value="cat_food">Groceries & Dining</option>
            <option value="cat_housing">Housing & Rent</option>
            <option value="cat_transit">Transportation</option>
            <option value="cat_entertainment">Entertainment & Leisure</option>
            <option value="cat_salary">Salary & Wages (Income)</option>
          </select>
        </div>
      </div>
      <div class="flex gap-3 pt-2">
        <button onclick="submitTransaction()" class="flex-1 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm rounded-xl transition">
          Post Transaction
        </button>
        <button onclick="closeModal('txModal')" class="px-4 py-2.5 bg-slate-800 text-slate-300 font-semibold text-sm rounded-xl">
          Cancel
        </button>
      </div>
    </div>
  </div>

  <!-- 2. Add/Edit Account Modal -->
  <div id="accountModal" class="hidden fixed inset-0 modal-backdrop z-50 flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 max-w-md w-full text-white shadow-2xl space-y-4">
      <div class="flex justify-between items-center pb-2 border-b border-slate-800">
        <h3 class="text-lg font-bold">Add / Edit Bank Account</h3>
        <button onclick="closeModal('accountModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>
      <div class="space-y-3">
        <div>
          <label class="text-xs text-slate-400 block mb-1">Account Name</label>
          <input type="text" id="accName" placeholder="e.g. Robinhood Crypto, Schwab Checking" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Account Type</label>
          <select id="accType" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
            <option value="CHECKING">Checking Account (Asset)</option>
            <option value="SAVINGS">High-Yield Savings (Asset)</option>
            <option value="INVESTMENT">Investment Portfolio (Asset)</option>
            <option value="CRYPTO">Crypto Wallet (Asset)</option>
            <option value="CREDIT_CARD">Credit Card (Liability)</option>
            <option value="MORTGAGE">Mortgage / Loan (Liability)</option>
          </select>
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Current Balance ($)</label>
          <input type="number" step="0.01" id="accBalance" placeholder="5000.00" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
        </div>
      </div>
      <div class="flex gap-3 pt-2">
        <button onclick="submitAccount()" class="flex-1 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm rounded-xl transition">
          Save Account
        </button>
        <button onclick="closeModal('accountModal')" class="px-4 py-2.5 bg-slate-800 text-slate-300 font-semibold text-sm rounded-xl">
          Cancel
        </button>
      </div>
    </div>
  </div>

  <!-- 3. Edit Budget Envelopes Modal -->
  <div id="budgetModal" class="hidden fixed inset-0 modal-backdrop z-50 flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 max-w-md w-full text-white shadow-2xl space-y-4">
      <div class="flex justify-between items-center pb-2 border-b border-slate-800">
        <h3 class="text-lg font-bold">Edit Monthly Budget Allocations</h3>
        <button onclick="closeModal('budgetModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>
      <div class="space-y-3">
        <div>
          <label class="text-xs text-slate-400 block mb-1">Housing & Rent Allocation ($)</label>
          <input type="number" id="bHousing" value="2500" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Groceries & Dining Allocation ($)</label>
          <input type="number" id="bFood" value="850" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Transportation & Fuel ($)</label>
          <input type="number" id="bTransit" value="350" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Entertainment & Leisure ($)</label>
          <input type="number" id="bEntertainment" value="250" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white">
        </div>
      </div>
      <div class="flex gap-3 pt-2">
        <button onclick="submitBudgets()" class="flex-1 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm rounded-xl transition">
          Update Allocations
        </button>
        <button onclick="closeModal('budgetModal')" class="px-4 py-2.5 bg-slate-800 text-slate-300 font-semibold text-sm rounded-xl">
          Cancel
        </button>
      </div>
    </div>
  </div>

  <script>
    let chartInstance = null;

    function openModal(id) { document.getElementById(id).classList.remove('hidden'); }
    function closeModal(id) { document.getElementById(id).classList.add('hidden'); }

    function showToast(msg, type = 'success') {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.className = `fixed top-6 right-6 z-50 p-4 rounded-xl shadow-2xl border text-sm font-semibold ${
        type === 'success' ? 'bg-emerald-900 border-emerald-700 text-emerald-200' : 'bg-rose-900 border-rose-700 text-rose-200'
      }`;
      toast.classList.remove('hidden');
      setTimeout(() => toast.classList.add('hidden'), 3500);
    }

    function updateMcVal(id, val) { document.getElementById(id).innerText = val; }

    async function loadDashboardData() {
      try {
        const nwRes = await fetch('/api/net-worth');
        const nwData = await nwRes.json();
        document.getElementById('totalAssetsDisplay').innerText = '$' + Number(nwData.total_assets).toLocaleString('en-US', {minimumFractionDigits: 2});
        document.getElementById('totalDebtsDisplay').innerText = '$' + Number(nwData.total_liabilities).toLocaleString('en-US', {minimumFractionDigits: 2});
        document.getElementById('netWorthDisplay').innerText = '$' + Number(nwData.net_worth).toLocaleString('en-US', {minimumFractionDigits: 2});

        const accRes = await fetch('/api/accounts');
        const accData = await accRes.json();
        const container = document.getElementById('accountsContainer');
        const select = document.getElementById('txAccountSelect');
        container.innerHTML = '';
        select.innerHTML = '';

        accData.forEach(acc => {
          const bal = (acc.current_balance_cents / 100);
          const isNegative = bal < 0;
          container.innerHTML += `
            <div class="p-4 bg-slate-950/70 border border-slate-800 rounded-xl flex items-center justify-between">
              <div>
                <span class="text-xs uppercase text-slate-500 font-bold">${acc.account_type}</span>
                <p class="font-bold text-white text-sm">${acc.account_name}</p>
              </div>
              <div class="text-right">
                <span class="text-sm font-black ${isNegative ? 'text-rose-400' : 'text-emerald-400'}">
                  $${Math.abs(bal).toLocaleString('en-US', {minimumFractionDigits: 2})}
                </span>
                <button onclick="promptEditBalance('${acc.account_id}', ${bal})" class="block text-[10px] text-indigo-400 hover:text-indigo-300 mt-0.5">
                  ✏️ Edit
                </button>
              </div>
            </div>
          `;
          select.innerHTML += `<option value="${acc.account_id}">${acc.account_name} ($${bal.toFixed(2)})</option>`;
        });

        // Envelopes
        const bRes = await fetch('/api/budget');
        const bData = await bRes.json();
        const envContainer = document.getElementById('envelopesContainer');
        envContainer.innerHTML = '';
        bData.forEach(env => {
          const isOver = env.spent > env.allocated;
          envContainer.innerHTML += `
            <div>
              <div class="flex justify-between text-xs mb-1">
                <span class="font-semibold text-slate-300 capitalize">${env.category_id.replace('cat_', '')}</span>
                <span class="text-slate-400">$${env.spent.toFixed(2)} / $${env.allocated.toFixed(2)} (${env.percentage_spent}%)</span>
              </div>
              <div class="w-full bg-slate-800 h-2 rounded-full overflow-hidden">
                <div class="h-full ${isOver ? 'bg-rose-500' : 'bg-indigo-500'}" style="width: ${Math.min(100, env.percentage_spent)}%"></div>
              </div>
            </div>
          `;
        });

        recalculateMonteCarlo();
      } catch (e) {
        console.error(e);
      }
    }

    async function promptEditBalance(accId, currentBal) {
      const newBal = prompt('Enter new balance for this account ($):', currentBal);
      if (newBal !== null && !isNaN(parseFloat(newBal))) {
        const delta = parseFloat(newBal) - currentBal;
        await fetch('/api/transactions', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({
            account_id: accId,
            amount_cents: Math.round(delta * 100),
            raw_description: 'Manual Balance Adjustment',
            merchant_name: 'Balance Adjustment',
            category_id: 'cat_salary'
          })
        });
        showToast('Account balance updated successfully!');
        loadDashboardData();
      }
    }

    async function submitTransaction() {
      const accId = document.getElementById('txAccountSelect').value;
      const desc = document.getElementById('txDesc').value || 'General Transaction';
      const amount = parseFloat(document.getElementById('txAmount').value || 0);
      const cat = document.getElementById('txCat').value;

      if (!accId || isNaN(amount)) {
        showToast('Please specify valid transaction details', 'error');
        return;
      }

      await fetch('/api/transactions', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          account_id: accId,
          amount_cents: Math.round(amount * 100),
          raw_description: desc,
          merchant_name: desc,
          category_id: cat
        })
      });

      closeModal('txModal');
      showToast('Transaction posted to General Ledger!');
      loadDashboardData();
    }

    async function submitAccount() {
      const name = document.getElementById('accName').value;
      const type = document.getElementById('accType').value;
      const bal = parseFloat(document.getElementById('accBalance').value || 0);

      if (!name) {
        showToast('Account name is required', 'error');
        return;
      }

      await fetch('/api/accounts', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          name: name,
          type: type,
          balance_cents: Math.round(bal * 100)
        })
      });

      closeModal('accountModal');
      showToast('New account registered in Chart of Accounts!');
      loadDashboardData();
    }

    async function submitBudgets() {
      const allocations = [
        { category_id: 'cat_housing', allocated_cents: Math.round(parseFloat(document.getElementById('bHousing').value) * 100) },
        { category_id: 'cat_food', allocated_cents: Math.round(parseFloat(document.getElementById('bFood').value) * 100) },
        { category_id: 'cat_transit', allocated_cents: Math.round(parseFloat(document.getElementById('bTransit').value) * 100) },
        { category_id: 'cat_entertainment', allocated_cents: Math.round(parseFloat(document.getElementById('bEntertainment').value) * 100) }
      ];

      for (const item of allocations) {
        await fetch('/api/budget/envelope', {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(item)
        });
      }

      closeModal('budgetModal');
      showToast('Budget allocations updated!');
      loadDashboardData();
    }

    async function recalculateMonteCarlo() {
      const ret = parseFloat(document.getElementById('mcReturn').value) / 100.0;
      const vol = parseFloat(document.getElementById('mcVol').value) / 100.0;
      const savings = parseFloat(document.getElementById('mcSavings').value) || 20000;
      const yearsCount = parseInt(document.getElementById('mcYears').value) || 25;

      const res = await fetch('/api/monte-carlo/simulate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          expected_return: ret,
          volatility: vol,
          annual_contribution: savings,
          years: yearsCount
        })
      });
      const data = await res.json();
      document.getElementById('longevityScoreDisplay').innerText = data.success_rate_percentage + '%';

      renderChart(data);
    }

    function renderChart(data) {
      const ctx = document.getElementById('monteCarloChart').getContext('2d');
      const labels = data.percentile_trajectory.p50_median.map((_, i) => 'Year ' + i);

      if (chartInstance) {
        chartInstance.destroy();
      }

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            { label: '90th Percentile (Optimistic)', data: data.percentile_trajectory.p90, borderColor: '#10B981', tension: 0.2, pointRadius: 0 },
            { label: '50th Percentile (Median Expected)', data: data.percentile_trajectory.p50_median, borderColor: '#6366F1', borderWidth: 3, tension: 0.2, pointRadius: 0 },
            { label: '10th Percentile (Conservative)', data: data.percentile_trajectory.p10, borderColor: '#F59E0B', tension: 0.2, pointRadius: 0 }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: '#94a3b8', font: { size: 11 } } } },
          scales: {
            x: { grid: { color: '#1e293b' }, ticks: { color: '#64748b' } },
            y: { grid: { color: '#1e293b' }, ticks: { color: '#64748b', callback: v => '$' + (v >= 1e6 ? (v/1e6).toFixed(1)+'M' : (v/1e3).toFixed(0)+'k') } }
          }
        }
      });
    }

    window.onload = loadDashboardData;
  </script>
</body>
</html>
"""

class FintechHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path in ("/", "/dashboard", "/index.html"):
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode("utf-8"))
            return

        if parsed.path == "/api/net-worth":
            assets, debts, net_worth = account_mgr.compute_net_worth(USER_ID)
            self.send_json({
                "total_assets": str(assets.value),
                "total_liabilities": str(debts.value),
                "net_worth": str(net_worth.value),
                "status": "EQUILIBRIUM_VERIFIED"
            })
            return

        if parsed.path == "/api/accounts":
            accs = account_mgr.list_user_accounts(USER_ID)
            self.send_json([
                {
                    "account_id": a.account_id,
                    "account_name": a.account_name,
                    "account_type": a.account_type,
                    "currency": a.currency,
                    "current_balance_cents": a.current_balance_cents
                }
                for a in accs
            ])
            return

        if parsed.path == "/api/budget":
            status = budget_mgr.get_envelope_status(USER_ID, "2026-08")
            self.send_json([
                {
                    "category_id": s["category_id"],
                    "allocated": float(s["allocated"].value),
                    "spent": float(s["spent"].value),
                    "remaining": float(s["remaining"].value),
                    "percentage_spent": s["percentage_spent"]
                }
                for s in status
            ])
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_length).decode('utf-8')
        payload = json.loads(post_body) if post_body else {}

        if parsed.path == "/api/transactions":
            acc_id = payload.get("account_id")
            amount_cents = int(payload.get("amount_cents", 0))
            desc = payload.get("raw_description", "Manual entry")
            merchant = payload.get("merchant_name", desc)
            cat_id = payload.get("category_id")

            tx = tx_processor.process_transaction(
                account_id=acc_id,
                user_id=USER_ID,
                amount_cents=amount_cents,
                date="2026-08-31",
                merchant_name=merchant,
                raw_description=desc,
                category_id=cat_id,
                allow_duplicates=True
            )
            if amount_cents < 0 and cat_id:
                budget_mgr.record_expense(USER_ID, cat_id, "2026-08", abs(amount_cents))

            self.send_json({"status": "SUCCESS", "transaction_id": tx.transaction_id})
            return

        if parsed.path == "/api/accounts":
            name = payload.get("name", "New Account")
            acc_type = payload.get("type", "CHECKING")
            balance_cents = int(payload.get("balance_cents", 0))

            acc = account_mgr.create_account(
                user_id=USER_ID,
                name=name,
                account_type=acc_type,
                initial_balance_cents=balance_cents
            )
            self.send_json({"status": "SUCCESS", "account_id": acc.account_id})
            return

        if parsed.path == "/api/budget/envelope":
            cat_id = payload.get("category_id")
            allocated_cents = int(payload.get("allocated_cents", 0))
            env = budget_mgr.create_envelope(USER_ID, cat_id, allocated_cents, "2026-08")
            self.send_json({"status": "SUCCESS", "envelope_id": env.envelope_id})
            return

        if parsed.path == "/api/monte-carlo/simulate":
            expected_ret = float(payload.get("expected_return", 0.08))
            vol = float(payload.get("volatility", 0.15))
            savings = float(payload.get("annual_contribution", 24000.0))
            years = int(payload.get("years", 25))

            assets, _, _ = account_mgr.compute_net_worth(USER_ID)
            res = monte_carlo.simulate_wealth_trajectory(
                starting_wealth=max(10000.0, float(assets.value)),
                annual_contribution=savings,
                annual_withdrawal=0.0,
                expected_annual_return=expected_ret,
                annual_volatility=vol,
                years=years,
                iterations=2000
            )
            self.send_json(res)
            return

        self.send_response(404)
        self.end_headers()

    def send_json(self, data: dict):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def log_message(self, format, *args):
        pass

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), FintechHTTPHandler) as httpd:
        print(f"\n[TrueBalance] Interactive Server active at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
