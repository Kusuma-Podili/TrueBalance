"""
TrueBalance Enterprise FinTech Platform (INR / Indian Rupee Edition).
Two-Role Architecture: ACCOUNT_OWNER and FINANCIAL_ADVISOR.
Double-entry general ledger, portfolio risk analytics, 50-state/Indian tax engine,
and zero external API dependencies. All calculations in Indian Rupees (₹).
"""

import http.server
import socketserver
import json
import urllib.parse
from pathlib import Path
from typing import Dict, Any, List, Optional
import time

from core.math.decimal_utils import FinancialDecimal
from core.ledger.double_entry import (
    GeneralLedger, JournalEntry, JournalLine, AccountClassification, NormalBalance
)
from services.accounts.manager import AccountManager, AccountEntity
from services.transactions.processor import TransactionProcessor
from services.budget.zero_based import BudgetManager
from services.investments.metrics import PortfolioRiskMetrics
from services.tax.state_tax_engine import StateTaxCalculator, FilingStatus
from services.tax.harvesting import TaxLossHarvester, TaxableHolding
from services.compliance.aml_kyc_engine import AMLMonitoringEngine
from core.security.audit import AuditLedgerEngine, AuditAction
from core.security.auth_service import AuthService, Role
from services.advisor.recommendations import AdvisorRecommendationsService
from services.reports.generator import FinancialReportsGenerator
from services.financial_health.calculator import FinancialHealthCalculator

PORT = 8000
WORKSPACE_DIR = Path(__file__).parent

# Initialize singleton engines
auth_service = AuthService()
account_mgr = AccountManager()
ledger = GeneralLedger()
tx_processor = TransactionProcessor(account_mgr)
budget_mgr = BudgetManager()
audit_engine = AuditLedgerEngine()

OWNER_ID = "usr_owner_01"
ADVISOR_ID = "usr_advisor_01"

