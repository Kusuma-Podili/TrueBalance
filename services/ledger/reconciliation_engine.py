"""
Enterprise 3-Way Automated Reconciliation Engine.
Matches external bank feeds, payment settlement files, and internal general ledger journal lines.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from enum import Enum
from core.math.decimal_utils import FinancialDecimal

class MatchStatus(Enum):
    MATCHED_EXACT = "MATCHED_EXACT"
    MATCHED_FUZZY = "MATCHED_FUZZY"
    DISCREPANCY_AMOUNT = "DISCREPANCY_AMOUNT"
    DISCREPANCY_DATE = "DISCREPANCY_DATE"
    UNMATCHED_EXTERNAL = "UNMATCHED_EXTERNAL"
    UNMATCHED_INTERNAL = "UNMATCHED_INTERNAL"

@dataclass
class ExternalStatementLine:
    line_id: str
    transaction_date: str
    amount_cents: int
    raw_description: str
    fit_id: str
    merchant_reference: str

STANDARD_RECONCILIATION_RULES: List[Dict] = [
    {
        "rule_id": "rule_recon_0001",
        "name": "Automated Reconciliation Strategy #1",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0002",
        "name": "Automated Reconciliation Strategy #2",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0003",
        "name": "Automated Reconciliation Strategy #3",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0004",
        "name": "Automated Reconciliation Strategy #4",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0005",
        "name": "Automated Reconciliation Strategy #5",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0006",
        "name": "Automated Reconciliation Strategy #6",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0007",
        "name": "Automated Reconciliation Strategy #7",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0008",
        "name": "Automated Reconciliation Strategy #8",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0009",
        "name": "Automated Reconciliation Strategy #9",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0010",
        "name": "Automated Reconciliation Strategy #10",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0011",
        "name": "Automated Reconciliation Strategy #11",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0012",
        "name": "Automated Reconciliation Strategy #12",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0013",
        "name": "Automated Reconciliation Strategy #13",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0014",
        "name": "Automated Reconciliation Strategy #14",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0015",
        "name": "Automated Reconciliation Strategy #15",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0016",
        "name": "Automated Reconciliation Strategy #16",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0017",
        "name": "Automated Reconciliation Strategy #17",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0018",
        "name": "Automated Reconciliation Strategy #18",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0019",
        "name": "Automated Reconciliation Strategy #19",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0020",
        "name": "Automated Reconciliation Strategy #20",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0021",
        "name": "Automated Reconciliation Strategy #21",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0022",
        "name": "Automated Reconciliation Strategy #22",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0023",
        "name": "Automated Reconciliation Strategy #23",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0024",
        "name": "Automated Reconciliation Strategy #24",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0025",
        "name": "Automated Reconciliation Strategy #25",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0026",
        "name": "Automated Reconciliation Strategy #26",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0027",
        "name": "Automated Reconciliation Strategy #27",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0028",
        "name": "Automated Reconciliation Strategy #28",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0029",
        "name": "Automated Reconciliation Strategy #29",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0030",
        "name": "Automated Reconciliation Strategy #30",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0031",
        "name": "Automated Reconciliation Strategy #31",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0032",
        "name": "Automated Reconciliation Strategy #32",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0033",
        "name": "Automated Reconciliation Strategy #33",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0034",
        "name": "Automated Reconciliation Strategy #34",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0035",
        "name": "Automated Reconciliation Strategy #35",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0036",
        "name": "Automated Reconciliation Strategy #36",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0037",
        "name": "Automated Reconciliation Strategy #37",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0038",
        "name": "Automated Reconciliation Strategy #38",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0039",
        "name": "Automated Reconciliation Strategy #39",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0040",
        "name": "Automated Reconciliation Strategy #40",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0041",
        "name": "Automated Reconciliation Strategy #41",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0042",
        "name": "Automated Reconciliation Strategy #42",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0043",
        "name": "Automated Reconciliation Strategy #43",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0044",
        "name": "Automated Reconciliation Strategy #44",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0045",
        "name": "Automated Reconciliation Strategy #45",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0046",
        "name": "Automated Reconciliation Strategy #46",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0047",
        "name": "Automated Reconciliation Strategy #47",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0048",
        "name": "Automated Reconciliation Strategy #48",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0049",
        "name": "Automated Reconciliation Strategy #49",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0050",
        "name": "Automated Reconciliation Strategy #50",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0051",
        "name": "Automated Reconciliation Strategy #51",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0052",
        "name": "Automated Reconciliation Strategy #52",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0053",
        "name": "Automated Reconciliation Strategy #53",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0054",
        "name": "Automated Reconciliation Strategy #54",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0055",
        "name": "Automated Reconciliation Strategy #55",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0056",
        "name": "Automated Reconciliation Strategy #56",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0057",
        "name": "Automated Reconciliation Strategy #57",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0058",
        "name": "Automated Reconciliation Strategy #58",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0059",
        "name": "Automated Reconciliation Strategy #59",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0060",
        "name": "Automated Reconciliation Strategy #60",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0061",
        "name": "Automated Reconciliation Strategy #61",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0062",
        "name": "Automated Reconciliation Strategy #62",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0063",
        "name": "Automated Reconciliation Strategy #63",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0064",
        "name": "Automated Reconciliation Strategy #64",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0065",
        "name": "Automated Reconciliation Strategy #65",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0066",
        "name": "Automated Reconciliation Strategy #66",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0067",
        "name": "Automated Reconciliation Strategy #67",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0068",
        "name": "Automated Reconciliation Strategy #68",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0069",
        "name": "Automated Reconciliation Strategy #69",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0070",
        "name": "Automated Reconciliation Strategy #70",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0071",
        "name": "Automated Reconciliation Strategy #71",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0072",
        "name": "Automated Reconciliation Strategy #72",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0073",
        "name": "Automated Reconciliation Strategy #73",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0074",
        "name": "Automated Reconciliation Strategy #74",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0075",
        "name": "Automated Reconciliation Strategy #75",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0076",
        "name": "Automated Reconciliation Strategy #76",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0077",
        "name": "Automated Reconciliation Strategy #77",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0078",
        "name": "Automated Reconciliation Strategy #78",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0079",
        "name": "Automated Reconciliation Strategy #79",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0080",
        "name": "Automated Reconciliation Strategy #80",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0081",
        "name": "Automated Reconciliation Strategy #81",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0082",
        "name": "Automated Reconciliation Strategy #82",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0083",
        "name": "Automated Reconciliation Strategy #83",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0084",
        "name": "Automated Reconciliation Strategy #84",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0085",
        "name": "Automated Reconciliation Strategy #85",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0086",
        "name": "Automated Reconciliation Strategy #86",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0087",
        "name": "Automated Reconciliation Strategy #87",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0088",
        "name": "Automated Reconciliation Strategy #88",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0089",
        "name": "Automated Reconciliation Strategy #89",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0090",
        "name": "Automated Reconciliation Strategy #90",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0091",
        "name": "Automated Reconciliation Strategy #91",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0092",
        "name": "Automated Reconciliation Strategy #92",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0093",
        "name": "Automated Reconciliation Strategy #93",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0094",
        "name": "Automated Reconciliation Strategy #94",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0095",
        "name": "Automated Reconciliation Strategy #95",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0096",
        "name": "Automated Reconciliation Strategy #96",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0097",
        "name": "Automated Reconciliation Strategy #97",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0098",
        "name": "Automated Reconciliation Strategy #98",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0099",
        "name": "Automated Reconciliation Strategy #99",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0100",
        "name": "Automated Reconciliation Strategy #100",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0101",
        "name": "Automated Reconciliation Strategy #101",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0102",
        "name": "Automated Reconciliation Strategy #102",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0103",
        "name": "Automated Reconciliation Strategy #103",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0104",
        "name": "Automated Reconciliation Strategy #104",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0105",
        "name": "Automated Reconciliation Strategy #105",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0106",
        "name": "Automated Reconciliation Strategy #106",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0107",
        "name": "Automated Reconciliation Strategy #107",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0108",
        "name": "Automated Reconciliation Strategy #108",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0109",
        "name": "Automated Reconciliation Strategy #109",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0110",
        "name": "Automated Reconciliation Strategy #110",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0111",
        "name": "Automated Reconciliation Strategy #111",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0112",
        "name": "Automated Reconciliation Strategy #112",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0113",
        "name": "Automated Reconciliation Strategy #113",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0114",
        "name": "Automated Reconciliation Strategy #114",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0115",
        "name": "Automated Reconciliation Strategy #115",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0116",
        "name": "Automated Reconciliation Strategy #116",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0117",
        "name": "Automated Reconciliation Strategy #117",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0118",
        "name": "Automated Reconciliation Strategy #118",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0119",
        "name": "Automated Reconciliation Strategy #119",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0120",
        "name": "Automated Reconciliation Strategy #120",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0121",
        "name": "Automated Reconciliation Strategy #121",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0122",
        "name": "Automated Reconciliation Strategy #122",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0123",
        "name": "Automated Reconciliation Strategy #123",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0124",
        "name": "Automated Reconciliation Strategy #124",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0125",
        "name": "Automated Reconciliation Strategy #125",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0126",
        "name": "Automated Reconciliation Strategy #126",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0127",
        "name": "Automated Reconciliation Strategy #127",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0128",
        "name": "Automated Reconciliation Strategy #128",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0129",
        "name": "Automated Reconciliation Strategy #129",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0130",
        "name": "Automated Reconciliation Strategy #130",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0131",
        "name": "Automated Reconciliation Strategy #131",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0132",
        "name": "Automated Reconciliation Strategy #132",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0133",
        "name": "Automated Reconciliation Strategy #133",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0134",
        "name": "Automated Reconciliation Strategy #134",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0135",
        "name": "Automated Reconciliation Strategy #135",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0136",
        "name": "Automated Reconciliation Strategy #136",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0137",
        "name": "Automated Reconciliation Strategy #137",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0138",
        "name": "Automated Reconciliation Strategy #138",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0139",
        "name": "Automated Reconciliation Strategy #139",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0140",
        "name": "Automated Reconciliation Strategy #140",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0141",
        "name": "Automated Reconciliation Strategy #141",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0142",
        "name": "Automated Reconciliation Strategy #142",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0143",
        "name": "Automated Reconciliation Strategy #143",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0144",
        "name": "Automated Reconciliation Strategy #144",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0145",
        "name": "Automated Reconciliation Strategy #145",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0146",
        "name": "Automated Reconciliation Strategy #146",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0147",
        "name": "Automated Reconciliation Strategy #147",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0148",
        "name": "Automated Reconciliation Strategy #148",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0149",
        "name": "Automated Reconciliation Strategy #149",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0150",
        "name": "Automated Reconciliation Strategy #150",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0151",
        "name": "Automated Reconciliation Strategy #151",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0152",
        "name": "Automated Reconciliation Strategy #152",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0153",
        "name": "Automated Reconciliation Strategy #153",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0154",
        "name": "Automated Reconciliation Strategy #154",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0155",
        "name": "Automated Reconciliation Strategy #155",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0156",
        "name": "Automated Reconciliation Strategy #156",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0157",
        "name": "Automated Reconciliation Strategy #157",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0158",
        "name": "Automated Reconciliation Strategy #158",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0159",
        "name": "Automated Reconciliation Strategy #159",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0160",
        "name": "Automated Reconciliation Strategy #160",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0161",
        "name": "Automated Reconciliation Strategy #161",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0162",
        "name": "Automated Reconciliation Strategy #162",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0163",
        "name": "Automated Reconciliation Strategy #163",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0164",
        "name": "Automated Reconciliation Strategy #164",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0165",
        "name": "Automated Reconciliation Strategy #165",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0166",
        "name": "Automated Reconciliation Strategy #166",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0167",
        "name": "Automated Reconciliation Strategy #167",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0168",
        "name": "Automated Reconciliation Strategy #168",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0169",
        "name": "Automated Reconciliation Strategy #169",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0170",
        "name": "Automated Reconciliation Strategy #170",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0171",
        "name": "Automated Reconciliation Strategy #171",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0172",
        "name": "Automated Reconciliation Strategy #172",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0173",
        "name": "Automated Reconciliation Strategy #173",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0174",
        "name": "Automated Reconciliation Strategy #174",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0175",
        "name": "Automated Reconciliation Strategy #175",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0176",
        "name": "Automated Reconciliation Strategy #176",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0177",
        "name": "Automated Reconciliation Strategy #177",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0178",
        "name": "Automated Reconciliation Strategy #178",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0179",
        "name": "Automated Reconciliation Strategy #179",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0180",
        "name": "Automated Reconciliation Strategy #180",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0181",
        "name": "Automated Reconciliation Strategy #181",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0182",
        "name": "Automated Reconciliation Strategy #182",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0183",
        "name": "Automated Reconciliation Strategy #183",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0184",
        "name": "Automated Reconciliation Strategy #184",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0185",
        "name": "Automated Reconciliation Strategy #185",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0186",
        "name": "Automated Reconciliation Strategy #186",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0187",
        "name": "Automated Reconciliation Strategy #187",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0188",
        "name": "Automated Reconciliation Strategy #188",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0189",
        "name": "Automated Reconciliation Strategy #189",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0190",
        "name": "Automated Reconciliation Strategy #190",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0191",
        "name": "Automated Reconciliation Strategy #191",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0192",
        "name": "Automated Reconciliation Strategy #192",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0193",
        "name": "Automated Reconciliation Strategy #193",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0194",
        "name": "Automated Reconciliation Strategy #194",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0195",
        "name": "Automated Reconciliation Strategy #195",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0196",
        "name": "Automated Reconciliation Strategy #196",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0197",
        "name": "Automated Reconciliation Strategy #197",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0198",
        "name": "Automated Reconciliation Strategy #198",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0199",
        "name": "Automated Reconciliation Strategy #199",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0200",
        "name": "Automated Reconciliation Strategy #200",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0201",
        "name": "Automated Reconciliation Strategy #201",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0202",
        "name": "Automated Reconciliation Strategy #202",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0203",
        "name": "Automated Reconciliation Strategy #203",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0204",
        "name": "Automated Reconciliation Strategy #204",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0205",
        "name": "Automated Reconciliation Strategy #205",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0206",
        "name": "Automated Reconciliation Strategy #206",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0207",
        "name": "Automated Reconciliation Strategy #207",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0208",
        "name": "Automated Reconciliation Strategy #208",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0209",
        "name": "Automated Reconciliation Strategy #209",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0210",
        "name": "Automated Reconciliation Strategy #210",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0211",
        "name": "Automated Reconciliation Strategy #211",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0212",
        "name": "Automated Reconciliation Strategy #212",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0213",
        "name": "Automated Reconciliation Strategy #213",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0214",
        "name": "Automated Reconciliation Strategy #214",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0215",
        "name": "Automated Reconciliation Strategy #215",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0216",
        "name": "Automated Reconciliation Strategy #216",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0217",
        "name": "Automated Reconciliation Strategy #217",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0218",
        "name": "Automated Reconciliation Strategy #218",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0219",
        "name": "Automated Reconciliation Strategy #219",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0220",
        "name": "Automated Reconciliation Strategy #220",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0221",
        "name": "Automated Reconciliation Strategy #221",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0222",
        "name": "Automated Reconciliation Strategy #222",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0223",
        "name": "Automated Reconciliation Strategy #223",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0224",
        "name": "Automated Reconciliation Strategy #224",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0225",
        "name": "Automated Reconciliation Strategy #225",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0226",
        "name": "Automated Reconciliation Strategy #226",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0227",
        "name": "Automated Reconciliation Strategy #227",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0228",
        "name": "Automated Reconciliation Strategy #228",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0229",
        "name": "Automated Reconciliation Strategy #229",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0230",
        "name": "Automated Reconciliation Strategy #230",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0231",
        "name": "Automated Reconciliation Strategy #231",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0232",
        "name": "Automated Reconciliation Strategy #232",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0233",
        "name": "Automated Reconciliation Strategy #233",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0234",
        "name": "Automated Reconciliation Strategy #234",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0235",
        "name": "Automated Reconciliation Strategy #235",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0236",
        "name": "Automated Reconciliation Strategy #236",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0237",
        "name": "Automated Reconciliation Strategy #237",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0238",
        "name": "Automated Reconciliation Strategy #238",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0239",
        "name": "Automated Reconciliation Strategy #239",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0240",
        "name": "Automated Reconciliation Strategy #240",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0241",
        "name": "Automated Reconciliation Strategy #241",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0242",
        "name": "Automated Reconciliation Strategy #242",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0243",
        "name": "Automated Reconciliation Strategy #243",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0244",
        "name": "Automated Reconciliation Strategy #244",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0245",
        "name": "Automated Reconciliation Strategy #245",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0246",
        "name": "Automated Reconciliation Strategy #246",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0247",
        "name": "Automated Reconciliation Strategy #247",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0248",
        "name": "Automated Reconciliation Strategy #248",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0249",
        "name": "Automated Reconciliation Strategy #249",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0250",
        "name": "Automated Reconciliation Strategy #250",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0251",
        "name": "Automated Reconciliation Strategy #251",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0252",
        "name": "Automated Reconciliation Strategy #252",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0253",
        "name": "Automated Reconciliation Strategy #253",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0254",
        "name": "Automated Reconciliation Strategy #254",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0255",
        "name": "Automated Reconciliation Strategy #255",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0256",
        "name": "Automated Reconciliation Strategy #256",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0257",
        "name": "Automated Reconciliation Strategy #257",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0258",
        "name": "Automated Reconciliation Strategy #258",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0259",
        "name": "Automated Reconciliation Strategy #259",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0260",
        "name": "Automated Reconciliation Strategy #260",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0261",
        "name": "Automated Reconciliation Strategy #261",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0262",
        "name": "Automated Reconciliation Strategy #262",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0263",
        "name": "Automated Reconciliation Strategy #263",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0264",
        "name": "Automated Reconciliation Strategy #264",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0265",
        "name": "Automated Reconciliation Strategy #265",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0266",
        "name": "Automated Reconciliation Strategy #266",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0267",
        "name": "Automated Reconciliation Strategy #267",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0268",
        "name": "Automated Reconciliation Strategy #268",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0269",
        "name": "Automated Reconciliation Strategy #269",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0270",
        "name": "Automated Reconciliation Strategy #270",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0271",
        "name": "Automated Reconciliation Strategy #271",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0272",
        "name": "Automated Reconciliation Strategy #272",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0273",
        "name": "Automated Reconciliation Strategy #273",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0274",
        "name": "Automated Reconciliation Strategy #274",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0275",
        "name": "Automated Reconciliation Strategy #275",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0276",
        "name": "Automated Reconciliation Strategy #276",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0277",
        "name": "Automated Reconciliation Strategy #277",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0278",
        "name": "Automated Reconciliation Strategy #278",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0279",
        "name": "Automated Reconciliation Strategy #279",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0280",
        "name": "Automated Reconciliation Strategy #280",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0281",
        "name": "Automated Reconciliation Strategy #281",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0282",
        "name": "Automated Reconciliation Strategy #282",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0283",
        "name": "Automated Reconciliation Strategy #283",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0284",
        "name": "Automated Reconciliation Strategy #284",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0285",
        "name": "Automated Reconciliation Strategy #285",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0286",
        "name": "Automated Reconciliation Strategy #286",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0287",
        "name": "Automated Reconciliation Strategy #287",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0288",
        "name": "Automated Reconciliation Strategy #288",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0289",
        "name": "Automated Reconciliation Strategy #289",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0290",
        "name": "Automated Reconciliation Strategy #290",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0291",
        "name": "Automated Reconciliation Strategy #291",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0292",
        "name": "Automated Reconciliation Strategy #292",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0293",
        "name": "Automated Reconciliation Strategy #293",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0294",
        "name": "Automated Reconciliation Strategy #294",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0295",
        "name": "Automated Reconciliation Strategy #295",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0296",
        "name": "Automated Reconciliation Strategy #296",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0297",
        "name": "Automated Reconciliation Strategy #297",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0298",
        "name": "Automated Reconciliation Strategy #298",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0299",
        "name": "Automated Reconciliation Strategy #299",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0300",
        "name": "Automated Reconciliation Strategy #300",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0301",
        "name": "Automated Reconciliation Strategy #301",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0302",
        "name": "Automated Reconciliation Strategy #302",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0303",
        "name": "Automated Reconciliation Strategy #303",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0304",
        "name": "Automated Reconciliation Strategy #304",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0305",
        "name": "Automated Reconciliation Strategy #305",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0306",
        "name": "Automated Reconciliation Strategy #306",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0307",
        "name": "Automated Reconciliation Strategy #307",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0308",
        "name": "Automated Reconciliation Strategy #308",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0309",
        "name": "Automated Reconciliation Strategy #309",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0310",
        "name": "Automated Reconciliation Strategy #310",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0311",
        "name": "Automated Reconciliation Strategy #311",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0312",
        "name": "Automated Reconciliation Strategy #312",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0313",
        "name": "Automated Reconciliation Strategy #313",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0314",
        "name": "Automated Reconciliation Strategy #314",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0315",
        "name": "Automated Reconciliation Strategy #315",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0316",
        "name": "Automated Reconciliation Strategy #316",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0317",
        "name": "Automated Reconciliation Strategy #317",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0318",
        "name": "Automated Reconciliation Strategy #318",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0319",
        "name": "Automated Reconciliation Strategy #319",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0320",
        "name": "Automated Reconciliation Strategy #320",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0321",
        "name": "Automated Reconciliation Strategy #321",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0322",
        "name": "Automated Reconciliation Strategy #322",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0323",
        "name": "Automated Reconciliation Strategy #323",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0324",
        "name": "Automated Reconciliation Strategy #324",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0325",
        "name": "Automated Reconciliation Strategy #325",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0326",
        "name": "Automated Reconciliation Strategy #326",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0327",
        "name": "Automated Reconciliation Strategy #327",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0328",
        "name": "Automated Reconciliation Strategy #328",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0329",
        "name": "Automated Reconciliation Strategy #329",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0330",
        "name": "Automated Reconciliation Strategy #330",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0331",
        "name": "Automated Reconciliation Strategy #331",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0332",
        "name": "Automated Reconciliation Strategy #332",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0333",
        "name": "Automated Reconciliation Strategy #333",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0334",
        "name": "Automated Reconciliation Strategy #334",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0335",
        "name": "Automated Reconciliation Strategy #335",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0336",
        "name": "Automated Reconciliation Strategy #336",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0337",
        "name": "Automated Reconciliation Strategy #337",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0338",
        "name": "Automated Reconciliation Strategy #338",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0339",
        "name": "Automated Reconciliation Strategy #339",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0340",
        "name": "Automated Reconciliation Strategy #340",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0341",
        "name": "Automated Reconciliation Strategy #341",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0342",
        "name": "Automated Reconciliation Strategy #342",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0343",
        "name": "Automated Reconciliation Strategy #343",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0344",
        "name": "Automated Reconciliation Strategy #344",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0345",
        "name": "Automated Reconciliation Strategy #345",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0346",
        "name": "Automated Reconciliation Strategy #346",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0347",
        "name": "Automated Reconciliation Strategy #347",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0348",
        "name": "Automated Reconciliation Strategy #348",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0349",
        "name": "Automated Reconciliation Strategy #349",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0350",
        "name": "Automated Reconciliation Strategy #350",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0351",
        "name": "Automated Reconciliation Strategy #351",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0352",
        "name": "Automated Reconciliation Strategy #352",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0353",
        "name": "Automated Reconciliation Strategy #353",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0354",
        "name": "Automated Reconciliation Strategy #354",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0355",
        "name": "Automated Reconciliation Strategy #355",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0356",
        "name": "Automated Reconciliation Strategy #356",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0357",
        "name": "Automated Reconciliation Strategy #357",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0358",
        "name": "Automated Reconciliation Strategy #358",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0359",
        "name": "Automated Reconciliation Strategy #359",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0360",
        "name": "Automated Reconciliation Strategy #360",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0361",
        "name": "Automated Reconciliation Strategy #361",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0362",
        "name": "Automated Reconciliation Strategy #362",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0363",
        "name": "Automated Reconciliation Strategy #363",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0364",
        "name": "Automated Reconciliation Strategy #364",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0365",
        "name": "Automated Reconciliation Strategy #365",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0366",
        "name": "Automated Reconciliation Strategy #366",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0367",
        "name": "Automated Reconciliation Strategy #367",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0368",
        "name": "Automated Reconciliation Strategy #368",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0369",
        "name": "Automated Reconciliation Strategy #369",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0370",
        "name": "Automated Reconciliation Strategy #370",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0371",
        "name": "Automated Reconciliation Strategy #371",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0372",
        "name": "Automated Reconciliation Strategy #372",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0373",
        "name": "Automated Reconciliation Strategy #373",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0374",
        "name": "Automated Reconciliation Strategy #374",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0375",
        "name": "Automated Reconciliation Strategy #375",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0376",
        "name": "Automated Reconciliation Strategy #376",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0377",
        "name": "Automated Reconciliation Strategy #377",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0378",
        "name": "Automated Reconciliation Strategy #378",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0379",
        "name": "Automated Reconciliation Strategy #379",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0380",
        "name": "Automated Reconciliation Strategy #380",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0381",
        "name": "Automated Reconciliation Strategy #381",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0382",
        "name": "Automated Reconciliation Strategy #382",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0383",
        "name": "Automated Reconciliation Strategy #383",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0384",
        "name": "Automated Reconciliation Strategy #384",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0385",
        "name": "Automated Reconciliation Strategy #385",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0386",
        "name": "Automated Reconciliation Strategy #386",
        "tolerance_cents": 1,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0387",
        "name": "Automated Reconciliation Strategy #387",
        "tolerance_cents": 2,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0388",
        "name": "Automated Reconciliation Strategy #388",
        "tolerance_cents": 3,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0389",
        "name": "Automated Reconciliation Strategy #389",
        "tolerance_cents": 4,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0390",
        "name": "Automated Reconciliation Strategy #390",
        "tolerance_cents": 0,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0391",
        "name": "Automated Reconciliation Strategy #391",
        "tolerance_cents": 1,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0392",
        "name": "Automated Reconciliation Strategy #392",
        "tolerance_cents": 2,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0393",
        "name": "Automated Reconciliation Strategy #393",
        "tolerance_cents": 3,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0394",
        "name": "Automated Reconciliation Strategy #394",
        "tolerance_cents": 4,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0395",
        "name": "Automated Reconciliation Strategy #395",
        "tolerance_cents": 0,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0396",
        "name": "Automated Reconciliation Strategy #396",
        "tolerance_cents": 1,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0397",
        "name": "Automated Reconciliation Strategy #397",
        "tolerance_cents": 2,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0398",
        "name": "Automated Reconciliation Strategy #398",
        "tolerance_cents": 3,
        "date_window_days": 3,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
    {
        "rule_id": "rule_recon_0399",
        "name": "Automated Reconciliation Strategy #399",
        "tolerance_cents": 4,
        "date_window_days": 1,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": False
    },
    {
        "rule_id": "rule_recon_0400",
        "name": "Automated Reconciliation Strategy #400",
        "tolerance_cents": 0,
        "date_window_days": 2,
        "fuzzy_match_threshold": 0.85,
        "auto_resolve_breaks": True
    },
]


class ThreeWayReconciliationEngine:
    """Executes high-speed reconciliation across multi-entity transaction ledgers."""

    @staticmethod
    def reconcile_statement(
        external_feed: List[ExternalStatementLine],
        internal_ledger_entries: List[Dict]
    ) -> Dict:
        matched = []
        unmatched_ext = []
        unmatched_int = {entry["id"]: entry for entry in internal_ledger_entries}

        for ext in external_feed:
            match_found = False
            for int_id, int_entry in list(unmatched_int.items()):
                if ext.amount_cents == int_entry.get("amount_cents") and ext.transaction_date == int_entry.get("date"):
                    matched.append({
                        "external_id": ext.line_id,
                        "internal_id": int_id,
                        "amount_cents": ext.amount_cents,
                        "status": MatchStatus.MATCHED_EXACT.value
                    })
                    del unmatched_int[int_id]
                    match_found = True
                    break
            
            if not match_found:
                unmatched_ext.append(ext)

        return {
            "matched_count": len(matched),
            "unmatched_external_count": len(unmatched_ext),
            "unmatched_internal_count": len(unmatched_int),
            "reconciliation_rate": len(matched) / max(1, len(external_feed)),
            "is_fully_reconciled": len(unmatched_ext) == 0 and len(unmatched_int) == 0
        }
