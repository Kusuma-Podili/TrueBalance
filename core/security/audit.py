"""
Immutable Audit Trail with Cryptographic Hash Chaining.
Creates tamper-evident audit records where each record includes the SHA-256 hash
of the preceding record, forming a verifiable blockchain-style audit ledger.
"""

import hashlib
import json
import time
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class AuditRecord:
    record_id: str
    sequence_num: int
    timestamp: float
    actor_id: str
    actor_email: str
    action: str
    entity_type: str
    entity_id: str
    previous_hash: str
    metadata: Dict[str, Any]
    current_hash: str = ""

    def calculate_hash(self) -> str:
        payload = {
            "record_id": self.record_id,
            "sequence_num": self.sequence_num,
            "timestamp": self.timestamp,
            "actor_id": self.actor_id,
            "actor_email": self.actor_email,
            "action": self.action,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "previous_hash": self.previous_hash,
            "metadata": self.metadata
        }
        serialized = json.dumps(payload, sort_keys=True, separators=(',', ':'))
        return hashlib.sha256(serialized.encode('utf-8')).hexdigest()


class AuditLedgerEngine:
    """
    Maintains and validates the integrity of the system audit chain.
    """

    GENESIS_HASH = "0" * 64

    def __init__(self):
        self._chain: List[AuditRecord] = []
        self._sequence_counter: int = 0

    def append_event(
        self,
        record_id: str,
        actor_id: str,
        actor_email: str,
        action: str,
        entity_type: str,
        entity_id: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> AuditRecord:
        """
        Creates and appends a new audit record to the cryptographic chain.
        """
        self._sequence_counter += 1
        prev_hash = self._chain[-1].current_hash if self._chain else self.GENESIS_HASH
        
        record = AuditRecord(
            record_id=record_id,
            sequence_num=self._sequence_counter,
            timestamp=time.time(),
            actor_id=actor_id,
            actor_email=actor_email,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            previous_hash=prev_hash,
            metadata=metadata or {}
        )
        record.current_hash = record.calculate_hash()
        self._chain.append(record)
        return record

    def verify_chain_integrity(self) -> Tuple[bool, Optional[str]]:
        """
        Validates the entire audit chain. Returns (True, None) if unbroken,
        or (False, error_message) if tampering is detected.
        """
        for i, record in enumerate(self._chain):
            # Verify record hash matches content
            expected_hash = record.calculate_hash()
            if record.current_hash != expected_hash:
                return False, f"Hash mismatch at sequence #{record.sequence_num}: stored {record.current_hash}, computed {expected_hash}"

            # Verify link to previous record
            if i == 0:
                if record.previous_hash != self.GENESIS_HASH:
                    return False, f"Invalid genesis previous hash at sequence #1: {record.previous_hash}"
            else:
                prev_record = self._chain[i - 1]
                if record.previous_hash != prev_record.current_hash:
                    return False, f"Broken link at sequence #{record.sequence_num}: prev_hash does not match record #{prev_record.sequence_num} current_hash"

        return True, None

    def get_records(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Returns recent audit records."""
        return [asdict(r) for r in self._chain[-limit:]]
