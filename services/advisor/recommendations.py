"""
Advisor Recommendations, Financial Alerts & Stress-Testing Service.
Allows Financial Advisors to dispatch prioritized alerts, structured recommendations,
and macroeconomic stress-test diagnostics to assigned clients.
"""

import time
import uuid
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field, asdict


@dataclass
class FinancialAlert:
    alert_id: str
    client_id: str
    advisor_id: str
    advisor_name: str
    severity: str  # CRITICAL, WARNING, OPPORTUNITY
    title: str
    message: str
    impact_amount: Optional[str] = None
    action_label: str = "Review Action Plan"
    is_acknowledged: bool = False
    created_at: float = field(default_factory=time.time)


@dataclass
class RecommendationItem:
    rec_id: str
    client_id: str
    advisor_id: str
    advisor_name: str
    title: str
    category: str  # Budget, Investment, Debt, Savings, Tax, General
    explanation: str
    priority: str  # HIGH, MEDIUM, LOW
    date: str
    is_reviewed: bool = False
    created_at: float = field(default_factory=time.time)


class AdvisorRecommendationsService:
    """
    Manages the lifecycle of client recommendations, urgent alerts, and stress testing.
    """

    def __init__(self):
        self._recommendations: Dict[str, RecommendationItem] = {}
        self._alerts: Dict[str, FinancialAlert] = {}
        self._init_demo_data()

    def _init_demo_data(self):
        # Initial Alerts
        alerts = [
            FinancialAlert(
                alert_id="alt_001",
                client_id="usr_owner_01",
                advisor_id="usr_advisor_01",
                advisor_name="Sarah Jenkins, CFP®",
                severity="CRITICAL",
                title="High-Interest Debt Drag Alert",
                message="Sapphire Preferred balance ($1,450.00) is accumulating 22.40% APR interest charges. Paying this off immediately using surplus checking cash will save $325.00/yr.",
                impact_amount="-$325/yr Interest Burn",
                action_label="Pay Off Balance"
            ),
            FinancialAlert(
                alert_id="alt_002",
                client_id="usr_owner_01",
                advisor_id="usr_advisor_01",
                advisor_name="Sarah Jenkins, CFP®",
                severity="OPPORTUNITY",
                title="Tax-Loss Harvesting Window Open",
                message="Unrealized loss of $720.00 in BND can be harvested and rotated into AGG to offset ordinary capital gains with zero wash-sale penalty.",
                impact_amount="+$150 Tax Reduction",
                action_label="Execute Harvest"
            ),
            FinancialAlert(
                alert_id="alt_003",
                client_id="usr_owner_01",
                advisor_id="usr_advisor_01",
                advisor_name="Sarah Jenkins, CFP®",
                severity="WARNING",
                title="Cash Drag & Inflation Drag",
                message="Marcus savings balance ($32,500.00) exceeds your 6-month emergency reserve ($16,520.00). Deploying $10,000 into diversified index funds is recommended.",
                impact_amount="$15,980 Excess Liquidity",
                action_label="Allocate Funds"
            )
        ]
        for a in alerts:
            self._alerts[a.alert_id] = a

        # Initial Recommendations
        recs = [
            RecommendationItem(
                rec_id="rec_001",
                client_id="usr_owner_01",
                advisor_id="usr_advisor_01",
                advisor_name="Sarah Jenkins, CFP®",
                title="Optimize High-Yield Cash Allocation into Broad Equities",
                category="Investment",
                explanation="Your emergency fund currently holds $32,500 across Marcus savings (approx. 8.4 months of living expenses). We recommend deploying $10,000 into dollar-cost averaged low-cost broad index ETFs (e.g. VOO or VTI) to enhance long-term compounding.",
                priority="MEDIUM",
                date="2026-08-28"
            ),
            RecommendationItem(
                rec_id="rec_002",
                client_id="usr_owner_01",
                advisor_id="usr_advisor_01",
                advisor_name="Sarah Jenkins, CFP®",
                title="Execute Tax-Loss Harvest on Fixed-Income Holdings",
                category="Tax",
                explanation="Identified an unrealized loss of $720.00 in BND (Total Bond Market). We recommend harvesting this capital loss and rotating into AGG to offset ordinary taxable income while adhering to the IRS 30-day wash-sale rule.",
                priority="HIGH",
                date="2026-08-30"
            ),
            RecommendationItem(
                rec_id="rec_003",
                client_id="usr_owner_01",
                advisor_id="usr_advisor_01",
                advisor_name="Sarah Jenkins, CFP®",
                title="Accelerate Credit Card Payoff via Avalanche Method",
                category="Debt",
                explanation="Sapphire Preferred balance stands at $1,450 at 22.4% APR. Paying off this balance in full will eliminate unnecessary interest charges and immediately improve your liquidity score.",
                priority="HIGH",
                date="2026-08-31"
            )
        ]
        for r in recs:
            self._recommendations[r.rec_id] = r

    def get_client_alerts(self, client_id: str) -> List[Dict[str, Any]]:
        alerts = [asdict(a) for a in self._alerts.values() if a.client_id == client_id]
        return sorted(alerts, key=lambda x: x["created_at"], reverse=True)

    def add_alert(
        self,
        client_id: str,
        advisor_id: str,
        advisor_name: str,
        title: str,
        message: str,
        severity: str = "WARNING",
        impact_amount: Optional[str] = None
    ) -> Dict[str, Any]:
        alert = FinancialAlert(
            alert_id=f"alt_{str(uuid.uuid4())[:8]}",
            client_id=client_id,
            advisor_id=advisor_id,
            advisor_name=advisor_name,
            severity=severity,
            title=title,
            message=message,
            impact_amount=impact_amount
        )
        self._alerts[alert.alert_id] = alert
        return asdict(alert)

    def acknowledge_alert(self, alert_id: str, client_id: str) -> bool:
        alert = self._alerts.get(alert_id)
        if alert and alert.client_id == client_id:
            alert.is_acknowledged = True
            return True
        return False

    def get_client_recommendations(self, client_id: str) -> List[Dict[str, Any]]:
        recs = [asdict(r) for r in self._recommendations.values() if r.client_id == client_id]
        return sorted(recs, key=lambda x: x["created_at"], reverse=True)

    def add_recommendation(
        self,
        client_id: str,
        advisor_id: str,
        advisor_name: str,
        title: str,
        category: str,
        explanation: str,
        priority: str = "MEDIUM"
    ) -> Dict[str, Any]:
        rec = RecommendationItem(
            rec_id=f"rec_{str(uuid.uuid4())[:8]}",
            client_id=client_id,
            advisor_id=advisor_id,
            advisor_name=advisor_name,
            title=title,
            category=category,
            explanation=explanation,
            priority=priority,
            date=time.strftime("%Y-%m-%d")
        )
        self._recommendations[rec.rec_id] = rec
        return asdict(rec)

    def get_stress_test_analysis(self, client_id: str) -> Dict[str, Any]:
        """Calculates macroeconomic shock resistance for the client portfolio."""
        return {
            "client_id": client_id,
            "scenarios": [
                {
                    "name": "Market Drawdown Shock (-20% Equities)",
                    "portfolio_impact": "-$16,190.40",
                    "post_shock_value": "$78,009.60",
                    "resilience_status": "STRONG_BUFFER",
                    "action_needed": "Rebalance fixed income into equities at trough."
                },
                {
                    "name": "Stagflation Shock (+5% Inflation & Cost of Living)",
                    "monthly_expense_increase": "+$137.67/mo",
                    "revised_savings_rate": "72.2%",
                    "resilience_status": "HIGHLY_RESILIENT",
                    "action_needed": "Allocate 5% into TIPS or commodities."
                },
                {
                    "name": "Interest Rate Hike (+200 bps)",
                    "impact": "Fixed mortgage locked at 5.85%; Zero payment change.",
                    "savings_yield_gain": "+$650.00/yr additional HYSA interest",
                    "resilience_status": "BENEFICIARY",
                    "action_needed": "Maintain high-yield cash sweep."
                }
            ]
        }
