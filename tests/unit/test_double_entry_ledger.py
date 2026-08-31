"""
Test Suite 1: Double-Entry Ledger Balancing Invariants & Integrity.
"""

import pytest
import unittest
from core.math.decimal_utils import FinancialDecimal
from core.ledger.types import AccountClassification, NormalBalance, EntryStatus
from core.ledger.journal_entry import JournalEntry, UnbalancedJournalEntryError
from core.ledger.double_entry import GeneralLedger


class TestDoubleEntryLedger(unittest.TestCase):

    def setUp(self):
        self.ledger = GeneralLedger()
        self.ledger.register_account("1010", "Cash", AccountClassification.ASSET)
        self.ledger.register_account("2010", "Credit Card", AccountClassification.LIABILITY)
        self.ledger.register_account("3010", "Retained Capital", AccountClassification.EQUITY)
        self.ledger.register_account("4010", "Salary Income", AccountClassification.REVENUE)
        self.ledger.register_account("5010", "Groceries Expense", AccountClassification.EXPENSE)

    def test_balanced_journal_entry_posting(self):
        """Verify that a balanced journal entry posts successfully and updates balances."""
        entry = JournalEntry("entry_01", "2026-08-25", "Bi-weekly paycheck")
        entry.add_line("line_1", "1010", "Cash", AccountClassification.ASSET, debit=FinancialDecimal("3500.00"))
        entry.add_line("line_2", "4010", "Salary Income", AccountClassification.REVENUE, credit=FinancialDecimal("3500.00"))
        
        self.assertTrue(entry.is_balanced())
        self.ledger.post_entry(entry)
        
        self.assertEqual(self.ledger.get_account_balance("1010"), FinancialDecimal("3500.00"))
        self.assertEqual(self.ledger.get_account_balance("4010"), FinancialDecimal("3500.00"))

    def test_unbalanced_journal_entry_raises_error(self):
        """Verify that posting an unbalanced journal entry raises an UnbalancedJournalEntryError."""
        entry = JournalEntry("entry_02", "2026-08-26", "Unbalanced grocery expense")
        entry.add_line("line_1", "5010", "Groceries Expense", AccountClassification.EXPENSE, debit=FinancialDecimal("150.00"))
        entry.add_line("line_2", "1010", "Cash", AccountClassification.ASSET, credit=FinancialDecimal("140.00"))
        
        self.assertFalse(entry.is_balanced())
        with self.assertRaises(UnbalancedJournalEntryError):
            self.ledger.post_entry(entry)

    def test_trial_balance_equilibrium(self):
        """Verify trial balance total debits equal total credits."""
        # Entry 1: Income
        e1 = JournalEntry("e1", "2026-08-20", "Paycheck")
        e1.add_line("l1", "1010", "Cash", AccountClassification.ASSET, debit=FinancialDecimal("5000.00"))
        e1.add_line("l2", "4010", "Salary Income", AccountClassification.REVENUE, credit=FinancialDecimal("5000.00"))
        self.ledger.post_entry(e1)

        # Entry 2: Grocery
        e2 = JournalEntry("e2", "2026-08-21", "Groceries")
        e2.add_line("l3", "5010", "Groceries Expense", AccountClassification.EXPENSE, debit=FinancialDecimal("250.00"))
        e2.add_line("l4", "1010", "Cash", AccountClassification.ASSET, credit=FinancialDecimal("250.00"))
        self.ledger.post_entry(e2)

        rows, total_debts, total_credits, is_balanced = self.ledger.generate_trial_balance()
        self.assertTrue(is_balanced)
        self.assertEqual(total_debts, total_credits)

    def test_balance_sheet_equilibrium(self):
        """Verify Balance Sheet fundamental equation: Assets = Liabilities + Equity + Net Income."""
        e1 = JournalEntry("e1", "2026-08-20", "Initial Capital")
        e1.add_line("l1", "1010", "Cash", AccountClassification.ASSET, debit=FinancialDecimal("10000.00"))
        e1.add_line("l2", "3010", "Retained Capital", AccountClassification.EQUITY, credit=FinancialDecimal("10000.00"))
        self.ledger.post_entry(e1)

        sheet = self.ledger.generate_balance_sheet()
        self.assertTrue(sheet["is_in_equilibrium"])
        self.assertEqual(sheet["total_assets"], sheet["total_liabilities_and_equity"])


if __name__ == "__main__":
    unittest.main()
