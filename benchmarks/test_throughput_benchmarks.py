"""
High-Throughput Performance Benchmarks for General Ledger & Monte Carlo Engine.
"""

import time
import unittest
from core.ledger.double_entry import GeneralLedger
from core.ledger.journal_entry import JournalEntry
from core.ledger.types import AccountClassification
from core.math.decimal_utils import FinancialDecimal
from services.investments.monte_carlo import MonteCarloEngine


class TestFintechPerformanceBenchmarks(unittest.TestCase):

    def test_ledger_posting_throughput(self):
        """Benchmark posting 1,000 double-entry journal entries."""
        ledger = GeneralLedger()
        ledger.register_account("1010", "Cash", AccountClassification.ASSET)
        ledger.register_account("4010", "Revenue", AccountClassification.REVENUE)

        start_time = time.time()
        for idx in range(1000):
            entry = JournalEntry(f"bench_entry_{idx}", "2026-08-30", f"Benchmark Transaction #{idx}")
            entry.add_line("l1", "1010", "Cash", AccountClassification.ASSET, debit=FinancialDecimal("100.00"))
            entry.add_line("l2", "4010", "Revenue", AccountClassification.REVENUE, credit=FinancialDecimal("100.00"))
            ledger.post_entry(entry)

        elapsed = time.time() - start_time
        tx_per_second = 1000.0 / elapsed
        print(f"\n[Benchmark] Ledger Posting Speed: {tx_per_second:,.1f} entries/sec ({elapsed*1000:.2f} ms total)")
        self.assertGreater(tx_per_second, 500)  # Must achieve > 500 tx/sec

    def test_monte_carlo_execution_speed(self):
        """Benchmark 10,000-path Monte Carlo simulation runtime."""
        engine = MonteCarloEngine(seed=42)
        start_time = time.time()
        res = engine.simulate_wealth_trajectory(
            starting_wealth=150000.0,
            annual_contribution=15000.0,
            annual_withdrawal=5000.0,
            expected_annual_return=0.08,
            annual_volatility=0.16,
            years=25,
            iterations=10000
        )
        elapsed = time.time() - start_time
        print(f"[Benchmark] 10k Monte Carlo 25-Year Simulation: {elapsed*1000:.2f} ms")
        self.assertEqual(res["iterations"], 10000)
        self.assertLess(elapsed, 5.0)  # Must complete within 5 seconds


if __name__ == "__main__":
    unittest.main()
