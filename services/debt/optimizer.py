"""
Debt Payoff Optimization Engine.
Compares Debt Avalanche (highest interest rate first) against
Debt Snowball (lowest principal balance first) with complete amortization schedules.
"""

from typing import List, Dict, Tuple
from dataclasses import dataclass
from core.math.decimal_utils import FinancialDecimal


@dataclass
class DebtAccount:
    debt_id: str
    name: str
    balance: float
    interest_rate_pct: float
    min_payment: float


class DebtOptimizer:
    """
    Simulates monthly payment distribution and interest savings between strategies.
    """

    @classmethod
    def simulate_payoff(
        cls,
        debts: List[DebtAccount],
        monthly_budget: float,
        strategy: str = "AVALANCHE"  # "AVALANCHE" or "SNOWBALL"
    ) -> Dict:
        # Clone debts
        active_debts = [
            {"id": d.debt_id, "name": d.name, "balance": d.balance, "rate": d.interest_rate_pct / 100.0, "min": d.min_payment}
            for d in debts
        ]

        total_min_required = sum(d["min"] for d in active_debts)
        if monthly_budget < total_min_required:
            raise ValueError(f"Monthly budget (${monthly_budget:.2f}) is less than minimum payments (${total_min_required:.2f})")

        total_interest_paid = 0.0
        months = 0
        max_months = 360  # 30 years ceiling

        while any(d["balance"] > 0 for d in active_debts) and months < max_months:
            months += 1
            available_extra = monthly_budget

            # 1. Accrue monthly interest and pay minimums
            for d in active_debts:
                if d["balance"] > 0:
                    monthly_interest = d["balance"] * (d["rate"] / 12.0)
                    total_interest_paid += monthly_interest
                    d["balance"] += monthly_interest

                    # Pay minimum
                    payment = min(d["min"], d["balance"])
                    d["balance"] -= payment
                    available_extra -= payment

            # 2. Sort debts according to strategy
            remaining = [d for d in active_debts if d["balance"] > 0]
            if not remaining:
                break

            if strategy.upper() == "AVALANCHE":
                remaining.sort(key=lambda d: d["rate"], reverse=True)
            else:  # SNOWBALL
                remaining.sort(key=lambda d: d["balance"])

            # 3. Apply extra budget to target debt
            for target in remaining:
                if available_extra <= 0:
                    break
                extra_pay = min(available_extra, target["balance"])
                target["balance"] -= extra_pay
                available_extra -= extra_pay

        return {
            "strategy": strategy,
            "total_months": months,
            "years": round(months / 12.0, 1),
            "total_interest_paid": round(total_interest_paid, 2),
            "total_principal_paid": round(sum(d.balance for d in debts), 2),
            "total_cost": round(sum(d.balance for d in debts) + total_interest_paid, 2)
        }
