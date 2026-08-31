"""
Multi-Currency Foreign Exchange (FX) & Triangulation Engine.
Maintains historical exchange rates, performs triangular conversions,
and calculates cross-currency transaction fees.
"""

from typing import Dict, Tuple, Optional
import time
from core.math.decimal_utils import FinancialDecimal
from core.math.currency import CurrencyCode


class FXEngine:
    """
    High-precision currency conversion engine using base currency triangulation (USD).
    """

    def __init__(self, base_currency: str = "USD"):
        self.base_currency = base_currency
        # Exchange rates relative to 1 USD
        self._rates_to_usd: Dict[str, FinancialDecimal] = {
            "USD": FinancialDecimal("1.000000"),
            "EUR": FinancialDecimal("1.085000"),  # 1 EUR = 1.085 USD
            "GBP": FinancialDecimal("1.275000"),  # 1 GBP = 1.275 USD
            "JPY": FinancialDecimal("0.006600"),  # 1 JPY = 0.0066 USD
            "CAD": FinancialDecimal("0.735000"),  # 1 CAD = 0.735 USD
            "AUD": FinancialDecimal("0.655000"),  # 1 AUD = 0.655 USD
            "CHF": FinancialDecimal("1.115000"),  # 1 CHF = 1.115 USD
            "CNY": FinancialDecimal("0.138000"),  # 1 CNY = 0.138 USD
            "INR": FinancialDecimal("0.012000"),  # 1 INR = 0.012 USD
            "SGD": FinancialDecimal("0.745000"),  # 1 SGD = 0.745 USD
            "BTC": FinancialDecimal("64250.000000"),
            "ETH": FinancialDecimal("3450.000000"),
        }

    def set_rate(self, currency: str, rate_in_usd: FinancialDecimal):
        """Sets currency rate in terms of USD."""
        self._rates_to_usd[currency.upper()] = rate_in_usd

    def get_rate(self, from_currency: str, to_currency: str) -> FinancialDecimal:
        """
        Calculates cross exchange rate: Rate(From -> To) = Rate(From -> USD) / Rate(To -> USD)
        """
        from_c = from_currency.upper()
        to_c = to_currency.upper()

        if from_c == to_c:
            return FinancialDecimal("1.000000")

        from_rate = self._rates_to_usd.get(from_c)
        to_rate = self._rates_to_usd.get(to_c)

        if not from_rate or not to_rate:
            raise KeyError(f"Exchange rate not available for pair {from_c}/{to_c}")

        return from_rate / to_rate

    def convert(
        self,
        amount: FinancialDecimal,
        from_currency: str,
        to_currency: str
    ) -> FinancialDecimal:
        """
        Converts an amount from one currency to another.
        """
        rate = self.get_rate(from_currency, to_currency)
        return (amount * rate).quantize(4)
