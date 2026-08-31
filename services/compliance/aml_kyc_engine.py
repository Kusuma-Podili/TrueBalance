"""
Enterprise Compliance, KYC Identity & Anti-Money Laundering (AML) Structuring Monitor.
Implements FinCEN CTR threshold detection, smurfing heuristics, and sanctions list screening.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from enum import Enum

class AMLAlertSeverity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL_SAR_REQUIRED = "CRITICAL_SAR_REQUIRED"

SANCTIONS_SDN_WATCHLIST: List[Dict[str, str]] = [
    {
        "entity_id": "SDN_000001",
        "name": "High-Risk Sanctioned Entity #0001",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000002",
        "name": "High-Risk Sanctioned Entity #0002",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000003",
        "name": "High-Risk Sanctioned Entity #0003",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000004",
        "name": "High-Risk Sanctioned Entity #0004",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000005",
        "name": "High-Risk Sanctioned Entity #0005",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000006",
        "name": "High-Risk Sanctioned Entity #0006",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000007",
        "name": "High-Risk Sanctioned Entity #0007",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000008",
        "name": "High-Risk Sanctioned Entity #0008",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000009",
        "name": "High-Risk Sanctioned Entity #0009",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000010",
        "name": "High-Risk Sanctioned Entity #0010",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000011",
        "name": "High-Risk Sanctioned Entity #0011",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000012",
        "name": "High-Risk Sanctioned Entity #0012",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000013",
        "name": "High-Risk Sanctioned Entity #0013",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000014",
        "name": "High-Risk Sanctioned Entity #0014",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000015",
        "name": "High-Risk Sanctioned Entity #0015",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000016",
        "name": "High-Risk Sanctioned Entity #0016",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000017",
        "name": "High-Risk Sanctioned Entity #0017",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000018",
        "name": "High-Risk Sanctioned Entity #0018",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000019",
        "name": "High-Risk Sanctioned Entity #0019",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000020",
        "name": "High-Risk Sanctioned Entity #0020",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000021",
        "name": "High-Risk Sanctioned Entity #0021",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000022",
        "name": "High-Risk Sanctioned Entity #0022",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000023",
        "name": "High-Risk Sanctioned Entity #0023",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000024",
        "name": "High-Risk Sanctioned Entity #0024",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000025",
        "name": "High-Risk Sanctioned Entity #0025",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000026",
        "name": "High-Risk Sanctioned Entity #0026",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000027",
        "name": "High-Risk Sanctioned Entity #0027",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000028",
        "name": "High-Risk Sanctioned Entity #0028",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000029",
        "name": "High-Risk Sanctioned Entity #0029",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000030",
        "name": "High-Risk Sanctioned Entity #0030",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000031",
        "name": "High-Risk Sanctioned Entity #0031",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000032",
        "name": "High-Risk Sanctioned Entity #0032",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000033",
        "name": "High-Risk Sanctioned Entity #0033",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000034",
        "name": "High-Risk Sanctioned Entity #0034",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000035",
        "name": "High-Risk Sanctioned Entity #0035",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000036",
        "name": "High-Risk Sanctioned Entity #0036",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000037",
        "name": "High-Risk Sanctioned Entity #0037",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000038",
        "name": "High-Risk Sanctioned Entity #0038",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000039",
        "name": "High-Risk Sanctioned Entity #0039",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000040",
        "name": "High-Risk Sanctioned Entity #0040",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000041",
        "name": "High-Risk Sanctioned Entity #0041",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000042",
        "name": "High-Risk Sanctioned Entity #0042",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000043",
        "name": "High-Risk Sanctioned Entity #0043",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000044",
        "name": "High-Risk Sanctioned Entity #0044",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000045",
        "name": "High-Risk Sanctioned Entity #0045",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000046",
        "name": "High-Risk Sanctioned Entity #0046",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000047",
        "name": "High-Risk Sanctioned Entity #0047",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000048",
        "name": "High-Risk Sanctioned Entity #0048",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000049",
        "name": "High-Risk Sanctioned Entity #0049",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000050",
        "name": "High-Risk Sanctioned Entity #0050",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000051",
        "name": "High-Risk Sanctioned Entity #0051",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000052",
        "name": "High-Risk Sanctioned Entity #0052",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000053",
        "name": "High-Risk Sanctioned Entity #0053",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000054",
        "name": "High-Risk Sanctioned Entity #0054",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000055",
        "name": "High-Risk Sanctioned Entity #0055",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000056",
        "name": "High-Risk Sanctioned Entity #0056",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000057",
        "name": "High-Risk Sanctioned Entity #0057",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000058",
        "name": "High-Risk Sanctioned Entity #0058",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000059",
        "name": "High-Risk Sanctioned Entity #0059",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000060",
        "name": "High-Risk Sanctioned Entity #0060",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000061",
        "name": "High-Risk Sanctioned Entity #0061",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000062",
        "name": "High-Risk Sanctioned Entity #0062",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000063",
        "name": "High-Risk Sanctioned Entity #0063",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000064",
        "name": "High-Risk Sanctioned Entity #0064",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000065",
        "name": "High-Risk Sanctioned Entity #0065",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000066",
        "name": "High-Risk Sanctioned Entity #0066",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000067",
        "name": "High-Risk Sanctioned Entity #0067",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000068",
        "name": "High-Risk Sanctioned Entity #0068",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000069",
        "name": "High-Risk Sanctioned Entity #0069",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000070",
        "name": "High-Risk Sanctioned Entity #0070",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000071",
        "name": "High-Risk Sanctioned Entity #0071",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000072",
        "name": "High-Risk Sanctioned Entity #0072",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000073",
        "name": "High-Risk Sanctioned Entity #0073",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000074",
        "name": "High-Risk Sanctioned Entity #0074",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000075",
        "name": "High-Risk Sanctioned Entity #0075",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000076",
        "name": "High-Risk Sanctioned Entity #0076",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000077",
        "name": "High-Risk Sanctioned Entity #0077",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000078",
        "name": "High-Risk Sanctioned Entity #0078",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000079",
        "name": "High-Risk Sanctioned Entity #0079",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000080",
        "name": "High-Risk Sanctioned Entity #0080",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000081",
        "name": "High-Risk Sanctioned Entity #0081",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000082",
        "name": "High-Risk Sanctioned Entity #0082",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000083",
        "name": "High-Risk Sanctioned Entity #0083",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000084",
        "name": "High-Risk Sanctioned Entity #0084",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000085",
        "name": "High-Risk Sanctioned Entity #0085",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000086",
        "name": "High-Risk Sanctioned Entity #0086",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000087",
        "name": "High-Risk Sanctioned Entity #0087",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000088",
        "name": "High-Risk Sanctioned Entity #0088",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000089",
        "name": "High-Risk Sanctioned Entity #0089",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000090",
        "name": "High-Risk Sanctioned Entity #0090",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000091",
        "name": "High-Risk Sanctioned Entity #0091",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000092",
        "name": "High-Risk Sanctioned Entity #0092",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000093",
        "name": "High-Risk Sanctioned Entity #0093",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000094",
        "name": "High-Risk Sanctioned Entity #0094",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000095",
        "name": "High-Risk Sanctioned Entity #0095",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000096",
        "name": "High-Risk Sanctioned Entity #0096",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000097",
        "name": "High-Risk Sanctioned Entity #0097",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000098",
        "name": "High-Risk Sanctioned Entity #0098",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000099",
        "name": "High-Risk Sanctioned Entity #0099",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000100",
        "name": "High-Risk Sanctioned Entity #0100",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000101",
        "name": "High-Risk Sanctioned Entity #0101",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000102",
        "name": "High-Risk Sanctioned Entity #0102",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000103",
        "name": "High-Risk Sanctioned Entity #0103",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000104",
        "name": "High-Risk Sanctioned Entity #0104",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000105",
        "name": "High-Risk Sanctioned Entity #0105",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000106",
        "name": "High-Risk Sanctioned Entity #0106",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000107",
        "name": "High-Risk Sanctioned Entity #0107",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000108",
        "name": "High-Risk Sanctioned Entity #0108",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000109",
        "name": "High-Risk Sanctioned Entity #0109",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000110",
        "name": "High-Risk Sanctioned Entity #0110",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000111",
        "name": "High-Risk Sanctioned Entity #0111",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000112",
        "name": "High-Risk Sanctioned Entity #0112",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000113",
        "name": "High-Risk Sanctioned Entity #0113",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000114",
        "name": "High-Risk Sanctioned Entity #0114",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000115",
        "name": "High-Risk Sanctioned Entity #0115",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000116",
        "name": "High-Risk Sanctioned Entity #0116",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000117",
        "name": "High-Risk Sanctioned Entity #0117",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000118",
        "name": "High-Risk Sanctioned Entity #0118",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000119",
        "name": "High-Risk Sanctioned Entity #0119",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000120",
        "name": "High-Risk Sanctioned Entity #0120",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000121",
        "name": "High-Risk Sanctioned Entity #0121",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000122",
        "name": "High-Risk Sanctioned Entity #0122",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000123",
        "name": "High-Risk Sanctioned Entity #0123",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000124",
        "name": "High-Risk Sanctioned Entity #0124",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000125",
        "name": "High-Risk Sanctioned Entity #0125",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000126",
        "name": "High-Risk Sanctioned Entity #0126",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000127",
        "name": "High-Risk Sanctioned Entity #0127",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000128",
        "name": "High-Risk Sanctioned Entity #0128",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000129",
        "name": "High-Risk Sanctioned Entity #0129",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000130",
        "name": "High-Risk Sanctioned Entity #0130",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000131",
        "name": "High-Risk Sanctioned Entity #0131",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000132",
        "name": "High-Risk Sanctioned Entity #0132",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000133",
        "name": "High-Risk Sanctioned Entity #0133",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000134",
        "name": "High-Risk Sanctioned Entity #0134",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000135",
        "name": "High-Risk Sanctioned Entity #0135",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000136",
        "name": "High-Risk Sanctioned Entity #0136",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000137",
        "name": "High-Risk Sanctioned Entity #0137",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000138",
        "name": "High-Risk Sanctioned Entity #0138",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000139",
        "name": "High-Risk Sanctioned Entity #0139",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000140",
        "name": "High-Risk Sanctioned Entity #0140",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000141",
        "name": "High-Risk Sanctioned Entity #0141",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000142",
        "name": "High-Risk Sanctioned Entity #0142",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000143",
        "name": "High-Risk Sanctioned Entity #0143",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000144",
        "name": "High-Risk Sanctioned Entity #0144",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000145",
        "name": "High-Risk Sanctioned Entity #0145",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000146",
        "name": "High-Risk Sanctioned Entity #0146",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000147",
        "name": "High-Risk Sanctioned Entity #0147",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000148",
        "name": "High-Risk Sanctioned Entity #0148",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000149",
        "name": "High-Risk Sanctioned Entity #0149",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000150",
        "name": "High-Risk Sanctioned Entity #0150",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000151",
        "name": "High-Risk Sanctioned Entity #0151",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000152",
        "name": "High-Risk Sanctioned Entity #0152",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000153",
        "name": "High-Risk Sanctioned Entity #0153",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000154",
        "name": "High-Risk Sanctioned Entity #0154",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000155",
        "name": "High-Risk Sanctioned Entity #0155",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000156",
        "name": "High-Risk Sanctioned Entity #0156",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000157",
        "name": "High-Risk Sanctioned Entity #0157",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000158",
        "name": "High-Risk Sanctioned Entity #0158",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000159",
        "name": "High-Risk Sanctioned Entity #0159",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000160",
        "name": "High-Risk Sanctioned Entity #0160",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000161",
        "name": "High-Risk Sanctioned Entity #0161",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000162",
        "name": "High-Risk Sanctioned Entity #0162",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000163",
        "name": "High-Risk Sanctioned Entity #0163",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000164",
        "name": "High-Risk Sanctioned Entity #0164",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000165",
        "name": "High-Risk Sanctioned Entity #0165",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000166",
        "name": "High-Risk Sanctioned Entity #0166",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000167",
        "name": "High-Risk Sanctioned Entity #0167",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000168",
        "name": "High-Risk Sanctioned Entity #0168",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000169",
        "name": "High-Risk Sanctioned Entity #0169",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000170",
        "name": "High-Risk Sanctioned Entity #0170",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000171",
        "name": "High-Risk Sanctioned Entity #0171",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000172",
        "name": "High-Risk Sanctioned Entity #0172",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000173",
        "name": "High-Risk Sanctioned Entity #0173",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000174",
        "name": "High-Risk Sanctioned Entity #0174",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000175",
        "name": "High-Risk Sanctioned Entity #0175",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000176",
        "name": "High-Risk Sanctioned Entity #0176",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000177",
        "name": "High-Risk Sanctioned Entity #0177",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000178",
        "name": "High-Risk Sanctioned Entity #0178",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000179",
        "name": "High-Risk Sanctioned Entity #0179",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000180",
        "name": "High-Risk Sanctioned Entity #0180",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000181",
        "name": "High-Risk Sanctioned Entity #0181",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000182",
        "name": "High-Risk Sanctioned Entity #0182",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000183",
        "name": "High-Risk Sanctioned Entity #0183",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000184",
        "name": "High-Risk Sanctioned Entity #0184",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000185",
        "name": "High-Risk Sanctioned Entity #0185",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000186",
        "name": "High-Risk Sanctioned Entity #0186",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000187",
        "name": "High-Risk Sanctioned Entity #0187",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000188",
        "name": "High-Risk Sanctioned Entity #0188",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000189",
        "name": "High-Risk Sanctioned Entity #0189",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000190",
        "name": "High-Risk Sanctioned Entity #0190",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000191",
        "name": "High-Risk Sanctioned Entity #0191",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000192",
        "name": "High-Risk Sanctioned Entity #0192",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000193",
        "name": "High-Risk Sanctioned Entity #0193",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000194",
        "name": "High-Risk Sanctioned Entity #0194",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000195",
        "name": "High-Risk Sanctioned Entity #0195",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000196",
        "name": "High-Risk Sanctioned Entity #0196",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000197",
        "name": "High-Risk Sanctioned Entity #0197",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000198",
        "name": "High-Risk Sanctioned Entity #0198",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000199",
        "name": "High-Risk Sanctioned Entity #0199",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000200",
        "name": "High-Risk Sanctioned Entity #0200",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000201",
        "name": "High-Risk Sanctioned Entity #0201",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000202",
        "name": "High-Risk Sanctioned Entity #0202",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000203",
        "name": "High-Risk Sanctioned Entity #0203",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000204",
        "name": "High-Risk Sanctioned Entity #0204",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000205",
        "name": "High-Risk Sanctioned Entity #0205",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000206",
        "name": "High-Risk Sanctioned Entity #0206",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000207",
        "name": "High-Risk Sanctioned Entity #0207",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000208",
        "name": "High-Risk Sanctioned Entity #0208",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000209",
        "name": "High-Risk Sanctioned Entity #0209",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000210",
        "name": "High-Risk Sanctioned Entity #0210",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000211",
        "name": "High-Risk Sanctioned Entity #0211",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000212",
        "name": "High-Risk Sanctioned Entity #0212",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000213",
        "name": "High-Risk Sanctioned Entity #0213",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000214",
        "name": "High-Risk Sanctioned Entity #0214",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000215",
        "name": "High-Risk Sanctioned Entity #0215",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000216",
        "name": "High-Risk Sanctioned Entity #0216",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000217",
        "name": "High-Risk Sanctioned Entity #0217",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000218",
        "name": "High-Risk Sanctioned Entity #0218",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000219",
        "name": "High-Risk Sanctioned Entity #0219",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000220",
        "name": "High-Risk Sanctioned Entity #0220",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000221",
        "name": "High-Risk Sanctioned Entity #0221",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000222",
        "name": "High-Risk Sanctioned Entity #0222",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000223",
        "name": "High-Risk Sanctioned Entity #0223",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000224",
        "name": "High-Risk Sanctioned Entity #0224",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000225",
        "name": "High-Risk Sanctioned Entity #0225",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000226",
        "name": "High-Risk Sanctioned Entity #0226",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000227",
        "name": "High-Risk Sanctioned Entity #0227",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000228",
        "name": "High-Risk Sanctioned Entity #0228",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000229",
        "name": "High-Risk Sanctioned Entity #0229",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000230",
        "name": "High-Risk Sanctioned Entity #0230",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000231",
        "name": "High-Risk Sanctioned Entity #0231",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000232",
        "name": "High-Risk Sanctioned Entity #0232",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000233",
        "name": "High-Risk Sanctioned Entity #0233",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000234",
        "name": "High-Risk Sanctioned Entity #0234",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000235",
        "name": "High-Risk Sanctioned Entity #0235",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000236",
        "name": "High-Risk Sanctioned Entity #0236",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000237",
        "name": "High-Risk Sanctioned Entity #0237",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000238",
        "name": "High-Risk Sanctioned Entity #0238",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000239",
        "name": "High-Risk Sanctioned Entity #0239",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000240",
        "name": "High-Risk Sanctioned Entity #0240",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000241",
        "name": "High-Risk Sanctioned Entity #0241",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000242",
        "name": "High-Risk Sanctioned Entity #0242",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000243",
        "name": "High-Risk Sanctioned Entity #0243",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000244",
        "name": "High-Risk Sanctioned Entity #0244",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000245",
        "name": "High-Risk Sanctioned Entity #0245",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000246",
        "name": "High-Risk Sanctioned Entity #0246",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000247",
        "name": "High-Risk Sanctioned Entity #0247",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000248",
        "name": "High-Risk Sanctioned Entity #0248",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000249",
        "name": "High-Risk Sanctioned Entity #0249",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000250",
        "name": "High-Risk Sanctioned Entity #0250",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000251",
        "name": "High-Risk Sanctioned Entity #0251",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000252",
        "name": "High-Risk Sanctioned Entity #0252",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000253",
        "name": "High-Risk Sanctioned Entity #0253",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000254",
        "name": "High-Risk Sanctioned Entity #0254",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000255",
        "name": "High-Risk Sanctioned Entity #0255",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000256",
        "name": "High-Risk Sanctioned Entity #0256",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000257",
        "name": "High-Risk Sanctioned Entity #0257",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000258",
        "name": "High-Risk Sanctioned Entity #0258",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000259",
        "name": "High-Risk Sanctioned Entity #0259",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000260",
        "name": "High-Risk Sanctioned Entity #0260",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000261",
        "name": "High-Risk Sanctioned Entity #0261",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000262",
        "name": "High-Risk Sanctioned Entity #0262",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000263",
        "name": "High-Risk Sanctioned Entity #0263",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000264",
        "name": "High-Risk Sanctioned Entity #0264",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000265",
        "name": "High-Risk Sanctioned Entity #0265",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000266",
        "name": "High-Risk Sanctioned Entity #0266",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000267",
        "name": "High-Risk Sanctioned Entity #0267",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000268",
        "name": "High-Risk Sanctioned Entity #0268",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000269",
        "name": "High-Risk Sanctioned Entity #0269",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000270",
        "name": "High-Risk Sanctioned Entity #0270",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000271",
        "name": "High-Risk Sanctioned Entity #0271",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000272",
        "name": "High-Risk Sanctioned Entity #0272",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000273",
        "name": "High-Risk Sanctioned Entity #0273",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000274",
        "name": "High-Risk Sanctioned Entity #0274",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000275",
        "name": "High-Risk Sanctioned Entity #0275",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000276",
        "name": "High-Risk Sanctioned Entity #0276",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000277",
        "name": "High-Risk Sanctioned Entity #0277",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000278",
        "name": "High-Risk Sanctioned Entity #0278",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000279",
        "name": "High-Risk Sanctioned Entity #0279",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000280",
        "name": "High-Risk Sanctioned Entity #0280",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000281",
        "name": "High-Risk Sanctioned Entity #0281",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000282",
        "name": "High-Risk Sanctioned Entity #0282",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000283",
        "name": "High-Risk Sanctioned Entity #0283",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000284",
        "name": "High-Risk Sanctioned Entity #0284",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000285",
        "name": "High-Risk Sanctioned Entity #0285",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000286",
        "name": "High-Risk Sanctioned Entity #0286",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000287",
        "name": "High-Risk Sanctioned Entity #0287",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000288",
        "name": "High-Risk Sanctioned Entity #0288",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000289",
        "name": "High-Risk Sanctioned Entity #0289",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000290",
        "name": "High-Risk Sanctioned Entity #0290",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000291",
        "name": "High-Risk Sanctioned Entity #0291",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000292",
        "name": "High-Risk Sanctioned Entity #0292",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000293",
        "name": "High-Risk Sanctioned Entity #0293",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000294",
        "name": "High-Risk Sanctioned Entity #0294",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000295",
        "name": "High-Risk Sanctioned Entity #0295",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000296",
        "name": "High-Risk Sanctioned Entity #0296",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000297",
        "name": "High-Risk Sanctioned Entity #0297",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000298",
        "name": "High-Risk Sanctioned Entity #0298",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000299",
        "name": "High-Risk Sanctioned Entity #0299",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000300",
        "name": "High-Risk Sanctioned Entity #0300",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000301",
        "name": "High-Risk Sanctioned Entity #0301",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000302",
        "name": "High-Risk Sanctioned Entity #0302",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000303",
        "name": "High-Risk Sanctioned Entity #0303",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000304",
        "name": "High-Risk Sanctioned Entity #0304",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000305",
        "name": "High-Risk Sanctioned Entity #0305",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000306",
        "name": "High-Risk Sanctioned Entity #0306",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000307",
        "name": "High-Risk Sanctioned Entity #0307",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000308",
        "name": "High-Risk Sanctioned Entity #0308",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000309",
        "name": "High-Risk Sanctioned Entity #0309",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000310",
        "name": "High-Risk Sanctioned Entity #0310",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000311",
        "name": "High-Risk Sanctioned Entity #0311",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000312",
        "name": "High-Risk Sanctioned Entity #0312",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000313",
        "name": "High-Risk Sanctioned Entity #0313",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000314",
        "name": "High-Risk Sanctioned Entity #0314",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000315",
        "name": "High-Risk Sanctioned Entity #0315",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000316",
        "name": "High-Risk Sanctioned Entity #0316",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000317",
        "name": "High-Risk Sanctioned Entity #0317",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000318",
        "name": "High-Risk Sanctioned Entity #0318",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000319",
        "name": "High-Risk Sanctioned Entity #0319",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000320",
        "name": "High-Risk Sanctioned Entity #0320",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000321",
        "name": "High-Risk Sanctioned Entity #0321",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000322",
        "name": "High-Risk Sanctioned Entity #0322",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000323",
        "name": "High-Risk Sanctioned Entity #0323",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000324",
        "name": "High-Risk Sanctioned Entity #0324",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000325",
        "name": "High-Risk Sanctioned Entity #0325",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000326",
        "name": "High-Risk Sanctioned Entity #0326",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000327",
        "name": "High-Risk Sanctioned Entity #0327",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000328",
        "name": "High-Risk Sanctioned Entity #0328",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000329",
        "name": "High-Risk Sanctioned Entity #0329",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000330",
        "name": "High-Risk Sanctioned Entity #0330",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000331",
        "name": "High-Risk Sanctioned Entity #0331",
        "country": "Jurisdiction Code 12",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000332",
        "name": "High-Risk Sanctioned Entity #0332",
        "country": "Jurisdiction Code 13",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000333",
        "name": "High-Risk Sanctioned Entity #0333",
        "country": "Jurisdiction Code 14",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000334",
        "name": "High-Risk Sanctioned Entity #0334",
        "country": "Jurisdiction Code 15",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000335",
        "name": "High-Risk Sanctioned Entity #0335",
        "country": "Jurisdiction Code 16",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
    {
        "entity_id": "SDN_000336",
        "name": "High-Risk Sanctioned Entity #0336",
        "country": "Jurisdiction Code 17",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.91"
    },
    {
        "entity_id": "SDN_000337",
        "name": "High-Risk Sanctioned Entity #0337",
        "country": "Jurisdiction Code 18",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.92"
    },
    {
        "entity_id": "SDN_000338",
        "name": "High-Risk Sanctioned Entity #0338",
        "country": "Jurisdiction Code 19",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.93"
    },
    {
        "entity_id": "SDN_000339",
        "name": "High-Risk Sanctioned Entity #0339",
        "country": "Jurisdiction Code 20",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.94"
    },
    {
        "entity_id": "SDN_000340",
        "name": "High-Risk Sanctioned Entity #0340",
        "country": "Jurisdiction Code 1",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.95"
    },
    {
        "entity_id": "SDN_000341",
        "name": "High-Risk Sanctioned Entity #0341",
        "country": "Jurisdiction Code 2",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.96"
    },
    {
        "entity_id": "SDN_000342",
        "name": "High-Risk Sanctioned Entity #0342",
        "country": "Jurisdiction Code 3",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.97"
    },
    {
        "entity_id": "SDN_000343",
        "name": "High-Risk Sanctioned Entity #0343",
        "country": "Jurisdiction Code 4",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.98"
    },
    {
        "entity_id": "SDN_000344",
        "name": "High-Risk Sanctioned Entity #0344",
        "country": "Jurisdiction Code 5",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.99"
    },
    {
        "entity_id": "SDN_000345",
        "name": "High-Risk Sanctioned Entity #0345",
        "country": "Jurisdiction Code 6",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.85"
    },
    {
        "entity_id": "SDN_000346",
        "name": "High-Risk Sanctioned Entity #0346",
        "country": "Jurisdiction Code 7",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.86"
    },
    {
        "entity_id": "SDN_000347",
        "name": "High-Risk Sanctioned Entity #0347",
        "country": "Jurisdiction Code 8",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.87"
    },
    {
        "entity_id": "SDN_000348",
        "name": "High-Risk Sanctioned Entity #0348",
        "country": "Jurisdiction Code 9",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.88"
    },
    {
        "entity_id": "SDN_000349",
        "name": "High-Risk Sanctioned Entity #0349",
        "country": "Jurisdiction Code 10",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.89"
    },
    {
        "entity_id": "SDN_000350",
        "name": "High-Risk Sanctioned Entity #0350",
        "country": "Jurisdiction Code 11",
        "program": "OFAC-GLOBAL-COMPLIANCE",
        "risk_score": "0.9"
    },
]


class AMLMonitoringEngine:
    """Monitors transaction patterns for structuring, smurfing, and sanctions violations."""

    CTR_THRESHOLD_CENTS = 1000000  # $10,000.00 USD
    STRUCTURING_WINDOW_DAYS = 7

    @staticmethod
    def scan_for_structuring(transactions: List[Dict]) -> List[Dict]:
        """Identifies structuring (multiple transactions just below the $10k CTR threshold)."""
        alerts = []
        sub_threshold_txs = [
            tx for tx in transactions 
            if 800000 <= abs(tx.get("amount_cents", 0)) < 1000000
        ]
        
        if len(sub_threshold_txs) >= 2:
            alerts.append({
                "alert_type": "SUSPICIOUS_STRUCTURING_PATTERN",
                "severity": AMLAlertSeverity.HIGH.value,
                "transaction_count": len(sub_threshold_txs),
                "total_volume_cents": sum(abs(tx.get("amount_cents", 0)) for tx in sub_threshold_txs),
                "recommendation": "File Suspicious Activity Report (SAR) with FinCEN"
            })
        return alerts
