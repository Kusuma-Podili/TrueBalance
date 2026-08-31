"""
Test Suite 2: Arbitrary Precision Decimal Math & Financial Formulas.
"""

import unittest
from decimal import Decimal
from core.math.decimal_utils import FinancialDecimal, FinancialCalculators


class TestFinancialMath(unittest.TestCase):

    def test_bankers_rounding_precision(self):
        """Verify Bankers Rounding (ROUND_HALF_EVEN) avoids statistical accumulation drift."""
        d1 = FinancialDecimal("2.545").quantize(2)
        d2 = FinancialDecimal("2.535").quantize(2)
        self.assertEqual(str(d1), "2.54")
        self.assertEqual(str(d2), "2.54")

    def test_compound_interest_calculation(self):
        """Verify compound interest formula: A = P(1 + r/n)^(nt)."""
        principal = FinancialDecimal("10000.00")
        rate = FinancialDecimal("0.05")  # 5% annual
        years = FinancialDecimal("10")
        times_compounded = 12  # Monthly

        fv = FinancialCalculators.compound_interest(principal, rate, times_compounded, years)
        # Expected: ~16,470.09
        self.assertAlmostEqual(float(fv.value), 16470.09, delta=0.5)

    def test_loan_payment_amortization(self):
        """Verify standard monthly loan payment calculation."""
        principal = FinancialDecimal("300000.00")  # $300k mortgage
        rate = FinancialDecimal("0.06")  # 6%
        num_payments = 360  # 30 years

        payment = FinancialCalculators.loan_payment(principal, rate, num_payments)
        # Expected monthly payment: ~$1,798.65
        self.assertAlmostEqual(float(payment.value), 1798.65, delta=0.5)

    def test_net_present_value(self):
        """Verify NPV calculation across multi-year cash flows."""
        discount_rate = FinancialDecimal("0.10")  # 10%
        cash_flows = [
            FinancialDecimal("-1000.00"),  # Initial investment
            FinancialDecimal("300.00"),
            FinancialDecimal("400.00"),
            FinancialDecimal("500.00"),
        ]
        npv = FinancialCalculators.net_present_value(discount_rate, cash_flows)
        # Expected: ~$48.16
        self.assertAlmostEqual(float(npv.value), 48.16, delta=0.5)


if __name__ == "__main__":
    unittest.main()
