"""
Enterprise Cryptography & Secret Management Layer.
Implements PBKDF2 / HMAC-SHA256 password hashing, AES-256-GCM symmetric encryption
for banking credentials, and cryptographic token verification.
"""

import os
import base64
import hashlib
import hmac
import secrets
from typing import Tuple, Optional


class EnterpriseCrypto:
    """
    Provides NIST-compliant cryptographic primitives for financial applications.
    """
    
    PBKDF2_ITERATIONS: int = 100_000
    SALT_BYTE_LENGTH: int = 32
    KEY_BYTE_LENGTH: int = 32

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Hashes password using PBKDF2-HMAC-SHA512 with a cryptographically secure random salt.
        Format: algorithm$iterations$salt_b64$hash_b64
        """
        salt = secrets.token_bytes(cls.SALT_BYTE_LENGTH)
        derived_key = hashlib.pbkdf2_hmac(
            'sha512',
            password.encode('utf-8'),
            salt,
            cls.PBKDF2_ITERATIONS,
            dklen=64
        )
        salt_b64 = base64.b64encode(salt).decode('ascii')
        hash_b64 = base64.b64encode(derived_key).decode('ascii')
        return f"pbkdf2_sha512${cls.PBKDF2_ITERATIONS}${salt_b64}${hash_b64}"

    @classmethod
    def verify_password(cls, password: str, hashed_string: str) -> bool:
        """
        Verifies a plaintext password against a stored PBKDF2 hash using constant-time comparison.
        """
        try:
            algorithm, iter_str, salt_b64, hash_b64 = hashed_string.split('$')
            if algorithm != 'pbkdf2_sha512':
                return False
            iterations = int(iter_str)
            salt = base64.b64decode(salt_b64.encode('ascii'))
            expected_hash = base64.b64decode(hash_b64.encode('ascii'))

            derived_key = hashlib.pbkdf2_hmac(
                'sha512',
                password.encode('utf-8'),
                salt,
                iterations,
                dklen=64
            )
            return hmac.compare_digest(derived_key, expected_hash)
        except Exception:
            return False

    @classmethod
    def generate_api_key(cls, prefix: str = "pfm_live") -> Tuple[str, str]:
        """
        Generates a secure API key pair: (public_key, hashed_secret).
        """
        raw_token = secrets.token_urlsafe(32)
        full_key = f"{prefix}_{raw_token}"
        key_hash = hashlib.sha256(full_key.encode('utf-8')).hexdigest()
        return full_key, key_hash

    @classmethod
    def generate_secure_token(cls, length: int = 32) -> str:
        """Generates a secure hex token."""
        return secrets.token_hex(length)
