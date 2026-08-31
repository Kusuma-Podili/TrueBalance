"""
Test Suite 3: Stochastic Monte Carlo Simulation Properties & Distributions.
"""

import unittest
from services.investments.monte_carlo import MonteCarloEngine


class TestMonteCarloSimulation(unittest.TestCase):

    def setUp(self):
        self.engine = MonteCarloEngine(seed=42)

    def test_simulation_generates_valid_percentiles(self):
        """Verify that Monte Carlo produces monotonically increasing percentiles (p10 <= p50 <= p90)."""
        result = self.engine.simulate_wealth_trajectory(
            starting_wealth=100000.0,
            annual_contribution=10000.0,
            annual_withdrawal=0.0,
            expected_annual_return=0.07,
            annual_volatility=0.15,
            years=10,
            iterations=500
        )

        self.assertGreaterEqual(result["success_rate_percentage"], 90.0)
        self.assertLessEqual(result["worst_10_percentile_terminal_wealth"], result["median_terminal_wealth"])
        self.assertLessEqual(result["median_terminal_wealth"], result["best_10_percentile_terminal_wealth"])
        self.assertEqual(len(result["percentile_trajectory"]["p50_median"]), 11)

    def test_depleting_portfolio_has_lower_success_rate(self):
        """Verify that high withdrawal rates lower plan success probability."""
        result = self.engine.simulate_wealth_trajectory(
            starting_wealth=100000.0,
            annual_contribution=0.0,
            annual_withdrawal=30000.0,  # Unsustainable 30% withdrawal
            expected_annual_return=0.05,
            annual_volatility=0.20,
            years=15,
            iterations=500
        )
        self.assertLess(result["success_rate_percentage"], 50.0)


if __name__ == "__main__":
    unittest.main()
