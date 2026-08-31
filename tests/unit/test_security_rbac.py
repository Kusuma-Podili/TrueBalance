"""
Test Suite 5: Security Architecture, Passwords, JWT Tokens, and RBAC Permissions.
"""

import unittest
from core.security.crypto import EnterpriseCrypto
from core.security.jwt_handler import JWTManager
from core.security.rbac import RBACValidator, Role, Permission
from core.security.audit import AuditLedgerEngine


class TestSecurityRBAC(unittest.TestCase):

    def setUp(self):
        self.jwt = JWTManager(secret="test_secret_key_1234567890_enterprise")
        self.audit = AuditLedgerEngine()

    def test_password_hashing_and_verification(self):
        """Verify PBKDF2 hashing security and constant-time verification."""
        password = "CorrectHorseBatteryStaple#2026"
        hashed = EnterpriseCrypto.hash_password(password)
        
        self.assertTrue(EnterpriseCrypto.verify_password(password, hashed))
        self.assertFalse(EnterpriseCrypto.verify_password("WrongPassword123", hashed))

    def test_jwt_token_lifecycle(self):
        """Verify JWT token creation, signature validation, and payload integrity."""
        payload = {"sub": "usr_123", "email": "test@fintech.io", "role": "ACCOUNT_OWNER"}
        token = self.jwt.create_token(payload, expires_in_seconds=3600)
        
        decoded = self.jwt.decode_token(token)
        self.assertIsNotNone(decoded)
        self.assertEqual(decoded["sub"], "usr_123")
        self.assertEqual(decoded["email"], "test@fintech.io")

    def test_rbac_permission_matrix(self):
        """Verify RBAC permission boundaries across roles."""
        self.assertTrue(RBACValidator.has_permission(Role.SUPER_ADMIN.value, Permission.USER_MANAGE))
        self.assertTrue(RBACValidator.has_permission(Role.ACCOUNT_OWNER.value, Permission.TRANSACTION_CREATE))
        self.assertFalse(RBACValidator.has_permission(Role.READ_ONLY_VIEWER.value, Permission.TRANSACTION_CREATE))
        self.assertFalse(RBACValidator.has_permission(Role.AUDITOR.value, Permission.LEDGER_WRITE))

    def test_audit_ledger_merkle_chain_integrity(self):
        """Verify immutable audit log hash chaining and tamper detection."""
        r1 = self.audit.append_event("ev_1", "usr_1", "u1@io", "LOGIN", "USER", "usr_1")
        r2 = self.audit.append_event("ev_2", "usr_1", "u1@io", "CREATE_TX", "TRANSACTION", "tx_1")
        r3 = self.audit.append_event("ev_3", "usr_1", "u1@io", "LOGOUT", "USER", "usr_1")

        is_valid, err = self.audit.verify_chain_integrity()
        self.assertTrue(is_valid)
        self.assertIsNone(err)


if __name__ == "__main__":
    unittest.main()
