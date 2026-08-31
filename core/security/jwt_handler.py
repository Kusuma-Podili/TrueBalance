"""
JWT Token Engine & Session Security.
Generates and validates signed JWT tokens with claims, expiration, and role scopes.
"""

import json
import base64
import hmac
import hashlib
import time
from typing import Dict, Any, Optional, Tuple


class JWTManager:
    """
    Lightweight, dependency-free HMAC-SHA256 JWT Token Manager.
    """
    
    DEFAULT_SECRET = "fintech_enterprise_hmac_secret_key_998877665544332211"
    ACCESS_TOKEN_LIFETIME_SEC = 3600  # 1 hour
    REFRESH_TOKEN_LIFETIME_SEC = 86400 * 30  # 30 days

    def __init__(self, secret: str = DEFAULT_SECRET):
        self.secret = secret.encode('utf-8')

    def _b64url_encode(self, data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')

    def _b64url_decode(self, data_str: str) -> bytes:
        padding = '=' * (4 - (len(data_str) % 4)) if len(data_str) % 4 != 0 else ''
        return base64.urlsafe_b64decode((data_str + padding).encode('utf-8'))

    def create_token(self, payload: Dict[str, Any], expires_in_seconds: int = ACCESS_TOKEN_LIFETIME_SEC) -> str:
        header = {"alg": "HS256", "typ": "JWT"}
        now = int(time.time())
        token_payload = payload.copy()
        token_payload.update({
            "iat": now,
            "exp": now + expires_in_seconds,
            "iss": "fintech.pfm.engine"
        })

        header_b64 = self._b64url_encode(json.dumps(header, separators=(',', ':')).encode('utf-8'))
        payload_b64 = self._b64url_encode(json.dumps(token_payload, separators=(',', ':')).encode('utf-8'))
        
        signing_input = f"{header_b64}.{payload_b64}".encode('utf-8')
        signature = hmac.new(self.secret, signing_input, hashlib.sha256).digest()
        sig_b64 = self._b64url_encode(signature)

        return f"{header_b64}.{payload_b64}.{sig_b64}"

    def decode_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Decodes and verifies a JWT token. Returns payload dict if valid, None otherwise.
        """
        try:
            parts = token.split('.')
            if len(parts) != 3:
                return None
            header_b64, payload_b64, sig_b64 = parts

            # Verify signature
            signing_input = f"{header_b64}.{payload_b64}".encode('utf-8')
            expected_sig = hmac.new(self.secret, signing_input, hashlib.sha256).digest()
            actual_sig = self._b64url_decode(sig_b64)

            if not hmac.compare_digest(expected_sig, actual_sig):
                return None

            # Parse payload
            payload_json = self._b64url_decode(payload_b64).decode('utf-8')
            payload = json.loads(payload_json)

            # Check expiration
            now = int(time.time())
            if payload.get("exp", 0) < now:
                return None

            return payload
        except Exception:
            return None

    def issue_token_pair(self, user_id: str, email: str, role: str) -> Tuple[str, str]:
        """Issues an access token and a refresh token."""
        access_payload = {"sub": user_id, "email": email, "role": role, "type": "access"}
        refresh_payload = {"sub": user_id, "type": "refresh"}
        access_token = self.create_token(access_payload, self.ACCESS_TOKEN_LIFETIME_SEC)
        refresh_token = self.create_token(refresh_payload, self.REFRESH_TOKEN_LIFETIME_SEC)
        return access_token, refresh_token
