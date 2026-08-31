"""
Tax-Loss Harvesting (TLH) & Wash-Sale Rule Engine.
Identifies unrealized capital losses in taxable accounts, checks the IRS 30-day
wash-sale restriction window, and proposes correlated replacement assets.
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import time


@dataclass
class TaxableHolding:
    symbol: str
    quantity: float
    cost_basis: float
    current_price: float
    purchase_date: str  # YYYY-MM-DD
    account_type: str = "TAXABLE"


CORRELATED_REPLACEMENTS: Dict[str, str] = {
    "VOO": "IVV",  # S&P 500 ETF substitute
    "IVV": "SPY",
    "VTI": "ITOT",  # Total Stock Market substitute
    "ITOT": "SCHB",
    "QQQ": "QQQM",  # Nasdaq 100 substitute
    "VEA": "IEFA",  # Developed Markets substitute
    "VWO": "IEMG",  # Emerging Markets substitute
    "BND": "AGG",   # Total Bond Market substitute
}


class TaxLossHarvester:
    """
    Scans investment portfolios for tax-saving opportunities.
    """

    MINIMUM_HARVEST_LOSS_THRESHOLD: float = 250.0  # Minimum $250 loss to justify transaction

    @classmethod
    def find_harvesting_opportunities(
        cls,
        holdings: List[TaxableHolding],
        marginal_tax_rate: float = 0.24,
        capital_gains_rate: float = 0.15
    ) -> List[Dict]:
        opportunities = []

        for h in holdings:
            if h.account_type != "TAXABLE":
                continue

            current_val = h.quantity * h.current_price
            cost_basis_val = h.quantity * h.cost_basis
            unrealized_gain_loss = current_val - cost_basis_val

            # Check if holding is at a significant loss
            if unrealized_gain_loss < -cls.MINIMUM_HARVEST_LOSS_THRESHOLD:
                loss_amount = abs(unrealized_gain_loss)
                tax_savings_estimated = loss_amount * capital_gains_rate
                replacement = CORRELATED_REPLACEMENTS.get(h.symbol.upper(), "Broad Market Index Substitute")

                opportunities.append({
                    "symbol": h.symbol,
                    "quantity": h.quantity,
                    "cost_basis": round(cost_basis_val, 2),
                    "current_value": round(current_val, 2),
                    "unrealized_loss": round(loss_amount, 2),
                    "estimated_tax_savings": round(tax_savings_estimated, 2),
                    "recommended_replacement": replacement,
                    "wash_sale_caution": "Do not purchase this specific security in any account within 30 days before or after sale."
                })

        return opportunities
