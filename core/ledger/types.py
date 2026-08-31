"""
Chart of Accounts & Double-Entry Accounting Core Types.
Enforces standard US GAAP & IFRS account taxonomy, normal balances,
and journal entry life-cycle states.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional
from core.math.decimal_utils import FinancialDecimal


class AccountClassification(str, Enum):
    ASSET = "ASSET"
    LIABILITY = "LIABILITY"
    EQUITY = "EQUITY"
    REVENUE = "REVENUE"
    EXPENSE = "EXPENSE"


class NormalBalance(str, Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class EntryStatus(str, Enum):
    DRAFT = "DRAFT"
    POSTED = "POSTED"
    VOIDED = "VOIDED"
    RECONCILED = "RECONCILED"


@dataclass
class AccountTypeSpec:
    classification: AccountClassification
    normal_balance: NormalBalance
    description: str


ACCOUNT_CLASSIFICATION_MAP: Dict[AccountClassification, AccountTypeSpec] = {
    AccountClassification.ASSET: AccountTypeSpec(
        AccountClassification.ASSET,
        NormalBalance.DEBIT,
        "Economic resources owned by the entity (Cash, Investments, Receivables, Property)."
    ),
    AccountClassification.LIABILITY: AccountTypeSpec(
        AccountClassification.LIABILITY,
        NormalBalance.CREDIT,
        "Obligations and debts owed to third parties (Credit Cards, Mortgages, Loans)."
    ),
    AccountClassification.EQUITY: AccountTypeSpec(
        AccountClassification.EQUITY,
        NormalBalance.CREDIT,
        "Residual interest in assets after deducting liabilities (Retained Earnings, Capital)."
    ),
    AccountClassification.REVENUE: AccountTypeSpec(
        AccountClassification.REVENUE,
        NormalBalance.CREDIT,
        "Gross inflows from ordinary activities (Salary, Dividends, Capital Gains, Interest)."
    ),
    AccountClassification.EXPENSE: AccountTypeSpec(
        AccountClassification.EXPENSE,
        NormalBalance.DEBIT,
        "Outflows and costs incurred in generating revenue (Rent, Groceries, Utilities, Interest Expense)."
    ),
}
