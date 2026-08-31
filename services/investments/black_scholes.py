"""
Black-Scholes-Merton (BSM) Analytical Options Pricing & Greeks Calculator.
Calculates European Call and Put fair market values, Delta, Gamma, Vega, Theta, and Rho.
"""

import math
from typing import Dict


class BlackScholesEngine:
    """
    Standard Black-Scholes options pricing formula with analytical Greeks.
    """

    @staticmethod
    def _cdf(x: float) -> float:
        """Standard normal cumulative distribution function approximation (Abramowitz and Stegun)."""
        return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

    @staticmethod
    def _pdf(x: float) -> float:
        """Standard normal probability density function."""
        return (1.0 / math.sqrt(2.0 * math.pi)) * math.exp(-0.5 * (x ** 2))

    @classmethod
    def price_option(
        cls,
        spot_price: float,
        strike_price: float,
        time_to_maturity_years: float,
        risk_free_rate: float,
        volatility: float,
        option_type: str = "CALL"  # "CALL" or "PUT"
    ) -> Dict:
        S = spot_price
        K = strike_price
        T = time_to_maturity_years
        r = risk_free_rate
        sigma = volatility

        if T <= 0:
            payoff = max(0.0, S - K) if option_type.upper() == "CALL" else max(0.0, K - S)
            return {"price": payoff, "delta": 1.0 if payoff > 0 else 0.0, "gamma": 0.0, "vega": 0.0, "theta": 0.0, "rho": 0.0}

        d1 = (math.log(S / K) + (r + 0.5 * (sigma ** 2)) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)

        discount = math.exp(-r * T)

        if option_type.upper() == "CALL":
            price = S * cls._cdf(d1) - K * discount * cls._cdf(d2)
            delta = cls._cdf(d1)
            rho = K * T * discount * cls._cdf(d2)
            theta = -(S * cls._pdf(d1) * sigma) / (2.0 * math.sqrt(T)) - r * K * discount * cls._cdf(d2)
        else:  # PUT
            price = K * discount * cls._cdf(-d2) - S * cls._cdf(-d1)
            delta = cls._cdf(d1) - 1.0
            rho = -K * T * discount * cls._cdf(-d2)
            theta = -(S * cls._pdf(d1) * sigma) / (2.0 * math.sqrt(T)) + r * K * discount * cls._cdf(-d2)

        gamma = cls._pdf(d1) / (S * sigma * math.sqrt(T))
        vega = S * cls._pdf(d1) * math.sqrt(T)

        return {
            "option_type": option_type.upper(),
            "fair_price": round(price, 4),
            "delta": round(delta, 4),
            "gamma": round(gamma, 4),
            "vega": round(vega, 4),
            "theta": round(theta / 365.0, 4),  # Per-day decay
            "rho": round(rho / 100.0, 4)       # Per 1% interest change
        }
