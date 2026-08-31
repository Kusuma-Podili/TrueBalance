"""
Test Suite 6: End-to-End Enterprise Integration & Reconciliation Flow.
Tests complete customer journey from multi-currency account creation,
general ledger postings, budget envelopes, and tax-loss harvesting.
"""

import unittest
from core.ledger.double_entry import GeneralLedger
from core.ledger.journal_entry import JournalEntry
from core.ledger.types import AccountClassification
from core.math.decimal_utils import FinancialDecimal
from services.accounts.manager import AccountManager
from services.transactions.processor import TransactionProcessor
from services.budget.zero_based import BudgetManager
from services.tax.harvesting import TaxLossHarvester, TaxableHolding


class TestEndToEndFintechFlow(unittest.TestCase):

    def setUp(self):
        self.ledger = GeneralLedger()
        self.acc_mgr = AccountManager()
        self.tx_proc = TransactionProcessor(self.acc_mgr)
        self.budget_mgr = BudgetManager()

    def test_complete_customer_financial_lifecycle(self):
        """Verify full lifecycle: banking -> ledger -> budgeting -> tax optimization."""
        # 1. Create accounts
        checking = self.acc_mgr.create_account("usr_test_01", "Checking Account", "CHECKING", initial_balance_cents=1000000)
        savings = self.acc_mgr.create_account("usr_test_01", "High Yield Savings", "SAVINGS", initial_balance_cents=2500000)
        cc = self.acc_mgr.create_account("usr_test_01", "Sapphire Rewards", "CREDIT_CARD", initial_balance_cents=-150000)

        # 2. Verify net worth
        assets, debts, net_worth = self.acc_mgr.compute_net_worth("usr_test_01")
        self.assertEqual(assets, FinancialDecimal("35000.00"))
        self.assertEqual(debts, FinancialDecimal("1500.00"))
        self.assertEqual(net_worth, FinancialDecimal("33500.00"))

        # 3. Post double-entry journal entry
        self.ledger.register_account("1010", "Cash", AccountClassification.ASSET)
        self.ledger.register_account("4010", "Salary", AccountClassification.REVENUE)
        entry = JournalEntry("entry_payroll_01", "2026-08-30", "Bi-weekly paycheck")
        entry.add_line("l1", "1010", "Cash", AccountClassification.ASSET, debit=FinancialDecimal("4500.00"))
        entry.add_line("l2", "4010", "Salary", AccountClassification.REVENUE, credit=FinancialDecimal("4500.00"))
        self.ledger.post_entry(entry)

        self.assertEqual(self.ledger.get_account_balance("1010"), FinancialDecimal("4500.00"))

        # 4. Budget envelope allocation
        env = self.budget_mgr.create_envelope("usr_test_01", "cat_food", allocated_cents=80000, period_month="2026-08")
        self.budget_mgr.record_expense("usr_test_01", "cat_food", "2026-08", 25000)
        status = self.budget_mgr.get_envelope_status("usr_test_01", "2026-08")
        self.assertEqual(len(status), 1)
        self.assertEqual(status[0]["spent"], FinancialDecimal("250.00"))
        self.assertEqual(status[0]["remaining"], FinancialDecimal("550.00"))

        # 5. Tax-loss harvesting scanning
        holdings = [
            TaxableHolding("VOO", 100.0, 480.0, 520.0, "2025-01-10"),  # Gain
            TaxableHolding("BND", 500.0, 78.0, 72.0, "2025-03-15"),   # Loss: 500 * -$6 = -$3,000
        ]
        opps = TaxLossHarvester.find_harvesting_opportunities(holdings)
        self.assertEqual(len(opps), 1)
        self.assertEqual(opps[0]["symbol"], "BND")
        self.assertEqual(opps[0]["unrealized_loss"], 3000.0)


if __name__ == "__main__":
    unittest.main()
