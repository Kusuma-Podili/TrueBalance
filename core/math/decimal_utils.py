"""
Enterprise Financial Math & Arbitrary Precision Decimal Engine.
Provides bank-grade arithmetic operations, IEEE 754 float drift mitigation,
strict rounding modes, and high-precision financial formulas.
"""

from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, ROUND_DOWN, InvalidOperation
from typing import Union, List, Tuple, Optional
import math

Numeric = Union[int, float, str, Decimal]

class FinancialDecimal:
    """
    Encapsulates arbitrary-precision decimal operations for enterprise financial ledgers.
    Enforces Bankers Rounding (ROUND_HALF_EVEN) by default to eliminate statistical bias.
    """
    
    DEFAULT_PRECISION: int = 4
    DISPLAY_PRECISION: int = 2
    INTERNAL_PRECISION: int = 8

    def __init__(self, value: Numeric = "0.0000"):
        if isinstance(value, FinancialDecimal):
            self._value: Decimal = value._value
        elif isinstance(value, Decimal):
            self._value = value
        elif isinstance(value, (int, str)):
            try:
                self._value = Decimal(str(value))
            except InvalidOperation as e:
                raise ValueError(f"Invalid numeric string for FinancialDecimal: {value}") from e
        elif isinstance(value, float):
            # Convert via string representation to avoid standard float binary rounding errors
            self._value = Decimal(str(value))
        else:
            raise TypeError(f"Unsupported type for FinancialDecimal: {type(value)}")

    @property
    def value(self) -> Decimal:
        """Returns the underlying Decimal value."""
        return self._value

    def quantize(self, places: int = 2, rounding=ROUND_HALF_EVEN) -> 'FinancialDecimal':
        """Quantizes the decimal to a specific number of decimal places."""
        target_exp = Decimal('10') ** -places
        return FinancialDecimal(self._value.quantize(target_exp, rounding=rounding))

    def to_cents(self) -> int:
        """Converts currency amount to integer minor units (cents / satoshis / pence)."""
        return int((self._value * Decimal('100')).quantize(Decimal('1'), rounding=ROUND_HALF_EVEN))

    @classmethod
    def from_cents(cls, cents: int) -> 'FinancialDecimal':
        """Creates FinancialDecimal from integer minor units."""
        return cls(Decimal(cents) / Decimal('100'))

    def is_zero(self) -> bool:
        """Returns True if the value is zero."""
        return self._value.is_zero()

    def is_positive(self) -> bool:
        """Returns True if strictly greater than zero."""
        return self._value > Decimal('0')

    def is_negative(self) -> bool:
        """Returns True if strictly less than zero."""
        return self._value < Decimal('0')

    def abs(self) -> 'FinancialDecimal':
        """Returns absolute value."""
        return FinancialDecimal(abs(self._value))

    # Operator Overloads
    def __add__(self, other: Union['FinancialDecimal', Numeric]) -> 'FinancialDecimal':
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return FinancialDecimal(self._value + other_val)

    def __radd__(self, other: Union['FinancialDecimal', Numeric]) -> 'FinancialDecimal':
        return self.__add__(other)

    def __sub__(self, other: Union['FinancialDecimal', Numeric]) -> 'FinancialDecimal':
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return FinancialDecimal(self._value - other_val)

    def __rsub__(self, other: Union['FinancialDecimal', Numeric]) -> 'FinancialDecimal':
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return FinancialDecimal(other_val - self._value)

    def __mul__(self, other: Union['FinancialDecimal', Numeric]) -> 'FinancialDecimal':
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return FinancialDecimal(self._value * other_val)

    def __rmul__(self, other: Union['FinancialDecimal', Numeric]) -> 'FinancialDecimal':
        return self.__mul__(other)

    def __truediv__(self, other: Union['FinancialDecimal', Numeric]) -> 'FinancialDecimal':
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        if other_val == Decimal('0'):
            raise ZeroDivisionError("Financial calculation division by zero.")
        return FinancialDecimal(self._value / other_val)

    def __rtruediv__(self, other: Union['FinancialDecimal', Numeric]) -> 'FinancialDecimal':
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        if self._value == Decimal('0'):
            raise ZeroDivisionError("Financial calculation division by zero.")
        return FinancialDecimal(other_val / self._value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (FinancialDecimal, int, float, str, Decimal)):
            return False
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return self._value == other_val

    def __lt__(self, other: Union['FinancialDecimal', Numeric]) -> bool:
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return self._value < other_val

    def __le__(self, other: Union['FinancialDecimal', Numeric]) -> bool:
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return self._value <= other_val

    def __gt__(self, other: Union['FinancialDecimal', Numeric]) -> bool:
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return self._value > other_val

    def __ge__(self, other: Union['FinancialDecimal', Numeric]) -> bool:
        other_val = other._value if isinstance(other, FinancialDecimal) else FinancialDecimal(other)._value
        return self._value >= other_val

    def __str__(self) -> str:
        return f"{self.quantize(self.DISPLAY_PRECISION)._value:,.2f}"

    def __repr__(self) -> str:
        return f"FinancialDecimal('{self._value}')"

    def format_currency(self, symbol: str = "$", include_symbol: bool = True) -> str:
        """Formats the financial decimal as a standard currency string."""
        formatted = f"{self.quantize(self.DISPLAY_PRECISION)._value:,.2f}"
        if include_symbol:
            if self.is_negative():
                return f"-{symbol}{abs(self).quantize(self.DISPLAY_PRECISION)._value:,.2f}"
            return f"{symbol}{formatted}"
        return formatted