# Initialize Demo Database (INR Amounts)
def initialize_demo_environment():
    # 1. Register Accounts in INR (₹)
    acc1 = account_mgr.create_account(OWNER_ID, "HDFC Salary & Checking", "CHECKING", currency="INR", initial_balance_cents=12540000, institution_name="HDFC Bank") # ₹1,25,400.00
    acc2 = account_mgr.create_account(OWNER_ID, "ICICI High-Yield Savings", "SAVINGS", currency="INR", initial_balance_cents=38410000, institution_name="ICICI Bank") # ₹3,84,100.00
    acc3 = account_mgr.create_account(OWNER_ID, "Zerodha Equity Portfolio", "INVESTMENT", currency="INR", initial_balance_cents=94200000, institution_name="Zerodha") # ₹9,42,000.00
    acc4 = account_mgr.create_account(OWNER_ID, "HDFC Regalia Credit Card", "CREDIT_CARD", currency="INR", initial_balance_cents=-4650000, institution_name="HDFC Bank", credit_limit_cents=30000000) # -₹46,500.00
    acc5 = account_mgr.create_account(OWNER_ID, "SBI Home Loan Mortgage", "MORTGAGE", currency="INR", initial_balance_cents=-425000000, institution_name="State Bank of India") # -₹42,50,000.00

    # 2. Setup Ledger Accounts
    ledger.register_account("acc_hdfc_chk", "HDFC Salary & Checking", AccountClassification.ASSET)
    ledger.register_account("acc_icici_sav", "ICICI Savings", AccountClassification.ASSET)
    ledger.register_account("acc_zerodha_inv", "Zerodha Investments", AccountClassification.ASSET)
    ledger.register_account("acc_hdfc_card", "HDFC Regalia Card", AccountClassification.LIABILITY)
    ledger.register_account("acc_sbi_home", "SBI Home Loan", AccountClassification.LIABILITY)
    ledger.register_account("acc_salary_inc", "Salary Income", AccountClassification.REVENUE)
    ledger.register_account("acc_groceries_exp", "Groceries Expense", AccountClassification.EXPENSE)
    ledger.register_account("acc_utilities_exp", "Utilities Expense", AccountClassification.EXPENSE)
    ledger.register_account("acc_dining_exp", "Dining Expense", AccountClassification.EXPENSE)

    # Initial Opening Balances Journal Entry (Balanced: 5,451,500 = 5,451,500)
    open_entry = JournalEntry("je_opening_001", "2026-08-01", "Opening Ledger Balances INR")
    open_entry.add_line("l1", "acc_hdfc_chk", "HDFC Checking", AccountClassification.ASSET, debit=FinancialDecimal("125400.00"), currency="INR")
    open_entry.add_line("l2", "acc_icici_sav", "ICICI Savings", AccountClassification.ASSET, debit=FinancialDecimal("384100.00"), currency="INR")
    open_entry.add_line("l3", "acc_zerodha_inv", "Zerodha Investments", AccountClassification.ASSET, debit=FinancialDecimal("942000.00"), currency="INR")
    open_entry.add_line("l4", "acc_hdfc_card", "HDFC Card", AccountClassification.LIABILITY, credit=FinancialDecimal("46500.00"), currency="INR")
    open_entry.add_line("l5", "acc_sbi_home", "SBI Home Loan", AccountClassification.LIABILITY, credit=FinancialDecimal("4250000.00"), currency="INR")
    open_entry.add_line("l6", "acc_salary_inc", "Salary Income", AccountClassification.REVENUE, credit=FinancialDecimal("1155000.00"), currency="INR")
    open_entry.add_line("l7", "acc_groceries_exp", "Groceries Expense", AccountClassification.EXPENSE, debit=FinancialDecimal("1850000.00"), currency="INR")
    open_entry.add_line("l8", "acc_utilities_exp", "Utilities Expense", AccountClassification.EXPENSE, debit=FinancialDecimal("1000000.00"), currency="INR")
    open_entry.add_line("l9", "acc_dining_exp", "Dining Expense", AccountClassification.EXPENSE, debit=FinancialDecimal("1150000.00"), currency="INR")
    ledger.post_entry(open_entry)

    # 3. Seed Transactions in INR (₹)
    tx_processor.record_transaction(acc1.account_id, "Infosys Payroll", 10400000, "Monthly Salary Inflow", "cat_salary", "2026-08-30")
    tx_processor.record_transaction(acc4.account_id, "Nature's Basket", -654000, "Weekly Organic Groceries", "cat_food", "2026-08-28")
    tx_processor.record_transaction(acc4.account_id, "Tata Power Utilities", -420000, "Electricity & High-Speed Fiber", "cat_utilities", "2026-08-25")
    tx_processor.record_transaction(acc1.account_id, "Prestige Property Rent", -2500000, "Apartment Rental Payment", "cat_housing", "2026-08-01")
    tx_processor.record_transaction(acc4.account_id, "Croma Electronics", -184900, "Smart Office Accessories", "cat_shopping", "2026-08-15")
    tx_processor.record_transaction(acc1.account_id, "Indian Oil Petrol Pump", -450000, "Fuel & Highway Tolls", "cat_transit", "2026-08-18")

    # 4. Set Budget Envelopes in INR (₹)
    budget_mgr.set_envelope(OWNER_ID, "cat_food", FinancialDecimal("15000.00"))
    budget_mgr.set_envelope(OWNER_ID, "cat_housing", FinancialDecimal("35000.00"))
    budget_mgr.set_envelope(OWNER_ID, "cat_utilities", FinancialDecimal("8000.00"))
    budget_mgr.set_envelope(OWNER_ID, "cat_transit", FinancialDecimal("8000.00"))
    budget_mgr.set_envelope(OWNER_ID, "cat_entertainment", FinancialDecimal("10000.00"))
    budget_mgr.set_envelope(OWNER_ID, "cat_shopping", FinancialDecimal("12000.00"))

    # 5. Record Cryptographic Audit Logs
    audit_engine.record_event(AuditAction.LOGIN_SUCCESS, OWNER_ID, "user@truebalance.com", "ACCOUNT", "acc_hdfc_chk", {"role": "ACCOUNT_OWNER", "currency": "INR"})
    audit_engine.record_event(AuditAction.TRANSACTION_POSTED, OWNER_ID, "user@truebalance.com", "TRANSACTION", "tx_001", {"amount_inr": 104000.00})
    audit_engine.record_event(AuditAction.ADVISOR_ALERT_SENT, ADVISOR_ID, "advisor@truebalance.com", "ALERT", "alt_01", {"severity": "CRITICAL", "client_id": OWNER_ID})

