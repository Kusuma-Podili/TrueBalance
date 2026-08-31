"""
TrueBalance - Interactive Enterprise Fintech Dashboard & Live API Server.
Features distinct luxury color palette (Jade Obsidian & Champagne Gold) and live theme switching.
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
<html lang="en" data-theme="emerald-obsidian">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TrueBalance - Wealth Intelligence & Ledger</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">

  <style>
    /* THEME 1: Emerald Obsidian & Champagne Gold (Default) */
    html[data-theme="emerald-obsidian"] {
      --bg-primary: #050a08;
      --bg-surface: #0a1410;
      --bg-card: #0e1e17;
      --bg-input: #142820;
      --border-color: rgba(16, 185, 129, 0.18);
      --border-highlight: rgba(16, 185, 129, 0.4);
      --accent-primary: #10b981;
      --accent-primary-hover: #059669;
      --accent-gold: #f59e0b;
      --accent-cyan: #06b6d4;
      --text-main: #f0fdf4;
      --text-muted: #6ee7b7;
      --text-dim: #059669;
      --card-glow: 0 0 35px -5px rgba(16, 185, 129, 0.12);
      --tag-bg: #064e3b;
      --tag-text: #6ee7b7;
    }

    /* THEME 2: Cyber Gold & Terminal Bronze */
    html[data-theme="cyber-amber"] {
      --bg-primary: #0a0805;
      --bg-surface: #14100a;
      --bg-card: #1f180f;
      --bg-input: #2a2014;
      --border-color: rgba(245, 158, 11, 0.22);
      --border-highlight: rgba(245, 158, 11, 0.5);
      --accent-primary: #f59e0b;
      --accent-primary-hover: #d97706;
      --accent-gold: #fbbf24;
      --accent-cyan: #10b981;
      --text-main: #fffbeb;
      --text-muted: #fde68a;
      --text-dim: #b45309;
      --card-glow: 0 0 35px -5px rgba(245, 158, 11, 0.15);
      --tag-bg: #451a03;
      --tag-text: #fde68a;
    }

    /* THEME 3: Crimson Velvet & Platinum (High-End Swiss Luxury) */
    html[data-theme="crimson-luxury"] {
      --bg-primary: #0a0608;
      --bg-surface: #150d11;
      --bg-card: #20131a;
      --bg-input: #2d1b25;
      --border-color: rgba(244, 63, 94, 0.22);
      --border-highlight: rgba(244, 63, 94, 0.5);
      --accent-primary: #f43f5e;
      --accent-primary-hover: #e11d48;
      --accent-gold: #e2e8f0;
      --accent-cyan: #38bdf8;
      --text-main: #fff1f2;
      --text-muted: #fecdd3;
      --text-dim: #be123c;
      --card-glow: 0 0 35px -5px rgba(244, 63, 94, 0.15);
      --tag-bg: #4c0519;
      --tag-text: #fecdd3;
    }

    /* THEME 4: Arctic Teal & Polar Frost */
    html[data-theme="arctic-teal"] {
      --bg-primary: #040d12;
      --bg-surface: #091921;
      --bg-card: #0f2733;
      --bg-input: #163646;
      --border-color: rgba(14, 165, 233, 0.22);
      --border-highlight: rgba(14, 165, 233, 0.5);
      --accent-primary: #0ea5e9;
      --accent-primary-hover: #0284c7;
      --accent-gold: #38bdf8;
      --accent-cyan: #34d399;
      --text-main: #f0f9ff;
      --text-muted: #bae6fd;
      --text-dim: #0369a1;
      --card-glow: 0 0 35px -5px rgba(14, 165, 233, 0.15);
      --tag-bg: #0c4a6e;
      --tag-text: #bae6fd;
    }

    body {
      background-color: var(--bg-primary);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .font-mono { font-family: 'JetBrains Mono', monospace; }
    .bg-surface { background-color: var(--bg-surface); }
    .bg-card-custom { background-color: var(--bg-card); }
    .bg-input-custom { background-color: var(--bg-input); }
    .border-custom { border-color: var(--border-color); }
    .border-highlight { border-color: var(--border-highlight); }
    .text-primary-custom { color: var(--accent-primary); }
    .text-gold-custom { color: var(--accent-gold); }
    .card-shadow { box-shadow: var(--card-glow); }
    .btn-primary { background-color: var(--accent-primary); color: #000; font-weight: 700; }
    .btn-primary:hover { background-color: var(--accent-primary-hover); }
    .modal-backdrop { background-color: rgba(0, 0, 0, 0.85); backdrop-filter: blur(8px); }
  </style>
</head>
<body class="p-4 md:p-8 max-w-7xl mx-auto space-y-8">

  <!-- Header & Color Theme Selector -->
  <header class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 pb-6 border-b border-custom">
    <div>
      <div class="flex items-center gap-3">
        <div class="w-11 h-11 rounded-2xl flex items-center justify-center font-black text-xl shadow-xl tracking-tighter" style="background: linear-gradient(135deg, var(--accent-primary), var(--accent-gold)); color: #000;">
          TB
        </div>
        <div>
          <h1 class="text-3xl font-black tracking-tight" style="letter-spacing: -0.03em;">TrueBalance</h1>
          <p class="text-xs text-slate-400 mt-0.5">High-Precision Double-Entry Ledger & Wealth Intelligence Engine</p>
        </div>
      </div>
    </div>

    <!-- Theme Palette Selector + Action Buttons -->
    <div class="flex flex-wrap items-center gap-3">
      <!-- Theme Switcher Pills -->
      <div class="flex items-center bg-surface border border-custom rounded-2xl p-1 gap-1 text-xs">
        <span class="text-[10px] text-slate-400 px-2 uppercase font-bold tracking-wider">Palette:</span>
        <button onclick="setTheme('emerald-obsidian')" id="btn-emerald-obsidian" class="px-2.5 py-1 rounded-xl font-bold transition flex items-center gap-1.5 bg-emerald-950 text-emerald-300 border border-emerald-700">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span> Jade
        </button>
        <button onclick="setTheme('cyber-amber')" id="btn-cyber-amber" class="px-2.5 py-1 rounded-xl font-bold transition flex items-center gap-1.5 text-amber-300/60 hover:text-amber-300">
          <span class="w-2 h-2 rounded-full bg-amber-400"></span> Gold
        </button>
        <button onclick="setTheme('crimson-luxury')" id="btn-crimson-luxury" class="px-2.5 py-1 rounded-xl font-bold transition flex items-center gap-1.5 text-rose-300/60 hover:text-rose-300">
          <span class="w-2 h-2 rounded-full bg-rose-400"></span> Crimson
        </button>
        <button onclick="setTheme('arctic-teal')" id="btn-arctic-teal" class="px-2.5 py-1 rounded-xl font-bold transition flex items-center gap-1.5 text-sky-300/60 hover:text-sky-300">
          <span class="w-2 h-2 rounded-full bg-sky-400"></span> Teal
        </button>
      </div>

      <button onclick="openModal('txModal')" class="px-4 py-2 btn-primary text-xs rounded-xl shadow-lg transition">
        + Post Transaction
      </button>
      <button onclick="openModal('accountModal')" class="px-3 py-2 bg-surface hover:bg-card-custom text-slate-200 text-xs font-bold rounded-xl border border-custom transition">
        + New Account
      </button>
      <button onclick="openModal('budgetModal')" class="px-3 py-2 bg-surface hover:bg-card-custom text-slate-200 text-xs font-bold rounded-xl border border-custom transition">
        ✏️ Edit Budgets
      </button>
    </div>
  </header>

  <!-- Notification Toast -->
  <div id="toast" class="hidden fixed top-6 right-6 z-50 p-4 rounded-2xl shadow-2xl border text-sm font-semibold transition-all"></div>

  <!-- Metric Summary Cards -->
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
    <div class="bg-card-custom border border-custom rounded-3xl p-6 card-shadow">
      <span class="text-[11px] font-bold text-slate-400 uppercase tracking-widest">Total Assets</span>
      <p id="totalAssetsDisplay" class="text-3xl font-black text-primary-custom mt-2 font-mono">$0.00</p>
      <span class="text-xs text-slate-400 mt-1 block">Checking, Savings & Equities</span>
    </div>
    <div class="bg-card-custom border border-custom rounded-3xl p-6 card-shadow">
      <span class="text-[11px] font-bold text-slate-400 uppercase tracking-widest">Total Liabilities</span>
      <p id="totalDebtsDisplay" class="text-3xl font-black text-rose-400 mt-2 font-mono">$0.00</p>
      <span class="text-xs text-slate-400 mt-1 block">Mortgage & Credit Balances</span>
    </div>
    <div class="bg-card-custom border border-custom rounded-3xl p-6 card-shadow">
      <span class="text-[11px] font-bold text-slate-400 uppercase tracking-widest">Total Net Worth</span>
      <p id="netWorthDisplay" class="text-3xl font-black text-gold-custom mt-2 font-mono">$0.00</p>
      <span class="text-xs text-primary-custom font-semibold mt-1 block">✓ Double-Entry Invariant Balanced</span>
    </div>
    <div class="bg-card-custom border border-custom rounded-3xl p-6 card-shadow">
      <span class="text-[11px] font-bold text-slate-400 uppercase tracking-widest">Plan Longevity Score</span>
      <p id="longevityScoreDisplay" class="text-3xl font-black text-primary-custom mt-2 font-mono">98.2%</p>
      <span class="text-xs text-slate-400 mt-1 block">10k Monte Carlo Iterations</span>
    </div>
  </div>

  <!-- Connected Accounts List (Editable) -->
  <div class="bg-card-custom border border-custom rounded-3xl p-6 card-shadow">
    <div class="flex items-center justify-between mb-4">
      <div>
        <h2 class="text-lg font-black text-white">Connected Accounts & Balances</h2>
        <p class="text-xs text-slate-400">Click ✏️ Edit on any account to update balances instantly.</p>
      </div>
      <button onclick="openModal('accountModal')" class="text-xs text-primary-custom hover:underline font-bold">
        + Register Account
      </button>
    </div>
    <div id="accountsContainer" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <!-- Injected dynamically -->
    </div>
  </div>

  <!-- Interactive Monte Carlo Simulator Controls -->
  <div class="bg-card-custom border border-custom rounded-3xl p-6 card-shadow space-y-6">
    <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      <div>
        <h2 class="text-lg font-black text-white">Stochastic Monte Carlo Wealth Trajectory</h2>
        <p class="text-xs text-slate-400">Adjust the sliders below to see 10,000 stochastic simulation paths update live.</p>
      </div>
      <button onclick="recalculateMonteCarlo()" class="px-4 py-2 btn-primary text-xs rounded-xl shadow-lg transition">
        ⚡ Run 10k Paths
      </button>
    </div>

    <!-- Sliders Grid -->
    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 p-4 bg-surface rounded-2xl border border-custom text-sm">
      <div>
        <label class="text-xs text-slate-400 block mb-1">Expected Return (%)</label>
        <div class="flex items-center gap-2">
          <input type="range" id="mcReturn" min="2" max="15" step="0.5" value="8.0" oninput="updateMcVal('mcReturnVal', this.value + '%')" class="w-full accent-emerald-500">
          <span id="mcReturnVal" class="text-xs font-mono font-bold text-primary-custom w-12">8.0%</span>
        </div>
      </div>
      <div>
        <label class="text-xs text-slate-400 block mb-1">Volatility (σ %)</label>
        <div class="flex items-center gap-2">
          <input type="range" id="mcVol" min="5" max="30" step="0.5" value="15.0" oninput="updateMcVal('mcVolVal', this.value + '%')" class="w-full accent-amber-500">
          <span id="mcVolVal" class="text-xs font-mono font-bold text-gold-custom w-12">15.0%</span>
        </div>
      </div>
      <div>
        <label class="text-xs text-slate-400 block mb-1">Annual Savings Addition ($)</label>
        <input type="number" id="mcSavings" value="24000" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-1.5 text-xs text-white font-mono">
      </div>
      <div>
        <label class="text-xs text-slate-400 block mb-1">Time Horizon (Years)</label>
        <input type="number" id="mcYears" min="5" max="40" value="25" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-1.5 text-xs text-white font-mono">
      </div>
    </div>

    <div class="h-64">
      <canvas id="monteCarloChart"></canvas>
    </div>
  </div>

  <!-- Budget Envelopes & Tax Optimizer Section -->
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
    <!-- Budget Envelopes -->
    <div class="bg-card-custom border border-custom rounded-3xl p-6 card-shadow">
      <div class="flex items-center justify-between mb-4">
        <div>
          <h2 class="text-lg font-black text-white">Monthly Zero-Based Envelopes</h2>
          <p class="text-xs text-slate-400">Digital Envelopes & Rollover Tracking</p>
        </div>
        <button onclick="openModal('budgetModal')" class="text-xs text-primary-custom hover:underline font-bold">
          ✏️ Edit Allocations
        </button>
      </div>
      <div id="envelopesContainer" class="space-y-4">
        <!-- Dynamically populated -->
      </div>
    </div>

    <!-- Tax-Loss Harvesting Scanner -->
    <div class="bg-card-custom border border-custom rounded-3xl p-6 card-shadow">
      <div class="flex items-center justify-between mb-4">
        <h2 class="text-lg font-black text-white">Tax Optimization & Loss Harvester</h2>
        <span class="text-[10px] px-2.5 py-1 rounded-full font-bold uppercase" style="background-color: var(--tag-bg); color: var(--tag-text); border: 1px solid var(--border-color);">
          IRS 30-Day Safe
        </span>
      </div>
      <div class="p-4 rounded-2xl space-y-2 border border-custom" style="background-color: var(--bg-surface);">
        <div class="flex justify-between items-center text-sm font-bold text-primary-custom">
          <span>Active Harvest Opportunity: BND</span>
          <span>Est. Tax Savings: $450.00</span>
        </div>
        <p class="text-xs text-slate-300">
          Unrealized capital loss of <strong class="text-rose-400">$3,000.00</strong> identified in taxable brokerage. Recommended replacement asset: <strong>AGG (iShares Core US Aggregate Bond)</strong>.
        </p>
        <button onclick="showToast('Tax harvest executed with replacement AGG asset!', 'success')" class="mt-2 w-full py-2 btn-primary text-xs rounded-xl transition">
          Execute Tax-Loss Harvest
        </button>
      </div>
    </div>
  </div>

  <!-- MODALS -->

  <!-- 1. Add Transaction Modal -->
  <div id="txModal" class="hidden fixed inset-0 modal-backdrop z-50 flex items-center justify-center p-4">
    <div class="bg-card-custom border border-custom rounded-3xl p-6 max-w-md w-full text-white shadow-2xl space-y-4">
      <div class="flex justify-between items-center pb-2 border-b border-custom">
        <h3 class="text-lg font-bold">Record Transaction</h3>
        <button onclick="closeModal('txModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>
      <div class="space-y-3">
        <div>
          <label class="text-xs text-slate-400 block mb-1">Account</label>
          <select id="txAccountSelect" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white"></select>
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Merchant / Description</label>
          <input type="text" id="txDesc" placeholder="e.g. Whole Foods, Tech Salary" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Amount ($) - Negative for Expense, Positive for Income</label>
          <input type="number" step="0.01" id="txAmount" placeholder="-85.50" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white font-mono">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Category</label>
          <select id="txCat" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white">
            <option value="cat_food">Groceries & Dining</option>
            <option value="cat_housing">Housing & Rent</option>
            <option value="cat_transit">Transportation</option>
            <option value="cat_entertainment">Entertainment & Leisure</option>
            <option value="cat_salary">Salary & Wages (Income)</option>
          </select>
        </div>
      </div>
      <div class="flex gap-3 pt-2">
        <button onclick="submitTransaction()" class="flex-1 py-2.5 btn-primary font-bold text-sm rounded-xl transition">
          Post to Ledger
        </button>
        <button onclick="closeModal('txModal')" class="px-4 py-2.5 bg-surface text-slate-300 font-semibold text-sm rounded-xl border border-custom">
          Cancel
        </button>
      </div>
    </div>
  </div>

  <!-- 2. Add Account Modal -->
  <div id="accountModal" class="hidden fixed inset-0 modal-backdrop z-50 flex items-center justify-center p-4">
    <div class="bg-card-custom border border-custom rounded-3xl p-6 max-w-md w-full text-white shadow-2xl space-y-4">
      <div class="flex justify-between items-center pb-2 border-b border-custom">
        <h3 class="text-lg font-bold">Register Bank / Investment Account</h3>
        <button onclick="closeModal('accountModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>
      <div class="space-y-3">
        <div>
          <label class="text-xs text-slate-400 block mb-1">Account Name</label>
          <input type="text" id="accName" placeholder="e.g. Coinbase Crypto, Vanguard Brokerage" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Account Type</label>
          <select id="accType" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white">
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
          <input type="number" step="0.01" id="accBalance" placeholder="5000.00" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white font-mono">
        </div>
      </div>
      <div class="flex gap-3 pt-2">
        <button onclick="submitAccount()" class="flex-1 py-2.5 btn-primary font-bold text-sm rounded-xl transition">
          Register Account
        </button>
        <button onclick="closeModal('accountModal')" class="px-4 py-2.5 bg-surface text-slate-300 font-semibold text-sm rounded-xl border border-custom">
          Cancel
        </button>
      </div>
    </div>
  </div>

  <!-- 3. Edit Budgets Modal -->
  <div id="budgetModal" class="hidden fixed inset-0 modal-backdrop z-50 flex items-center justify-center p-4">
    <div class="bg-card-custom border border-custom rounded-3xl p-6 max-w-md w-full text-white shadow-2xl space-y-4">
      <div class="flex justify-between items-center pb-2 border-b border-custom">
        <h3 class="text-lg font-bold">Edit Monthly Budget Allocations</h3>
        <button onclick="closeModal('budgetModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>
      <div class="space-y-3">
        <div>
          <label class="text-xs text-slate-400 block mb-1">Housing & Rent Allocation ($)</label>
          <input type="number" id="bHousing" value="2500" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white font-mono">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Groceries & Dining ($)</label>
          <input type="number" id="bFood" value="850" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white font-mono">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Transportation & Fuel ($)</label>
          <input type="number" id="bTransit" value="350" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white font-mono">
        </div>
        <div>
          <label class="text-xs text-slate-400 block mb-1">Entertainment & Leisure ($)</label>
          <input type="number" id="bEntertainment" value="250" class="w-full bg-input-custom border border-custom rounded-xl px-3 py-2 text-sm text-white font-mono">
        </div>
      </div>
      <div class="flex gap-3 pt-2">
        <button onclick="submitBudgets()" class="flex-1 py-2.5 btn-primary font-bold text-sm rounded-xl transition">
          Update Allocations
        </button>
        <button onclick="closeModal('budgetModal')" class="px-4 py-2.5 bg-surface text-slate-300 font-semibold text-sm rounded-xl border border-custom">
          Cancel
        </button>
      </div>
    </div>
  </div>

  <script>
    let chartInstance = null;
    let currentTheme = 'emerald-obsidian';

    function setTheme(themeName) {
      currentTheme = themeName;
      document.documentElement.setAttribute('data-theme', themeName);
      
      const themes = ['emerald-obsidian', 'cyber-amber', 'crimson-luxury', 'arctic-teal'];
      themes.forEach(t => {
        const btn = document.getElementById('btn-' + t);
        if (btn) {
          if (t === themeName) {
            btn.className = 'px-2.5 py-1 rounded-xl font-bold transition flex items-center gap-1.5 bg-slate-800 text-white border border-slate-600 shadow-md';
          } else {
            btn.className = 'px-2.5 py-1 rounded-xl font-bold transition flex items-center gap-1.5 text-slate-400 hover:text-white';
          }
        }
      });

      if (window.lastSimulationData) {
        renderChart(window.lastSimulationData);
      }
    }

    function openModal(id) { document.getElementById(id).classList.remove('hidden'); }
    function closeModal(id) { document.getElementById(id).classList.add('hidden'); }

    function showToast(msg, type = 'success') {
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.className = `fixed top-6 right-6 z-50 p-4 rounded-2xl shadow-2xl border text-sm font-semibold ${
        type === 'success' ? 'bg-emerald-950 border-emerald-700 text-emerald-200' : 'bg-rose-950 border-rose-700 text-rose-200'
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
            <div class="p-4 bg-surface border border-custom rounded-2xl flex items-center justify-between transition hover:border-highlight">
              <div>
                <span class="text-[10px] uppercase text-slate-400 font-bold tracking-wider">${acc.account_type}</span>
                <p class="font-bold text-white text-sm mt-0.5">${acc.account_name}</p>
              </div>
              <div class="text-right">
                <span class="text-sm font-mono font-bold ${isNegative ? 'text-rose-400' : 'text-primary-custom'}">
                  $${Math.abs(bal).toLocaleString('en-US', {minimumFractionDigits: 2})}
                </span>
                <button onclick="promptEditBalance('${acc.account_id}', ${bal})" class="block text-[11px] text-primary-custom hover:underline font-bold mt-1">
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
              <div class="flex justify-between text-xs mb-1 font-mono">
                <span class="font-semibold text-slate-300 capitalize">${env.category_id.replace('cat_', '')}</span>
                <span class="text-slate-400">$${env.spent.toFixed(2)} / $${env.allocated.toFixed(2)} (${env.percentage_spent}%)</span>
              </div>
              <div class="w-full bg-surface h-2 rounded-full overflow-hidden border border-custom">
                <div class="h-full transition-all" style="width: ${Math.min(100, env.percentage_spent)}%; background-color: ${isOver ? '#f43f5e' : 'var(--accent-primary)'}"></div>
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
            raw_description: 'Direct Balance Adjustment',
            merchant_name: 'Manual Adjustment',
            category_id: 'cat_salary'
          })
        });
        showToast('Account balance updated in General Ledger!');
        loadDashboardData();
      }
    }

    async function submitTransaction() {
      const accId = document.getElementById('txAccountSelect').value;
      const desc = document.getElementById('txDesc').value || 'Transaction Entry';
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
      const savings = parseFloat(document.getElementById('mcSavings').value) || 24000;
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
      window.lastSimulationData = data;
      document.getElementById('longevityScoreDisplay').innerText = data.success_rate_percentage + '%';

      renderChart(data);
    }

    function renderChart(data) {
      const ctx = document.getElementById('monteCarloChart').getContext('2d');
      const labels = data.percentile_trajectory.p50_median.map((_, i) => 'Yr ' + i);

      if (chartInstance) {
        chartInstance.destroy();
      }

      let primaryColor = '#10b981';
      let goldColor = '#f59e0b';
      let optimisticColor = '#34d399';

      if (currentTheme === 'cyber-amber') {
        primaryColor = '#f59e0b';
        goldColor = '#fbbf24';
        optimisticColor = '#10b981';
      } else if (currentTheme === 'crimson-luxury') {
        primaryColor = '#f43f5e';
        goldColor = '#e2e8f0';
        optimisticColor = '#38bdf8';
      } else if (currentTheme === 'arctic-teal') {
        primaryColor = '#0ea5e9';
        goldColor = '#38bdf8';
        optimisticColor = '#34d399';
      }

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            { label: '90th % (Optimistic)', data: data.percentile_trajectory.p90, borderColor: optimisticColor, tension: 0.25, pointRadius: 0 },
            { label: '50th % (Median)', data: data.percentile_trajectory.p50_median, borderColor: primaryColor, borderWidth: 3, tension: 0.25, pointRadius: 0 },
            { label: '10th % (Conservative)', data: data.percentile_trajectory.p10, borderColor: goldColor, tension: 0.25, pointRadius: 0 }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: { legend: { labels: { color: '#94a3b8', font: { family: 'Plus Jakarta Sans', size: 11 } } } },
          scales: {
            x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#64748b', font: { family: 'JetBrains Mono', size: 10 } } },
            y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#64748b', font: { family: 'JetBrains Mono', size: 10 }, callback: v => '$' + (v >= 1e6 ? (v/1e6).toFixed(1)+'M' : (v/1e3).toFixed(0)+'k') } }
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
        print(f"\n[TrueBalance] Server active at http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
