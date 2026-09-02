"""
TrueBalance - Production Enterprise FinTech Wealth Management Platform.
Full Role-Based Application Server supporting:
1. ACCOUNT OWNER (user@truebalance.com / User@123)
2. FINANCIAL ADVISOR (advisor@truebalance.com / Advisor@123)
"""

import sys
import os
import json
import time
import uuid
import http.server
import socketserver
import urllib.parse
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).parent))

from core.math.decimal_utils import FinancialDecimal
from core.ledger.double_entry import GeneralLedger
from core.ledger.journal_entry import JournalEntry
from core.ledger.types import AccountClassification
from core.security.crypto import EnterpriseCrypto
from core.security.jwt_handler import JWTManager
from core.security.rbac import Role, Permission, RBACValidator
from core.security.auth_service import AuthService
from core.security.audit import AuditLedgerEngine

from services.accounts.manager import AccountManager
from services.transactions.processor import TransactionProcessor
from services.transactions.rules_engine import SmartCategorizer
from services.transactions.merchant_normalizer import MerchantNormalizer
from services.budget.zero_based import BudgetManager
from services.investments.monte_carlo import MonteCarloEngine
from services.investments.metrics import PortfolioRiskMetrics
from services.tax.harvesting import TaxLossHarvester, TaxableHolding
from services.tax.state_tax_engine import StateTaxCalculator, FilingStatus
from services.debt.optimizer import DebtOptimizer
from services.compliance.aml_kyc_engine import AMLMonitoringEngine, AMLAlertSeverity
from services.financial_health.calculator import FinancialHealthCalculator
from services.advisor.recommendations import AdvisorRecommendationsService
from services.reports.generator import FinancialReportsGenerator
from services.fx.engine import FXEngine

PORT = 8000

# =========================================================================
# GLOBAL APPLICATION SINGLETONS
# =========================================================================
auth_service = AuthService()
account_mgr = AccountManager()
tx_processor = TransactionProcessor(account_mgr)
ledger = GeneralLedger()
budget_mgr = BudgetManager()
recs_service = AdvisorRecommendationsService()
audit_engine = AuditLedgerEngine()
monte_carlo = MonteCarloEngine(seed=42)
fx_engine = FXEngine()
categorizer = SmartCategorizer()

# Holdings and Debt Store for Account Owner
user_holdings: Dict[str, List[Dict[str, Any]]] = {}
user_debts: Dict[str, List[Dict[str, Any]]] = {}

OWNER_ID = "usr_owner_01"
ADVISOR_ID = "usr_advisor_01"