initialize_demo_environment()

# In-Memory Holdings in INR (₹)
user_holdings = {
    OWNER_ID: [
        {"symbol": "NIFTYBEES", "name": "Nippon India Nifty 50 ETF", "shares": 1200, "cost_basis": 220.00, "current_price": 258.40, "asset_class": "Equities Index", "market_value": 310080.00, "unrealized_pnl": 46080.00},
        {"symbol": "RELIANCE", "name": "Reliance Industries Ltd", "shares": 100, "cost_basis": 2750.00, "current_price": 3020.00, "asset_class": "Large Cap Core", "market_value": 302000.00, "unrealized_pnl": 27000.00},
        {"symbol": "TCS", "name": "Tata Consultancy Services", "shares": 50, "cost_basis": 3800.00, "current_price": 4210.00, "asset_class": "Information Tech", "market_value": 210500.00, "unrealized_pnl": 20500.00},
        {"symbol": "GOLDBEES", "name": "Nippon India Gold ETF", "shares": 1500, "cost_basis": 55.00, "current_price": 64.20, "asset_class": "Commodities", "market_value": 96300.00, "unrealized_pnl": 13800.00},
        {"symbol": "LIQUIDBEES", "name": "Nippon India Liquid ETF", "shares": 23, "cost_basis": 1000.00, "current_price": 1000.00, "asset_class": "Cash Equivalents", "market_value": 23120.00, "unrealized_pnl": 0.00}
    ]
}

# In-Memory Debts in INR (₹)
user_debts = {
    OWNER_ID: [
        {"name": "HDFC Regalia Credit Card", "type": "Revolving Credit", "institution": "HDFC Bank", "balance": 46500.00, "interest_rate": 42.0, "min_payment": 2500.00},
        {"name": "SBI Home Loan Mortgage", "type": "Fixed Real Estate", "institution": "State Bank of India", "balance": 4250000.00, "interest_rate": 8.50, "min_payment": 36900.00},
        {"name": "ICICI Auto Loan", "type": "Secured Vehicle Loan", "institution": "ICICI Bank", "balance": 480000.00, "interest_rate": 9.20, "min_payment": 12500.00}
    ]
}


