"""
Abstract Protocol for OpenBanking Providers (Plaid, Teller, MX, Salt Edge).
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class OpenBankingAdapter(ABC):
    @abstractmethod
    def exchange_public_token(self, public_token: str) -> str:
        """Exchanges public link token for persistent access token."""
        pass

    @abstractmethod
    def get_accounts(self, access_token: str) -> List[Dict[str, Any]]:
        """Fetches list of accounts from the financial institution."""
        pass

    @abstractmethod
    def get_transactions(self, access_token: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """Fetches transactions within date range."""
        pass