class FinancialCalculators:
    """
    Mathematical implementations of standard financial formulas.
    """

    @staticmethod
    def compound_interest(
        principal: FinancialDecimal,
        annual_rate: FinancialDecimal,
        times_compounded: int,
        years: FinancialDecimal
    ) -> FinancialDecimal:
        """
        Calculates future value using standard compound interest: A = P(1 + r/n)^(nt)
        """
        p = principal.value
        r = annual_rate.value
        n = Decimal(times_compounded)
        t = years.value

        rate_per_period = r / n
        total_periods = n * t
        
        # High-precision exponentiation
        factor = (Decimal('1') + rate_per_period) ** total_periods
        future_value = p * factor
        return FinancialDecimal(future_value)

    @staticmethod
    def loan_payment(
        principal: FinancialDecimal,
        annual_rate: FinancialDecimal,
        num_payments: int
    ) -> FinancialDecimal:
        """
        Calculates fixed periodic payment for an amortized loan.
        Formula: M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
        """
        p = principal.value
        r = annual_rate.value
        n = Decimal(num_payments)
        
        # Monthly interest rate
        i = r / Decimal('12')
        if i == Decimal('0'):
            return FinancialDecimal(p / n)

        compounded = (Decimal('1') + i) ** n
        numerator = i * compounded
        denominator = compounded - Decimal('1')
        
        payment = p * (numerator / denominator)
        return FinancialDecimal(payment)

    @staticmethod
    def net_present_value(
        discount_rate: FinancialDecimal,
        cash_flows: List[FinancialDecimal]
    ) -> FinancialDecimal:
        """
        Calculates Net Present Value (NPV) of a series of cash flows.
        NPV = Sum( CF_t / (1 + r)^t )
        """
        r = discount_rate.value
        npv = Decimal('0')
        for t, cf in enumerate(cash_flows):
            t_dec = Decimal(t)
            discount_factor = (Decimal('1') + r) ** t_dec
            discounted_cf = cf.value / discount_factor
            npv += discounted_cf
        return FinancialDecimal(npv)

    @staticmethod
    def internal_rate_of_return(
        cash_flows: List[FinancialDecimal],
        precision: Decimal = Decimal('0.00001'),
        max_iterations: int = 1000
    ) -> Optional[FinancialDecimal]:
        """
        Solves for Internal Rate of Return (IRR) using Newton-Raphson approximation.
        """
        if not cash_flows or len(cash_flows) < 2:
            return None

        # Check if there is at least one negative and one positive cash flow
        has_positive = any(cf.is_positive() for cf in cash_flows)
        has_negative = any(cf.is_negative() for cf in cash_flows)
        if not (has_positive and has_negative):
            return None

        # Initial guess: 10% (0.10)
        rate = Decimal('0.10')

        for _ in range(max_iterations):
            npv = Decimal('0')
            d_npv = Decimal('0')  # Derivative of NPV with respect to rate

            for t, cf in enumerate(cash_flows):
                t_dec = Decimal(t)
                cf_val = cf.value
                denom = (Decimal('1') + rate) ** t_dec
                
                npv += cf_val / denom
                if t > 0:
                    d_npv -= (t_dec * cf_val) / ((Decimal('1') + rate) ** (t_dec + Decimal('1')))

            if abs(npv) < precision:
                return FinancialDecimal(rate)

            if d_npv == Decimal('0'):
                break

            new_rate = rate - (npv / d_npv)
            if abs(new_rate - rate) < precision:
                return FinancialDecimal(new_rate)
            rate = new_rate

        return FinancialDecimal(rate)
