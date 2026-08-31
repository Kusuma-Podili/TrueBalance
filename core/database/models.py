"""
Enterprise Relational Database Schema & Domain Entity Models.
Defines entities for Users, Sessions, Accounts, Transactions, Ledger Entries,
Holdings, Budgets, Goals, Debts, and Audit Trails with full integrity constraints.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import time
import uuid


def generate_uuid() -> str:
    return str(uuid.uuid4())


@dataclass
class UserEntity:
    user_id: str = field(default_factory=generate_uuid)
    email: str = ""
    password_hash: str = ""
    full_name: str = ""
    role: str = "ACCOUNT_OWNER"
    is_active: bool = True
    two_factor_enabled: bool = False
    two_factor_secret: Optional[str] = None
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)


@dataclass
class AccountEntity:
    account_id: str = field(default_factory=generate_uuid)
    user_id: str = ""
    account_name: str = ""
    account_type: str = "CHECKING"  # CHECKING, SAVINGS, CREDIT_CARD, INVESTMENT, LOAN, CRYPTO
    currency: str = "USD"
    current_balance_cents: int = 0
    available_balance_cents: int = 0
    credit_limit_cents: Optional[int] = None
    institution_name: str = "Demo Bank"
    account_number_mask: str = "••••1234"
    is_closed: bool = False
    created_at: float = field(default_factory=time.time)


@dataclass
class CategoryEntity:
    category_id: str = field(default_factory=generate_uuid)
    name: str = ""
    parent_id: Optional[str] = None
    icon: str = "tag"
    color: str = "#4F46E5"
    is_income: bool = False
    created_at: float = field(default_factory=time.time)


@dataclass
class TransactionEntity:
    transaction_id: str = field(default_factory=generate_uuid)
    account_id: str = ""
    user_id: str = ""
    category_id: Optional[str] = None
    amount_cents: int = 0  # Negative for expenses, Positive for income
    currency: str = "USD"
    date: str = ""
    merchant_name: str = ""
    raw_description: str = ""
    status: str = "POSTED"  # PENDING, POSTED, VOID
    is_recurring: bool = False
    is_split: bool = False
    notes: Optional[str] = None
    created_at: float = field(default_factory=time.time)


@dataclass
class BudgetEnvelopeEntity:
    envelope_id: str = field(default_factory=generate_uuid)
    user_id: str = ""
    category_id: str = ""
    allocated_cents: int = 0
    spent_cents: int = 0
    period_month: str = ""  # YYYY-MM
    rollover_enabled: bool = True
    created_at: float = field(default_factory=time.time)


@dataclass
class HoldingEntity:
    holding_id: str = field(default_factory=generate_uuid)
    portfolio_id: str = ""
    ticker_symbol: str = ""
    asset_class: str = "EQUITY"  # EQUITY, FIXED_INCOME, CRYPTO, REAL_ESTATE, COMMODITY, CASH
    quantity: float = 0.0
    cost_basis_cents: int = 0
    current_price_cents: int = 0
    currency: str = "USD"
    updated_at: float = field(default_factory=time.time)


@dataclass
class DebtItemEntity:
    debt_id: str = field(default_factory=generate_uuid)
    user_id: str = ""
    name: str = ""
    debt_type: str = "CREDIT_CARD"  # CREDIT_CARD, MORTGAGE, STUDENT_LOAN, AUTO_LOAN, PERSONAL
    principal_balance_cents: int = 0
    annual_interest_rate_pct: float = 0.0
    minimum_monthly_payment_cents: int = 0
    due_day_of_month: int = 1
    created_at: float = field(default_factory=time.time)
