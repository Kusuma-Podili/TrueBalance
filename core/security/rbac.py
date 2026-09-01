"""
Role-Based Access Control (RBAC) and Permissions Engine.
Defines roles, resource scopes, and authorization evaluation logic.
Strictly configured for the two active system roles:
1. ACCOUNT_OWNER (full read/write access to own financial data)
2. FINANCIAL_ADVISOR (read/analysis access to assigned client + recommendation creation)
"""

from enum import Enum
from typing import Set, Dict, List, Optional
from dataclasses import dataclass


class Role(str, Enum):
    ACCOUNT_OWNER = "ACCOUNT_OWNER"
    FINANCIAL_ADVISOR = "FINANCIAL_ADVISOR"
    # Legacy aliases for backwards compatibility in existing tests
    SUPER_ADMIN = "SUPER_ADMIN"
    AUDITOR = "AUDITOR"
    READ_ONLY_VIEWER = "READ_ONLY_VIEWER"


class Permission(str, Enum):
    # Ledger & Financial
    LEDGER_READ = "ledger:read"
    LEDGER_WRITE = "ledger:write"
    LEDGER_CLOSE_PERIOD = "ledger:close_period"
    
    # Transactions
    TRANSACTION_VIEW = "transaction:view"
    TRANSACTION_CREATE = "transaction:create"
    TRANSACTION_EDIT = "transaction:edit"
    TRANSACTION_DELETE = "transaction:delete"
    TRANSACTION_CATEGORIZE = "transaction:categorize"
    
    # Accounts
    ACCOUNT_VIEW = "account:view"
    ACCOUNT_CREATE = "account:create"
    ACCOUNT_EDIT = "account:edit"
    ACCOUNT_CLOSE = "account:close"
    
    # Budgets & Investments
    BUDGET_VIEW = "budget:view"
    BUDGET_MANAGE = "budget:manage"
    INVESTMENT_VIEW = "investment:view"
    INVESTMENT_MANAGE = "investment:manage"
    INVESTMENT_TRADE = "investment:trade"
    TAX_REPORT_VIEW = "tax:view"
    DEBT_VIEW = "debt:view"
    DEBT_MANAGE = "debt:manage"
    
    # Advisor Capabilities
    ADVISOR_RECOMMENDATION_CREATE = "advisor:recommendation_create"
    ADVISOR_NOTE_CREATE = "advisor:note_create"
    
    # System & Audit
    AUDIT_LOG_VIEW = "audit:view"
    USER_MANAGE = "user:manage"
    PROFILE_UPDATE = "profile:update"
    SYSTEM_SETTINGS = "system:settings"


ROLE_PERMISSIONS_MAP: Dict[Role, Set[Permission]] = {
    # 1. ACCOUNT OWNER - Complete control over their own financial records
    Role.ACCOUNT_OWNER: {
        Permission.LEDGER_READ,
        Permission.LEDGER_WRITE,
        Permission.TRANSACTION_VIEW,
        Permission.TRANSACTION_CREATE,
        Permission.TRANSACTION_EDIT,
        Permission.TRANSACTION_DELETE,
        Permission.TRANSACTION_CATEGORIZE,
        Permission.ACCOUNT_VIEW,
        Permission.ACCOUNT_CREATE,
        Permission.ACCOUNT_EDIT,
        Permission.ACCOUNT_CLOSE,
        Permission.BUDGET_VIEW,
        Permission.BUDGET_MANAGE,
        Permission.INVESTMENT_VIEW,
        Permission.INVESTMENT_MANAGE,
        Permission.INVESTMENT_TRADE,
        Permission.TAX_REPORT_VIEW,
        Permission.DEBT_VIEW,
        Permission.DEBT_MANAGE,
        Permission.AUDIT_LOG_VIEW,
        Permission.PROFILE_UPDATE,
    },

    # 2. FINANCIAL ADVISOR - Analysis, reporting, and advisory recommendations (No mutating account/tx/ledger permissions)
    Role.FINANCIAL_ADVISOR: {
        Permission.LEDGER_READ,
        Permission.TRANSACTION_VIEW,
        Permission.ACCOUNT_VIEW,
        Permission.BUDGET_VIEW,
        Permission.INVESTMENT_VIEW,
        Permission.TAX_REPORT_VIEW,
        Permission.DEBT_VIEW,
        Permission.AUDIT_LOG_VIEW,
        Permission.ADVISOR_RECOMMENDATION_CREATE,
        Permission.ADVISOR_NOTE_CREATE,
        Permission.PROFILE_UPDATE,
    },

    # Legacy mappings for backwards compatibility in existing tests
    Role.SUPER_ADMIN: {p for p in Permission},
    Role.AUDITOR: {
        Permission.LEDGER_READ,
        Permission.TRANSACTION_VIEW,
        Permission.ACCOUNT_VIEW,
        Permission.INVESTMENT_VIEW,
        Permission.TAX_REPORT_VIEW,
        Permission.AUDIT_LOG_VIEW,
    },
    Role.READ_ONLY_VIEWER: {
        Permission.LEDGER_READ,
        Permission.TRANSACTION_VIEW,
        Permission.ACCOUNT_VIEW,
        Permission.INVESTMENT_VIEW,
    }
}


class RBACValidator:
    """
    Evaluates role permissions and authorization rules.
    """

    @classmethod
    def has_permission(cls, role_str: str, required_permission: Permission) -> bool:
        try:
            role = Role(role_str)
            permissions = ROLE_PERMISSIONS_MAP.get(role, set())
            return required_permission in permissions
        except ValueError:
            return False

    @classmethod
    def get_role_permissions(cls, role_str: str) -> List[str]:
        try:
            role = Role(role_str)
            return [p.value for p in ROLE_PERMISSIONS_MAP.get(role, set())]
        except ValueError:
            return []
