# TrueBalance - Enterprise Personal Finance & Wealth Intelligence Platform

TrueBalance is a production-grade fintech application engineered with strict US GAAP / IFRS double-entry general ledger bookkeeping, modern portfolio theory risk analytics (Sharpe, Sortino, VaR), 10,000-path Monte Carlo simulations, automated tax-loss harvesting, and multi-currency transaction processing.

---

## Key Features

1. **Double-Entry General Ledger**:
   - Enforces mathematical balance invariants: `Sum(Debits) == Sum(Credits)`.
   - Real-time Trial Balance, Balance Sheet, and Income Statement generation.
   - Arbitrary-precision decimal arithmetic (`FinancialDecimal`) with Bankers Rounding (`ROUND_HALF_EVEN`).

2. **Quantitative Risk & Econometric Analytics**:
   - **Modern Portfolio Theory (MPT)**: Covariance matrix, Markowitz efficient frontier, Sharpe, Sortino, and Treynor ratios.
   - **Monte Carlo Simulation**: 10,000-path stochastic retirement longevity simulator with percentile fan charts.
   - **Valuation Models**: Discounted Cash Flow (DCF), Dividend Discount Model (DDM), and Black-Scholes options pricing.
   - **Fama-French Multi-Factor Decomposition & GARCH(1,1)** Volatility Models.

3. **Transaction Engine & Smart Categorization**:
   - Dynamic regex and heuristics rules engine with confidence scoring.
   - Merchant name normalizer and recurring subscription detector.
   - Real-time multi-currency FX triangulation across 12+ fiat and crypto currencies.

4. **Tax Optimization & 50-State Planning**:
   - Automated Tax-Loss Harvesting (TLH) with IRS 30-day wash-sale rule prevention.
   - 50-State statutory progressive tax bracket computation engine.
   - Debt Avalanche vs. Snowball amortization optimizer.

---

## Dependencies

The platform requires the following runtime dependencies:

- **Python**: `Python >= 3.10`
- **Node.js**: `Node.js >= 18.0.0` (for frontend building)
- **Docker**: `Docker Engine >= 24.0` (optional for containerized deployment)

---

## Installation

### 1. Python Environment Setup
```bash
# Clone the repository
git clone https://github.com/Kusuma-Podili/TrueBalance.git
cd TrueBalance

# Create and activate virtual environment
python -m venv venv

# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Frontend Dependencies Setup
```bash
# Install Node.js dependencies
npm install
```

---

## Build

### Local Project Build
```bash
# Type check and build frontend assets
npm run build

# Verify Python package build
python setup.py build
```

### Containerized Docker Build
```bash
# Build the production Docker container
docker build -t truebalance-app:latest .

# Build with Docker Compose
docker compose build
```

---

## Run

### 1. Running the Interactive Live Dashboard
```bash
# Start the TrueBalance server on http://localhost:8000
python main.py
```
Open your browser to `http://localhost:8000` to interact with the live financial dashboard.

### 2. Running with Docker Compose
```bash
docker compose up -d
```

### 3. Running Automated Test Suites
```bash
# Execute all unit and integration test suites
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## Usage

### 1. Double-Entry General Ledger Posting
```python
from core.ledger.double_entry import GeneralLedger
from core.ledger.journal_entry import JournalEntry
from core.ledger.types import AccountClassification
from core.math.decimal_utils import FinancialDecimal

ledger = GeneralLedger()
ledger.register_account("1010", "Cash", AccountClassification.ASSET)
ledger.register_account("4010", "Salary Income", AccountClassification.REVENUE)

entry = JournalEntry("tx_01", "2026-08-31", "Paycheck")
entry.add_line("l1", "1010", "Cash", AccountClassification.ASSET, debit=FinancialDecimal("5000.00"))
entry.add_line("l2", "4010", "Salary Income", AccountClassification.REVENUE, credit=FinancialDecimal("5000.00"))
ledger.post_entry(entry)

# Verify trial balance equilibrium
rows, total_debits, total_credits, is_balanced = ledger.generate_trial_balance()
assert is_balanced is True
```

### 2. Stochastic Monte Carlo Simulation
```python
from services.investments.monte_carlo import MonteCarloEngine

engine = MonteCarloEngine(seed=42)
result = engine.simulate_wealth_trajectory(
    starting_wealth=150000.0,
    annual_contribution=24000.0,
    annual_withdrawal=0.0,
    expected_annual_return=0.08,
    annual_volatility=0.15,
    years=25,
    iterations=10000
)
print("Plan Success Rate:", result["success_rate_percentage"], "%")
```

---

## License
MIT License. Copyright (c) 2026 TrueBalance Team.
