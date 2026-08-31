"""
Journal Entry Domain Model & Balancing Invariant Verification.
Enforces the fundamental double-entry invariant: Sum(Debits) == Sum(Credits).
"""

from dataclasses import dataclass, field
from typing import List, Optional
import time
from core.math.decimal_utils import FinancialDecimal
from core.ledger.types import EntryStatus, AccountClassification, NormalBalance


class UnbalancedJournalEntryError(ValueError):
    """Raised when total debits do not equal total credits in a journal entry."""
    pass


@dataclass
class JournalLine:
    line_id: str
    account_id: str
    account_name: str
    account_classification: AccountClassification
    debit: FinancialDecimal = field(default_factory=lambda: FinancialDecimal("0.00"))
    credit: FinancialDecimal = field(default_factory=lambda: FinancialDecimal("0.00"))
    currency: str = "USD"
    fx_rate: FinancialDecimal = field(default_factory=lambda: FinancialDecimal("1.0000"))
    memo: Optional[str] = None

    def __post_init__(self):
        if self.debit.is_positive() and self.credit.is_positive():
            raise ValueError(f"Line {self.line_id} cannot have both positive Debit and Credit.")
        if self.debit.is_negative() or self.credit.is_negative():
            raise ValueError(f"Line {self.line_id} cannot have negative Debit or Credit amounts.")

    @property
    def base_debit(self) -> FinancialDecimal:
        """Returns debit amount converted to base currency using FX rate."""
        return self.debit * self.fx_rate

    @property
    def base_credit(self) -> FinancialDecimal:
        """Returns credit amount converted to base currency using FX rate."""
        return self.credit * self.fx_rate


@dataclass
class JournalEntry:
    entry_id: str
    date: str
    description: str
    lines: List[JournalLine] = field(default_factory=list)
    status: EntryStatus = EntryStatus.DRAFT
    posted_at: Optional[float] = None
    created_at: float = field(default_factory=time.time)
    metadata: dict = field(default_factory=dict)

    def add_line(
        self,
        line_id: str,
        account_id: str,
        account_name: str,
        classification: AccountClassification,
        debit: FinancialDecimal = FinancialDecimal("0.00"),
        credit: FinancialDecimal = FinancialDecimal("0.00"),
        currency: str = "USD",
        fx_rate: FinancialDecimal = FinancialDecimal("1.0000"),
        memo: Optional[str] = None
    ) -> 'JournalEntry':
        """Adds a new journal line to the entry."""
        if self.status != EntryStatus.DRAFT:
            raise ValueError(f"Cannot modify entry {self.entry_id} with status {self.status.value}")
        line = JournalLine(
            line_id=line_id,
            account_id=account_id,
            account_name=account_name,
            account_classification=classification,
            debit=debit,
            credit=credit,
            currency=currency,
            fx_rate=fx_rate,
            memo=memo
        )
        self.lines.append(line)
        return self

    @property
    def total_debit(self) -> FinancialDecimal:
        """Calculates total base currency debits."""
        return sum([line.base_debit for line in self.lines], FinancialDecimal("0.00"))

    @property
    def total_credit(self) -> FinancialDecimal:
        """Calculates total base currency credits."""
        return sum([line.base_credit for line in self.lines], FinancialDecimal("0.00"))

    def is_balanced(self) -> bool:
        """Checks whether Sum(Debits) == Sum(Credits) within financial precision."""
        diff = (self.total_debit - self.total_credit).abs()
        return diff.value < FinancialDecimal("0.0001").value

    def post(self) -> 'JournalEntry':
        """
        Posts the journal entry to the general ledger after validating balance invariants.
        """
        if len(self.lines) < 2:
            raise UnbalancedJournalEntryError(f"Entry {self.entry_id} must have at least two journal lines.")
        
        if not self.is_balanced():
            raise UnbalancedJournalEntryError(
                f"Entry {self.entry_id} is unbalanced: Debits ({self.total_debit}) != Credits ({self.total_credit}). Difference: {self.total_debit - self.total_credit}"
            )

        self.status = EntryStatus.POSTED
        self.posted_at = time.time()
        return self

    def void(self, reason: str = "Voided by user") -> 'JournalEntry':
        """Voids an existing entry."""
        self.status = EntryStatus.VOIDED
        self.metadata["void_reason"] = reason
        self.metadata["voided_at"] = time.time()
        return self
