"""
Bank & Asset Account Management Service.
Handles account aggregation, lifecycle events, credit limit monitoring,
and balance snapshot synchronizations.
"""

from typing import List, Dict, Optional, Tuple
import time
from core.database.models import AccountEntity, generate_uuid
from core.math.decimal_utils import FinancialDecimal


class AccountType:
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"
    CREDIT_CARD = "CREDIT_CARD"
    INVESTMENT = "INVESTMENT"
    MORTGAGE = "MORTGAGE"
    STUDENT_LOAN = "STUDENT_LOAN"
    CRYPTO = "CRYPTO"


class AccountManager:
    """
    Manages user bank accounts, credit cards, and investment holdings.
    """

    def __init__(self):
        self._accounts: Dict[str, AccountEntity] = {}

    def create_account(
        self,
        user_id: str,
        name: str,
        account_type: str,
        currency: str = "USD",
        initial_balance_cents: int = 0,
        institution_name: str = "Community Bank",
        credit_limit_cents: Optional[int] = None
    ) -> AccountEntity:
        acc = AccountEntity(
            account_id=f"acc_{generate_uuid()[:12]}",
            user_id=user_id,
            account_name=name,
            account_type=account_type,
            currency=currency,
            current_balance_cents=initial_balance_cents,
            available_balance_cents=initial_balance_cents,
            credit_limit_cents=credit_limit_cents,
            institution_name=institution_name
        )
        self._accounts[acc.account_id] = acc
        return acc

    def get_account(self, account_id: str) -> Optional[AccountEntity]:
        return self._accounts.get(account_id)

    def list_user_accounts(self, user_id: str) -> List[AccountEntity]:
        return [acc for acc in self._accounts.values() if acc.user_id == user_id and not acc.is_closed]

    def update_balance(self, account_id: str, delta_cents: int) -> AccountEntity:
        acc = self._accounts.get(account_id)
        if not acc:
            raise KeyError(f"Account {account_id} not found.")
        acc.current_balance_cents += delta_cents
        acc.available_balance_cents += delta_cents
        return acc

    def compute_net_worth(self, user_id: str) -> Tuple[FinancialDecimal, FinancialDecimal, FinancialDecimal]:
        """
        Computes (Total Assets, Total Liabilities, Net Worth).
        """
        accounts = self.list_user_accounts(user_id)
        total_assets = 0
        total_liabilities = 0

        for acc in accounts:
            if acc.account_type in (AccountType.CHECKING, AccountType.SAVINGS, AccountType.INVESTMENT, AccountType.CRYPTO):
                total_assets += max(0, acc.current_balance_cents)
            elif acc.account_type in (AccountType.CREDIT_CARD, AccountType.MORTGAGE, AccountType.STUDENT_LOAN):
                total_liabilities += abs(acc.current_balance_cents)

        assets_dec = FinancialDecimal.from_cents(total_assets)
        liabilities_dec = FinancialDecimal.from_cents(total_liabilities)
        net_worth_dec = assets_dec - liabilities_dec
        return assets_dec, liabilities_dec, net_worth_dec
