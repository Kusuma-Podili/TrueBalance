"""
Mock Plaid API Adapter for Sandbox & Enterprise Integration.
"""

from typing import List, Dict, Any
from adapters.banking.base import OpenBankingAdapter
import time


class MockPlaidAdapter(OpenBankingAdapter):
    """
    Simulates Plaid Link and Core Transactions API.
    """

    def exchange_public_token(self, public_token: str) -> str:
        return f"access-sandbox-{public_token[:8]}-plaid-live"

    def get_accounts(self, access_token: str) -> List[Dict[str, Any]]:
        return [
            {
                "account_id": "plaid_acc_chk_01",
                "name": "Plaid Premier Checking",
                "type": "depository",
                "subtype": "checking",
                "balance_current": 5420.50,
                "balance_available": 5300.00,
                "currency": "USD"
            },
            {
                "account_id": "plaid_acc_sav_02",
                "name": "Plaid High Yield Savings",
                "type": "depository",
                "subtype": "savings",
                "balance_current": 28450.00,
                "balance_available": 28450.00,
                "currency": "USD"
            },
            {
                "account_id": "plaid_acc_cc_03",
                "name": "Plaid Diamond Rewards Credit Card",
                "type": "credit",
                "subtype": "credit card",
                "balance_current": 1240.25,
                "limit": 10000.00,
                "currency": "USD"
            }
        ]

    def get_transactions(self, access_token: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        return [
            {
                "transaction_id": "plaid_tx_001",
                "account_id": "plaid_acc_chk_01",
                "amount": -84.20,
                "date": "2026-08-25",
                "name": "Whole Foods Market #1029",
                "merchant_name": "Whole Foods Market",
                "category": ["Food and Drink", "Groceries"],
                "pending": False
            },
            {
                "transaction_id": "plaid_tx_002",
                "account_id": "plaid_acc_chk_01",
                "amount": -18.50,
                "date": "2026-08-26",
                "name": "Uber *Trip San Francisco",
                "merchant_name": "Uber",
                "category": ["Travel", "Ride Share"],
                "pending": False
            },
            {
                "transaction_id": "plaid_tx_003",
                "account_id": "plaid_acc_chk_01",
                "amount": 4200.00,
                "date": "2026-08-28",
                "name": "Acme Corp DIRECT DEP PAYROLL",
                "merchant_name": "Acme Corp",
                "category": ["Transfer", "Payroll"],
                "pending": False
            }
        ]
