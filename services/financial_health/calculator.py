"""
Financial Health Scoring & Metric Assessment Engine.
Evaluates 5 quantitative pillars:
1. Savings Rate (20 pts)
2. Emergency Reserves / Liquidity (20 pts)
3. Debt Burden / DTI Ratio (20 pts)
4. Budget Adherence (20 pts)
5. Investment Diversification (20 pts)
Produces an overall score (0-100) with grade and actionable feedback.
"""

from typing import Dict, Any, List
from core.math.decimal_utils import FinancialDecimal


class FinancialHealthCalculator:
    """Computes holistic financial health scores and supporting metrics."""

    @staticmethod
    def evaluate_health(
        monthly_income_cents: int,
        monthly_expenses_cents: int,
        liquid_assets_cents: int,
        total_debt_cents: int,
        budget_utilization_pct: float,
        asset_classes_count: int
    ) -> Dict[str, Any]:
        monthly_income = monthly_income_cents / 100.0
        monthly_expenses = monthly_expenses_cents / 100.0
        liquid_assets = liquid_assets_cents / 100.0
        total_debt = total_debt_cents / 100.0

        # 1. Savings Rate Score (0-20)
        # Ideal: >= 20%
        monthly_savings = max(0.0, monthly_income - monthly_expenses)
        savings_rate_pct = (monthly_savings / monthly_income * 100.0) if monthly_income > 0 else 0.0
        if savings_rate_pct >= 25.0:
            savings_score = 20
        elif savings_rate_pct >= 20.0:
            savings_score = 18
        elif savings_rate_pct >= 10.0:
            savings_score = 14
        elif savings_rate_pct > 0.0:
            savings_score = 8
        else:
            savings_score = 2

        # 2. Emergency Reserves Score (0-20)
        # Ideal: 6 months of living expenses
        emergency_months = (liquid_assets / monthly_expenses) if monthly_expenses > 0 else 0.0
        if emergency_months >= 6.0:
            emergency_score = 20
        elif emergency_months >= 3.0:
            emergency_score = 16
        elif emergency_months >= 1.0:
            emergency_score = 10
        else:
            emergency_score = 4

        # 3. Debt Burden Score (0-20)
        # Annualized DTI ratio
        annual_income = monthly_income * 12.0
        dti_ratio_pct = (total_debt / annual_income * 100.0) if annual_income > 0 else 0.0
        if total_debt == 0.0:
            debt_score = 20
        elif dti_ratio_pct < 30.0:
            debt_score = 18
        elif dti_ratio_pct < 50.0:
            debt_score = 14
        elif dti_ratio_pct < 100.0:
            debt_score = 10
        else:
            debt_score = 5

        # 4. Budget Adherence Score (0-20)
        # Ideal: <= 100% of budgeted envelope spent
        if budget_utilization_pct <= 90.0:
            budget_score = 20
        elif budget_utilization_pct <= 100.0:
            budget_score = 17
        elif budget_utilization_pct <= 110.0:
            budget_score = 12
        else:
            budget_score = 5

        # 5. Diversification Score (0-20)
        # Ideal: 4+ distinct asset classes (Equities, Fixed Income, Real Estate, Crypto, Cash)
        if asset_classes_count >= 4:
            diversification_score = 20
        elif asset_classes_count >= 3:
            diversification_score = 16
        elif asset_classes_count >= 2:
            diversification_score = 12
        else:
            diversification_score = 6

        total_score = savings_score + emergency_score + debt_score + budget_score + diversification_score

        if total_score >= 85:
            grade = "A (Excellent)"
            status = "HEALTHY"
        elif total_score >= 70:
            grade = "B (Good)"
            status = "STABLE"
        elif total_score >= 50:
            grade = "C (Fair)"
            status = "NEEDS_ATTENTION"
        else:
            grade = "D (Vulnerable)"
            status = "AT_RISK"

        return {
            "overall_score": total_score,
            "grade": grade,
            "status": status,
            "pillars": {
                "savings_rate": {
                    "score": savings_score,
                    "max": 20,
                    "value_pct": round(savings_rate_pct, 1),
                    "label": f"{savings_rate_pct:.1f}% monthly savings rate"
                },
                "emergency_fund": {
                    "score": emergency_score,
                    "max": 20,
                    "months": round(emergency_months, 1),
                    "label": f"{emergency_months:.1f} months of expenses covered"
                },
                "debt_burden": {
                    "score": debt_score,
                    "max": 20,
                    "dti_ratio_pct": round(dti_ratio_pct, 1),
                    "label": f"{dti_ratio_pct:.1f}% debt-to-income ratio"
                },
                "budget_adherence": {
                    "score": budget_score,
                    "max": 20,
                    "utilization_pct": round(budget_utilization_pct, 1),
                    "label": f"{budget_utilization_pct:.1f}% budget utilized"
                },
                "diversification": {
                    "score": diversification_score,
                    "max": 20,
                    "asset_classes": asset_classes_count,
                    "label": f"{asset_classes_count} asset classes held"
                }
            }
        }
