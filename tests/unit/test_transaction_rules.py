"""
Test Suite 4: Transaction Processing, Rules Engine & Merchant Normalization.
"""

import unittest
from services.transactions.rules_engine import SmartCategorizer
from services.transactions.merchant_normalizer import MerchantNormalizer
from services.fx.engine import FXEngine
from core.math.decimal_utils import FinancialDecimal


class TestTransactionRules(unittest.TestCase):

    def setUp(self):
        self.categorizer = SmartCategorizer()
        self.fx = FXEngine()

    def test_merchant_categorization_heuristics(self):
        """Verify automatic rule-based categorization for various merchants."""
        cat1, conf1 = self.categorizer.categorize("WHOLE FOODS MARKET STORE 102", "Whole Foods", 8500)
        self.assertEqual(cat1, "cat_food")
        self.assertGreater(conf1, 0.5)

        cat2, conf2 = self.categorizer.categorize("GUSTO PAYROLL DIRECT DEP", "Gusto", 400000)
        self.assertEqual(cat2, "cat_salary")

        cat3, conf3 = self.categorizer.categorize("NETFLIX.COM PAYMENT", "Netflix", 1999)
        self.assertEqual(cat3, "cat_entertainment")

    def test_merchant_name_cleaning(self):
        """Verify cleanup of terminal numbers and noisy descriptions."""
        clean1 = MerchantNormalizer.normalize("SQ *BLUE BOTTLE COFFEE #104 SAN FRANCISCO CA")
        self.assertEqual(clean1, "Blue Bottle Coffee")

        clean2 = MerchantNormalizer.normalize("AMZN Mktp US*9X44Y2")
        self.assertEqual(clean2, "Amazon")

    def test_multi_currency_fx_conversion(self):
        """Verify cross-currency triangulation and conversion."""
        usd_amount = FinancialDecimal("100.00")
        eur_amount = self.fx.convert(usd_amount, "USD", "EUR")
        # 1 EUR = 1.085 USD -> 100 USD = 92.1659 EUR
        self.assertAlmostEqual(float(eur_amount.value), 92.17, delta=0.1)


if __name__ == "__main__":
    unittest.main()
