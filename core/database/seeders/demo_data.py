"""
Deterministic Seed Data Generator for Fintech Platform.
Populates standard chart of accounts, users, mock banking institutions,
and baseline ledger configurations.
"""

from typing import List, Dict, Any
from core.database.models import UserEntity, AccountEntity, CategoryEntity
from core.security.crypto import EnterpriseCrypto
from core.ledger.double_entry import GeneralLedger
from core.ledger.types import AccountClassification


def get_default_categories() -> List[Dict[str, Any]]:
    return [
        {"id": "cat_salary", "name": "Salary & Wages", "is_income": True, "icon": "briefcase", "color": "#10B981"},
        {"id": "cat_invest", "name": "Investment Income", "is_income": True, "icon": "trending-up", "color": "#059669"},
        {"id": "cat_housing", "name": "Housing & Rent", "is_income": False, "icon": "home", "color": "#EF4444"},
        {"id": "cat_food", "name": "Groceries & Dining", "is_income": False, "icon": "shopping-bag", "color": "#F59E0B"},
        {"id": "cat_transit", "name": "Transportation", "is_income": False, "icon": "truck", "color": "#3B82F6"},
        {"id": "cat_utilities", "name": "Utilities & Bills", "is_income": False, "icon": "zap", "color": "#6366F1"},
        {"id": "cat_health", "name": "Healthcare & Medical", "is_income": False, "icon": "activity", "color": "#EC4899"},
        {"id": "cat_entertainment", "name": "Entertainment & Leisure", "is_income": False, "icon": "film", "color": "#8B5CF6"},
    ]


def initialize_chart_of_accounts(ledger: GeneralLedger):
    """
    Standard enterprise Chart of Accounts (COA) initialization.
    """
    # 1000 - Assets
    ledger.register_account("1010", "Cash & Checking Accounts", AccountClassification.ASSET)
    ledger.register_account("1020", "High-Yield Savings Accounts", AccountClassification.ASSET)
    ledger.register_account("1030", "Brokerage & Equity Holdings", AccountClassification.ASSET)
    ledger.register_account("1040", "Crypto Assets", AccountClassification.ASSET)
    
    # 2000 - Liabilities
    ledger.register_account("2010", "Credit Card Balances", AccountClassification.LIABILITY)
    ledger.register_account("2020", "Mortgage Payable", AccountClassification.LIABILITY)
    ledger.register_account("2030", "Student Loan Debt", AccountClassification.LIABILITY)
    
    # 3000 - Equity
    ledger.register_account("3010", "Owner's Net Worth / Retained Capital", AccountClassification.EQUITY)
    
    # 4000 - Revenues
    ledger.register_account("4010", "Employment Compensation", AccountClassification.REVENUE)
    ledger.register_account("4020", "Dividend & Interest Inflows", AccountClassification.REVENUE)
    ledger.register_account("4030", "Realized Capital Gains", AccountClassification.REVENUE)
    
    # 5000 - Expenses
    ledger.register_account("5010", "Housing, Rent & HOA", AccountClassification.EXPENSE)
    ledger.register_account("5020", "Food & Sustenance", AccountClassification.EXPENSE)
    ledger.register_account("5030", "Transportation & Fuel", AccountClassification.EXPENSE)
    ledger.register_account("5040", "Utilities & Telecommunications", AccountClassification.EXPENSE)
    ledger.register_account("5050", "Healthcare & Insurance", AccountClassification.EXPENSE)
    ledger.register_account("5060", "Leisure & Discretionary", AccountClassification.EXPENSE)
    ledger.register_account("5070", "Debt Interest Incurred", AccountClassification.EXPENSE)


def create_demo_user() -> UserEntity:
    return UserEntity(
        user_id="usr_enterprise_demo_01",
        email="alex.morgan@fintech-enterprise.io",
        password_hash=EnterpriseCrypto.hash_password("FintechSecure#2026"),
        full_name="Alex Morgan, CFA",
        role="ACCOUNT_OWNER",
        is_active=True,
        two_factor_enabled=True
    )
