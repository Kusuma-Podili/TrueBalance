"""
Authentication Service & User Store for TrueBalance.
Implements secure PBKDF2 password hashing, JWT session lifecycle,
and user-level data access isolation for exactly two roles:
1. ACCOUNT_OWNER (user@truebalance.com / User@123)
2. FINANCIAL_ADVISOR (advisor@truebalance.com / Advisor@123)
"""

import time
from typing import Dict, Optional, Tuple, List, Any
from dataclasses import dataclass, field
from core.security.crypto import EnterpriseCrypto
from core.security.jwt_handler import JWTManager
from core.security.rbac import Role, Permission, RBACValidator


@dataclass
class UserSession:
    user_id: str
    email: str
    full_name: str
    role: str
    assigned_client_id: Optional[str] = None
    created_at: float = field(default_factory=time.time)


class AuthService:
    """
    Manages user credentials, authentication tokens, password changes,
    and client-advisor relationship mappings.
    """

    def __init__(self, jwt_manager: Optional[JWTManager] = None):
        self.jwt = jwt_manager or JWTManager()
        self._users: Dict[str, Dict[str, Any]] = {}
        self._user_by_email: Dict[str, str] = {}
        self._init_demo_users()

    def _init_demo_users(self):
        """Initializes the two required role accounts with PBKDF2 hashed credentials."""
        # 1. Account Owner
        owner_id = "usr_owner_01"
        owner_email = "user@truebalance.com"
        owner_hash = EnterpriseCrypto.hash_password("User@123")
        self._users[owner_id] = {
            "user_id": owner_id,
            "email": owner_email,
            "password_hash": owner_hash,
            "full_name": "Alex Vance",
            "role": Role.ACCOUNT_OWNER.value,
            "is_active": True,
            "created_at": time.time(),
            "assigned_advisor_id": "usr_advisor_01"
        }
        self._user_by_email[owner_email.lower()] = owner_id

        # 2. Financial Advisor
        advisor_id = "usr_advisor_01"
        advisor_email = "advisor@truebalance.com"
        advisor_hash = EnterpriseCrypto.hash_password("Advisor@123")
        self._users[advisor_id] = {
            "user_id": advisor_id,
            "email": advisor_email,
            "password_hash": advisor_hash,
            "full_name": "Sarah Jenkins, CFP®",
            "role": Role.FINANCIAL_ADVISOR.value,
            "is_active": True,
            "created_at": time.time(),
            "assigned_client_id": owner_id
        }
        self._user_by_email[advisor_email.lower()] = advisor_id

    def authenticate(self, email: str, password: str) -> Optional[Tuple[Dict[str, Any], str, str]]:
        """
        Validates email and password, returning (user_info, access_token, refresh_token).
        Returns None if credentials are invalid.
        """
        user_id = self._user_by_email.get(email.strip().lower())
        if not user_id:
            return None

        user = self._users.get(user_id)
        if not user or not user.get("is_active"):
            return None

        if not EnterpriseCrypto.verify_password(password, user["password_hash"]):
            return None

        # Issue JWT pair
        access_token, refresh_token = self.jwt.issue_token_pair(
            user_id=user["user_id"],
            email=user["email"],
            role=user["role"]
        )

        user_info = {
            "user_id": user["user_id"],
            "email": user["email"],
            "full_name": user["full_name"],
            "role": user["role"],
            "assigned_client_id": user.get("assigned_client_id")
        }
        return user_info, access_token, refresh_token

    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Validates an incoming Bearer JWT and returns the decoded token payload."""
        return self.jwt.decode_token(token)

    def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        user = self._users.get(user_id)
        if not user:
            return None
        return {
            "user_id": user["user_id"],
            "email": user["email"],
            "full_name": user["full_name"],
            "role": user["role"],
            "assigned_client_id": user.get("assigned_client_id")
        }

    def change_password(self, user_id: str, old_password: str, new_password: str) -> Tuple[bool, str]:
        """Changes user password with strict validation."""
        user = self._users.get(user_id)
        if not user:
            return False, "User not found"

        if not EnterpriseCrypto.verify_password(old_password, user["password_hash"]):
            return False, "Current password is incorrect"

        if len(new_password) < 6:
            return False, "New password must be at least 6 characters"

        user["password_hash"] = EnterpriseCrypto.hash_password(new_password)
        return True, "Password changed successfully"

    def get_assigned_client_id_for_advisor(self, advisor_id: str) -> Optional[str]:
        advisor = self._users.get(advisor_id)
        if advisor and advisor.get("role") == Role.FINANCIAL_ADVISOR.value:
            return advisor.get("assigned_client_id")
        return None
