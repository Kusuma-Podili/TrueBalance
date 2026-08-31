"""
Discounted Cash Flow (DCF) & Enterprise Intrinsic Valuation Model.
Computes Free Cash Flows to Firm (FCFF), Weighted Average Cost of Capital (WACC),
and Terminal Value using Gordon Growth or Exit Multiple methods.
"""

from typing import List, Dict
from core.math.decimal_utils import FinancialDecimal


class DCFValuationEngine:
    """
    Computes enterprise and equity intrinsic value from projected free cash flows.
    """

    @classmethod
    def calculate_wacc(
        cls,
        equity_market_cap: float,
        total_debt: float,
        cost_of_equity: float,
        cost_of_debt: float,
        corporate_tax_rate: float
    ) -> float:
        total_capital = equity_market_cap + total_debt
        if total_capital == 0:
            return cost_of_equity
        we = equity_market_cap / total_capital
        wd = total_debt / total_capital
        after_tax_cost_of_debt = cost_of_debt * (1.0 - corporate_tax_rate)
        return (we * cost_of_equity) + (wd * after_tax_cost_of_debt)

    @classmethod
    def calculate_intrinsic_value(
        cls,
        projected_fcf: List[float],
        wacc: float,
        terminal_growth_rate: float,
        net_debt: float,
        shares_outstanding: float
    ) -> Dict:
        discounted_fcfs = []
        cumulative_pv = 0.0

        for t, fcf in enumerate(projected_fcf, start=1):
            pv = fcf / ((1.0 + wacc) ** t)
            discounted_fcfs.append(pv)
            cumulative_pv += pv

        # Terminal Value via Gordon Growth
        last_fcf = projected_fcf[-1]
        terminal_value = (last_fcf * (1.0 + terminal_growth_rate)) / (wacc - terminal_growth_rate)
        pv_terminal_value = terminal_value / ((1.0 + wacc) ** len(projected_fcf))

        enterprise_value = cumulative_pv + pv_terminal_value
        equity_value = enterprise_value - net_debt
        per_share_value = equity_value / shares_outstanding if shares_outstanding > 0 else 0.0

        return {
            "wacc": round(wacc, 4),
            "cumulative_pv_fcf": round(cumulative_pv, 2),
            "pv_terminal_value": round(pv_terminal_value, 2),
            "enterprise_value": round(enterprise_value, 2),
            "equity_value": round(equity_value, 2),
            "intrinsic_value_per_share": round(per_share_value, 2)
        }
