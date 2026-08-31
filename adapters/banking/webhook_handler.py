"""
OpenBanking Webhook Event Dispatcher & Signature Verification.
Handles real-time item updates, default balance refreshes, and sync events.
"""

import hmac
import hashlib
import time
from typing import Dict, Any, Tuple, Optional, Callable


class BankingWebhookDispatcher:
    """
    Verifies cryptographic signatures on inbound banking webhooks and dispatches handlers.
    """

    def __init__(self, webhook_secret: str = "whsec_live_plaid_mock_9988"):
        self.webhook_secret = webhook_secret.encode('utf-8')
        self._handlers: Dict[str, Callable[[Dict[str, Any]], None]] = {}

    def register_handler(self, event_type: str, handler: Callable[[Dict[str, Any]], None]):
        self._handlers[event_type] = handler

    def verify_signature(self, raw_body: bytes, signature_header: str) -> bool:
        """
        Verifies SHA-256 HMAC signature of webhook payload.
        """
        try:
            expected = hmac.new(self.webhook_secret, raw_body, hashlib.sha256).hexdigest()
            return hmac.compare_digest(expected, signature_header)
        except Exception:
            return False

    def handle_payload(self, event_type: str, payload: Dict[str, Any]) -> Tuple[bool, str]:
        handler = self._handlers.get(event_type)
        if not handler:
            return False, f"No handler registered for webhook event: {event_type}"

        try:
            handler(payload)
            return True, "Event processed successfully."
        except Exception as e:
            return False, f"Handler exception: {str(e)}"
