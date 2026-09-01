"""
Financial Reports Generation & Export Engine.
Generates comprehensive Balance Sheets, Income Statements, Net Worth summaries,
Budget Performance audits, Tax reports, and CSV exports.
"""

import csv
import io
import time
from typing import Dict, Any, List
from core.ledger.double_entry import GeneralLedger
from services.accounts.manager import AccountManager
from services.budget.zero_based import BudgetManager


class FinancialReportsGenerator:
    """Generates structured financial reports for Account Owners and Advisors."""

    @staticmethod
    def generate_full_financial_summary(
        user_id: str,
        account_mgr: AccountManager,
        ledger: GeneralLedger,
        budget_mgr: BudgetManager
    ) -> Dict[str, Any]:
        assets, debts, net_worth = account_mgr.compute_net_worth(user_id)
        accounts = account_mgr.list_user_accounts(user_id)
        sheet = ledger.generate_balance_sheet()
        tb_rows, total_debits, total_credits, is_balanced = ledger.generate_trial_balance()
        budget_status = budget_mgr.get_envelope_status(user_id, time.strftime("%Y-%m"))

        return {
            "generated_at": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
            "user_id": user_id,
            "net_worth_summary": {
                "total_assets": str(assets.value),
                "total_liabilities": str(debts.value),
                "net_worth": str(net_worth.value),
                "ledger_status": "BALANCED" if is_balanced else "UNBALANCED",
                "total_debits": str(total_debits.value),
                "total_credits": str(total_credits.value)
            },
            "accounts_count": len(accounts),
            "accounts": [
                {
                    "name": a.account_name,
                    "type": a.account_type,
                    "balance": a.current_balance_cents / 100.0,
                    "institution": a.institution_name
                }
                for a in accounts
            ],
            "balance_sheet": sheet,
            "budget_envelopes": [
                {
                    "category": b["category_id"].replace("cat_", ""),
                    "allocated": float(b["allocated"].value),
                    "spent": float(b["spent"].value),
                    "remaining": float(b["remaining"].value),
                    "pct_used": b["percentage_spent"]
                }
                for b in budget_status
            ]
        }

    @staticmethod
    def export_accounts_csv(user_id: str, account_mgr: AccountManager) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Account ID", "Account Name", "Type", "Institution", "Currency", "Balance (USD)"])
        for acc in account_mgr.list_user_accounts(user_id):
            writer.writerow([
                acc.account_id,
                acc.account_name,
                acc.account_type,
                acc.institution_name,
                acc.currency,
                f"{acc.current_balance_cents / 100.0:.2f}"
            ])
        return output.getvalue()

    @staticmethod
    def export_transactions_csv(transactions: List[Any]) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Transaction ID", "Date", "Merchant", "Description", "Category", "Amount (USD)", "Status"])
        for tx in transactions:
            writer.writerow([
                tx.transaction_id,
                tx.date,
                tx.merchant_name,
                tx.raw_description,
                tx.category_id or "Uncategorized",
                f"{tx.amount_cents / 100.0:.2f}",
                tx.status
            ])
        return output.getvalue()
