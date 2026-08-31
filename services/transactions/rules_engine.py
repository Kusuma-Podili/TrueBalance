"""
Smart Transaction Auto-Categorization Engine.
Employs regex matching, keyword heuristics, amount intervals,
and merchant brand mappings with confidence scoring.
"""

import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class CategorizationRule:
    rule_id: str
    target_category_id: str
    priority: int  # Higher priority rules evaluated first
    pattern: str
    min_amount_cents: Optional[int] = None
    max_amount_cents: Optional[int] = None
    is_regex: bool = False
    confidence_score: float = 1.0


class SmartCategorizer:
    """
    High-performance rule-based classification engine for financial transactions.
    """

    def __init__(self):
        self._rules: List[CategorizationRule] = []
        self._initialize_built_in_rules()

    def add_rule(self, rule: CategorizationRule):
        self._rules.append(rule)
        self._rules.sort(key=lambda r: r.priority, reverse=True)

    def _initialize_built_in_rules(self):
        rules = [
            # Income / Salary
            CategorizationRule("r_salary", "cat_salary", 100, r"(payroll|direct dep|gusto|adp|salary)", is_regex=True),
            # Housing & Utilities
            CategorizationRule("r_rent", "cat_housing", 90, r"(rent|landlord|leasing|mortgage|property mgmt)", is_regex=True),
            CategorizationRule("r_electric", "cat_utilities", 80, r"(coned|pge|electric|national grid|water bill)", is_regex=True),
            # Groceries & Food
            CategorizationRule("r_wholefoods", "cat_food", 85, r"(whole foods|trader joe|kroger|safeway|heb|costco|walmart)", is_regex=True),
            CategorizationRule("r_starbucks", "cat_food", 80, r"(starbucks|dunkin|blue bottle|peet's coffee|cafe)", is_regex=True),
            CategorizationRule("r_ubereats", "cat_food", 80, r"(uber eats|doordash|grubhub|postmates|seamless)", is_regex=True),
            # Transportation
            CategorizationRule("r_uber", "cat_transit", 75, r"(uber\.com|lyft|mta|subway|metro|gas station|shell|chevron|exxon)", is_regex=True),
            # Entertainment & Subscriptions
            CategorizationRule("r_netflix", "cat_entertainment", 70, r"(netflix|spotify|hulu|disney\+|apple tv|hbomax|youtube premium)", is_regex=True),
            # Investments
            CategorizationRule("r_fidelity", "cat_invest", 95, r"(vanguard|fidelity|schwab|robinhood|coinbase)", is_regex=True),
        ]
        for r in rules:
            self.add_rule(r)

    def categorize(self, raw_description: str, merchant_name: str, amount_cents: int) -> Tuple[Optional[str], float]:
        """
        Evaluates rules against transaction data.
        Returns (category_id, confidence_score).
        """
        search_text = f"{raw_description} {merchant_name}".lower()

        for rule in self._rules:
            # Check amount constraints if defined
            if rule.min_amount_cents is not None and amount_cents < rule.min_amount_cents:
                continue
            if rule.max_amount_cents is not None and amount_cents > rule.max_amount_cents:
                continue

            # Match pattern
            if rule.is_regex:
                if re.search(rule.pattern, search_text, re.IGNORECASE):
                    return rule.target_category_id, rule.confidence_score
            else:
                if rule.pattern.lower() in search_text:
                    return rule.target_category_id, rule.confidence_score

        return None, 0.0
