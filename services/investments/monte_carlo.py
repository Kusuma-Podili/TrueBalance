"""
Monte Carlo Retirement & Wealth Simulation Engine.
Runs 10,000 stochastic paths using Geometric Brownian Motion (GBM) to forecast
retirement portfolio longevity, success probability, and percentile cones.
"""

import math
import random
from typing import List, Dict, Tuple, Optional


class MonteCarloEngine:
    """
    Simulates portfolio trajectories across thousands of stochastic market iterations.
    """

    def __init__(self, seed: Optional[int] = 42):
        if seed is not None:
            random.seed(seed)

    def simulate_wealth_trajectory(
        self,
        starting_wealth: float,
        annual_contribution: float,
        annual_withdrawal: float,
        expected_annual_return: float,
        annual_volatility: float,
        years: int,
        iterations: int = 1000
    ) -> Dict:
        """
        Simulates wealth paths using Geometric Brownian Motion.
        """
        dt = 1.0  # 1 year step
        mu = expected_annual_return
        sigma = annual_volatility
        drift = (mu - 0.5 * (sigma ** 2)) * dt
        shock_factor = sigma * math.sqrt(dt)

        all_paths: List[List[float]] = []
        terminal_wealths: List[float] = []
        survived_count = 0

        for _ in range(iterations):
            path = [starting_wealth]
            current_wealth = starting_wealth

            for year in range(1, years + 1):
                # Standard normal random variable using Box-Muller transform
                z = random.gauss(0, 1)
                growth_factor = math.exp(drift + shock_factor * z)
                current_wealth = (current_wealth + annual_contribution - annual_withdrawal) * growth_factor
                current_wealth = max(0.0, current_wealth)
                path.append(round(current_wealth, 2))

            all_paths.append(path)
            terminal_wealths.append(current_wealth)
            if current_wealth > 0:
                survived_count += 1

        terminal_wealths.sort()
        p10_idx = int(0.10 * iterations)
        p25_idx = int(0.25 * iterations)
        p50_idx = int(0.50 * iterations)
        p75_idx = int(0.75 * iterations)
        p90_idx = int(0.90 * iterations)

        # Compute percentile paths year by year
        percentile_paths = {
            "p10": [],
            "p25": [],
            "p50_median": [],
            "p75": [],
            "p90": []
        }

        for y in range(years + 1):
            year_values = sorted([all_paths[i][y] for i in range(iterations)])
            percentile_paths["p10"].append(year_values[p10_idx])
            percentile_paths["p25"].append(year_values[p25_idx])
            percentile_paths["p50_median"].append(year_values[p50_idx])
            percentile_paths["p75"].append(year_values[p75_idx])
            percentile_paths["p90"].append(year_values[p90_idx])

        success_rate_pct = (survived_count / iterations) * 100.0

        return {
            "iterations": iterations,
            "years": years,
            "success_rate_percentage": round(success_rate_pct, 2),
            "median_terminal_wealth": round(terminal_wealths[p50_idx], 2),
            "worst_10_percentile_terminal_wealth": round(terminal_wealths[p10_idx], 2),
            "best_10_percentile_terminal_wealth": round(terminal_wealths[p90_idx], 2),
            "percentile_trajectory": percentile_paths
        }
