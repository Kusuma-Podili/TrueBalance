"""
Advisor Recommendations & Client Notes Service.
Allows Financial Advisors to submit structured, prioritized financial insights
for assigned clients. Account Owners can view and act on these recommendations.
"""

import time
import uuid
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field, asdict


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
    Manages the lifecycle of client recommendations and notes.
    """

    def __init__(self):
        self._recommendations: Dict[str, RecommendationItem] = {}
        self._init_demo_recommendations()

    def _init_demo_recommendations(self):
        """Seeds realistic initial financial advisor recommendations."""
        demo_recs = [
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
                explanation="Identified an unrealized loss of $3,000 in BND (Total Bond Market). We recommend harvesting this capital loss and rotating into AGG to offset ordinary taxable income while adhering to the IRS 30-day wash-sale rule.",
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
        for r in demo_recs:
            self._recommendations[r.rec_id] = r

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

    def mark_reviewed(self, rec_id: str, client_id: str) -> bool:
        rec = self._recommendations.get(rec_id)
        if rec and rec.client_id == client_id:
            rec.is_reviewed = True
            return True
        return False