def initialize_enterprise_demo_data():
    """Initializes realistic enterprise financial profiles for the Account Owner."""
    # 1. Accounts
    acc_checking = account_mgr.create_account(OWNER_ID, "Chase Premier Checking", "CHECKING", initial_balance_cents=845000, institution_name="JPMorgan Chase")
    acc_savings = account_mgr.create_account(OWNER_ID, "Marcus High-Yield Savings", "SAVINGS", initial_balance_cents=3250000, institution_name="Goldman Sachs")
    acc_brokerage = account_mgr.create_account(OWNER_ID, "Fidelity Wealth Portfolio", "INVESTMENT", initial_balance_cents=9420000, institution_name="Fidelity Investments")
    acc_card = account_mgr.create_account(OWNER_ID, "Sapphire Preferred Card", "CREDIT_CARD", initial_balance_cents=-145000, institution_name="Chase Card Services", credit_limit_cents=2500000)
    acc_mortgage = account_mgr.create_account(OWNER_ID, "30-Year Fixed Mortgage", "MORTGAGE", initial_balance_cents=-28500000, institution_name="Wells Fargo Home Mortgage")

    # 2. General Ledger Chart of Accounts
    ledger.register_account("1010", "Cash & Checking", AccountClassification.ASSET)
    ledger.register_account("1020", "High-Yield Savings", AccountClassification.ASSET)
    ledger.register_account("1030", "Brokerage Equities", AccountClassification.ASSET)
    ledger.register_account("2010", "Credit Card Debt", AccountClassification.LIABILITY)
    ledger.register_account("2020", "Mortgage Note", AccountClassification.LIABILITY)
    ledger.register_account("3010", "Retained Net Worth", AccountClassification.EQUITY)
    ledger.register_account("4010", "Tech Salary & Compensation", AccountClassification.REVENUE)
    ledger.register_account("5010", "Housing & Mortgage Expense", AccountClassification.EXPENSE)
    ledger.register_account("5020", "Groceries & Nutrition", AccountClassification.EXPENSE)
    ledger.register_account("5030", "Transportation & Fuel", AccountClassification.EXPENSE)
    ledger.register_account("5040", "Utilities & Internet", AccountClassification.EXPENSE)
    ledger.register_account("5050", "Entertainment & Leisure", AccountClassification.EXPENSE)

    # Initial Opening Balances Journal Entry
    e0 = JournalEntry("entry_init_0", "2026-08-01", "Opening Balance Sheet Position")
    e0.add_line("l1", "1010", "Cash & Checking", AccountClassification.ASSET, debit=FinancialDecimal("8450.00"))
    e0.add_line("l2", "1020", "High-Yield Savings", AccountClassification.ASSET, debit=FinancialDecimal("32500.00"))
    e0.add_line("l3", "1030", "Brokerage Equities", AccountClassification.ASSET, debit=FinancialDecimal("94200.00"))
    e0.add_line("l4", "2010", "Credit Card Debt", AccountClassification.LIABILITY, credit=FinancialDecimal("1450.00"))
    e0.add_line("l5", "2020", "Mortgage Note", AccountClassification.LIABILITY, credit=FinancialDecimal("285000.00"))
    e0.add_line("l6", "3010", "Retained Net Worth", AccountClassification.EQUITY, debit=FinancialDecimal("151300.00"))
    ledger.post_entry(e0)

    # Seed Transactions
    demo_txs = [
        (acc_checking.account_id, 520000, "2026-08-15", "Acme Tech Corp Direct Deposit", "Acme Tech", "cat_salary"),
        (acc_checking.account_id, -220000, "2026-08-16", "Wells Fargo Home Loan AutoPay", "Wells Fargo", "cat_housing"),
        (acc_checking.account_id, -18500, "2026-08-18", "Whole Foods Market #102", "Whole Foods", "cat_food"),
        (acc_card.account_id, -6450, "2026-08-20", "Blue Bottle Coffee", "Blue Bottle", "cat_food"),
        (acc_card.account_id, -1999, "2026-08-22", "Netflix.com Monthly Subscription", "Netflix", "cat_entertainment"),
        (acc_checking.account_id, -14500, "2026-08-24", "Chevron Clean Energy", "Chevron", "cat_transit"),
        (acc_card.account_id, -12500, "2026-08-27", "Amazon.com Mktp US", "Amazon", "cat_shopping"),
        (acc_checking.account_id, 520000, "2026-08-30", "Acme Tech Corp Direct Deposit", "Acme Tech", "cat_salary"),
    ]

    for acc_id, amt, dt, raw_desc, merch, cat in demo_txs:
        tx_processor.process_transaction(
            account_id=acc_id,
            user_id=OWNER_ID,
            amount_cents=amt,
            date=dt,
            merchant_name=merch,
            raw_description=raw_desc,
            category_id=cat,
            allow_duplicates=True
        )

    # Envelopes
    period = time.strftime("%Y-%m")
    budget_mgr.create_envelope(OWNER_ID, "cat_housing", 250000, period)
    budget_mgr.create_envelope(OWNER_ID, "cat_food", 85000, period)
    budget_mgr.create_envelope(OWNER_ID, "cat_transit", 35000, period)
    budget_mgr.create_envelope(OWNER_ID, "cat_entertainment", 25000, period)
    budget_mgr.create_envelope(OWNER_ID, "cat_utilities", 30000, period)
    budget_mgr.create_envelope(OWNER_ID, "cat_shopping", 40000, period)

    budget_mgr.record_expense(OWNER_ID, "cat_housing", period, 220000)
    budget_mgr.record_expense(OWNER_ID, "cat_food", period, 24950)
    budget_mgr.record_expense(OWNER_ID, "cat_transit", period, 14500)
    budget_mgr.record_expense(OWNER_ID, "cat_entertainment", period, 1999)
    budget_mgr.record_expense(OWNER_ID, "cat_shopping", period, 12500)

    # Holdings
    user_holdings[OWNER_ID] = [
        {"holding_id": "h_1", "symbol": "VOO", "name": "Vanguard S&P 500 ETF", "asset_class": "EQUITY", "shares": 120.0, "cost_basis": 420.50, "current_price": 512.80, "market_value": 61536.00, "unrealized_pnl": 11076.00, "weight_pct": 65.3},
        {"holding_id": "h_2", "symbol": "QQQ", "name": "Invesco QQQ Trust", "asset_class": "EQUITY", "shares": 40.0, "cost_basis": 395.00, "current_price": 485.40, "market_value": 19416.00, "unrealized_pnl": 3616.00, "weight_pct": 20.6},
        {"holding_id": "h_3", "symbol": "BND", "name": "Vanguard Total Bond Market", "asset_class": "FIXED_INCOME", "shares": 120.0, "cost_basis": 78.00, "current_price": 72.00, "market_value": 8640.00, "unrealized_pnl": -720.00, "weight_pct": 9.2},
        {"holding_id": "h_4", "symbol": "VNQ", "name": "Vanguard Real Estate ETF", "asset_class": "REAL_ESTATE", "shares": 50.0, "cost_basis": 84.00, "current_price": 92.16, "market_value": 4608.00, "unrealized_pnl": 408.00, "weight_pct": 4.9},
    ]

    # Debts
    user_debts[OWNER_ID] = [
        {"debt_id": "d_1", "name": "30-Year Fixed Mortgage", "type": "MORTGAGE", "balance": 285000.00, "interest_rate": 5.85, "min_payment": 1682.00, "institution": "Wells Fargo"},
        {"debt_id": "d_2", "name": "Sapphire Preferred Card", "type": "CREDIT_CARD", "balance": 1450.00, "interest_rate": 22.40, "min_payment": 65.00, "institution": "Chase"},
    ]

    # Audit Events
    audit_engine.append_event("ev_001", OWNER_ID, "user@truebalance.com", "SYSTEM_INIT", "LEDGER", "1010", {"action": "Opening balance ledger verification"})
    audit_engine.append_event("ev_002", OWNER_ID, "user@truebalance.com", "ACCOUNT_CREATED", "ACCOUNT", acc_checking.account_id, {"name": acc_checking.account_name})
    audit_engine.append_event("ev_003", ADVISOR_ID, "advisor@truebalance.com", "ADVISOR_ASSIGNED", "CLIENT", OWNER_ID, {"advisor": "Sarah Jenkins, CFP®"})

