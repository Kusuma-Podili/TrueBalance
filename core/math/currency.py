"""
ISO 4217 Currency Standards and Precision Definitions.
Provides currency models, fractional subunit specs, and symbol lookups.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Optional


class CurrencyCode(str, Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    CAD = "CAD"
    AUD = "AUD"
    CHF = "CHF"
    CNY = "CNY"
    INR = "INR"
    SGD = "SGD"
    BTC = "BTC"
    ETH = "ETH"


@dataclass(frozen=True)
class CurrencySpec:
    code: CurrencyCode
    name: str
    symbol: str
    minor_unit_digits: int
    subunit_name: str
    is_fiat: bool = True


CURRENCY_REGISTRY: Dict[CurrencyCode, CurrencySpec] = {
    CurrencyCode.USD: CurrencySpec(CurrencyCode.USD, "US Dollar", "$", 2, "Cent", True),
    CurrencyCode.EUR: CurrencySpec(CurrencyCode.EUR, "Euro", "€", 2, "Cent", True),
    CurrencyCode.GBP: CurrencySpec(CurrencyCode.GBP, "British Pound", "£", 2, "Penny", True),
    CurrencyCode.JPY: CurrencySpec(CurrencyCode.JPY, "Japanese Yen", "¥", 0, "Yen", True),
    CurrencyCode.CAD: CurrencySpec(CurrencyCode.CAD, "Canadian Dollar", "CA$", 2, "Cent", True),
    CurrencyCode.AUD: CurrencySpec(CurrencyCode.AUD, "Australian Dollar", "A$", 2, "Cent", True),
    CurrencyCode.CHF: CurrencySpec(CurrencyCode.CHF, "Swiss Franc", "CHF", 2, "Rappen", True),
    CurrencyCode.CNY: CurrencySpec(CurrencyCode.CNY, "Chinese Yuan", "¥", 2, "Fen", True),
    CurrencyCode.INR: CurrencySpec(CurrencyCode.INR, "Indian Rupee", "₹", 2, "Paisa", True),
    CurrencyCode.SGD: CurrencySpec(CurrencyCode.SGD, "Singapore Dollar", "S$", 2, "Cent", True),
    CurrencyCode.BTC: CurrencySpec(CurrencyCode.BTC, "Bitcoin", "₿", 8, "Satoshi", False),
    CurrencyCode.ETH: CurrencySpec(CurrencyCode.ETH, "Ethereum", "Ξ", 18, "Wei", False),
}


class CurrencyHelper:
    @staticmethod
    def get_spec(code: str) -> CurrencySpec:
        try:
            curr = CurrencyCode(code.upper())
            return CURRENCY_REGISTRY[curr]
        except (ValueError, KeyError):
            return CurrencySpec(CurrencyCode.USD, f"Unknown ({code})", code, 2, "Unit", True)

    @staticmethod
    def format_amount(amount_dec, currency_code: str = "USD") -> str:
        spec = CurrencyHelper.get_spec(currency_code)
        val = round(float(amount_dec), spec.minor_unit_digits)
        if spec.minor_unit_digits == 0:
            return f"{spec.symbol}{int(val):,}"
        return f"{spec.symbol}{val:,.{spec.minor_unit_digits}f}"
