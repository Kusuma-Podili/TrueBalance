"""
Automated Test Suite: Two-Role Authentication & Strict Backend RBAC Isolation.
Verifies:
1. Account Owner login & permissions
2. Financial Advisor login & read-only enforcement
3. Rejection of invalid credentials
4. Prevention of unauthorized actions across roles
"""

import unittest
from core.security.auth_service import AuthService
from core.security.rbac import Role, Permission, RBACValidator
from core.security.jwt_handler import JWTManager


class TestTwoRoleAuthAndRBAC(unittest.TestCase):

    def setUp(self):
        self.auth = AuthService()
        self.jwt = JWTManager()

    def test_account_owner_valid_authentication(self):
        """Verify Account Owner can authenticate with correct demo credentials."""
        res = self.auth.authenticate("user@truebalance.com", "User@123")
        self.assertIsNotNone(res)
        user_info, access_token, refresh_token = res
        self.assertEqual(user_info["email"], "user@truebalance.com")
        self.assertEqual(user_info["role"], Role.ACCOUNT_OWNER.value)
        self.assertTrue(len(access_token) > 20)

    def test_financial_advisor_valid_authentication(self):
        """Verify Financial Advisor can authenticate with correct demo credentials."""
        res = self.auth.authenticate("advisor@truebalance.com", "Advisor@123")
        self.assertIsNotNone(res)
        user_info, access_token, refresh_token = res
        self.assertEqual(user_info["email"], "advisor@truebalance.com")
        self.assertEqual(user_info["role"], Role.FINANCIAL_ADVISOR.value)
        self.assertEqual(user_info["assigned_client_id"], "usr_owner_01")

    def test_invalid_credentials_rejected(self):
        """Verify invalid passwords or emails fail authentication."""
        self.assertIsNone(self.auth.authenticate("user@truebalance.com", "WrongPassword!"))
        self.assertIsNone(self.auth.authenticate("nonexistent@domain.com", "User@123"))

    def test_account_owner_permissions_matrix(self):
        """Verify Account Owner has mutating financial permissions."""
        owner_role = Role.ACCOUNT_OWNER.value
        self.assertTrue(RBACValidator.has_permission(owner_role, Permission.ACCOUNT_CREATE))
        self.assertTrue(RBACValidator.has_permission(owner_role, Permission.TRANSACTION_CREATE))
        self.assertTrue(RBACValidator.has_permission(owner_role, Permission.BUDGET_MANAGE))
        self.assertTrue(RBACValidator.has_permission(owner_role, Permission.LEDGER_WRITE))

    def test_financial_advisor_strict_readonly_permissions(self):
        """Verify Financial Advisor has view + recommendation permissions, but cannot mutate accounts/txs/ledger."""
        advisor_role = Role.FINANCIAL_ADVISOR.value
        # Allowed
        self.assertTrue(RBACValidator.has_permission(advisor_role, Permission.ACCOUNT_VIEW))
        self.assertTrue(RBACValidator.has_permission(advisor_role, Permission.TRANSACTION_VIEW))
        self.assertTrue(RBACValidator.has_permission(advisor_role, Permission.TAX_REPORT_VIEW))
        self.assertTrue(RBACValidator.has_permission(advisor_role, Permission.ADVISOR_RECOMMENDATION_CREATE))
        
        # Strictly Forbidden
        self.assertFalse(RBACValidator.has_permission(advisor_role, Permission.ACCOUNT_CREATE))
        self.assertFalse(RBACValidator.has_permission(advisor_role, Permission.TRANSACTION_CREATE))
        self.assertFalse(RBACValidator.has_permission(advisor_role, Permission.TRANSACTION_DELETE))
        self.assertFalse(RBACValidator.has_permission(advisor_role, Permission.LEDGER_WRITE))

    def test_password_change_flow(self):
        """Verify password update with correct validation."""
        owner_id = "usr_owner_01"
        ok, msg = self.auth.change_password(owner_id, "User@123", "NewSecurePassword#2026")
        self.assertTrue(ok)

        # Authenticate with new password
        res = self.auth.authenticate("user@truebalance.com", "NewSecurePassword#2026")
        self.assertIsNotNone(res)

        # Restore original demo password
        self.auth.change_password(owner_id, "NewSecurePassword#2026", "User@123")


if __name__ == "__main__":
    unittest.main()
