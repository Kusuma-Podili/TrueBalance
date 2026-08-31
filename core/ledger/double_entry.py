"""
General Ledger Posting Engine, Trial Balance, & Financial Statement Generator.
Implements the core accounting equation: Assets = Liabilities + Equity + (Revenue - Expenses).
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from core.math.decimal_utils import FinancialDecimal
from core.ledger.types import AccountClassification, NormalBalance, EntryStatus
from core.ledger.journal_entry import JournalEntry, JournalLine


@dataclass
class AccountBalance:
    account_id: str
    account_name: str
    classification: AccountClassification
    normal_balance: NormalBalance
    total_debits: FinancialDecimal = FinancialDecimal("0.00")
    total_credits: FinancialDecimal = FinancialDecimal("0.00")

    @property
    def balance(self) -> FinancialDecimal:
        """
        Computes net account balance according to its normal balance convention.
        Assets & Expenses: Balance = Debits - Credits
        Liabilities, Equity & Revenue: Balance = Credits - Debits
        """
        if self.normal_balance == NormalBalance.DEBIT:
            return self.total_debits - self.total_credits
        else:
            return self.total_credits - self.total_debits


class GeneralLedger:
    """
    Enterprise General Ledger engine. Manages posted journal entries, account balances,
    trial balance generation, and financial reporting.
    """

    def __init__(self):
        self._entries: Dict[str, JournalEntry] = {}
        self._accounts: Dict[str, AccountBalance] = {}

    def register_account(
        self,
        account_id: str,
        account_name: str,
        classification: AccountClassification
    ) -> AccountBalance:
        """Registers a new account in the chart of accounts."""
        normal_bal = (
            NormalBalance.DEBIT
            if classification in (AccountClassification.ASSET, AccountClassification.EXPENSE)
            else NormalBalance.CREDIT
        )
        acc = AccountBalance(
            account_id=account_id,
            account_name=account_name,
            classification=classification,
            normal_balance=normal_bal
        )
        self._accounts[account_id] = acc
        return acc

    def post_entry(self, entry: JournalEntry) -> None:
        """
        Posts a journal entry to the ledger and updates all constituent account balances.
        """
        if entry.status != EntryStatus.POSTED:
            entry.post()

        self._entries[entry.entry_id] = entry

        for line in entry.lines:
            if line.account_id not in self._accounts:
                self.register_account(line.account_id, line.account_name, line.account_classification)

            acc = self._accounts[line.account_id]
            acc.total_debits = acc.total_debits + line.base_debit
            acc.total_credits = acc.total_credits + line.base_credit

    def get_account_balance(self, account_id: str) -> Optional[FinancialDecimal]:
        """Gets current net balance of an account."""
        acc = self._accounts.get(account_id)
        return acc.balance if acc else None

    def generate_trial_balance(self) -> Tuple[List[Dict], FinancialDecimal, FinancialDecimal, bool]:
        """
        Generates Trial Balance report and verifies that Total Debits == Total Credits.
        """
        rows = []
        sum_debits = FinancialDecimal("0.00")
        sum_credits = FinancialDecimal("0.00")

        for acc in self._accounts.values():
            debit_col = FinancialDecimal("0.00")
            credit_col = FinancialDecimal("0.00")

            if acc.normal_balance == NormalBalance.DEBIT:
                if acc.balance.is_positive():
                    debit_col = acc.balance
                else:
                    credit_col = acc.balance.abs()
            else:
                if acc.balance.is_positive():
                    credit_col = acc.balance
                else:
                    debit_col = acc.balance.abs()

            sum_debits += debit_col
            sum_credits += credit_col

            rows.append({
                "account_id": acc.account_id,
                "account_name": acc.account_name,
                "classification": acc.classification.value,
                "debit": debit_col,
                "credit": credit_col
            })

        is_balanced = (sum_debits - sum_credits).abs().value < FinancialDecimal("0.0001").value
        return rows, sum_debits, sum_credits, is_balanced

    def generate_balance_sheet(self) -> Dict:
        """
        Generates Balance Sheet: Assets = Liabilities + Equity + Net Income.
        """
        assets = {}
        liabilities = {}
        equity = {}
        total_assets = FinancialDecimal("0.00")
        total_liabilities = FinancialDecimal("0.00")
        total_equity = FinancialDecimal("0.00")

        for acc in self._accounts.values():
            if acc.classification == AccountClassification.ASSET:
                assets[acc.account_name] = acc.balance
                total_assets += acc.balance
            elif acc.classification == AccountClassification.LIABILITY:
                liabilities[acc.account_name] = acc.balance
                total_liabilities += acc.balance
            elif acc.classification == AccountClassification.EQUITY:
                equity[acc.account_name] = acc.balance
                total_equity += acc.balance

        # Calculate Net Income from Revenue and Expenses
        income_statement = self.generate_income_statement()
        net_income = income_statement["net_income"]
        total_equity_and_liabilities = total_liabilities + total_equity + net_income

        return {
            "assets": assets,
            "total_assets": total_assets,
            "liabilities": liabilities,
            "total_liabilities": total_liabilities,
            "equity": equity,
            "total_equity": total_equity,
            "net_income": net_income,
            "total_liabilities_and_equity": total_equity_and_liabilities,
            "is_in_equilibrium": (total_assets - total_equity_and_liabilities).abs().value < FinancialDecimal("0.0001").value
        }

    def generate_income_statement(self) -> Dict:
        """
        Generates Income Statement (P&L): Net Income = Total Revenue - Total Expenses.
        """
        revenue = {}
        expenses = {}
        total_revenue = FinancialDecimal("0.00")
        total_expenses = FinancialDecimal("0.00")

        for acc in self._accounts.values():
            if acc.classification == AccountClassification.REVENUE:
                revenue[acc.account_name] = acc.balance
                total_revenue += acc.balance
            elif acc.classification == AccountClassification.EXPENSE:
                expenses[acc.account_name] = acc.balance
                total_expenses += acc.balance

        net_income = total_revenue - total_expenses
        return {
            "revenue": revenue,
            "total_revenue": total_revenue,
            "expenses": expenses,
            "total_expenses": total_expenses,
            "net_income": net_income,
            "profit_margin_pct": float(net_income / total_revenue * 100) if total_revenue.is_positive() else 0.0
        }