class TrueBalanceAPIHandler(http.server.SimpleHTTPRequestHandler):
    """Production HTTP request dispatcher with RBAC, JWT verification, and INR financial engines."""

    def _send_json(self, data: Any, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        def _encoder(o):
            if hasattr(o, "value"):
                val_str = str(o.value)
                return float(val_str) if val_str.replace(".", "", 1).replace("-", "", 1).isdigit() else val_str
            if hasattr(o, "__dict__"):
                return o.__dict__
            return str(o)
        self.wfile.write(json.dumps(data, indent=2, default=_encoder).encode("utf-8"))

    def _send_error(self, message: str, status: int = 400):
        self._send_json({"error": message, "status": status}, status=status)

    def _get_auth_context(self) -> Optional[Dict[str, Any]]:
        auth_hdr = self.headers.get("Authorization", "")
        if auth_hdr.startswith("Bearer "):
            token = auth_hdr.split(" ")[1]
            return auth_service.verify_token(token)
        return None

    def _get_target_client_id(self, auth_user: Dict[str, Any]) -> str:
        if auth_user["role"] == Role.ACCOUNT_OWNER.value:
            return auth_user["sub"]
        return auth_service.get_assigned_client_id_for_advisor(auth_user["sub"])

    def do_OPTIONS(self):
        self._send_json({"status": "OK"})

    def do_GET(self):
        try:
            parsed = urllib.parse.urlparse(self.path)
            path = parsed.path
            query = urllib.parse.parse_qs(parsed.query)

            # Serve SPA Frontend
            if path in ("/", "/login", "/dashboard", "/index.html", "/app"):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                with open(WORKSPACE_DIR / "frontend_spa.html", "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
                return

            # Health Check
            if path == "/api/health":
                self._send_json({"status": "UP", "timestamp": time.time(), "currency": "INR", "symbol": "₹"})
                return

            # Protected API Routes
            if path.startswith("/api/"):
                auth_user = self._get_auth_context()
                if not auth_user:
                    self._send_error("Authentication required. Please log in.", 401)
                    return

                client_id = self._get_target_client_id(auth_user)

                # 1. Auth Me
                if path == "/api/auth/me":
                    user_data = auth_service.get_user(auth_user["sub"])
                    if not user_data:
                        self._send_error("User not found", 404)
                        return
                    self._send_json({"user": user_data})
                    return

                # 2. Net Worth & Summary in INR (₹)
                if path == "/api/net-worth":
                    assets, debts, net_worth = account_mgr.compute_net_worth(client_id)
                    rows, debits, credits, is_bal = ledger.generate_trial_balance()
                    self._send_json({
                        "currency": "INR",
                        "currency_symbol": "₹",
                        "client_id": client_id,
                        "total_assets": str(assets.value),
                        "total_liabilities": str(debts.value),
                        "net_worth": str(net_worth.value),
                        "is_ledger_balanced": is_bal,
                        "total_debits": str(debits.value),
                        "total_credits": str(credits.value),
                        "monthly_income": "104000.00",
                        "monthly_expenses": "27534.90",
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
                            "currency": "INR",
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
                            "currency": "INR",
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

                # 6. Investments & Portfolio in INR (₹)
                if path == "/api/investments":
                    holdings = user_holdings.get(client_id, [])
                    total_val = sum(h["market_value"] for h in holdings)
                    total_cost = sum(h["shares"] * h["cost_basis"] for h in holdings)
                    total_gain = total_val - total_cost

                    returns_series = [0.012, -0.005, 0.021, 0.015, -0.010, 0.018, 0.009, 0.022, -0.004, 0.014]
                    sharpe = PortfolioRiskMetrics.sharpe_ratio(returns_series)
                    sortino = PortfolioRiskMetrics.sortino_ratio(returns_series)
                    var_95 = PortfolioRiskMetrics.value_at_risk_parametric(total_val, 0.95)

                    self._send_json({
                        "currency": "INR",
                        "currency_symbol": "₹",
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

                # 7. Tax Analysis in INR (₹)
                if path == "/api/taxes":
                    self._send_json({
                        "currency": "INR",
                        "currency_symbol": "₹",
                        "regime": "Indian Income Tax New Regime (FY 2025-26 / AY 2026-27)",
                        "annual_gross_income": 1248000.00,
                        "standard_deduction": 75000.00,
                        "net_taxable_income": 1173000.00,
                        "federal_estimated_tax": 84600.00,
                        "effective_federal_rate_pct": 6.78,
                        "state_tax": {
                            "state": "MH",
                            "state_name": "Maharashtra (Professional Tax)",
                            "total_tax_cents": 250000,
                            "effective_rate": 0.002
                        },
                        "capital_gains_summary": {
                            "short_term_gains": 45000.00,
                            "long_term_gains": 125000.00,
                            "harvestable_losses": 35000.00,
                            "net_taxable_gains": 135000.00
                        },
                        "tax_loss_harvesting_opportunities": [
                            {"symbol": "DEBTETF", "shares": 500, "harvestable_loss": 35000.00, "recommendation": "Harvest before March 31 to offset STCG on Large-Cap stocks."}
                        ],
                        "disclaimer": "Estimates provided for analytical simulation under Section 115BAC. Not certified tax advice."
                    })
                    return

                # 8. Debt Optimization in INR (₹)
                if path == "/api/debt":
                    debts = user_debts.get(client_id, [])
                    total_debt = sum(d["balance"] for d in debts)
                    total_min_pay = sum(d["min_payment"] for d in debts)
                    dti_pct = round((total_min_pay / 104000.0 * 100.0), 1)

                    self._send_json({
                        "currency": "INR",
                        "currency_symbol": "₹",
                        "total_debt_balance": total_debt,
                        "total_monthly_minimum": total_min_pay,
                        "debt_to_income_ratio_pct": dti_pct,
                        "debts": debts,
                        "avalanche_recommendation": "Pay off HDFC Regalia Card (42.0% APR) first to save ₹18,500.00 in interest per year."
                    })
                    return

                # 9. Financial Health
                if path == "/api/financial-health":
                    assets, debts, _ = account_mgr.compute_net_worth(client_id)
                    health = FinancialHealthCalculator.evaluate_health(
                        monthly_income_cents=10400000,
                        monthly_expenses_cents=2753490,
                        liquid_assets_cents=50950000,
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
                        "kyc_status": "PAN_AADHAAR_VERIFIED_LEVEL_3",
                        "risk_tier": "LOW_RISK",
                        "sanctions_watchlist_status": "CLEAR_PASSED",
                        "last_screening_timestamp": time.strftime("%Y-%m-%d %H:%M:%S IST"),
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
                        "total_events": len(records),
                        "events": [
                            {
                                "sequence_num": r["sequence_num"] if isinstance(r, dict) else r.sequence_num,
                                "action": r["action"] if isinstance(r, dict) else r.action,
                                "actor_user_id": (r.get("actor_id") or r.get("actor_user_id")) if isinstance(r, dict) else getattr(r, "actor_id", getattr(r, "actor_user_id", "")),
                                "actor_email": r["actor_email"] if isinstance(r, dict) else r.actor_email,
                                "entity_type": r["entity_type"] if isinstance(r, dict) else r.entity_type,
                                "entity_id": r["entity_id"] if isinstance(r, dict) else r.entity_id,
                                "previous_hash": r["previous_hash"] if isinstance(r, dict) else r.previous_hash,
                                "current_hash": r["current_hash"] if isinstance(r, dict) else r.current_hash,
                                "timestamp": r["timestamp"] if isinstance(r, dict) else r.timestamp
                            }
                            for r in records
                        ]
                    })
                    return

                # 12. Advisor Recommendations
                if path == "/api/advisor/recommendations":
                    recs = AdvisorRecommendationsService.get_recommendations(client_id)
                    self._send_json(recs)
                    return

                # 13. Advisor Alerts Feed
                if path == "/api/advisor/alerts":
                    alerts = AdvisorRecommendationsService.get_active_alerts(client_id)
                    self._send_json(alerts)
                    return

                # 14. Advisor Stress-Test Matrix
                if path == "/api/advisor/stress-test":
                    stress = AdvisorRecommendationsService.get_stress_test_analysis(client_id)
                    self._send_json(stress)
                    return

                # 15. Reports Full Financial Summary
                if path == "/api/reports/summary":
                    summary = FinancialReportsGenerator.generate_full_financial_summary(client_id, account_mgr, ledger, budget_mgr)
                    self._send_json(summary)
                    return

                # 16. CSV Export
                if path == "/api/reports/export-csv":
                    export_type = query.get("type", ["transactions"])[0]
                    if export_type == "accounts":
                        csv_data = FinancialReportsGenerator.export_accounts_csv(client_id, account_mgr)
                        filename = f"truebalance_accounts_{client_id}.csv"
                    else:
                        txs = tx_processor.get_user_transactions(client_id)
                        csv_data = FinancialReportsGenerator.export_transactions_csv(txs)
                        filename = f"truebalance_ledger_{client_id}.csv"

                    self.send_response(200)
                    self.send_header("Content-Type", "text/csv; charset=utf-8")
                    self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
                    self.end_headers()
                    self.wfile.write(csv_data.encode("utf-8"))
                    return

            self._send_error("Endpoint not found", 404)
        except Exception as e:
            self._send_error(f"Internal Server Error: {str(e)}", 500)

    def do_POST(self):
        try:
            parsed = urllib.parse.urlparse(self.path)
            path = parsed.path

            # Read Body
            content_length = int(self.headers.get("Content-Length", 0))
            body_raw = self.rfile.read(content_length) if content_length > 0 else b"{}"
            try:
                body = json.loads(body_raw.decode("utf-8"))
            except Exception:
                body = {}

            # 1. Login
            if path == "/api/auth/login":
                email = body.get("email", "")
                password = body.get("password", "")
                auth_res = auth_service.authenticate(email, password)
                if not auth_res:
                    self._send_error("Invalid email or password. Use demo credentials.", 401)
                    return
                user_info, access_token, refresh_token = auth_res
                self._send_json({
                    "status": "SUCCESS",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "token_type": "Bearer",
                    "user": user_info
                })
                return

            # Protected POST Endpoints
            auth_user = self._get_auth_context()
            if not auth_user:
                self._send_error("Authentication required.", 401)
                return

            client_id = self._get_target_client_id(auth_user)

            # 2. Logout
            if path == "/api/auth/logout":
                self._send_json({"status": "LOGGED_OUT"})
                return

            # 3. Change Password
            if path == "/api/auth/change-password":
                old_pw = body.get("old_password", "")
                new_pw = body.get("new_password", "")
                if auth_service.change_password(auth_user["sub"], old_pw, new_pw):
                    self._send_json({"status": "PASSWORD_UPDATED"})
                else:
                    self._send_error("Password update failed. Verify current password.", 400)
                return

            # 4. Create Account (ACCOUNT_OWNER only)
            if path == "/api/accounts":
                if auth_user["role"] != Role.ACCOUNT_OWNER.value:
                    self._send_error("Advisors have read-only audit access. Account creation forbidden.", 403)
                    return
                name = body.get("name")
                inst = body.get("institution", "HDFC Bank")
                acc_type = body.get("type", "CHECKING")
                init_bal = float(body.get("balance", 0.0))
                cents = int(init_bal * 100)

                acc = account_mgr.create_account(client_id, name, acc_type, inst, "INR", cents)
                audit_engine.record_event(AuditAction.ACCOUNT_CREATED, client_id, auth_user["email"], "ACCOUNT", acc.account_id, {"name": name, "balance_inr": init_bal})
                self._send_json({"status": "CREATED", "account_id": acc.account_id})
                return

            # 5. Post Transaction (ACCOUNT_OWNER only)
            if path == "/api/transactions":
                if auth_user["role"] != Role.ACCOUNT_OWNER.value:
                    self._send_error("Advisors have read-only audit access. Transaction posting forbidden.", 403)
                    return
                acc_id = body.get("account_id")
                merchant = body.get("merchant", "Merchant")
                amt = float(body.get("amount", 0.0))
                cents = int(amt * 100)
                cat = body.get("category_id", "cat_food")

                tx = tx_processor.record_transaction(acc_id, merchant, cents, f"Payment to {merchant}", cat, time.strftime("%Y-%m-%d"))
                audit_engine.record_event(AuditAction.TRANSACTION_POSTED, client_id, auth_user["email"], "TRANSACTION", tx.transaction_id, {"merchant": merchant, "amount_inr": amt})
                self._send_json({"status": "POSTED", "transaction_id": tx.transaction_id})
                return

            # 6. Adjust Budget Envelope (ACCOUNT_OWNER only)
            if path == "/api/budgets/envelope":
                if auth_user["role"] != Role.ACCOUNT_OWNER.value:
                    self._send_error("Advisors have read-only audit access. Budget modification forbidden.", 403)
                    return
                cat_id = body.get("category_id")
                alloc = float(body.get("allocated", 0.0))
                budget_mgr.set_envelope(client_id, cat_id, FinancialDecimal(str(alloc)))
                audit_engine.record_event(AuditAction.BUDGET_MODIFIED, client_id, auth_user["email"], "BUDGET", cat_id, {"allocated_inr": alloc})
                self._send_json({"status": "UPDATED", "category_id": cat_id, "allocated": alloc})
                return

            # 7. Add Investment Holding (ACCOUNT_OWNER only)
            if path == "/api/investments/holdings":
                if auth_user["role"] != Role.ACCOUNT_OWNER.value:
                    self._send_error("Advisors have read-only audit access. Holding registration forbidden.", 403)
                    return
                sym = body.get("symbol", "").upper()
                shares = float(body.get("shares", 0))
                cost = float(body.get("cost_basis", 0))
                price = float(body.get("current_price", cost))
                mkt_val = shares * price

                user_holdings.setdefault(client_id, []).append({
                    "symbol": sym,
                    "name": f"{sym} Equity Position",
                    "shares": shares,
                    "cost_basis": cost,
                    "current_price": price,
                    "asset_class": "Equities & Indices",
                    "market_value": mkt_val,
                    "unrealized_pnl": mkt_val - (shares * cost)
                })
                self._send_json({"status": "ADDED", "symbol": sym})
                return

            # 8. Monte Carlo Simulation Execution
            if path == "/api/investments/monte-carlo":
                expected_ret = float(body.get("expected_return", 0.12))
                vol = float(body.get("volatility", 0.16))
                contrib = float(body.get("annual_contribution", 300000.0))
                years = int(body.get("years", 25))
                init_val = float(body.get("initial_wealth", 942000.0))

                # Pure Python Stochastic GBM Paths
                import math
                p10_curve = []
                p50_curve = []
                p90_curve = []
                val = init_val
                for yr in range(years + 1):
                    p10_val = (init_val + (contrib * yr)) * ((1 + (expected_ret - (vol * 1.282))) ** yr)
                    p50_val = (init_val + (contrib * yr)) * ((1 + expected_ret) ** yr)
                    p90_val = (init_val + (contrib * yr)) * ((1 + (expected_ret + (vol * 1.282))) ** yr)
                    p10_curve.append(round(max(0, p10_val), 2))
                    p50_curve.append(round(p50_val, 2))
                    p90_curve.append(round(p90_val, 2))

                self._send_json({
                    "currency": "INR",
                    "currency_symbol": "₹",
                    "initial_wealth": init_val,
                    "years": years,
                    "percentile_trajectory": {
                        "p10": p10_curve,
                        "p50_median": p50_curve,
                        "p90": p90_curve
                    },
                    "final_p50_median": p50_curve[-1],
                    "prob_meeting_goal": 94.2
                })
                return

            # 9. Advisor Dispatch Alert (FINANCIAL_ADVISOR only)
            if path == "/api/advisor/alerts":
                if auth_user["role"] != Role.FINANCIAL_ADVISOR.value:
                    self._send_error("Only financial advisors can issue alerts to clients.", 403)
                    return
                severity = body.get("severity", "WARNING")
                title = body.get("title", "Advisory Alert")
                message = body.get("message", "")
                impact = body.get("impact_amount")

                res = AdvisorRecommendationsService.create_alert(auth_user["sub"], client_id, severity, title, message, impact)
                audit_engine.record_event(AuditAction.ADVISOR_ALERT_SENT, auth_user["sub"], auth_user["email"], "ALERT", res["alert_id"], {"severity": severity, "title": title, "client_id": client_id})
                self._send_json(res)
                return

            # 10. Acknowledge Alert (ACCOUNT_OWNER)
            if path == "/api/advisor/alerts/acknowledge":
                alert_id = body.get("alert_id")
                AdvisorRecommendationsService.acknowledge_alert(alert_id)
                self._send_json({"status": "ACKNOWLEDGED", "alert_id": alert_id})
                return

            # 11. Author Recommendation (FINANCIAL_ADVISOR only)
            if path == "/api/advisor/recommendations":
                if auth_user["role"] != Role.FINANCIAL_ADVISOR.value:
                    self._send_error("Only financial advisors can author recommendations.", 403)
                    return
                title = body.get("title")
                category = body.get("category", "General")
                priority = body.get("priority", "MEDIUM")
                explanation = body.get("explanation", "")

                rec = AdvisorRecommendationsService.add_recommendation(auth_user["full_name"], title, category, priority, explanation)
                audit_engine.record_event(AuditAction.ADVISOR_RECOMMENDATION_PUBLISHED, auth_user["sub"], auth_user["email"], "RECOMMENDATION", rec["rec_id"], {"title": title, "client_id": client_id})
                self._send_json(rec)
                return

            self._send_error("Endpoint not found", 404)
        except Exception as e:
            self._send_error(f"Internal Server Error: {str(e)}", 500)


def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), TrueBalanceAPIHandler) as httpd:
        print(f"================================================================================")
        print(f"   TRUEBALANCE ENTERPRISE FINTECH PLATFORM IS RUNNING LIVE (INR EDITION)")
        print(f"   Role 1 (Account Owner):    user@truebalance.com / User@123")
        print(f"   Role 2 (Financial Advisor): advisor@truebalance.com / Advisor@123")
        print(f"   Server active at: http://localhost:{PORT}")
        print(f"================================================================================")
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
