"""
Transaction Ingestion & Processing Pipeline.
Performs deduplication, idempotency checks, category enrichment,
and atomic account balance mutations.
"""

from typing import List, Dict, Optional, Tuple, Set
import hashlib
import time
from core.database.models import TransactionEntity, generate_uuid
from core.math.decimal_utils import FinancialDecimal
from services.accounts.manager import AccountManager


class TransactionProcessor:
    """
    Orchestrates the ingestion, validation, and posting of financial transactions.
    """

    def __init__(self, account_manager: AccountManager):
        self.account_manager = account_manager
        self._transactions: Dict[str, TransactionEntity] = {}
        self._idempotency_hashes: Set[str] = set()

    def _compute_fingerprint(self, account_id: str, amount_cents: int, date: str, raw_desc: str) -> str:
        payload = f"{account_id}:{amount_cents}:{date}:{raw_desc.strip().lower()}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    def process_transaction(
        self,
        account_id: str,
        user_id: str,
        amount_cents: int,
        date: str,
        merchant_name: str,
        raw_description: str,
        category_id: Optional[str] = None,
        is_recurring: bool = False,
        allow_duplicates: bool = False
    ) -> TransactionEntity:
        """
        Ingests a single transaction, applies idempotency checks, and updates account balance.
        """
        fingerprint = self._compute_fingerprint(account_id, amount_cents, date, raw_description)
        if not allow_duplicates and fingerprint in self._idempotency_hashes:
            raise ValueError(f"Duplicate transaction detected for account {account_id} on {date}.")

        # Verify account existence
        acc = self.account_manager.get_account(account_id)
        if not acc:
            raise KeyError(f"Account {account_id} not found.")

        tx = TransactionEntity(
            transaction_id=f"tx_{generate_uuid()[:12]}",
            account_id=account_id,
            user_id=user_id,
            category_id=category_id,
            amount_cents=amount_cents,
            currency=acc.currency,
            date=date,
            merchant_name=merchant_name,
            raw_description=raw_description,
            status="POSTED",
            is_recurring=is_recurring
        )

        # Apply balance change
        self.account_manager.update_balance(account_id, amount_cents)
        
        self._transactions[tx.transaction_id] = tx
        self._idempotency_hashes.add(fingerprint)
        return tx

    def batch_process(self, transactions_data: List[Dict]) -> Tuple[List[TransactionEntity], List[str]]:
        """
        Ingests a batch of transactions. Returns (successful_transactions, error_messages).
        """
        successful = []
        errors = []

        for item in transactions_data:
            try:
                tx = self.process_transaction(
                    account_id=item["account_id"],
                    user_id=item["user_id"],
                    amount_cents=item["amount_cents"],
                    date=item["date"],
                    merchant_name=item.get("merchant_name", "Unknown Merchant"),
                    raw_description=item.get("raw_description", ""),
                    category_id=item.get("category_id"),
                    is_recurring=item.get("is_recurring", False)
                )
                successful.append(tx)
            except Exception as e:
                errors.append(f"Failed to process {item.get('raw_description', 'transaction')}: {str(e)}")

        return successful, errors

    def record_transaction(
        self,
        account_id: str,
        merchant_name: str,
        amount_cents: int,
        raw_description: str,
        category_id: str,
        date: str
    ) -> TransactionEntity:
        acc = self.account_manager.get_account(account_id)
        user_id = acc.user_id if acc else "usr_owner_01"
        return self.process_transaction(
            account_id=account_id,
            user_id=user_id,
            amount_cents=amount_cents,
            date=date,
            merchant_name=merchant_name,
            raw_description=raw_description,
            category_id=category_id,
            allow_duplicates=True
        )

    def get_user_transactions(self, user_id: str) -> List[TransactionEntity]:
        return [tx for tx in self._transactions.values() if tx.user_id == user_id]
