"""
Zero-Based Budgeting (ZBB) & Envelope Allocation Engine.
Assigns every dollar a job, enforces category limits, and tracks monthly rollover balances.
"""

from typing import Dict, List, Optional, Tuple
import time
from core.database.models import BudgetEnvelopeEntity, generate_uuid
from core.math.decimal_utils import FinancialDecimal


class BudgetManager:
    """
    Manages monthly budget envelopes and spending allocations.
    """

    def __init__(self):
        self._envelopes: Dict[str, BudgetEnvelopeEntity] = {}

    def create_envelope(
        self,
        user_id: str,
        category_id: str,
        allocated_cents: int,
        period_month: str,  # YYYY-MM
        rollover_enabled: bool = True
    ) -> BudgetEnvelopeEntity:
        key = f"{user_id}:{category_id}:{period_month}"
        env = BudgetEnvelopeEntity(
            envelope_id=f"env_{generate_uuid()[:12]}",
            user_id=user_id,
            category_id=category_id,
            allocated_cents=allocated_cents,
            spent_cents=0,
            period_month=period_month,
            rollover_enabled=rollover_enabled
        )
        self._envelopes[key] = env
        return env

    def set_envelope(self, user_id: str, category_id: str, allocated: FinancialDecimal, period_month: Optional[str] = None):
        if not period_month:
            period_month = time.strftime("%Y-%m")
        key = f"{user_id}:{category_id}:{period_month}"
        alloc_cents = allocated.to_cents() if hasattr(allocated, 'to_cents') else int(float(str(allocated)) * 100)
        if key in self._envelopes:
            self._envelopes[key].allocated_cents = alloc_cents
        else:
            self.create_envelope(user_id, category_id, alloc_cents, period_month)

    def record_expense(self, user_id: str, category_id: str, period_month: str, amount_cents: int):
        key = f"{user_id}:{category_id}:{period_month}"
        env = self._envelopes.get(key)
        if env:
            env.spent_cents += abs(amount_cents)

    def get_envelope_status(self, user_id: str, period_month: str) -> List[Dict]:
        results = []
        for key, env in self._envelopes.items():
            if env.user_id == user_id and env.period_month == period_month:
                remaining_cents = env.allocated_cents - env.spent_cents
                pct_spent = (env.spent_cents / env.allocated_cents * 100) if env.allocated_cents > 0 else 0.0
                results.append({
                    "envelope_id": env.envelope_id,
                    "category_id": env.category_id,
                    "allocated": FinancialDecimal.from_cents(env.allocated_cents),
                    "spent": FinancialDecimal.from_cents(env.spent_cents),
                    "remaining": FinancialDecimal.from_cents(remaining_cents),
                    "percentage_spent": round(pct_spent, 1),
                    "is_over_budget": remaining_cents < 0
                })
        return results
