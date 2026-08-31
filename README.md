# Enterprise Personal Finance Manager (PFM) Platform

A production-grade, enterprise fintech application featuring double-entry general ledger bookkeeping, modern portfolio theory risk analytics (Sharpe ratio, Sortino, VaR, Monte Carlo), zero-based budgeting, automated tax-loss harvesting, and multi-currency transaction intelligence.

---

## Key Features

1. **Double-Entry General Ledger**:
   - Built on strict US GAAP / IFRS accounting standards.
   - Enforces mathematical balance invariants: `Sum(Debits) == Sum(Credits)`.
   - Real-time Trial Balance, Balance Sheet, and Income Statement generation.

2. **Quantitative Risk & Portfolio Intelligence**:
   - **Modern Portfolio Theory (MPT)**: Covariance matrix, Markowitz efficient frontier, Sharpe, Sortino, and Treynor ratios.
   - **Monte Carlo Simulation**: 10,000-path stochastic retirement longevity simulator with percentile fan charts.
   - **Valuation Models**: Discounted Cash Flow (DCF), Dividend Discount Model (DDM), and Black-Scholes options pricing.

3. **Transaction Engine & Smart Categorization**:
   - Dynamic regex and heuristics rules engine with confidence scoring.
   - Merchant name normalizer and recurring subscription detector.
   - Real-time multi-currency FX triangulation across 12+ fiat and crypto currencies.

4. **Tax Optimization & Debt Payoff**:
   - Automated Tax-Loss Harvesting (TLH) with IRS 30-day wash-sale rule prevention.
   - Debt Avalanche vs. Snowball amortization optimizer.

5. **Security & Cryptography**:
   - NIST-compliant PBKDF2-HMAC-SHA512 password hashing.
   - Cryptographic tamper-evident audit ledger with SHA-256 hash chaining.
   - Fine-grained Role-Based Access Control (RBAC) matrix and JWT session management.

---

## Running the Automated Test Suite

```bash
# Run all unit and integration test suites
python -m unittest discover -s tests -p "test_*.py"
```