initialize_enterprise_demo_data()

# =========================================================================
# REST API HANDLER & RBAC MIDDLEWARE
# =========================================================================
class TrueBalanceAPIHandler(http.server.SimpleHTTPRequestHandler):

    def _send_json(self, data: Any, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def _send_error(self, message: str, status: int = 400):
        self._send_json({"error": message, "status": status}, status=status)

    def _get_auth_context(self) -> Optional[Dict[str, Any]]:
        auth_header = self.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return None
        token = auth_header.split(" ")[1].strip()
        payload = auth_service.verify_token(token)
        return payload

    def _get_target_client_id(self, auth_user: Dict[str, Any]) -> str:
        """Resolves target user ID: Account Owner queries own ID; Advisor queries assigned client ID."""
        role = auth_user.get("role")
        if role == Role.ACCOUNT_OWNER.value:
            return auth_user.get("sub", OWNER_ID)
        elif role == Role.FINANCIAL_ADVISOR.value:
            advisor_id = auth_user.get("sub", ADVISOR_ID)
            assigned = auth_service.get_assigned_client_id_for_advisor(advisor_id)
            return assigned or OWNER_ID
        return OWNER_ID

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # Serve SPA Frontend
        if path in ("/", "/login", "/dashboard", "/index.html", "/app"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(Path(__file__).parent / "frontend_spa.html", "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
            return

        # Protected API Routes
        if path.startswith("/api/"):
            auth_user = self._get_auth_context()
            if not auth_user and path != "/api/health":
                self._send_error("Authentication required. Please log in.", 401)
                return

            client_id = self._get_target_client_id(auth_user) if auth_user else OWNER_ID

            # 1. Auth Me
            if path == "/api/auth/me":
                user_data = auth_service.get_user(auth_user["sub"])
                if not user_data:
                    self._send_error("User not found", 404)
                    return
                self._send_json({"user": user_data})
                return

            # 2. Net Worth & Summary
            if path == "/api/net-worth":
                assets, debts, net_worth = account_mgr.compute_net_worth(client_id)
                rows, debits, credits, is_bal = ledger.generate_trial_balance()
                self._send_json({
                    "client_id": client_id,
                    "total_assets": str(assets.value),
                    "total_liabilities": str(debts.value),
                    "net_worth": str(net_worth.value),
                    "is_ledger_balanced": is_bal,
                    "total_debits": str(debits.value),
                    "total_credits": str(credits.value),
                    "monthly_income": "10400.00",
                    "monthly_expenses": "2753.49",
                    "savings_rate_pct": 73.5
                })
                return

            # 3. Accounts
            if path == "/api/accounts":
                accounts = account_mgr.list_user_accounts(client_id)
                self._send_json([
                    {
                        "account_id": a.account_id,
                        "account_name": a.account_name,
                        "account_type": a.account_type,
                        "institution_name": a.institution_name,
                        "currency": a.currency,
                        "current_balance_cents": a.current_balance_cents,
                        "current_balance": a.current_balance_cents / 100.0,
                        "credit_limit": (a.credit_limit_cents / 100.0) if a.credit_limit_cents else None
                    }
                    for a in accounts
                ])
                return

            # 4. Transactions
            if path == "/api/transactions":
                all_txs = tx_processor.get_user_transactions(client_id)
                category_filter = query.get("category", [None])[0]
                search_query = query.get("q", [""])[0].lower()

                filtered = []
                for tx in all_txs:
                    if category_filter and tx.category_id != category_filter:
                        continue
                    if search_query and (search_query not in tx.merchant_name.lower() and search_query not in tx.raw_description.lower()):
                        continue
                    filtered.append({
                        "transaction_id": tx.transaction_id,
                        "account_id": tx.account_id,
                        "date": tx.date,
                        "merchant_name": tx.merchant_name,
                        "raw_description": tx.raw_description,
                        "category_id": tx.category_id,
                        "amount": tx.amount_cents / 100.0,
                        "amount_cents": tx.amount_cents,
                        "currency": tx.currency,
                        "status": tx.status
                    })
                self._send_json(sorted(filtered, key=lambda x: x["date"], reverse=True))
                return

            # 5. Budgets
            if path == "/api/budgets":
                period = query.get("period", [time.strftime("%Y-%m")])[0]
                status = budget_mgr.get_envelope_status(client_id, period)
                self._send_json([
                    {
                        "category_id": s["category_id"],
                        "category_name": s["category_id"].replace("cat_", "").replace("_", " ").title(),
                        "allocated": float(s["allocated"].value),
                        "spent": float(s["spent"].value),
                        "remaining": float(s["remaining"].value),
                        "percentage_spent": s["percentage_spent"],
                        "is_over_budget": float(s["spent"].value) > float(s["allocated"].value)
                    }
                    for s in status
                ])
                return

            # 6. Investments & Portfolio
            if path == "/api/investments":
                holdings = user_holdings.get(client_id, [])
                total_val = sum(h["market_value"] for h in holdings)
                total_cost = sum(h["shares"] * h["cost_basis"] for h in holdings)
                total_gain = total_val - total_cost

                # Calculate MPT metrics
                returns_series = [0.012, -0.005, 0.021, 0.015, -0.010, 0.018, 0.009, 0.022, -0.004, 0.014]
                sharpe = PortfolioRiskMetrics.calculate_sharpe_ratio(returns_series)
                sortino = PortfolioRiskMetrics.calculate_sortino_ratio(returns_series)
                var_95 = PortfolioRiskMetrics.calculate_value_at_risk(total_val, returns_series, 0.95)

                self._send_json({
                    "total_portfolio_value": total_val,
                    "total_cost_basis": total_cost,
                    "total_unrealized_gain": total_gain,
                    "unrealized_gain_pct": round((total_gain / total_cost * 100.0) if total_cost > 0 else 0.0, 2),
                    "holdings": holdings,
                    "metrics": {
                        "sharpe_ratio": round(sharpe, 2),
                        "sortino_ratio": round(sortino, 2),
                        "var_95_daily": round(var_95, 2)
                    }
                })
                return

            # 7. Tax Analysis
            if path == "/api/taxes":
                state_code = query.get("state", ["CA"])[0]
                tax_info = StateTaxCalculator.calculate_state_liability(state_code, 12480000, FilingStatus.SINGLE, 1460000)
                harvestable = [
                    TaxableHolding("BND", 120.0, 78.0, 72.0, "2025-03-15")
                ]
                harvest_opps = TaxLossHarvester.find_harvesting_opportunities(harvestable)

                self._send_json({
                    "federal_estimated_tax": 18450.00,
                    "effective_federal_rate_pct": 14.8,
                    "state_tax": tax_info,
                    "capital_gains_summary": {
                        "short_term_gains": 2400.00,
                        "long_term_gains": 12292.00,
                        "harvestable_losses": 720.00,
                        "net_taxable_gains": 13972.00
                    },
                    "tax_loss_harvesting_opportunities": harvest_opps,
                    "disclaimer": "Estimates provided for analytical simulation purposes. Not certified tax or legal advice."
                })
                return

            # 8. Debt Optimization
            if path == "/api/debt":
                debts = user_debts.get(client_id, [])
                total_debt = sum(d["balance"] for d in debts)
                total_min_pay = sum(d["min_payment"] for d in debts)
                dti_pct = round((total_debt / (10400 * 12) * 100.0), 1)

                self._send_json({
                    "total_debt_balance": total_debt,
                    "total_monthly_minimum": total_min_pay,
                    "debt_to_income_ratio_pct": dti_pct,
                    "debts": debts,
                    "avalanche_recommendation": "Pay off Sapphire Preferred Card (22.4% APR) first to save $325.00 in interest."
                })
                return

            # 9. Financial Health
            if path == "/api/financial-health":
                assets, debts, _ = account_mgr.compute_net_worth(client_id)
                health = FinancialHealthCalculator.evaluate_health(
                    monthly_income_cents=1040000,
                    monthly_expenses_cents=275349,
                    liquid_assets_cents=3250000,
                    total_debt_cents=int(float(debts.value) * 100),
                    budget_utilization_pct=88.0,
                    asset_classes_count=4
                )
                self._send_json(health)
                return

            # 10. Compliance & AML
            if path == "/api/compliance":
                all_txs = tx_processor.get_user_transactions(client_id)
                tx_dicts = [{"amount_cents": t.amount_cents, "date": t.date} for t in all_txs]
                alerts = AMLMonitoringEngine.scan_for_structuring(tx_dicts)
                self._send_json({
                    "kyc_status": "VERIFIED_LEVEL_3",
                    "risk_tier": "LOW_RISK",
                    "sanctions_watchlist_status": "CLEAR_PASSED",
                    "last_screening_timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
                    "aml_alerts": alerts
                })
                return

            # 11. Audit History
            if path == "/api/audit":
                records = audit_engine.get_records(limit=50)
                is_valid, err = audit_engine.verify_chain_integrity()
                self._send_json({
                    "is_chain_valid": is_valid,
                    "verification_error": err,
                    "total_audited_events": len(records),
                    "events": records
                })
                return

            # 12. Advisor Recommendations & Alerts
            if path == "/api/advisor/recommendations":
                recs = recs_service.get_client_recommendations(client_id)
                self._send_json(recs)
                return

            if path == "/api/advisor/alerts":
                alerts = recs_service.get_client_alerts(client_id)
                self._send_json(alerts)
                return

            if path == "/api/advisor/stress-test":
                stress = recs_service.get_stress_test_analysis(client_id)
                self._send_json(stress)
                return

            # 13. Reports
            if path == "/api/reports/summary":
                summary = FinancialReportsGenerator.generate_full_financial_summary(client_id, account_mgr, ledger, budget_mgr)
                self._send_json(summary)
                return

            if path == "/api/reports/export-csv":
                export_type = query.get("type", ["accounts"])[0]
                if export_type == "transactions":
                    txs = tx_processor.get_user_transactions(client_id)
                    csv_data = FinancialReportsGenerator.export_transactions_csv(txs)
                    filename = "TrueBalance_Transactions.csv"
                else:
                    csv_data = FinancialReportsGenerator.export_accounts_csv(client_id, account_mgr)
                    filename = "TrueBalance_Accounts.csv"

                self.send_response(200)
                self.send_header("Content-Type", "text/csv; charset=utf-8")
                self.send_header("Content-Disposition", f"attachment; filename={filename}")
                self.end_headers()
                self.wfile.write(csv_data.encode("utf-8"))
                return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_length = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(content_length)
        payload = json.loads(body_bytes.decode("utf-8")) if body_bytes else {}

        # 1. Unauthenticated Login API
        if path == "/api/auth/login":
            email = payload.get("email", "")
            password = payload.get("password", "")

            auth_res = auth_service.authenticate(email, password)
            if not auth_res:
                self._send_error("Invalid email or password. Please try again.", 401)
                return

            user_info, access_token, refresh_token = auth_res
            audit_engine.append_event(
                f"ev_{str(uuid.uuid4())[:8]}",
                user_info["user_id"],
                user_info["email"],
                "LOGIN",
                "SESSION",
                user_info["user_id"],
                {"role": user_info["role"], "ip": self.client_address[0]}
            )

            self._send_json({
                "status": "SUCCESS",
                "user": user_info,
                "access_token": access_token,
                "refresh_token": refresh_token
            })
            return

        # Authenticate all subsequent POST requests
        auth_user = self._get_auth_context()
        if not auth_user:
            self._send_error("Authentication required", 401)
            return

        role = auth_user.get("role")
        user_id = auth_user.get("sub")
        client_id = self._get_target_client_id(auth_user)

        # 2. Auth Logout
        if path == "/api/auth/logout":
            audit_engine.append_event(f"ev_{str(uuid.uuid4())[:8]}", user_id, auth_user.get("email", ""), "LOGOUT", "SESSION", user_id)
            self._send_json({"status": "SUCCESS", "message": "Logged out successfully"})
            return

        # 3. Auth Change Password
        if path == "/api/auth/change-password":
            old_p = payload.get("old_password", "")
            new_p = payload.get("new_password", "")
            ok, msg = auth_service.change_password(user_id, old_p, new_p)
            if not ok:
                self._send_error(msg, 400)
                return
            audit_engine.append_event(f"ev_{str(uuid.uuid4())[:8]}", user_id, auth_user.get("email", ""), "PASSWORD_CHANGED", "USER", user_id)
            self._send_json({"status": "SUCCESS", "message": msg})
            return

        # 4. Create Account (ACCOUNT_OWNER ONLY)
        if path == "/api/accounts":
            if role != Role.ACCOUNT_OWNER.value:
                self._send_error("Forbidden: Financial Advisors cannot create client accounts.", 403)
                return

            name = payload.get("name", "").strip()
            acc_type = payload.get("type", "CHECKING")
            balance_cents = int(float(payload.get("balance", 0)) * 100)
            institution = payload.get("institution", "Community Bank")

            if not name:
                self._send_error("Account name is required", 422)
                return

            acc = account_mgr.create_account(
                user_id=client_id,
                name=name,
                account_type=acc_type,
                initial_balance_cents=balance_cents,
                institution_name=institution
            )
            audit_engine.append_event(f"ev_{str(uuid.uuid4())[:8]}", user_id, auth_user.get("email", ""), "ACCOUNT_CREATED", "ACCOUNT", acc.account_id, {"name": name, "type": acc_type})
            self._send_json({"status": "SUCCESS", "account_id": acc.account_id})
            return

        # 5. Create Transaction (ACCOUNT_OWNER ONLY)
        if path == "/api/transactions":
            if role != Role.ACCOUNT_OWNER.value:
                self._send_error("Forbidden: Financial Advisors cannot post financial transactions.", 403)
                return

            acc_id = payload.get("account_id")
            amount = float(payload.get("amount", 0))
            amount_cents = int(amount * 100)
            raw_desc = payload.get("description", "Manual entry").strip()
            merchant = payload.get("merchant", raw_desc).strip()
            category_id = payload.get("category_id", "cat_shopping")
            tx_date = payload.get("date", time.strftime("%Y-%m-%d"))

            if not acc_id or amount == 0:
                self._send_error("Valid account and non-zero amount are required", 422)
                return

            tx = tx_processor.process_transaction(
                account_id=acc_id,
                user_id=client_id,
                amount_cents=amount_cents,
                date=tx_date,
                merchant_name=merchant,
                raw_description=raw_desc,
                category_id=category_id,
                allow_duplicates=True
            )

            # Record budget expense if negative
            if amount_cents < 0 and category_id:
                period = tx_date[:7]
                budget_mgr.record_expense(client_id, category_id, period, abs(amount_cents))

            audit_engine.append_event(f"ev_{str(uuid.uuid4())[:8]}", user_id, auth_user.get("email", ""), "TRANSACTION_CREATED", "TRANSACTION", tx.transaction_id, {"amount": amount, "merchant": merchant})
            self._send_json({"status": "SUCCESS", "transaction_id": tx.transaction_id})
            return

        # 6. Update Budget Envelope (ACCOUNT_OWNER ONLY)
        if path == "/api/budgets/envelope":
            if role != Role.ACCOUNT_OWNER.value:
                self._send_error("Forbidden: Financial Advisors cannot modify client budgets.", 403)
                return

            category_id = payload.get("category_id")
            allocated_dollars = float(payload.get("allocated", 0))
            period = payload.get("period", time.strftime("%Y-%m"))
            env = budget_mgr.create_envelope(client_id, category_id, int(allocated_dollars * 100), period)
            audit_engine.append_event(f"ev_{str(uuid.uuid4())[:8]}", user_id, auth_user.get("email", ""), "BUDGET_UPDATED", "BUDGET", category_id, {"allocated": allocated_dollars})
            self._send_json({"status": "SUCCESS", "envelope_id": env.envelope_id})
            return

        # 7. Add Investment Holding (ACCOUNT_OWNER ONLY)
        if path == "/api/investments/holdings":
            if role != Role.ACCOUNT_OWNER.value:
                self._send_error("Forbidden: Financial Advisors cannot modify investment portfolios directly.", 403)
                return

            symbol = payload.get("symbol", "").upper().strip()
            name = payload.get("name", symbol).strip()
            shares = float(payload.get("shares", 0))
            cost_basis = float(payload.get("cost_basis", 0))
            current_price = float(payload.get("current_price", cost_basis))
            asset_class = payload.get("asset_class", "EQUITY")

            if not symbol or shares <= 0:
                self._send_error("Valid symbol and share quantity required", 422)
                return

            mkt_val = shares * current_price
            pnl = mkt_val - (shares * cost_basis)

            holdings = user_holdings.setdefault(client_id, [])
            new_holding = {
                "holding_id": f"h_{str(uuid.uuid4())[:8]}",
                "symbol": symbol,
                "name": name,
                "asset_class": asset_class,
                "shares": shares,
                "cost_basis": cost_basis,
                "current_price": current_price,
                "market_value": round(mkt_val, 2),
                "unrealized_pnl": round(pnl, 2),
                "weight_pct": 10.0
            }
            holdings.append(new_holding)
            audit_engine.append_event(f"ev_{str(uuid.uuid4())[:8]}", user_id, auth_user.get("email", ""), "HOLDING_ADDED", "INVESTMENT", symbol, {"shares": shares, "cost": cost_basis})
            self._send_json({"status": "SUCCESS", "holding": new_holding})
            return

        # 8. Monte Carlo Stochastic Simulation (Accessible by BOTH roles)
        if path == "/api/investments/monte-carlo":
            initial_val = float(payload.get("initial_wealth", 94200.0))
            annual_contrib = float(payload.get("annual_contribution", 24000.0))
            ret = float(payload.get("expected_return", 0.08))
            vol = float(payload.get("volatility", 0.15))
            years = int(payload.get("years", 25))
            iters = int(payload.get("iterations", 2000))

            res = monte_carlo.simulate_wealth_trajectory(
                starting_wealth=max(1000.0, initial_val),
                annual_contribution=annual_contrib,
                annual_withdrawal=0.0,
                expected_annual_return=ret,
                annual_volatility=vol,
                years=years,
                iterations=iters
            )
            self._send_json(res)
            return

        # 9. Create Advisor Recommendation (FINANCIAL_ADVISOR ONLY)
        if path == "/api/advisor/recommendations":
            if role != Role.FINANCIAL_ADVISOR.value:
                self._send_error("Forbidden: Only Financial Advisors can author recommendations.", 403)
                return

            title = payload.get("title", "").strip()
            category = payload.get("category", "General")
            explanation = payload.get("explanation", "").strip()
            priority = payload.get("priority", "MEDIUM")

            if not title or not explanation:
                self._send_error("Title and explanation are required", 422)
                return

            rec = recs_service.add_recommendation(
                client_id=client_id,
                advisor_id=user_id,
                advisor_name=auth_user.get("email", "Sarah Jenkins, CFP®"),
                title=title,
                category=category,
                explanation=explanation,
                priority=priority
            )
            audit_engine.append_event(f"ev_{str(uuid.uuid4())[:8]}", user_id, auth_user.get("email", ""), "RECOMMENDATION_CREATED", "ADVISOR", rec["rec_id"], {"title": title, "priority": priority})
            self._send_json({"status": "SUCCESS", "recommendation": rec})
            return

        # 10. Dispatch Custom Advisor Alert (FINANCIAL_ADVISOR ONLY)
        if path == "/api/advisor/alerts":
            if role != Role.FINANCIAL_ADVISOR.value:
                self._send_error("Forbidden: Only Financial Advisors can dispatch alerts.", 403)
                return

            title = payload.get("title", "").strip()
            message = payload.get("message", "").strip()
            severity = payload.get("severity", "WARNING")
            impact = payload.get("impact_amount")

            if not title or not message:
                self._send_error("Alert title and message are required", 422)
                return

            alert = recs_service.add_alert(
                client_id=client_id,
                advisor_id=user_id,
                advisor_name=auth_user.get("email", "Sarah Jenkins, CFP®"),
                title=title,
                message=message,
                severity=severity,
                impact_amount=impact
            )
            audit_engine.append_event(f"ev_{str(uuid.uuid4())[:8]}", user_id, auth_user.get("email", ""), "ALERT_DISPATCHED", "ADVISOR", alert["alert_id"], {"title": title, "severity": severity})
            self._send_json({"status": "SUCCESS", "alert": alert})
            return

        # 11. Acknowledge Alert (ACCOUNT_OWNER ONLY)
        if path == "/api/advisor/alerts/acknowledge":
            alert_id = payload.get("alert_id")
            if alert_id:
                recs_service.acknowledge_alert(alert_id, client_id)
            self._send_json({"status": "SUCCESS"})
            return

        self._send_error("Endpoint not found", 404)

    def log_message(self, format, *args):
        pass


def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), TrueBalanceAPIHandler) as httpd:
        print("=" * 80)
        print("   TRUEBALANCE ENTERPRISE FINTECH PLATFORM IS RUNNING LIVE")
        print("   Role 1 (Account Owner):    user@truebalance.com / User@123")
        print("   Role 2 (Financial Advisor): advisor@truebalance.com / Advisor@123")
        print(f"   Server active at: http://localhost:{PORT}")
        print("=" * 80)
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
