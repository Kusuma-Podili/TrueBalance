# Enterprise Financial Math & Algorithms Specification

## 1. Bankers Rounding (ROUND_HALF_EVEN)
To prevent statistical bias in high-volume transaction reconciliation, all fractional currency conversions are quantized using IEEE 854 / Bankers Rounding:
$$\text{Round}(2.545, 2) = 2.54, \quad \text{Round}(2.535, 2) = 2.54$$

## 2. Modern Portfolio Theory (MPT) Sharpe Ratio
The risk-adjusted performance of investment portfolios is measured using:
$$\text{Sharpe Ratio} = \frac{\mathbb{E}[R_p] - R_f}{\sigma_p}$$
where $\mathbb{E}[R_p]$ is annualized portfolio return, $R_f$ is risk-free rate, and $\sigma_p$ is annualized volatility.

## 3. Monte Carlo Geometric Brownian Motion (GBM)
Wealth trajectories are modeled via stochastic differential equations:
$$S_{t+\Delta t} = S_t \exp\left( \left(\mu - \frac{\sigma^2}{2}\right)\Delta t + \sigma \sqrt{\Delta t} \cdot Z \right)$$
where $Z \sim \mathcal{N}(0, 1)$.
