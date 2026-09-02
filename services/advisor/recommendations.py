"""
Financial Advisor Recommendation Engine & Direct Client Alert Dispatcher (INR).
Enables certified financial advisors to analyze client portfolios, macroeconomic risks,
and publish structured alerts and actionable guidance in Indian Rupees (₹).
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
import time
import uuid


@dataclass
class FinancialAlert:
    alert_id: str
    severity: str # 'CRITICAL', 'WARNING', 'OPPORTUNITY'
    title: str
    message: str
    impact_amount: Optional[str] = None
    created_at: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S IST"))
    is_acknowledged: bool = False
    advisor_id: str = "usr_advisor_01"
    client_id: str = "usr_owner_01"


class AdvisorRecommendationsService:
    """Manages advisor analysis, macroeconomic stress tests, and alert dispatches in INR."""

    _alerts: List[FinancialAlert] = [
        FinancialAlert(
            alert_id="alt_01",
            severity="CRITICAL",
            title="High-Interest Credit Card Drag",
            impact_amount="-₹18,500/yr Interest Burn",
            message="Your HDFC Regalia balance carries a 42.0% APR. Immediate repayment using idle savings will guarantee a risk-free savings of ₹18,500.00 per year.",
            created_at="2026-09-02 08:30:00 IST",
            is_acknowledged=False
        ),
        FinancialAlert(
            alert_id="alt_02",
            severity="OPPORTUNITY",
            title="Tax-Loss Harvesting Available",
            impact_amount="+₹35,000 Offset",
            message="Short-term capital gains can be offset by harvesting ₹35,000.00 unrealized loss in Debt ETF before financial year close.",
            created_at="2026-09-02 08:35:00 IST",
            is_acknowledged=False
        ),
        FinancialAlert(
            alert_id="alt_03",
            severity="WARNING",
            title="Cash Drag in Savings Account",
            impact_amount="₹1,50,000 Excess Cash",
            message="You have ₹1,50,000.00 in low-yield savings exceeding your 6-month emergency buffer. Reallocating to Arbitrage or Liquid Funds will generate ~7.2% tax-efficient yield.",
            created_at="2026-09-02 08:40:00 IST",
            is_acknowledged=False
        )
    ]

    _recommendations: List[Dict[str, Any]] = [
        {
            "rec_id": "rec_01",
            "title": "Maximize Section 80C & NPS Tier-1 Contributions",
            "category": "Tax & Retirement",
            "priority": "HIGH",
            "explanation": "Deploy ₹1,50,000 in ELSS equity tax-saving funds and ₹50,000 in NPS Section 80CCD(1B) to reduce taxable income by ₹2,00,000 in the old regime.",
            "advisor_name": "Sarah Jenkins, CFP®",
            "date": "2026-09-01"
        },
        {
            "rec_id": "rec_02",
            "title": "Accelerate Home Loan Prepayment via Annual Bonus",
            "category": "Debt Strategy",
            "priority": "MEDIUM",
            "explanation": "Making 1 extra EMI payment per year on your SBI Home Loan (8.50% floating) reduces total loan tenure from 20 years to 16.4 years, saving over ₹6,80,000 in interest.",
            "advisor_name": "Sarah Jenkins, CFP®",
            "date": "2026-08-28"
        },
        {
            "rec_id": "rec_03",
            "title": "Automate Monthly SIP in Nifty 50 & Midcap Indices",
            "category": "Wealth Building",
            "priority": "HIGH",
            "explanation": "Maintain an automated ₹50,000 monthly SIP split 60:40 across Nifty 50 Index and Nifty Midcap 150 Index for long-term compound alpha.",
            "advisor_name": "Sarah Jenkins, CFP®",
            "date": "2026-08-25"
        }
    ]

    @classmethod
    def get_active_alerts(cls, client_id: str) -> List[Dict[str, Any]]:
        return [
            {
                "alert_id": a.alert_id,
                "severity": a.severity,
                "title": a.title,
                "message": a.message,
                "impact_amount": a.impact_amount,
                "created_at": a.created_at,
                "is_acknowledged": a.is_acknowledged
            }
            for a in cls._alerts if a.client_id == client_id
        ]

    @classmethod
    def create_alert(cls, advisor_id: str, client_id: str, severity: str, title: str, message: str, impact_amount: Optional[str] = None) -> Dict[str, Any]:
        new_alert = FinancialAlert(
            alert_id=f"alt_{uuid.uuid4().hex[:6]}",
            severity=severity,
            title=title,
            message=message,
            impact_amount=impact_amount,
            advisor_id=advisor_id,
            client_id=client_id
        )
        cls._alerts.insert(0, new_alert)
        return {"alert_id": new_alert.alert_id, "status": "DISPATCHED"}

    @classmethod
    def acknowledge_alert(cls, alert_id: str) -> bool:
        for a in cls._alerts:
            if a.alert_id == alert_id:
                a.is_acknowledged = True
                return True
        return False

    @classmethod
    def get_recommendations(cls, client_id: str) -> List[Dict[str, Any]]:
        return cls._recommendations

    @classmethod
    def add_recommendation(cls, advisor_name: str, title: str, category: str, priority: str, explanation: str) -> Dict[str, Any]:
        rec = {
            "rec_id": f"rec_{uuid.uuid4().hex[:6]}",
            "title": title,
            "category": category,
            "priority": priority,
            "explanation": explanation,
            "advisor_name": advisor_name,
            "date": time.strftime("%Y-%m-%d")
        }
        cls._recommendations.insert(0, rec)
        return rec

    @classmethod
    def get_stress_test_analysis(cls, client_id: str) -> Dict[str, Any]:
        return {
            "client_id": client_id,
            "simulated_at": time.strftime("%Y-%m-%d %H:%M:%S IST"),
            "resilience_grade": "HIGH",
            "scenarios": [
                {
                    "name": "Equity Market Correction (-20% Domestic Equities)",
                    "portfolio_impact": "-₹1,88,400.00",
                    "action_needed": "Portfolio retains 8.4 months of net cash reserve. No panic liquidation needed; initiate tactical rebalancing into Large-Cap Equities."
                },
                {
                    "name": "Stagflation Shock (+6.5% CPI Inflation)",
                    "monthly_expense_increase": "+₹4,800.00/mo",
                    "action_needed": "Current monthly savings rate (73.5%) easily absorbs cost of living shock without tapping debt."
                },
                {
                    "name": "RBI Rate Hike (+150 bps Repo Rate)",
                    "savings_yield_gain": "+₹6,500.00/yr",
                    "action_needed": "Fixed deposits and liquid funds yield higher returns. Floating home loan EMI should be partially prepaid."
                }
            ]
        }
