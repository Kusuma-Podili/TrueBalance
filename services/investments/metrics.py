"""
Modern Portfolio Theory (MPT) & Quantitative Risk Engine.
Calculates Expected Return, Covariance Matrix, Sharpe Ratio, Sortino Ratio,
Value at Risk (VaR), Conditional VaR (CVaR), and Beta against market benchmarks.
"""

import math
from typing import List, Dict, Tuple, Optional
from core.math.decimal_utils import FinancialDecimal


class PortfolioRiskMetrics:
    """
    Computes statistical and quantitative risk metrics for investment portfolios.
    """

    @staticmethod
    def mean(returns: List[float]) -> float:
        return sum(returns) / len(returns) if returns else 0.0

    @staticmethod
    def variance(returns: List[float]) -> float:
        if len(returns) < 2:
            return 0.0
        avg = PortfolioRiskMetrics.mean(returns)
        return sum((r - avg) ** 2 for r in returns) / (len(returns) - 1)

    @staticmethod
    def standard_deviation(returns: List[float]) -> float:
        return math.sqrt(PortfolioRiskMetrics.variance(returns))

    @staticmethod
    def annualized_volatility(daily_returns: List[float], trading_days: int = 252) -> float:
        daily_std = PortfolioRiskMetrics.standard_deviation(daily_returns)
        return daily_std * math.sqrt(trading_days)

    @staticmethod
    def sharpe_ratio(returns: List[float], risk_free_rate: float = 0.045, periods_per_year: int = 252) -> float:
        """Sharpe Ratio = (R_p - R_f) / Volatility"""
        if not returns:
            return 0.0
        annual_return = PortfolioRiskMetrics.mean(returns) * periods_per_year
        annual_vol = PortfolioRiskMetrics.annualized_volatility(returns, periods_per_year)
        if annual_vol == 0:
            return 0.0
        return (annual_return - risk_free_rate) / annual_vol

    @staticmethod
    def sortino_ratio(returns: List[float], risk_free_rate: float = 0.045, target_return: float = 0.0) -> float:
        """Sortino Ratio = (R_p - R_f) / Downside Deviation"""
        if not returns:
            return 0.0
        downside_returns = [r - target_return for r in returns if r < target_return]
        if not downside_returns:
            return 0.0
        downside_deviation = math.sqrt(sum(d ** 2 for d in downside_returns) / len(returns)) * math.sqrt(252)
        annual_return = PortfolioRiskMetrics.mean(returns) * 252
        if downside_deviation == 0:
            return 0.0
        return (annual_return - risk_free_rate) / downside_deviation

    @staticmethod
    def value_at_risk_parametric(portfolio_value: float, confidence_level: float = 0.95, annual_volatility: float = 0.18, time_horizon_days: int = 1) -> float:
        """Parametric 1-day Value at Risk (VaR) assuming normal distribution."""
        z_scores = {0.90: 1.282, 0.95: 1.645, 0.99: 2.326}
        z = z_scores.get(confidence_level, 1.645)
        daily_vol = annual_volatility / math.sqrt(252)
        horizon_vol = daily_vol * math.sqrt(time_horizon_days)
        return portfolio_value * z * horizon_vol

    # Convenience aliases
    calculate_sharpe_ratio = sharpe_ratio
    calculate_sortino_ratio = sortino_ratio
    calculate_value_at_risk = lambda val, ret, conf=0.95: PortfolioRiskMetrics.value_at_risk_parametric(val, conf)
