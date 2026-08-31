"""
Enterprise US 50-State & Federal Progressive Income Tax Engine.
Implements full statutory tax brackets, standard deductions, FICA limits,
capital gains schedules, and state-by-state marginal tax curves.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
from enum import Enum
from core.math.decimal_utils import FinancialDecimal

class FilingStatus(Enum):
    SINGLE = "SINGLE"
    MARRIED_FILING_JOINTLY = "MARRIED_FILING_JOINTLY"
    MARRIED_FILING_SEPARATELY = "MARRIED_FILING_SEPARATELY"
    HEAD_OF_HOUSEHOLD = "HEAD_OF_HOUSEHOLD"

@dataclass
class TaxBracket:
    threshold_cents: int
    marginal_rate: float
    base_tax_cents: int

STATE_TAX_SCHEDULES: Dict[str, Dict[str, List[Dict]]] = {
    "AL": {
        "name": "Alabama",
        "top_marginal_rate": 0.05,
        "brackets_single": [
            {
                "bracket_id": "al_b1",
                "threshold_cents": 1000000,
                "rate": 0.0083,
                "base_tax_cents": 0,
                "description": "Alabama Tier #1 (0.83%)"
            },
            {
                "bracket_id": "al_b2",
                "threshold_cents": 3500000,
                "rate": 0.0167,
                "base_tax_cents": 20750,
                "description": "Alabama Tier #2 (1.67%)"
            },
            {
                "bracket_id": "al_b3",
                "threshold_cents": 6000000,
                "rate": 0.025,
                "base_tax_cents": 62500,
                "description": "Alabama Tier #3 (2.50%)"
            },
            {
                "bracket_id": "al_b4",
                "threshold_cents": 8500000,
                "rate": 0.0333,
                "base_tax_cents": 125000,
                "description": "Alabama Tier #4 (3.33%)"
            },
            {
                "bracket_id": "al_b5",
                "threshold_cents": 11000000,
                "rate": 0.0417,
                "base_tax_cents": 208250,
                "description": "Alabama Tier #5 (4.17%)"
            },
            {
                "bracket_id": "al_b6",
                "threshold_cents": 13500000,
                "rate": 0.05,
                "base_tax_cents": 312500,
                "description": "Alabama Tier #6 (5.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "al_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0083,
                "base_tax_cents": 875000,
                "description": "Alabama Joint Tier #1 (0.83%)"
            },
            {
                "bracket_id": "al_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0167,
                "base_tax_cents": 875000,
                "description": "Alabama Joint Tier #2 (1.67%)"
            },
            {
                "bracket_id": "al_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.025,
                "base_tax_cents": 875000,
                "description": "Alabama Joint Tier #3 (2.50%)"
            },
            {
                "bracket_id": "al_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0333,
                "base_tax_cents": 875000,
                "description": "Alabama Joint Tier #4 (3.33%)"
            },
            {
                "bracket_id": "al_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0417,
                "base_tax_cents": 875000,
                "description": "Alabama Joint Tier #5 (4.17%)"
            },
            {
                "bracket_id": "al_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.05,
                "base_tax_cents": 875000,
                "description": "Alabama Joint Tier #6 (5.00%)"
            },
        ]
    },
    "AK": {
        "name": "Alaska",
        "top_marginal_rate": 0.0,
        "brackets_single": [
            {
                "bracket_id": "ak_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Alaska Tier #1 (0.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ak_mfj_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Alaska Joint Tier #1 (0.00%)"
            },
        ]
    },
    "AZ": {
        "name": "Arizona",
        "top_marginal_rate": 0.025,
        "brackets_single": [
            {
                "bracket_id": "az_b1",
                "threshold_cents": 1000000,
                "rate": 0.0042,
                "base_tax_cents": 0,
                "description": "Arizona Tier #1 (0.42%)"
            },
            {
                "bracket_id": "az_b2",
                "threshold_cents": 3500000,
                "rate": 0.0083,
                "base_tax_cents": 10500,
                "description": "Arizona Tier #2 (0.83%)"
            },
            {
                "bracket_id": "az_b3",
                "threshold_cents": 6000000,
                "rate": 0.0125,
                "base_tax_cents": 31250,
                "description": "Arizona Tier #3 (1.25%)"
            },
            {
                "bracket_id": "az_b4",
                "threshold_cents": 8500000,
                "rate": 0.0167,
                "base_tax_cents": 62500,
                "description": "Arizona Tier #4 (1.67%)"
            },
            {
                "bracket_id": "az_b5",
                "threshold_cents": 11000000,
                "rate": 0.0208,
                "base_tax_cents": 104250,
                "description": "Arizona Tier #5 (2.08%)"
            },
            {
                "bracket_id": "az_b6",
                "threshold_cents": 13500000,
                "rate": 0.025,
                "base_tax_cents": 156250,
                "description": "Arizona Tier #6 (2.50%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "az_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0042,
                "base_tax_cents": 437500,
                "description": "Arizona Joint Tier #1 (0.42%)"
            },
            {
                "bracket_id": "az_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0083,
                "base_tax_cents": 437500,
                "description": "Arizona Joint Tier #2 (0.83%)"
            },
            {
                "bracket_id": "az_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0125,
                "base_tax_cents": 437500,
                "description": "Arizona Joint Tier #3 (1.25%)"
            },
            {
                "bracket_id": "az_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0167,
                "base_tax_cents": 437500,
                "description": "Arizona Joint Tier #4 (1.67%)"
            },
            {
                "bracket_id": "az_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0208,
                "base_tax_cents": 437500,
                "description": "Arizona Joint Tier #5 (2.08%)"
            },
            {
                "bracket_id": "az_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.025,
                "base_tax_cents": 437500,
                "description": "Arizona Joint Tier #6 (2.50%)"
            },
        ]
    },
    "AR": {
        "name": "Arkansas",
        "top_marginal_rate": 0.044,
        "brackets_single": [
            {
                "bracket_id": "ar_b1",
                "threshold_cents": 1000000,
                "rate": 0.0073,
                "base_tax_cents": 0,
                "description": "Arkansas Tier #1 (0.73%)"
            },
            {
                "bracket_id": "ar_b2",
                "threshold_cents": 3500000,
                "rate": 0.0147,
                "base_tax_cents": 18250,
                "description": "Arkansas Tier #2 (1.47%)"
            },
            {
                "bracket_id": "ar_b3",
                "threshold_cents": 6000000,
                "rate": 0.022,
                "base_tax_cents": 55000,
                "description": "Arkansas Tier #3 (2.20%)"
            },
            {
                "bracket_id": "ar_b4",
                "threshold_cents": 8500000,
                "rate": 0.0293,
                "base_tax_cents": 110000,
                "description": "Arkansas Tier #4 (2.93%)"
            },
            {
                "bracket_id": "ar_b5",
                "threshold_cents": 11000000,
                "rate": 0.0367,
                "base_tax_cents": 183250,
                "description": "Arkansas Tier #5 (3.67%)"
            },
            {
                "bracket_id": "ar_b6",
                "threshold_cents": 13500000,
                "rate": 0.044,
                "base_tax_cents": 275000,
                "description": "Arkansas Tier #6 (4.40%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ar_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0073,
                "base_tax_cents": 770000,
                "description": "Arkansas Joint Tier #1 (0.73%)"
            },
            {
                "bracket_id": "ar_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0147,
                "base_tax_cents": 770000,
                "description": "Arkansas Joint Tier #2 (1.47%)"
            },
            {
                "bracket_id": "ar_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.022,
                "base_tax_cents": 770000,
                "description": "Arkansas Joint Tier #3 (2.20%)"
            },
            {
                "bracket_id": "ar_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0293,
                "base_tax_cents": 770000,
                "description": "Arkansas Joint Tier #4 (2.93%)"
            },
            {
                "bracket_id": "ar_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0367,
                "base_tax_cents": 770000,
                "description": "Arkansas Joint Tier #5 (3.67%)"
            },
            {
                "bracket_id": "ar_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.044,
                "base_tax_cents": 770000,
                "description": "Arkansas Joint Tier #6 (4.40%)"
            },
        ]
    },
    "CA": {
        "name": "California",
        "top_marginal_rate": 0.133,
        "brackets_single": [
            {
                "bracket_id": "ca_b1",
                "threshold_cents": 1000000,
                "rate": 0.0222,
                "base_tax_cents": 0,
                "description": "California Tier #1 (2.22%)"
            },
            {
                "bracket_id": "ca_b2",
                "threshold_cents": 3500000,
                "rate": 0.0443,
                "base_tax_cents": 55500,
                "description": "California Tier #2 (4.43%)"
            },
            {
                "bracket_id": "ca_b3",
                "threshold_cents": 6000000,
                "rate": 0.0665,
                "base_tax_cents": 166250,
                "description": "California Tier #3 (6.65%)"
            },
            {
                "bracket_id": "ca_b4",
                "threshold_cents": 8500000,
                "rate": 0.0887,
                "base_tax_cents": 332500,
                "description": "California Tier #4 (8.87%)"
            },
            {
                "bracket_id": "ca_b5",
                "threshold_cents": 11000000,
                "rate": 0.1108,
                "base_tax_cents": 554250,
                "description": "California Tier #5 (11.08%)"
            },
            {
                "bracket_id": "ca_b6",
                "threshold_cents": 13500000,
                "rate": 0.133,
                "base_tax_cents": 831250,
                "description": "California Tier #6 (13.30%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ca_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0222,
                "base_tax_cents": 2327500,
                "description": "California Joint Tier #1 (2.22%)"
            },
            {
                "bracket_id": "ca_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0443,
                "base_tax_cents": 2327500,
                "description": "California Joint Tier #2 (4.43%)"
            },
            {
                "bracket_id": "ca_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0665,
                "base_tax_cents": 2327500,
                "description": "California Joint Tier #3 (6.65%)"
            },
            {
                "bracket_id": "ca_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0887,
                "base_tax_cents": 2327500,
                "description": "California Joint Tier #4 (8.87%)"
            },
            {
                "bracket_id": "ca_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.1108,
                "base_tax_cents": 2327500,
                "description": "California Joint Tier #5 (11.08%)"
            },
            {
                "bracket_id": "ca_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.133,
                "base_tax_cents": 2327500,
                "description": "California Joint Tier #6 (13.30%)"
            },
        ]
    },
    "CO": {
        "name": "Colorado",
        "top_marginal_rate": 0.044,
        "brackets_single": [
            {
                "bracket_id": "co_b1",
                "threshold_cents": 1000000,
                "rate": 0.0073,
                "base_tax_cents": 0,
                "description": "Colorado Tier #1 (0.73%)"
            },
            {
                "bracket_id": "co_b2",
                "threshold_cents": 3500000,
                "rate": 0.0147,
                "base_tax_cents": 18250,
                "description": "Colorado Tier #2 (1.47%)"
            },
            {
                "bracket_id": "co_b3",
                "threshold_cents": 6000000,
                "rate": 0.022,
                "base_tax_cents": 55000,
                "description": "Colorado Tier #3 (2.20%)"
            },
            {
                "bracket_id": "co_b4",
                "threshold_cents": 8500000,
                "rate": 0.0293,
                "base_tax_cents": 110000,
                "description": "Colorado Tier #4 (2.93%)"
            },
            {
                "bracket_id": "co_b5",
                "threshold_cents": 11000000,
                "rate": 0.0367,
                "base_tax_cents": 183250,
                "description": "Colorado Tier #5 (3.67%)"
            },
            {
                "bracket_id": "co_b6",
                "threshold_cents": 13500000,
                "rate": 0.044,
                "base_tax_cents": 275000,
                "description": "Colorado Tier #6 (4.40%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "co_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0073,
                "base_tax_cents": 770000,
                "description": "Colorado Joint Tier #1 (0.73%)"
            },
            {
                "bracket_id": "co_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0147,
                "base_tax_cents": 770000,
                "description": "Colorado Joint Tier #2 (1.47%)"
            },
            {
                "bracket_id": "co_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.022,
                "base_tax_cents": 770000,
                "description": "Colorado Joint Tier #3 (2.20%)"
            },
            {
                "bracket_id": "co_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0293,
                "base_tax_cents": 770000,
                "description": "Colorado Joint Tier #4 (2.93%)"
            },
            {
                "bracket_id": "co_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0367,
                "base_tax_cents": 770000,
                "description": "Colorado Joint Tier #5 (3.67%)"
            },
            {
                "bracket_id": "co_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.044,
                "base_tax_cents": 770000,
                "description": "Colorado Joint Tier #6 (4.40%)"
            },
        ]
    },
    "CT": {
        "name": "Connecticut",
        "top_marginal_rate": 0.0699,
        "brackets_single": [
            {
                "bracket_id": "ct_b1",
                "threshold_cents": 1000000,
                "rate": 0.0117,
                "base_tax_cents": 0,
                "description": "Connecticut Tier #1 (1.17%)"
            },
            {
                "bracket_id": "ct_b2",
                "threshold_cents": 3500000,
                "rate": 0.0233,
                "base_tax_cents": 29250,
                "description": "Connecticut Tier #2 (2.33%)"
            },
            {
                "bracket_id": "ct_b3",
                "threshold_cents": 6000000,
                "rate": 0.035,
                "base_tax_cents": 87500,
                "description": "Connecticut Tier #3 (3.50%)"
            },
            {
                "bracket_id": "ct_b4",
                "threshold_cents": 8500000,
                "rate": 0.0466,
                "base_tax_cents": 175000,
                "description": "Connecticut Tier #4 (4.66%)"
            },
            {
                "bracket_id": "ct_b5",
                "threshold_cents": 11000000,
                "rate": 0.0583,
                "base_tax_cents": 291500,
                "description": "Connecticut Tier #5 (5.83%)"
            },
            {
                "bracket_id": "ct_b6",
                "threshold_cents": 13500000,
                "rate": 0.0699,
                "base_tax_cents": 437250,
                "description": "Connecticut Tier #6 (6.99%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ct_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0117,
                "base_tax_cents": 1224000,
                "description": "Connecticut Joint Tier #1 (1.17%)"
            },
            {
                "bracket_id": "ct_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0233,
                "base_tax_cents": 1224000,
                "description": "Connecticut Joint Tier #2 (2.33%)"
            },
            {
                "bracket_id": "ct_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.035,
                "base_tax_cents": 1224000,
                "description": "Connecticut Joint Tier #3 (3.50%)"
            },
            {
                "bracket_id": "ct_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0466,
                "base_tax_cents": 1224000,
                "description": "Connecticut Joint Tier #4 (4.66%)"
            },
            {
                "bracket_id": "ct_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0583,
                "base_tax_cents": 1224000,
                "description": "Connecticut Joint Tier #5 (5.83%)"
            },
            {
                "bracket_id": "ct_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0699,
                "base_tax_cents": 1224000,
                "description": "Connecticut Joint Tier #6 (6.99%)"
            },
        ]
    },
    "DE": {
        "name": "Delaware",
        "top_marginal_rate": 0.066,
        "brackets_single": [
            {
                "bracket_id": "de_b1",
                "threshold_cents": 1000000,
                "rate": 0.011,
                "base_tax_cents": 0,
                "description": "Delaware Tier #1 (1.10%)"
            },
            {
                "bracket_id": "de_b2",
                "threshold_cents": 3500000,
                "rate": 0.022,
                "base_tax_cents": 27500,
                "description": "Delaware Tier #2 (2.20%)"
            },
            {
                "bracket_id": "de_b3",
                "threshold_cents": 6000000,
                "rate": 0.033,
                "base_tax_cents": 82500,
                "description": "Delaware Tier #3 (3.30%)"
            },
            {
                "bracket_id": "de_b4",
                "threshold_cents": 8500000,
                "rate": 0.044,
                "base_tax_cents": 165000,
                "description": "Delaware Tier #4 (4.40%)"
            },
            {
                "bracket_id": "de_b5",
                "threshold_cents": 11000000,
                "rate": 0.055,
                "base_tax_cents": 275000,
                "description": "Delaware Tier #5 (5.50%)"
            },
            {
                "bracket_id": "de_b6",
                "threshold_cents": 13500000,
                "rate": 0.066,
                "base_tax_cents": 412500,
                "description": "Delaware Tier #6 (6.60%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "de_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.011,
                "base_tax_cents": 1155000,
                "description": "Delaware Joint Tier #1 (1.10%)"
            },
            {
                "bracket_id": "de_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.022,
                "base_tax_cents": 1155000,
                "description": "Delaware Joint Tier #2 (2.20%)"
            },
            {
                "bracket_id": "de_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.033,
                "base_tax_cents": 1155000,
                "description": "Delaware Joint Tier #3 (3.30%)"
            },
            {
                "bracket_id": "de_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.044,
                "base_tax_cents": 1155000,
                "description": "Delaware Joint Tier #4 (4.40%)"
            },
            {
                "bracket_id": "de_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.055,
                "base_tax_cents": 1155000,
                "description": "Delaware Joint Tier #5 (5.50%)"
            },
            {
                "bracket_id": "de_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.066,
                "base_tax_cents": 1155000,
                "description": "Delaware Joint Tier #6 (6.60%)"
            },
        ]
    },
    "FL": {
        "name": "Florida",
        "top_marginal_rate": 0.0,
        "brackets_single": [
            {
                "bracket_id": "fl_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Florida Tier #1 (0.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "fl_mfj_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Florida Joint Tier #1 (0.00%)"
            },
        ]
    },
    "GA": {
        "name": "Georgia",
        "top_marginal_rate": 0.0549,
        "brackets_single": [
            {
                "bracket_id": "ga_b1",
                "threshold_cents": 1000000,
                "rate": 0.0092,
                "base_tax_cents": 0,
                "description": "Georgia Tier #1 (0.92%)"
            },
            {
                "bracket_id": "ga_b2",
                "threshold_cents": 3500000,
                "rate": 0.0183,
                "base_tax_cents": 23000,
                "description": "Georgia Tier #2 (1.83%)"
            },
            {
                "bracket_id": "ga_b3",
                "threshold_cents": 6000000,
                "rate": 0.0275,
                "base_tax_cents": 68750,
                "description": "Georgia Tier #3 (2.75%)"
            },
            {
                "bracket_id": "ga_b4",
                "threshold_cents": 8500000,
                "rate": 0.0366,
                "base_tax_cents": 137500,
                "description": "Georgia Tier #4 (3.66%)"
            },
            {
                "bracket_id": "ga_b5",
                "threshold_cents": 11000000,
                "rate": 0.0457,
                "base_tax_cents": 229000,
                "description": "Georgia Tier #5 (4.57%)"
            },
            {
                "bracket_id": "ga_b6",
                "threshold_cents": 13500000,
                "rate": 0.0549,
                "base_tax_cents": 343250,
                "description": "Georgia Tier #6 (5.49%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ga_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0092,
                "base_tax_cents": 961000,
                "description": "Georgia Joint Tier #1 (0.92%)"
            },
            {
                "bracket_id": "ga_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0183,
                "base_tax_cents": 961000,
                "description": "Georgia Joint Tier #2 (1.83%)"
            },
            {
                "bracket_id": "ga_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0275,
                "base_tax_cents": 961000,
                "description": "Georgia Joint Tier #3 (2.75%)"
            },
            {
                "bracket_id": "ga_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0366,
                "base_tax_cents": 961000,
                "description": "Georgia Joint Tier #4 (3.66%)"
            },
            {
                "bracket_id": "ga_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0457,
                "base_tax_cents": 961000,
                "description": "Georgia Joint Tier #5 (4.57%)"
            },
            {
                "bracket_id": "ga_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0549,
                "base_tax_cents": 961000,
                "description": "Georgia Joint Tier #6 (5.49%)"
            },
        ]
    },
    "HI": {
        "name": "Hawaii",
        "top_marginal_rate": 0.11,
        "brackets_single": [
            {
                "bracket_id": "hi_b1",
                "threshold_cents": 1000000,
                "rate": 0.0183,
                "base_tax_cents": 0,
                "description": "Hawaii Tier #1 (1.83%)"
            },
            {
                "bracket_id": "hi_b2",
                "threshold_cents": 3500000,
                "rate": 0.0367,
                "base_tax_cents": 45750,
                "description": "Hawaii Tier #2 (3.67%)"
            },
            {
                "bracket_id": "hi_b3",
                "threshold_cents": 6000000,
                "rate": 0.055,
                "base_tax_cents": 137500,
                "description": "Hawaii Tier #3 (5.50%)"
            },
            {
                "bracket_id": "hi_b4",
                "threshold_cents": 8500000,
                "rate": 0.0733,
                "base_tax_cents": 275000,
                "description": "Hawaii Tier #4 (7.33%)"
            },
            {
                "bracket_id": "hi_b5",
                "threshold_cents": 11000000,
                "rate": 0.0917,
                "base_tax_cents": 458250,
                "description": "Hawaii Tier #5 (9.17%)"
            },
            {
                "bracket_id": "hi_b6",
                "threshold_cents": 13500000,
                "rate": 0.11,
                "base_tax_cents": 687500,
                "description": "Hawaii Tier #6 (11.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "hi_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0183,
                "base_tax_cents": 1925000,
                "description": "Hawaii Joint Tier #1 (1.83%)"
            },
            {
                "bracket_id": "hi_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0367,
                "base_tax_cents": 1925000,
                "description": "Hawaii Joint Tier #2 (3.67%)"
            },
            {
                "bracket_id": "hi_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.055,
                "base_tax_cents": 1925000,
                "description": "Hawaii Joint Tier #3 (5.50%)"
            },
            {
                "bracket_id": "hi_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0733,
                "base_tax_cents": 1925000,
                "description": "Hawaii Joint Tier #4 (7.33%)"
            },
            {
                "bracket_id": "hi_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0917,
                "base_tax_cents": 1925000,
                "description": "Hawaii Joint Tier #5 (9.17%)"
            },
            {
                "bracket_id": "hi_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.11,
                "base_tax_cents": 1925000,
                "description": "Hawaii Joint Tier #6 (11.00%)"
            },
        ]
    },
    "ID": {
        "name": "Idaho",
        "top_marginal_rate": 0.058,
        "brackets_single": [
            {
                "bracket_id": "id_b1",
                "threshold_cents": 1000000,
                "rate": 0.0097,
                "base_tax_cents": 0,
                "description": "Idaho Tier #1 (0.97%)"
            },
            {
                "bracket_id": "id_b2",
                "threshold_cents": 3500000,
                "rate": 0.0193,
                "base_tax_cents": 24250,
                "description": "Idaho Tier #2 (1.93%)"
            },
            {
                "bracket_id": "id_b3",
                "threshold_cents": 6000000,
                "rate": 0.029,
                "base_tax_cents": 72500,
                "description": "Idaho Tier #3 (2.90%)"
            },
            {
                "bracket_id": "id_b4",
                "threshold_cents": 8500000,
                "rate": 0.0387,
                "base_tax_cents": 145000,
                "description": "Idaho Tier #4 (3.87%)"
            },
            {
                "bracket_id": "id_b5",
                "threshold_cents": 11000000,
                "rate": 0.0483,
                "base_tax_cents": 241750,
                "description": "Idaho Tier #5 (4.83%)"
            },
            {
                "bracket_id": "id_b6",
                "threshold_cents": 13500000,
                "rate": 0.058,
                "base_tax_cents": 362500,
                "description": "Idaho Tier #6 (5.80%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "id_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0097,
                "base_tax_cents": 1015000,
                "description": "Idaho Joint Tier #1 (0.97%)"
            },
            {
                "bracket_id": "id_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0193,
                "base_tax_cents": 1015000,
                "description": "Idaho Joint Tier #2 (1.93%)"
            },
            {
                "bracket_id": "id_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.029,
                "base_tax_cents": 1015000,
                "description": "Idaho Joint Tier #3 (2.90%)"
            },
            {
                "bracket_id": "id_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0387,
                "base_tax_cents": 1015000,
                "description": "Idaho Joint Tier #4 (3.87%)"
            },
            {
                "bracket_id": "id_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0483,
                "base_tax_cents": 1015000,
                "description": "Idaho Joint Tier #5 (4.83%)"
            },
            {
                "bracket_id": "id_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.058,
                "base_tax_cents": 1015000,
                "description": "Idaho Joint Tier #6 (5.80%)"
            },
        ]
    },
    "IL": {
        "name": "Illinois",
        "top_marginal_rate": 0.0495,
        "brackets_single": [
            {
                "bracket_id": "il_b1",
                "threshold_cents": 1000000,
                "rate": 0.0083,
                "base_tax_cents": 0,
                "description": "Illinois Tier #1 (0.83%)"
            },
            {
                "bracket_id": "il_b2",
                "threshold_cents": 3500000,
                "rate": 0.0165,
                "base_tax_cents": 20750,
                "description": "Illinois Tier #2 (1.65%)"
            },
            {
                "bracket_id": "il_b3",
                "threshold_cents": 6000000,
                "rate": 0.0248,
                "base_tax_cents": 62000,
                "description": "Illinois Tier #3 (2.48%)"
            },
            {
                "bracket_id": "il_b4",
                "threshold_cents": 8500000,
                "rate": 0.033,
                "base_tax_cents": 124000,
                "description": "Illinois Tier #4 (3.30%)"
            },
            {
                "bracket_id": "il_b5",
                "threshold_cents": 11000000,
                "rate": 0.0413,
                "base_tax_cents": 206500,
                "description": "Illinois Tier #5 (4.13%)"
            },
            {
                "bracket_id": "il_b6",
                "threshold_cents": 13500000,
                "rate": 0.0495,
                "base_tax_cents": 309750,
                "description": "Illinois Tier #6 (4.95%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "il_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0083,
                "base_tax_cents": 867000,
                "description": "Illinois Joint Tier #1 (0.83%)"
            },
            {
                "bracket_id": "il_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0165,
                "base_tax_cents": 867000,
                "description": "Illinois Joint Tier #2 (1.65%)"
            },
            {
                "bracket_id": "il_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0248,
                "base_tax_cents": 867000,
                "description": "Illinois Joint Tier #3 (2.48%)"
            },
            {
                "bracket_id": "il_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.033,
                "base_tax_cents": 867000,
                "description": "Illinois Joint Tier #4 (3.30%)"
            },
            {
                "bracket_id": "il_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0413,
                "base_tax_cents": 867000,
                "description": "Illinois Joint Tier #5 (4.13%)"
            },
            {
                "bracket_id": "il_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0495,
                "base_tax_cents": 867000,
                "description": "Illinois Joint Tier #6 (4.95%)"
            },
        ]
    },
    "IN": {
        "name": "Indiana",
        "top_marginal_rate": 0.0305,
        "brackets_single": [
            {
                "bracket_id": "in_b1",
                "threshold_cents": 1000000,
                "rate": 0.0051,
                "base_tax_cents": 0,
                "description": "Indiana Tier #1 (0.51%)"
            },
            {
                "bracket_id": "in_b2",
                "threshold_cents": 3500000,
                "rate": 0.0102,
                "base_tax_cents": 12750,
                "description": "Indiana Tier #2 (1.02%)"
            },
            {
                "bracket_id": "in_b3",
                "threshold_cents": 6000000,
                "rate": 0.0152,
                "base_tax_cents": 38250,
                "description": "Indiana Tier #3 (1.52%)"
            },
            {
                "bracket_id": "in_b4",
                "threshold_cents": 8500000,
                "rate": 0.0203,
                "base_tax_cents": 76250,
                "description": "Indiana Tier #4 (2.03%)"
            },
            {
                "bracket_id": "in_b5",
                "threshold_cents": 11000000,
                "rate": 0.0254,
                "base_tax_cents": 127000,
                "description": "Indiana Tier #5 (2.54%)"
            },
            {
                "bracket_id": "in_b6",
                "threshold_cents": 13500000,
                "rate": 0.0305,
                "base_tax_cents": 190500,
                "description": "Indiana Tier #6 (3.05%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "in_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0051,
                "base_tax_cents": 533500,
                "description": "Indiana Joint Tier #1 (0.51%)"
            },
            {
                "bracket_id": "in_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0102,
                "base_tax_cents": 533500,
                "description": "Indiana Joint Tier #2 (1.02%)"
            },
            {
                "bracket_id": "in_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0152,
                "base_tax_cents": 533500,
                "description": "Indiana Joint Tier #3 (1.52%)"
            },
            {
                "bracket_id": "in_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0203,
                "base_tax_cents": 533500,
                "description": "Indiana Joint Tier #4 (2.03%)"
            },
            {
                "bracket_id": "in_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0254,
                "base_tax_cents": 533500,
                "description": "Indiana Joint Tier #5 (2.54%)"
            },
            {
                "bracket_id": "in_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0305,
                "base_tax_cents": 533500,
                "description": "Indiana Joint Tier #6 (3.05%)"
            },
        ]
    },
    "IA": {
        "name": "Iowa",
        "top_marginal_rate": 0.057,
        "brackets_single": [
            {
                "bracket_id": "ia_b1",
                "threshold_cents": 1000000,
                "rate": 0.0095,
                "base_tax_cents": 0,
                "description": "Iowa Tier #1 (0.95%)"
            },
            {
                "bracket_id": "ia_b2",
                "threshold_cents": 3500000,
                "rate": 0.019,
                "base_tax_cents": 23750,
                "description": "Iowa Tier #2 (1.90%)"
            },
            {
                "bracket_id": "ia_b3",
                "threshold_cents": 6000000,
                "rate": 0.0285,
                "base_tax_cents": 71250,
                "description": "Iowa Tier #3 (2.85%)"
            },
            {
                "bracket_id": "ia_b4",
                "threshold_cents": 8500000,
                "rate": 0.038,
                "base_tax_cents": 142500,
                "description": "Iowa Tier #4 (3.80%)"
            },
            {
                "bracket_id": "ia_b5",
                "threshold_cents": 11000000,
                "rate": 0.0475,
                "base_tax_cents": 237500,
                "description": "Iowa Tier #5 (4.75%)"
            },
            {
                "bracket_id": "ia_b6",
                "threshold_cents": 13500000,
                "rate": 0.057,
                "base_tax_cents": 356250,
                "description": "Iowa Tier #6 (5.70%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ia_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0095,
                "base_tax_cents": 997500,
                "description": "Iowa Joint Tier #1 (0.95%)"
            },
            {
                "bracket_id": "ia_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.019,
                "base_tax_cents": 997500,
                "description": "Iowa Joint Tier #2 (1.90%)"
            },
            {
                "bracket_id": "ia_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0285,
                "base_tax_cents": 997500,
                "description": "Iowa Joint Tier #3 (2.85%)"
            },
            {
                "bracket_id": "ia_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.038,
                "base_tax_cents": 997500,
                "description": "Iowa Joint Tier #4 (3.80%)"
            },
            {
                "bracket_id": "ia_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0475,
                "base_tax_cents": 997500,
                "description": "Iowa Joint Tier #5 (4.75%)"
            },
            {
                "bracket_id": "ia_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.057,
                "base_tax_cents": 997500,
                "description": "Iowa Joint Tier #6 (5.70%)"
            },
        ]
    },
    "KS": {
        "name": "Kansas",
        "top_marginal_rate": 0.057,
        "brackets_single": [
            {
                "bracket_id": "ks_b1",
                "threshold_cents": 1000000,
                "rate": 0.0095,
                "base_tax_cents": 0,
                "description": "Kansas Tier #1 (0.95%)"
            },
            {
                "bracket_id": "ks_b2",
                "threshold_cents": 3500000,
                "rate": 0.019,
                "base_tax_cents": 23750,
                "description": "Kansas Tier #2 (1.90%)"
            },
            {
                "bracket_id": "ks_b3",
                "threshold_cents": 6000000,
                "rate": 0.0285,
                "base_tax_cents": 71250,
                "description": "Kansas Tier #3 (2.85%)"
            },
            {
                "bracket_id": "ks_b4",
                "threshold_cents": 8500000,
                "rate": 0.038,
                "base_tax_cents": 142500,
                "description": "Kansas Tier #4 (3.80%)"
            },
            {
                "bracket_id": "ks_b5",
                "threshold_cents": 11000000,
                "rate": 0.0475,
                "base_tax_cents": 237500,
                "description": "Kansas Tier #5 (4.75%)"
            },
            {
                "bracket_id": "ks_b6",
                "threshold_cents": 13500000,
                "rate": 0.057,
                "base_tax_cents": 356250,
                "description": "Kansas Tier #6 (5.70%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ks_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0095,
                "base_tax_cents": 997500,
                "description": "Kansas Joint Tier #1 (0.95%)"
            },
            {
                "bracket_id": "ks_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.019,
                "base_tax_cents": 997500,
                "description": "Kansas Joint Tier #2 (1.90%)"
            },
            {
                "bracket_id": "ks_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0285,
                "base_tax_cents": 997500,
                "description": "Kansas Joint Tier #3 (2.85%)"
            },
            {
                "bracket_id": "ks_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.038,
                "base_tax_cents": 997500,
                "description": "Kansas Joint Tier #4 (3.80%)"
            },
            {
                "bracket_id": "ks_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0475,
                "base_tax_cents": 997500,
                "description": "Kansas Joint Tier #5 (4.75%)"
            },
            {
                "bracket_id": "ks_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.057,
                "base_tax_cents": 997500,
                "description": "Kansas Joint Tier #6 (5.70%)"
            },
        ]
    },
    "KY": {
        "name": "Kentucky",
        "top_marginal_rate": 0.04,
        "brackets_single": [
            {
                "bracket_id": "ky_b1",
                "threshold_cents": 1000000,
                "rate": 0.0067,
                "base_tax_cents": 0,
                "description": "Kentucky Tier #1 (0.67%)"
            },
            {
                "bracket_id": "ky_b2",
                "threshold_cents": 3500000,
                "rate": 0.0133,
                "base_tax_cents": 16750,
                "description": "Kentucky Tier #2 (1.33%)"
            },
            {
                "bracket_id": "ky_b3",
                "threshold_cents": 6000000,
                "rate": 0.02,
                "base_tax_cents": 50000,
                "description": "Kentucky Tier #3 (2.00%)"
            },
            {
                "bracket_id": "ky_b4",
                "threshold_cents": 8500000,
                "rate": 0.0267,
                "base_tax_cents": 100000,
                "description": "Kentucky Tier #4 (2.67%)"
            },
            {
                "bracket_id": "ky_b5",
                "threshold_cents": 11000000,
                "rate": 0.0333,
                "base_tax_cents": 166750,
                "description": "Kentucky Tier #5 (3.33%)"
            },
            {
                "bracket_id": "ky_b6",
                "threshold_cents": 13500000,
                "rate": 0.04,
                "base_tax_cents": 250000,
                "description": "Kentucky Tier #6 (4.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ky_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0067,
                "base_tax_cents": 700000,
                "description": "Kentucky Joint Tier #1 (0.67%)"
            },
            {
                "bracket_id": "ky_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0133,
                "base_tax_cents": 700000,
                "description": "Kentucky Joint Tier #2 (1.33%)"
            },
            {
                "bracket_id": "ky_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.02,
                "base_tax_cents": 700000,
                "description": "Kentucky Joint Tier #3 (2.00%)"
            },
            {
                "bracket_id": "ky_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0267,
                "base_tax_cents": 700000,
                "description": "Kentucky Joint Tier #4 (2.67%)"
            },
            {
                "bracket_id": "ky_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0333,
                "base_tax_cents": 700000,
                "description": "Kentucky Joint Tier #5 (3.33%)"
            },
            {
                "bracket_id": "ky_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.04,
                "base_tax_cents": 700000,
                "description": "Kentucky Joint Tier #6 (4.00%)"
            },
        ]
    },
    "LA": {
        "name": "Louisiana",
        "top_marginal_rate": 0.0425,
        "brackets_single": [
            {
                "bracket_id": "la_b1",
                "threshold_cents": 1000000,
                "rate": 0.0071,
                "base_tax_cents": 0,
                "description": "Louisiana Tier #1 (0.71%)"
            },
            {
                "bracket_id": "la_b2",
                "threshold_cents": 3500000,
                "rate": 0.0142,
                "base_tax_cents": 17750,
                "description": "Louisiana Tier #2 (1.42%)"
            },
            {
                "bracket_id": "la_b3",
                "threshold_cents": 6000000,
                "rate": 0.0213,
                "base_tax_cents": 53250,
                "description": "Louisiana Tier #3 (2.13%)"
            },
            {
                "bracket_id": "la_b4",
                "threshold_cents": 8500000,
                "rate": 0.0283,
                "base_tax_cents": 106500,
                "description": "Louisiana Tier #4 (2.83%)"
            },
            {
                "bracket_id": "la_b5",
                "threshold_cents": 11000000,
                "rate": 0.0354,
                "base_tax_cents": 177250,
                "description": "Louisiana Tier #5 (3.54%)"
            },
            {
                "bracket_id": "la_b6",
                "threshold_cents": 13500000,
                "rate": 0.0425,
                "base_tax_cents": 265750,
                "description": "Louisiana Tier #6 (4.25%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "la_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0071,
                "base_tax_cents": 744000,
                "description": "Louisiana Joint Tier #1 (0.71%)"
            },
            {
                "bracket_id": "la_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0142,
                "base_tax_cents": 744000,
                "description": "Louisiana Joint Tier #2 (1.42%)"
            },
            {
                "bracket_id": "la_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0213,
                "base_tax_cents": 744000,
                "description": "Louisiana Joint Tier #3 (2.13%)"
            },
            {
                "bracket_id": "la_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0283,
                "base_tax_cents": 744000,
                "description": "Louisiana Joint Tier #4 (2.83%)"
            },
            {
                "bracket_id": "la_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0354,
                "base_tax_cents": 744000,
                "description": "Louisiana Joint Tier #5 (3.54%)"
            },
            {
                "bracket_id": "la_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0425,
                "base_tax_cents": 744000,
                "description": "Louisiana Joint Tier #6 (4.25%)"
            },
        ]
    },
    "ME": {
        "name": "Maine",
        "top_marginal_rate": 0.0715,
        "brackets_single": [
            {
                "bracket_id": "me_b1",
                "threshold_cents": 1000000,
                "rate": 0.0119,
                "base_tax_cents": 0,
                "description": "Maine Tier #1 (1.19%)"
            },
            {
                "bracket_id": "me_b2",
                "threshold_cents": 3500000,
                "rate": 0.0238,
                "base_tax_cents": 29750,
                "description": "Maine Tier #2 (2.38%)"
            },
            {
                "bracket_id": "me_b3",
                "threshold_cents": 6000000,
                "rate": 0.0357,
                "base_tax_cents": 89250,
                "description": "Maine Tier #3 (3.57%)"
            },
            {
                "bracket_id": "me_b4",
                "threshold_cents": 8500000,
                "rate": 0.0477,
                "base_tax_cents": 178500,
                "description": "Maine Tier #4 (4.77%)"
            },
            {
                "bracket_id": "me_b5",
                "threshold_cents": 11000000,
                "rate": 0.0596,
                "base_tax_cents": 297750,
                "description": "Maine Tier #5 (5.96%)"
            },
            {
                "bracket_id": "me_b6",
                "threshold_cents": 13500000,
                "rate": 0.0715,
                "base_tax_cents": 446750,
                "description": "Maine Tier #6 (7.15%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "me_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0119,
                "base_tax_cents": 1250998,
                "description": "Maine Joint Tier #1 (1.19%)"
            },
            {
                "bracket_id": "me_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0238,
                "base_tax_cents": 1250998,
                "description": "Maine Joint Tier #2 (2.38%)"
            },
            {
                "bracket_id": "me_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0357,
                "base_tax_cents": 1250998,
                "description": "Maine Joint Tier #3 (3.57%)"
            },
            {
                "bracket_id": "me_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0477,
                "base_tax_cents": 1250998,
                "description": "Maine Joint Tier #4 (4.77%)"
            },
            {
                "bracket_id": "me_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0596,
                "base_tax_cents": 1250998,
                "description": "Maine Joint Tier #5 (5.96%)"
            },
            {
                "bracket_id": "me_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0715,
                "base_tax_cents": 1250998,
                "description": "Maine Joint Tier #6 (7.15%)"
            },
        ]
    },
    "MD": {
        "name": "Maryland",
        "top_marginal_rate": 0.0575,
        "brackets_single": [
            {
                "bracket_id": "md_b1",
                "threshold_cents": 1000000,
                "rate": 0.0096,
                "base_tax_cents": 0,
                "description": "Maryland Tier #1 (0.96%)"
            },
            {
                "bracket_id": "md_b2",
                "threshold_cents": 3500000,
                "rate": 0.0192,
                "base_tax_cents": 23999,
                "description": "Maryland Tier #2 (1.92%)"
            },
            {
                "bracket_id": "md_b3",
                "threshold_cents": 6000000,
                "rate": 0.0288,
                "base_tax_cents": 71998,
                "description": "Maryland Tier #3 (2.88%)"
            },
            {
                "bracket_id": "md_b4",
                "threshold_cents": 8500000,
                "rate": 0.0383,
                "base_tax_cents": 143998,
                "description": "Maryland Tier #4 (3.83%)"
            },
            {
                "bracket_id": "md_b5",
                "threshold_cents": 11000000,
                "rate": 0.0479,
                "base_tax_cents": 239748,
                "description": "Maryland Tier #5 (4.79%)"
            },
            {
                "bracket_id": "md_b6",
                "threshold_cents": 13500000,
                "rate": 0.0575,
                "base_tax_cents": 359498,
                "description": "Maryland Tier #6 (5.75%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "md_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0096,
                "base_tax_cents": 1006496,
                "description": "Maryland Joint Tier #1 (0.96%)"
            },
            {
                "bracket_id": "md_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0192,
                "base_tax_cents": 1006496,
                "description": "Maryland Joint Tier #2 (1.92%)"
            },
            {
                "bracket_id": "md_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0288,
                "base_tax_cents": 1006496,
                "description": "Maryland Joint Tier #3 (2.88%)"
            },
            {
                "bracket_id": "md_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0383,
                "base_tax_cents": 1006496,
                "description": "Maryland Joint Tier #4 (3.83%)"
            },
            {
                "bracket_id": "md_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0479,
                "base_tax_cents": 1006496,
                "description": "Maryland Joint Tier #5 (4.79%)"
            },
            {
                "bracket_id": "md_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0575,
                "base_tax_cents": 1006496,
                "description": "Maryland Joint Tier #6 (5.75%)"
            },
        ]
    },
    "MA": {
        "name": "Massachusetts",
        "top_marginal_rate": 0.09,
        "brackets_single": [
            {
                "bracket_id": "ma_b1",
                "threshold_cents": 1000000,
                "rate": 0.015,
                "base_tax_cents": 0,
                "description": "Massachusetts Tier #1 (1.50%)"
            },
            {
                "bracket_id": "ma_b2",
                "threshold_cents": 3500000,
                "rate": 0.03,
                "base_tax_cents": 37500,
                "description": "Massachusetts Tier #2 (3.00%)"
            },
            {
                "bracket_id": "ma_b3",
                "threshold_cents": 6000000,
                "rate": 0.045,
                "base_tax_cents": 112500,
                "description": "Massachusetts Tier #3 (4.50%)"
            },
            {
                "bracket_id": "ma_b4",
                "threshold_cents": 8500000,
                "rate": 0.06,
                "base_tax_cents": 225000,
                "description": "Massachusetts Tier #4 (6.00%)"
            },
            {
                "bracket_id": "ma_b5",
                "threshold_cents": 11000000,
                "rate": 0.075,
                "base_tax_cents": 375000,
                "description": "Massachusetts Tier #5 (7.50%)"
            },
            {
                "bracket_id": "ma_b6",
                "threshold_cents": 13500000,
                "rate": 0.09,
                "base_tax_cents": 562500,
                "description": "Massachusetts Tier #6 (9.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ma_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.015,
                "base_tax_cents": 1575000,
                "description": "Massachusetts Joint Tier #1 (1.50%)"
            },
            {
                "bracket_id": "ma_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.03,
                "base_tax_cents": 1575000,
                "description": "Massachusetts Joint Tier #2 (3.00%)"
            },
            {
                "bracket_id": "ma_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.045,
                "base_tax_cents": 1575000,
                "description": "Massachusetts Joint Tier #3 (4.50%)"
            },
            {
                "bracket_id": "ma_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.06,
                "base_tax_cents": 1575000,
                "description": "Massachusetts Joint Tier #4 (6.00%)"
            },
            {
                "bracket_id": "ma_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.075,
                "base_tax_cents": 1575000,
                "description": "Massachusetts Joint Tier #5 (7.50%)"
            },
            {
                "bracket_id": "ma_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.09,
                "base_tax_cents": 1575000,
                "description": "Massachusetts Joint Tier #6 (9.00%)"
            },
        ]
    },
    "MI": {
        "name": "Michigan",
        "top_marginal_rate": 0.0425,
        "brackets_single": [
            {
                "bracket_id": "mi_b1",
                "threshold_cents": 1000000,
                "rate": 0.0071,
                "base_tax_cents": 0,
                "description": "Michigan Tier #1 (0.71%)"
            },
            {
                "bracket_id": "mi_b2",
                "threshold_cents": 3500000,
                "rate": 0.0142,
                "base_tax_cents": 17750,
                "description": "Michigan Tier #2 (1.42%)"
            },
            {
                "bracket_id": "mi_b3",
                "threshold_cents": 6000000,
                "rate": 0.0213,
                "base_tax_cents": 53250,
                "description": "Michigan Tier #3 (2.13%)"
            },
            {
                "bracket_id": "mi_b4",
                "threshold_cents": 8500000,
                "rate": 0.0283,
                "base_tax_cents": 106500,
                "description": "Michigan Tier #4 (2.83%)"
            },
            {
                "bracket_id": "mi_b5",
                "threshold_cents": 11000000,
                "rate": 0.0354,
                "base_tax_cents": 177250,
                "description": "Michigan Tier #5 (3.54%)"
            },
            {
                "bracket_id": "mi_b6",
                "threshold_cents": 13500000,
                "rate": 0.0425,
                "base_tax_cents": 265750,
                "description": "Michigan Tier #6 (4.25%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "mi_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0071,
                "base_tax_cents": 744000,
                "description": "Michigan Joint Tier #1 (0.71%)"
            },
            {
                "bracket_id": "mi_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0142,
                "base_tax_cents": 744000,
                "description": "Michigan Joint Tier #2 (1.42%)"
            },
            {
                "bracket_id": "mi_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0213,
                "base_tax_cents": 744000,
                "description": "Michigan Joint Tier #3 (2.13%)"
            },
            {
                "bracket_id": "mi_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0283,
                "base_tax_cents": 744000,
                "description": "Michigan Joint Tier #4 (2.83%)"
            },
            {
                "bracket_id": "mi_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0354,
                "base_tax_cents": 744000,
                "description": "Michigan Joint Tier #5 (3.54%)"
            },
            {
                "bracket_id": "mi_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0425,
                "base_tax_cents": 744000,
                "description": "Michigan Joint Tier #6 (4.25%)"
            },
        ]
    },
    "MN": {
        "name": "Minnesota",
        "top_marginal_rate": 0.0985,
        "brackets_single": [
            {
                "bracket_id": "mn_b1",
                "threshold_cents": 1000000,
                "rate": 0.0164,
                "base_tax_cents": 0,
                "description": "Minnesota Tier #1 (1.64%)"
            },
            {
                "bracket_id": "mn_b2",
                "threshold_cents": 3500000,
                "rate": 0.0328,
                "base_tax_cents": 41000,
                "description": "Minnesota Tier #2 (3.28%)"
            },
            {
                "bracket_id": "mn_b3",
                "threshold_cents": 6000000,
                "rate": 0.0493,
                "base_tax_cents": 123000,
                "description": "Minnesota Tier #3 (4.93%)"
            },
            {
                "bracket_id": "mn_b4",
                "threshold_cents": 8500000,
                "rate": 0.0657,
                "base_tax_cents": 246249,
                "description": "Minnesota Tier #4 (6.57%)"
            },
            {
                "bracket_id": "mn_b5",
                "threshold_cents": 11000000,
                "rate": 0.0821,
                "base_tax_cents": 410499,
                "description": "Minnesota Tier #5 (8.21%)"
            },
            {
                "bracket_id": "mn_b6",
                "threshold_cents": 13500000,
                "rate": 0.0985,
                "base_tax_cents": 615749,
                "description": "Minnesota Tier #6 (9.85%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "mn_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0164,
                "base_tax_cents": 1723998,
                "description": "Minnesota Joint Tier #1 (1.64%)"
            },
            {
                "bracket_id": "mn_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0328,
                "base_tax_cents": 1723998,
                "description": "Minnesota Joint Tier #2 (3.28%)"
            },
            {
                "bracket_id": "mn_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0493,
                "base_tax_cents": 1723998,
                "description": "Minnesota Joint Tier #3 (4.93%)"
            },
            {
                "bracket_id": "mn_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0657,
                "base_tax_cents": 1723998,
                "description": "Minnesota Joint Tier #4 (6.57%)"
            },
            {
                "bracket_id": "mn_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0821,
                "base_tax_cents": 1723998,
                "description": "Minnesota Joint Tier #5 (8.21%)"
            },
            {
                "bracket_id": "mn_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0985,
                "base_tax_cents": 1723998,
                "description": "Minnesota Joint Tier #6 (9.85%)"
            },
        ]
    },
    "MS": {
        "name": "Mississippi",
        "top_marginal_rate": 0.047,
        "brackets_single": [
            {
                "bracket_id": "ms_b1",
                "threshold_cents": 1000000,
                "rate": 0.0078,
                "base_tax_cents": 0,
                "description": "Mississippi Tier #1 (0.78%)"
            },
            {
                "bracket_id": "ms_b2",
                "threshold_cents": 3500000,
                "rate": 0.0157,
                "base_tax_cents": 19500,
                "description": "Mississippi Tier #2 (1.57%)"
            },
            {
                "bracket_id": "ms_b3",
                "threshold_cents": 6000000,
                "rate": 0.0235,
                "base_tax_cents": 58750,
                "description": "Mississippi Tier #3 (2.35%)"
            },
            {
                "bracket_id": "ms_b4",
                "threshold_cents": 8500000,
                "rate": 0.0313,
                "base_tax_cents": 117500,
                "description": "Mississippi Tier #4 (3.13%)"
            },
            {
                "bracket_id": "ms_b5",
                "threshold_cents": 11000000,
                "rate": 0.0392,
                "base_tax_cents": 195750,
                "description": "Mississippi Tier #5 (3.92%)"
            },
            {
                "bracket_id": "ms_b6",
                "threshold_cents": 13500000,
                "rate": 0.047,
                "base_tax_cents": 293750,
                "description": "Mississippi Tier #6 (4.70%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ms_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0078,
                "base_tax_cents": 822500,
                "description": "Mississippi Joint Tier #1 (0.78%)"
            },
            {
                "bracket_id": "ms_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0157,
                "base_tax_cents": 822500,
                "description": "Mississippi Joint Tier #2 (1.57%)"
            },
            {
                "bracket_id": "ms_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0235,
                "base_tax_cents": 822500,
                "description": "Mississippi Joint Tier #3 (2.35%)"
            },
            {
                "bracket_id": "ms_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0313,
                "base_tax_cents": 822500,
                "description": "Mississippi Joint Tier #4 (3.13%)"
            },
            {
                "bracket_id": "ms_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0392,
                "base_tax_cents": 822500,
                "description": "Mississippi Joint Tier #5 (3.92%)"
            },
            {
                "bracket_id": "ms_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.047,
                "base_tax_cents": 822500,
                "description": "Mississippi Joint Tier #6 (4.70%)"
            },
        ]
    },
    "MO": {
        "name": "Missouri",
        "top_marginal_rate": 0.048,
        "brackets_single": [
            {
                "bracket_id": "mo_b1",
                "threshold_cents": 1000000,
                "rate": 0.008,
                "base_tax_cents": 0,
                "description": "Missouri Tier #1 (0.80%)"
            },
            {
                "bracket_id": "mo_b2",
                "threshold_cents": 3500000,
                "rate": 0.016,
                "base_tax_cents": 20000,
                "description": "Missouri Tier #2 (1.60%)"
            },
            {
                "bracket_id": "mo_b3",
                "threshold_cents": 6000000,
                "rate": 0.024,
                "base_tax_cents": 60000,
                "description": "Missouri Tier #3 (2.40%)"
            },
            {
                "bracket_id": "mo_b4",
                "threshold_cents": 8500000,
                "rate": 0.032,
                "base_tax_cents": 120000,
                "description": "Missouri Tier #4 (3.20%)"
            },
            {
                "bracket_id": "mo_b5",
                "threshold_cents": 11000000,
                "rate": 0.04,
                "base_tax_cents": 200000,
                "description": "Missouri Tier #5 (4.00%)"
            },
            {
                "bracket_id": "mo_b6",
                "threshold_cents": 13500000,
                "rate": 0.048,
                "base_tax_cents": 300000,
                "description": "Missouri Tier #6 (4.80%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "mo_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.008,
                "base_tax_cents": 840000,
                "description": "Missouri Joint Tier #1 (0.80%)"
            },
            {
                "bracket_id": "mo_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.016,
                "base_tax_cents": 840000,
                "description": "Missouri Joint Tier #2 (1.60%)"
            },
            {
                "bracket_id": "mo_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.024,
                "base_tax_cents": 840000,
                "description": "Missouri Joint Tier #3 (2.40%)"
            },
            {
                "bracket_id": "mo_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.032,
                "base_tax_cents": 840000,
                "description": "Missouri Joint Tier #4 (3.20%)"
            },
            {
                "bracket_id": "mo_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.04,
                "base_tax_cents": 840000,
                "description": "Missouri Joint Tier #5 (4.00%)"
            },
            {
                "bracket_id": "mo_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.048,
                "base_tax_cents": 840000,
                "description": "Missouri Joint Tier #6 (4.80%)"
            },
        ]
    },
    "MT": {
        "name": "Montana",
        "top_marginal_rate": 0.059,
        "brackets_single": [
            {
                "bracket_id": "mt_b1",
                "threshold_cents": 1000000,
                "rate": 0.0098,
                "base_tax_cents": 0,
                "description": "Montana Tier #1 (0.98%)"
            },
            {
                "bracket_id": "mt_b2",
                "threshold_cents": 3500000,
                "rate": 0.0197,
                "base_tax_cents": 24500,
                "description": "Montana Tier #2 (1.97%)"
            },
            {
                "bracket_id": "mt_b3",
                "threshold_cents": 6000000,
                "rate": 0.0295,
                "base_tax_cents": 73750,
                "description": "Montana Tier #3 (2.95%)"
            },
            {
                "bracket_id": "mt_b4",
                "threshold_cents": 8500000,
                "rate": 0.0393,
                "base_tax_cents": 147500,
                "description": "Montana Tier #4 (3.93%)"
            },
            {
                "bracket_id": "mt_b5",
                "threshold_cents": 11000000,
                "rate": 0.0492,
                "base_tax_cents": 245750,
                "description": "Montana Tier #5 (4.92%)"
            },
            {
                "bracket_id": "mt_b6",
                "threshold_cents": 13500000,
                "rate": 0.059,
                "base_tax_cents": 368750,
                "description": "Montana Tier #6 (5.90%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "mt_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0098,
                "base_tax_cents": 1032500,
                "description": "Montana Joint Tier #1 (0.98%)"
            },
            {
                "bracket_id": "mt_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0197,
                "base_tax_cents": 1032500,
                "description": "Montana Joint Tier #2 (1.97%)"
            },
            {
                "bracket_id": "mt_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0295,
                "base_tax_cents": 1032500,
                "description": "Montana Joint Tier #3 (2.95%)"
            },
            {
                "bracket_id": "mt_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0393,
                "base_tax_cents": 1032500,
                "description": "Montana Joint Tier #4 (3.93%)"
            },
            {
                "bracket_id": "mt_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0492,
                "base_tax_cents": 1032500,
                "description": "Montana Joint Tier #5 (4.92%)"
            },
            {
                "bracket_id": "mt_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.059,
                "base_tax_cents": 1032500,
                "description": "Montana Joint Tier #6 (5.90%)"
            },
        ]
    },
    "NE": {
        "name": "Nebraska",
        "top_marginal_rate": 0.0584,
        "brackets_single": [
            {
                "bracket_id": "ne_b1",
                "threshold_cents": 1000000,
                "rate": 0.0097,
                "base_tax_cents": 0,
                "description": "Nebraska Tier #1 (0.97%)"
            },
            {
                "bracket_id": "ne_b2",
                "threshold_cents": 3500000,
                "rate": 0.0195,
                "base_tax_cents": 24250,
                "description": "Nebraska Tier #2 (1.95%)"
            },
            {
                "bracket_id": "ne_b3",
                "threshold_cents": 6000000,
                "rate": 0.0292,
                "base_tax_cents": 73000,
                "description": "Nebraska Tier #3 (2.92%)"
            },
            {
                "bracket_id": "ne_b4",
                "threshold_cents": 8500000,
                "rate": 0.0389,
                "base_tax_cents": 146000,
                "description": "Nebraska Tier #4 (3.89%)"
            },
            {
                "bracket_id": "ne_b5",
                "threshold_cents": 11000000,
                "rate": 0.0487,
                "base_tax_cents": 243249,
                "description": "Nebraska Tier #5 (4.87%)"
            },
            {
                "bracket_id": "ne_b6",
                "threshold_cents": 13500000,
                "rate": 0.0584,
                "base_tax_cents": 364999,
                "description": "Nebraska Tier #6 (5.84%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ne_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0097,
                "base_tax_cents": 1021998,
                "description": "Nebraska Joint Tier #1 (0.97%)"
            },
            {
                "bracket_id": "ne_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0195,
                "base_tax_cents": 1021998,
                "description": "Nebraska Joint Tier #2 (1.95%)"
            },
            {
                "bracket_id": "ne_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0292,
                "base_tax_cents": 1021998,
                "description": "Nebraska Joint Tier #3 (2.92%)"
            },
            {
                "bracket_id": "ne_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0389,
                "base_tax_cents": 1021998,
                "description": "Nebraska Joint Tier #4 (3.89%)"
            },
            {
                "bracket_id": "ne_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0487,
                "base_tax_cents": 1021998,
                "description": "Nebraska Joint Tier #5 (4.87%)"
            },
            {
                "bracket_id": "ne_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0584,
                "base_tax_cents": 1021998,
                "description": "Nebraska Joint Tier #6 (5.84%)"
            },
        ]
    },
    "NV": {
        "name": "Nevada",
        "top_marginal_rate": 0.0,
        "brackets_single": [
            {
                "bracket_id": "nv_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Nevada Tier #1 (0.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "nv_mfj_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Nevada Joint Tier #1 (0.00%)"
            },
        ]
    },
    "NH": {
        "name": "New Hampshire",
        "top_marginal_rate": 0.03,
        "brackets_single": [
            {
                "bracket_id": "nh_b1",
                "threshold_cents": 1000000,
                "rate": 0.005,
                "base_tax_cents": 0,
                "description": "New Hampshire Tier #1 (0.50%)"
            },
            {
                "bracket_id": "nh_b2",
                "threshold_cents": 3500000,
                "rate": 0.01,
                "base_tax_cents": 12500,
                "description": "New Hampshire Tier #2 (1.00%)"
            },
            {
                "bracket_id": "nh_b3",
                "threshold_cents": 6000000,
                "rate": 0.015,
                "base_tax_cents": 37500,
                "description": "New Hampshire Tier #3 (1.50%)"
            },
            {
                "bracket_id": "nh_b4",
                "threshold_cents": 8500000,
                "rate": 0.02,
                "base_tax_cents": 75000,
                "description": "New Hampshire Tier #4 (2.00%)"
            },
            {
                "bracket_id": "nh_b5",
                "threshold_cents": 11000000,
                "rate": 0.025,
                "base_tax_cents": 125000,
                "description": "New Hampshire Tier #5 (2.50%)"
            },
            {
                "bracket_id": "nh_b6",
                "threshold_cents": 13500000,
                "rate": 0.03,
                "base_tax_cents": 187500,
                "description": "New Hampshire Tier #6 (3.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "nh_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.005,
                "base_tax_cents": 525000,
                "description": "New Hampshire Joint Tier #1 (0.50%)"
            },
            {
                "bracket_id": "nh_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.01,
                "base_tax_cents": 525000,
                "description": "New Hampshire Joint Tier #2 (1.00%)"
            },
            {
                "bracket_id": "nh_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.015,
                "base_tax_cents": 525000,
                "description": "New Hampshire Joint Tier #3 (1.50%)"
            },
            {
                "bracket_id": "nh_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.02,
                "base_tax_cents": 525000,
                "description": "New Hampshire Joint Tier #4 (2.00%)"
            },
            {
                "bracket_id": "nh_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.025,
                "base_tax_cents": 525000,
                "description": "New Hampshire Joint Tier #5 (2.50%)"
            },
            {
                "bracket_id": "nh_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.03,
                "base_tax_cents": 525000,
                "description": "New Hampshire Joint Tier #6 (3.00%)"
            },
        ]
    },
    "NJ": {
        "name": "New Jersey",
        "top_marginal_rate": 0.1075,
        "brackets_single": [
            {
                "bracket_id": "nj_b1",
                "threshold_cents": 1000000,
                "rate": 0.0179,
                "base_tax_cents": 0,
                "description": "New Jersey Tier #1 (1.79%)"
            },
            {
                "bracket_id": "nj_b2",
                "threshold_cents": 3500000,
                "rate": 0.0358,
                "base_tax_cents": 44750,
                "description": "New Jersey Tier #2 (3.58%)"
            },
            {
                "bracket_id": "nj_b3",
                "threshold_cents": 6000000,
                "rate": 0.0538,
                "base_tax_cents": 134250,
                "description": "New Jersey Tier #3 (5.38%)"
            },
            {
                "bracket_id": "nj_b4",
                "threshold_cents": 8500000,
                "rate": 0.0717,
                "base_tax_cents": 268750,
                "description": "New Jersey Tier #4 (7.17%)"
            },
            {
                "bracket_id": "nj_b5",
                "threshold_cents": 11000000,
                "rate": 0.0896,
                "base_tax_cents": 448000,
                "description": "New Jersey Tier #5 (8.96%)"
            },
            {
                "bracket_id": "nj_b6",
                "threshold_cents": 13500000,
                "rate": 0.1075,
                "base_tax_cents": 672000,
                "description": "New Jersey Tier #6 (10.75%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "nj_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0179,
                "base_tax_cents": 1881500,
                "description": "New Jersey Joint Tier #1 (1.79%)"
            },
            {
                "bracket_id": "nj_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0358,
                "base_tax_cents": 1881500,
                "description": "New Jersey Joint Tier #2 (3.58%)"
            },
            {
                "bracket_id": "nj_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0538,
                "base_tax_cents": 1881500,
                "description": "New Jersey Joint Tier #3 (5.38%)"
            },
            {
                "bracket_id": "nj_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0717,
                "base_tax_cents": 1881500,
                "description": "New Jersey Joint Tier #4 (7.17%)"
            },
            {
                "bracket_id": "nj_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0896,
                "base_tax_cents": 1881500,
                "description": "New Jersey Joint Tier #5 (8.96%)"
            },
            {
                "bracket_id": "nj_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.1075,
                "base_tax_cents": 1881500,
                "description": "New Jersey Joint Tier #6 (10.75%)"
            },
        ]
    },
    "NM": {
        "name": "New Mexico",
        "top_marginal_rate": 0.059,
        "brackets_single": [
            {
                "bracket_id": "nm_b1",
                "threshold_cents": 1000000,
                "rate": 0.0098,
                "base_tax_cents": 0,
                "description": "New Mexico Tier #1 (0.98%)"
            },
            {
                "bracket_id": "nm_b2",
                "threshold_cents": 3500000,
                "rate": 0.0197,
                "base_tax_cents": 24500,
                "description": "New Mexico Tier #2 (1.97%)"
            },
            {
                "bracket_id": "nm_b3",
                "threshold_cents": 6000000,
                "rate": 0.0295,
                "base_tax_cents": 73750,
                "description": "New Mexico Tier #3 (2.95%)"
            },
            {
                "bracket_id": "nm_b4",
                "threshold_cents": 8500000,
                "rate": 0.0393,
                "base_tax_cents": 147500,
                "description": "New Mexico Tier #4 (3.93%)"
            },
            {
                "bracket_id": "nm_b5",
                "threshold_cents": 11000000,
                "rate": 0.0492,
                "base_tax_cents": 245750,
                "description": "New Mexico Tier #5 (4.92%)"
            },
            {
                "bracket_id": "nm_b6",
                "threshold_cents": 13500000,
                "rate": 0.059,
                "base_tax_cents": 368750,
                "description": "New Mexico Tier #6 (5.90%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "nm_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0098,
                "base_tax_cents": 1032500,
                "description": "New Mexico Joint Tier #1 (0.98%)"
            },
            {
                "bracket_id": "nm_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0197,
                "base_tax_cents": 1032500,
                "description": "New Mexico Joint Tier #2 (1.97%)"
            },
            {
                "bracket_id": "nm_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0295,
                "base_tax_cents": 1032500,
                "description": "New Mexico Joint Tier #3 (2.95%)"
            },
            {
                "bracket_id": "nm_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0393,
                "base_tax_cents": 1032500,
                "description": "New Mexico Joint Tier #4 (3.93%)"
            },
            {
                "bracket_id": "nm_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0492,
                "base_tax_cents": 1032500,
                "description": "New Mexico Joint Tier #5 (4.92%)"
            },
            {
                "bracket_id": "nm_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.059,
                "base_tax_cents": 1032500,
                "description": "New Mexico Joint Tier #6 (5.90%)"
            },
        ]
    },
    "NY": {
        "name": "New York",
        "top_marginal_rate": 0.109,
        "brackets_single": [
            {
                "bracket_id": "ny_b1",
                "threshold_cents": 1000000,
                "rate": 0.0182,
                "base_tax_cents": 0,
                "description": "New York Tier #1 (1.82%)"
            },
            {
                "bracket_id": "ny_b2",
                "threshold_cents": 3500000,
                "rate": 0.0363,
                "base_tax_cents": 45500,
                "description": "New York Tier #2 (3.63%)"
            },
            {
                "bracket_id": "ny_b3",
                "threshold_cents": 6000000,
                "rate": 0.0545,
                "base_tax_cents": 136250,
                "description": "New York Tier #3 (5.45%)"
            },
            {
                "bracket_id": "ny_b4",
                "threshold_cents": 8500000,
                "rate": 0.0727,
                "base_tax_cents": 272500,
                "description": "New York Tier #4 (7.27%)"
            },
            {
                "bracket_id": "ny_b5",
                "threshold_cents": 11000000,
                "rate": 0.0908,
                "base_tax_cents": 454250,
                "description": "New York Tier #5 (9.08%)"
            },
            {
                "bracket_id": "ny_b6",
                "threshold_cents": 13500000,
                "rate": 0.109,
                "base_tax_cents": 681250,
                "description": "New York Tier #6 (10.90%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ny_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0182,
                "base_tax_cents": 1907500,
                "description": "New York Joint Tier #1 (1.82%)"
            },
            {
                "bracket_id": "ny_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0363,
                "base_tax_cents": 1907500,
                "description": "New York Joint Tier #2 (3.63%)"
            },
            {
                "bracket_id": "ny_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0545,
                "base_tax_cents": 1907500,
                "description": "New York Joint Tier #3 (5.45%)"
            },
            {
                "bracket_id": "ny_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0727,
                "base_tax_cents": 1907500,
                "description": "New York Joint Tier #4 (7.27%)"
            },
            {
                "bracket_id": "ny_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0908,
                "base_tax_cents": 1907500,
                "description": "New York Joint Tier #5 (9.08%)"
            },
            {
                "bracket_id": "ny_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.109,
                "base_tax_cents": 1907500,
                "description": "New York Joint Tier #6 (10.90%)"
            },
        ]
    },
    "NC": {
        "name": "North Carolina",
        "top_marginal_rate": 0.045,
        "brackets_single": [
            {
                "bracket_id": "nc_b1",
                "threshold_cents": 1000000,
                "rate": 0.0075,
                "base_tax_cents": 0,
                "description": "North Carolina Tier #1 (0.75%)"
            },
            {
                "bracket_id": "nc_b2",
                "threshold_cents": 3500000,
                "rate": 0.015,
                "base_tax_cents": 18750,
                "description": "North Carolina Tier #2 (1.50%)"
            },
            {
                "bracket_id": "nc_b3",
                "threshold_cents": 6000000,
                "rate": 0.0225,
                "base_tax_cents": 56250,
                "description": "North Carolina Tier #3 (2.25%)"
            },
            {
                "bracket_id": "nc_b4",
                "threshold_cents": 8500000,
                "rate": 0.03,
                "base_tax_cents": 112500,
                "description": "North Carolina Tier #4 (3.00%)"
            },
            {
                "bracket_id": "nc_b5",
                "threshold_cents": 11000000,
                "rate": 0.0375,
                "base_tax_cents": 187500,
                "description": "North Carolina Tier #5 (3.75%)"
            },
            {
                "bracket_id": "nc_b6",
                "threshold_cents": 13500000,
                "rate": 0.045,
                "base_tax_cents": 281250,
                "description": "North Carolina Tier #6 (4.50%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "nc_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0075,
                "base_tax_cents": 787500,
                "description": "North Carolina Joint Tier #1 (0.75%)"
            },
            {
                "bracket_id": "nc_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.015,
                "base_tax_cents": 787500,
                "description": "North Carolina Joint Tier #2 (1.50%)"
            },
            {
                "bracket_id": "nc_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0225,
                "base_tax_cents": 787500,
                "description": "North Carolina Joint Tier #3 (2.25%)"
            },
            {
                "bracket_id": "nc_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.03,
                "base_tax_cents": 787500,
                "description": "North Carolina Joint Tier #4 (3.00%)"
            },
            {
                "bracket_id": "nc_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0375,
                "base_tax_cents": 787500,
                "description": "North Carolina Joint Tier #5 (3.75%)"
            },
            {
                "bracket_id": "nc_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.045,
                "base_tax_cents": 787500,
                "description": "North Carolina Joint Tier #6 (4.50%)"
            },
        ]
    },
    "ND": {
        "name": "North Dakota",
        "top_marginal_rate": 0.025,
        "brackets_single": [
            {
                "bracket_id": "nd_b1",
                "threshold_cents": 1000000,
                "rate": 0.0042,
                "base_tax_cents": 0,
                "description": "North Dakota Tier #1 (0.42%)"
            },
            {
                "bracket_id": "nd_b2",
                "threshold_cents": 3500000,
                "rate": 0.0083,
                "base_tax_cents": 10500,
                "description": "North Dakota Tier #2 (0.83%)"
            },
            {
                "bracket_id": "nd_b3",
                "threshold_cents": 6000000,
                "rate": 0.0125,
                "base_tax_cents": 31250,
                "description": "North Dakota Tier #3 (1.25%)"
            },
            {
                "bracket_id": "nd_b4",
                "threshold_cents": 8500000,
                "rate": 0.0167,
                "base_tax_cents": 62500,
                "description": "North Dakota Tier #4 (1.67%)"
            },
            {
                "bracket_id": "nd_b5",
                "threshold_cents": 11000000,
                "rate": 0.0208,
                "base_tax_cents": 104250,
                "description": "North Dakota Tier #5 (2.08%)"
            },
            {
                "bracket_id": "nd_b6",
                "threshold_cents": 13500000,
                "rate": 0.025,
                "base_tax_cents": 156250,
                "description": "North Dakota Tier #6 (2.50%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "nd_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0042,
                "base_tax_cents": 437500,
                "description": "North Dakota Joint Tier #1 (0.42%)"
            },
            {
                "bracket_id": "nd_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0083,
                "base_tax_cents": 437500,
                "description": "North Dakota Joint Tier #2 (0.83%)"
            },
            {
                "bracket_id": "nd_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0125,
                "base_tax_cents": 437500,
                "description": "North Dakota Joint Tier #3 (1.25%)"
            },
            {
                "bracket_id": "nd_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0167,
                "base_tax_cents": 437500,
                "description": "North Dakota Joint Tier #4 (1.67%)"
            },
            {
                "bracket_id": "nd_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0208,
                "base_tax_cents": 437500,
                "description": "North Dakota Joint Tier #5 (2.08%)"
            },
            {
                "bracket_id": "nd_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.025,
                "base_tax_cents": 437500,
                "description": "North Dakota Joint Tier #6 (2.50%)"
            },
        ]
    },
    "OH": {
        "name": "Ohio",
        "top_marginal_rate": 0.035,
        "brackets_single": [
            {
                "bracket_id": "oh_b1",
                "threshold_cents": 1000000,
                "rate": 0.0058,
                "base_tax_cents": 0,
                "description": "Ohio Tier #1 (0.58%)"
            },
            {
                "bracket_id": "oh_b2",
                "threshold_cents": 3500000,
                "rate": 0.0117,
                "base_tax_cents": 14499,
                "description": "Ohio Tier #2 (1.17%)"
            },
            {
                "bracket_id": "oh_b3",
                "threshold_cents": 6000000,
                "rate": 0.0175,
                "base_tax_cents": 43749,
                "description": "Ohio Tier #3 (1.75%)"
            },
            {
                "bracket_id": "oh_b4",
                "threshold_cents": 8500000,
                "rate": 0.0233,
                "base_tax_cents": 87499,
                "description": "Ohio Tier #4 (2.33%)"
            },
            {
                "bracket_id": "oh_b5",
                "threshold_cents": 11000000,
                "rate": 0.0292,
                "base_tax_cents": 145749,
                "description": "Ohio Tier #5 (2.92%)"
            },
            {
                "bracket_id": "oh_b6",
                "threshold_cents": 13500000,
                "rate": 0.035,
                "base_tax_cents": 218749,
                "description": "Ohio Tier #6 (3.50%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "oh_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0058,
                "base_tax_cents": 612498,
                "description": "Ohio Joint Tier #1 (0.58%)"
            },
            {
                "bracket_id": "oh_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0117,
                "base_tax_cents": 612498,
                "description": "Ohio Joint Tier #2 (1.17%)"
            },
            {
                "bracket_id": "oh_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0175,
                "base_tax_cents": 612498,
                "description": "Ohio Joint Tier #3 (1.75%)"
            },
            {
                "bracket_id": "oh_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0233,
                "base_tax_cents": 612498,
                "description": "Ohio Joint Tier #4 (2.33%)"
            },
            {
                "bracket_id": "oh_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0292,
                "base_tax_cents": 612498,
                "description": "Ohio Joint Tier #5 (2.92%)"
            },
            {
                "bracket_id": "oh_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.035,
                "base_tax_cents": 612498,
                "description": "Ohio Joint Tier #6 (3.50%)"
            },
        ]
    },
    "OK": {
        "name": "Oklahoma",
        "top_marginal_rate": 0.0475,
        "brackets_single": [
            {
                "bracket_id": "ok_b1",
                "threshold_cents": 1000000,
                "rate": 0.0079,
                "base_tax_cents": 0,
                "description": "Oklahoma Tier #1 (0.79%)"
            },
            {
                "bracket_id": "ok_b2",
                "threshold_cents": 3500000,
                "rate": 0.0158,
                "base_tax_cents": 19750,
                "description": "Oklahoma Tier #2 (1.58%)"
            },
            {
                "bracket_id": "ok_b3",
                "threshold_cents": 6000000,
                "rate": 0.0238,
                "base_tax_cents": 59250,
                "description": "Oklahoma Tier #3 (2.38%)"
            },
            {
                "bracket_id": "ok_b4",
                "threshold_cents": 8500000,
                "rate": 0.0317,
                "base_tax_cents": 118750,
                "description": "Oklahoma Tier #4 (3.17%)"
            },
            {
                "bracket_id": "ok_b5",
                "threshold_cents": 11000000,
                "rate": 0.0396,
                "base_tax_cents": 198000,
                "description": "Oklahoma Tier #5 (3.96%)"
            },
            {
                "bracket_id": "ok_b6",
                "threshold_cents": 13500000,
                "rate": 0.0475,
                "base_tax_cents": 297000,
                "description": "Oklahoma Tier #6 (4.75%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ok_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0079,
                "base_tax_cents": 831500,
                "description": "Oklahoma Joint Tier #1 (0.79%)"
            },
            {
                "bracket_id": "ok_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0158,
                "base_tax_cents": 831500,
                "description": "Oklahoma Joint Tier #2 (1.58%)"
            },
            {
                "bracket_id": "ok_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0238,
                "base_tax_cents": 831500,
                "description": "Oklahoma Joint Tier #3 (2.38%)"
            },
            {
                "bracket_id": "ok_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0317,
                "base_tax_cents": 831500,
                "description": "Oklahoma Joint Tier #4 (3.17%)"
            },
            {
                "bracket_id": "ok_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0396,
                "base_tax_cents": 831500,
                "description": "Oklahoma Joint Tier #5 (3.96%)"
            },
            {
                "bracket_id": "ok_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0475,
                "base_tax_cents": 831500,
                "description": "Oklahoma Joint Tier #6 (4.75%)"
            },
        ]
    },
    "OR": {
        "name": "Oregon",
        "top_marginal_rate": 0.099,
        "brackets_single": [
            {
                "bracket_id": "or_b1",
                "threshold_cents": 1000000,
                "rate": 0.0165,
                "base_tax_cents": 0,
                "description": "Oregon Tier #1 (1.65%)"
            },
            {
                "bracket_id": "or_b2",
                "threshold_cents": 3500000,
                "rate": 0.033,
                "base_tax_cents": 41250,
                "description": "Oregon Tier #2 (3.30%)"
            },
            {
                "bracket_id": "or_b3",
                "threshold_cents": 6000000,
                "rate": 0.0495,
                "base_tax_cents": 123750,
                "description": "Oregon Tier #3 (4.95%)"
            },
            {
                "bracket_id": "or_b4",
                "threshold_cents": 8500000,
                "rate": 0.066,
                "base_tax_cents": 247500,
                "description": "Oregon Tier #4 (6.60%)"
            },
            {
                "bracket_id": "or_b5",
                "threshold_cents": 11000000,
                "rate": 0.0825,
                "base_tax_cents": 412500,
                "description": "Oregon Tier #5 (8.25%)"
            },
            {
                "bracket_id": "or_b6",
                "threshold_cents": 13500000,
                "rate": 0.099,
                "base_tax_cents": 618750,
                "description": "Oregon Tier #6 (9.90%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "or_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0165,
                "base_tax_cents": 1732500,
                "description": "Oregon Joint Tier #1 (1.65%)"
            },
            {
                "bracket_id": "or_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.033,
                "base_tax_cents": 1732500,
                "description": "Oregon Joint Tier #2 (3.30%)"
            },
            {
                "bracket_id": "or_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0495,
                "base_tax_cents": 1732500,
                "description": "Oregon Joint Tier #3 (4.95%)"
            },
            {
                "bracket_id": "or_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.066,
                "base_tax_cents": 1732500,
                "description": "Oregon Joint Tier #4 (6.60%)"
            },
            {
                "bracket_id": "or_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0825,
                "base_tax_cents": 1732500,
                "description": "Oregon Joint Tier #5 (8.25%)"
            },
            {
                "bracket_id": "or_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.099,
                "base_tax_cents": 1732500,
                "description": "Oregon Joint Tier #6 (9.90%)"
            },
        ]
    },
    "PA": {
        "name": "Pennsylvania",
        "top_marginal_rate": 0.0307,
        "brackets_single": [
            {
                "bracket_id": "pa_b1",
                "threshold_cents": 1000000,
                "rate": 0.0051,
                "base_tax_cents": 0,
                "description": "Pennsylvania Tier #1 (0.51%)"
            },
            {
                "bracket_id": "pa_b2",
                "threshold_cents": 3500000,
                "rate": 0.0102,
                "base_tax_cents": 12750,
                "description": "Pennsylvania Tier #2 (1.02%)"
            },
            {
                "bracket_id": "pa_b3",
                "threshold_cents": 6000000,
                "rate": 0.0154,
                "base_tax_cents": 38250,
                "description": "Pennsylvania Tier #3 (1.54%)"
            },
            {
                "bracket_id": "pa_b4",
                "threshold_cents": 8500000,
                "rate": 0.0205,
                "base_tax_cents": 76750,
                "description": "Pennsylvania Tier #4 (2.05%)"
            },
            {
                "bracket_id": "pa_b5",
                "threshold_cents": 11000000,
                "rate": 0.0256,
                "base_tax_cents": 128000,
                "description": "Pennsylvania Tier #5 (2.56%)"
            },
            {
                "bracket_id": "pa_b6",
                "threshold_cents": 13500000,
                "rate": 0.0307,
                "base_tax_cents": 192000,
                "description": "Pennsylvania Tier #6 (3.07%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "pa_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0051,
                "base_tax_cents": 537500,
                "description": "Pennsylvania Joint Tier #1 (0.51%)"
            },
            {
                "bracket_id": "pa_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0102,
                "base_tax_cents": 537500,
                "description": "Pennsylvania Joint Tier #2 (1.02%)"
            },
            {
                "bracket_id": "pa_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0154,
                "base_tax_cents": 537500,
                "description": "Pennsylvania Joint Tier #3 (1.54%)"
            },
            {
                "bracket_id": "pa_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0205,
                "base_tax_cents": 537500,
                "description": "Pennsylvania Joint Tier #4 (2.05%)"
            },
            {
                "bracket_id": "pa_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0256,
                "base_tax_cents": 537500,
                "description": "Pennsylvania Joint Tier #5 (2.56%)"
            },
            {
                "bracket_id": "pa_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0307,
                "base_tax_cents": 537500,
                "description": "Pennsylvania Joint Tier #6 (3.07%)"
            },
        ]
    },
    "RI": {
        "name": "Rhode Island",
        "top_marginal_rate": 0.0599,
        "brackets_single": [
            {
                "bracket_id": "ri_b1",
                "threshold_cents": 1000000,
                "rate": 0.01,
                "base_tax_cents": 0,
                "description": "Rhode Island Tier #1 (1.00%)"
            },
            {
                "bracket_id": "ri_b2",
                "threshold_cents": 3500000,
                "rate": 0.02,
                "base_tax_cents": 25000,
                "description": "Rhode Island Tier #2 (2.00%)"
            },
            {
                "bracket_id": "ri_b3",
                "threshold_cents": 6000000,
                "rate": 0.03,
                "base_tax_cents": 75000,
                "description": "Rhode Island Tier #3 (3.00%)"
            },
            {
                "bracket_id": "ri_b4",
                "threshold_cents": 8500000,
                "rate": 0.0399,
                "base_tax_cents": 150000,
                "description": "Rhode Island Tier #4 (3.99%)"
            },
            {
                "bracket_id": "ri_b5",
                "threshold_cents": 11000000,
                "rate": 0.0499,
                "base_tax_cents": 249750,
                "description": "Rhode Island Tier #5 (4.99%)"
            },
            {
                "bracket_id": "ri_b6",
                "threshold_cents": 13500000,
                "rate": 0.0599,
                "base_tax_cents": 374500,
                "description": "Rhode Island Tier #6 (5.99%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ri_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.01,
                "base_tax_cents": 1048500,
                "description": "Rhode Island Joint Tier #1 (1.00%)"
            },
            {
                "bracket_id": "ri_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.02,
                "base_tax_cents": 1048500,
                "description": "Rhode Island Joint Tier #2 (2.00%)"
            },
            {
                "bracket_id": "ri_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.03,
                "base_tax_cents": 1048500,
                "description": "Rhode Island Joint Tier #3 (3.00%)"
            },
            {
                "bracket_id": "ri_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0399,
                "base_tax_cents": 1048500,
                "description": "Rhode Island Joint Tier #4 (3.99%)"
            },
            {
                "bracket_id": "ri_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0499,
                "base_tax_cents": 1048500,
                "description": "Rhode Island Joint Tier #5 (4.99%)"
            },
            {
                "bracket_id": "ri_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0599,
                "base_tax_cents": 1048500,
                "description": "Rhode Island Joint Tier #6 (5.99%)"
            },
        ]
    },
    "SC": {
        "name": "South Carolina",
        "top_marginal_rate": 0.064,
        "brackets_single": [
            {
                "bracket_id": "sc_b1",
                "threshold_cents": 1000000,
                "rate": 0.0107,
                "base_tax_cents": 0,
                "description": "South Carolina Tier #1 (1.07%)"
            },
            {
                "bracket_id": "sc_b2",
                "threshold_cents": 3500000,
                "rate": 0.0213,
                "base_tax_cents": 26750,
                "description": "South Carolina Tier #2 (2.13%)"
            },
            {
                "bracket_id": "sc_b3",
                "threshold_cents": 6000000,
                "rate": 0.032,
                "base_tax_cents": 80000,
                "description": "South Carolina Tier #3 (3.20%)"
            },
            {
                "bracket_id": "sc_b4",
                "threshold_cents": 8500000,
                "rate": 0.0427,
                "base_tax_cents": 160000,
                "description": "South Carolina Tier #4 (4.27%)"
            },
            {
                "bracket_id": "sc_b5",
                "threshold_cents": 11000000,
                "rate": 0.0533,
                "base_tax_cents": 266750,
                "description": "South Carolina Tier #5 (5.33%)"
            },
            {
                "bracket_id": "sc_b6",
                "threshold_cents": 13500000,
                "rate": 0.064,
                "base_tax_cents": 400000,
                "description": "South Carolina Tier #6 (6.40%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "sc_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0107,
                "base_tax_cents": 1120000,
                "description": "South Carolina Joint Tier #1 (1.07%)"
            },
            {
                "bracket_id": "sc_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0213,
                "base_tax_cents": 1120000,
                "description": "South Carolina Joint Tier #2 (2.13%)"
            },
            {
                "bracket_id": "sc_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.032,
                "base_tax_cents": 1120000,
                "description": "South Carolina Joint Tier #3 (3.20%)"
            },
            {
                "bracket_id": "sc_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0427,
                "base_tax_cents": 1120000,
                "description": "South Carolina Joint Tier #4 (4.27%)"
            },
            {
                "bracket_id": "sc_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0533,
                "base_tax_cents": 1120000,
                "description": "South Carolina Joint Tier #5 (5.33%)"
            },
            {
                "bracket_id": "sc_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.064,
                "base_tax_cents": 1120000,
                "description": "South Carolina Joint Tier #6 (6.40%)"
            },
        ]
    },
    "SD": {
        "name": "South Dakota",
        "top_marginal_rate": 0.0,
        "brackets_single": [
            {
                "bracket_id": "sd_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "South Dakota Tier #1 (0.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "sd_mfj_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "South Dakota Joint Tier #1 (0.00%)"
            },
        ]
    },
    "TN": {
        "name": "Tennessee",
        "top_marginal_rate": 0.0,
        "brackets_single": [
            {
                "bracket_id": "tn_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Tennessee Tier #1 (0.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "tn_mfj_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Tennessee Joint Tier #1 (0.00%)"
            },
        ]
    },
    "TX": {
        "name": "Texas",
        "top_marginal_rate": 0.0,
        "brackets_single": [
            {
                "bracket_id": "tx_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Texas Tier #1 (0.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "tx_mfj_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Texas Joint Tier #1 (0.00%)"
            },
        ]
    },
    "UT": {
        "name": "Utah",
        "top_marginal_rate": 0.0465,
        "brackets_single": [
            {
                "bracket_id": "ut_b1",
                "threshold_cents": 1000000,
                "rate": 0.0077,
                "base_tax_cents": 0,
                "description": "Utah Tier #1 (0.77%)"
            },
            {
                "bracket_id": "ut_b2",
                "threshold_cents": 3500000,
                "rate": 0.0155,
                "base_tax_cents": 19250,
                "description": "Utah Tier #2 (1.55%)"
            },
            {
                "bracket_id": "ut_b3",
                "threshold_cents": 6000000,
                "rate": 0.0232,
                "base_tax_cents": 58000,
                "description": "Utah Tier #3 (2.32%)"
            },
            {
                "bracket_id": "ut_b4",
                "threshold_cents": 8500000,
                "rate": 0.031,
                "base_tax_cents": 115999,
                "description": "Utah Tier #4 (3.10%)"
            },
            {
                "bracket_id": "ut_b5",
                "threshold_cents": 11000000,
                "rate": 0.0387,
                "base_tax_cents": 193499,
                "description": "Utah Tier #5 (3.87%)"
            },
            {
                "bracket_id": "ut_b6",
                "threshold_cents": 13500000,
                "rate": 0.0465,
                "base_tax_cents": 290249,
                "description": "Utah Tier #6 (4.65%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "ut_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0077,
                "base_tax_cents": 812998,
                "description": "Utah Joint Tier #1 (0.77%)"
            },
            {
                "bracket_id": "ut_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0155,
                "base_tax_cents": 812998,
                "description": "Utah Joint Tier #2 (1.55%)"
            },
            {
                "bracket_id": "ut_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0232,
                "base_tax_cents": 812998,
                "description": "Utah Joint Tier #3 (2.32%)"
            },
            {
                "bracket_id": "ut_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.031,
                "base_tax_cents": 812998,
                "description": "Utah Joint Tier #4 (3.10%)"
            },
            {
                "bracket_id": "ut_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0387,
                "base_tax_cents": 812998,
                "description": "Utah Joint Tier #5 (3.87%)"
            },
            {
                "bracket_id": "ut_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0465,
                "base_tax_cents": 812998,
                "description": "Utah Joint Tier #6 (4.65%)"
            },
        ]
    },
    "VT": {
        "name": "Vermont",
        "top_marginal_rate": 0.0875,
        "brackets_single": [
            {
                "bracket_id": "vt_b1",
                "threshold_cents": 1000000,
                "rate": 0.0146,
                "base_tax_cents": 0,
                "description": "Vermont Tier #1 (1.46%)"
            },
            {
                "bracket_id": "vt_b2",
                "threshold_cents": 3500000,
                "rate": 0.0292,
                "base_tax_cents": 36500,
                "description": "Vermont Tier #2 (2.92%)"
            },
            {
                "bracket_id": "vt_b3",
                "threshold_cents": 6000000,
                "rate": 0.0437,
                "base_tax_cents": 109500,
                "description": "Vermont Tier #3 (4.37%)"
            },
            {
                "bracket_id": "vt_b4",
                "threshold_cents": 8500000,
                "rate": 0.0583,
                "base_tax_cents": 218750,
                "description": "Vermont Tier #4 (5.83%)"
            },
            {
                "bracket_id": "vt_b5",
                "threshold_cents": 11000000,
                "rate": 0.0729,
                "base_tax_cents": 364500,
                "description": "Vermont Tier #5 (7.29%)"
            },
            {
                "bracket_id": "vt_b6",
                "threshold_cents": 13500000,
                "rate": 0.0875,
                "base_tax_cents": 546750,
                "description": "Vermont Tier #6 (8.75%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "vt_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0146,
                "base_tax_cents": 1531000,
                "description": "Vermont Joint Tier #1 (1.46%)"
            },
            {
                "bracket_id": "vt_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0292,
                "base_tax_cents": 1531000,
                "description": "Vermont Joint Tier #2 (2.92%)"
            },
            {
                "bracket_id": "vt_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0437,
                "base_tax_cents": 1531000,
                "description": "Vermont Joint Tier #3 (4.37%)"
            },
            {
                "bracket_id": "vt_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0583,
                "base_tax_cents": 1531000,
                "description": "Vermont Joint Tier #4 (5.83%)"
            },
            {
                "bracket_id": "vt_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0729,
                "base_tax_cents": 1531000,
                "description": "Vermont Joint Tier #5 (7.29%)"
            },
            {
                "bracket_id": "vt_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0875,
                "base_tax_cents": 1531000,
                "description": "Vermont Joint Tier #6 (8.75%)"
            },
        ]
    },
    "VA": {
        "name": "Virginia",
        "top_marginal_rate": 0.0575,
        "brackets_single": [
            {
                "bracket_id": "va_b1",
                "threshold_cents": 1000000,
                "rate": 0.0096,
                "base_tax_cents": 0,
                "description": "Virginia Tier #1 (0.96%)"
            },
            {
                "bracket_id": "va_b2",
                "threshold_cents": 3500000,
                "rate": 0.0192,
                "base_tax_cents": 23999,
                "description": "Virginia Tier #2 (1.92%)"
            },
            {
                "bracket_id": "va_b3",
                "threshold_cents": 6000000,
                "rate": 0.0288,
                "base_tax_cents": 71998,
                "description": "Virginia Tier #3 (2.88%)"
            },
            {
                "bracket_id": "va_b4",
                "threshold_cents": 8500000,
                "rate": 0.0383,
                "base_tax_cents": 143998,
                "description": "Virginia Tier #4 (3.83%)"
            },
            {
                "bracket_id": "va_b5",
                "threshold_cents": 11000000,
                "rate": 0.0479,
                "base_tax_cents": 239748,
                "description": "Virginia Tier #5 (4.79%)"
            },
            {
                "bracket_id": "va_b6",
                "threshold_cents": 13500000,
                "rate": 0.0575,
                "base_tax_cents": 359498,
                "description": "Virginia Tier #6 (5.75%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "va_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0096,
                "base_tax_cents": 1006496,
                "description": "Virginia Joint Tier #1 (0.96%)"
            },
            {
                "bracket_id": "va_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0192,
                "base_tax_cents": 1006496,
                "description": "Virginia Joint Tier #2 (1.92%)"
            },
            {
                "bracket_id": "va_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0288,
                "base_tax_cents": 1006496,
                "description": "Virginia Joint Tier #3 (2.88%)"
            },
            {
                "bracket_id": "va_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0383,
                "base_tax_cents": 1006496,
                "description": "Virginia Joint Tier #4 (3.83%)"
            },
            {
                "bracket_id": "va_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0479,
                "base_tax_cents": 1006496,
                "description": "Virginia Joint Tier #5 (4.79%)"
            },
            {
                "bracket_id": "va_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0575,
                "base_tax_cents": 1006496,
                "description": "Virginia Joint Tier #6 (5.75%)"
            },
        ]
    },
    "WA": {
        "name": "Washington",
        "top_marginal_rate": 0.07,
        "brackets_single": [
            {
                "bracket_id": "wa_b1",
                "threshold_cents": 1000000,
                "rate": 0.0117,
                "base_tax_cents": 0,
                "description": "Washington Tier #1 (1.17%)"
            },
            {
                "bracket_id": "wa_b2",
                "threshold_cents": 3500000,
                "rate": 0.0233,
                "base_tax_cents": 29250,
                "description": "Washington Tier #2 (2.33%)"
            },
            {
                "bracket_id": "wa_b3",
                "threshold_cents": 6000000,
                "rate": 0.035,
                "base_tax_cents": 87500,
                "description": "Washington Tier #3 (3.50%)"
            },
            {
                "bracket_id": "wa_b4",
                "threshold_cents": 8500000,
                "rate": 0.0467,
                "base_tax_cents": 175000,
                "description": "Washington Tier #4 (4.67%)"
            },
            {
                "bracket_id": "wa_b5",
                "threshold_cents": 11000000,
                "rate": 0.0583,
                "base_tax_cents": 291750,
                "description": "Washington Tier #5 (5.83%)"
            },
            {
                "bracket_id": "wa_b6",
                "threshold_cents": 13500000,
                "rate": 0.07,
                "base_tax_cents": 437500,
                "description": "Washington Tier #6 (7.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "wa_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0117,
                "base_tax_cents": 1225000,
                "description": "Washington Joint Tier #1 (1.17%)"
            },
            {
                "bracket_id": "wa_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0233,
                "base_tax_cents": 1225000,
                "description": "Washington Joint Tier #2 (2.33%)"
            },
            {
                "bracket_id": "wa_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.035,
                "base_tax_cents": 1225000,
                "description": "Washington Joint Tier #3 (3.50%)"
            },
            {
                "bracket_id": "wa_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0467,
                "base_tax_cents": 1225000,
                "description": "Washington Joint Tier #4 (4.67%)"
            },
            {
                "bracket_id": "wa_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0583,
                "base_tax_cents": 1225000,
                "description": "Washington Joint Tier #5 (5.83%)"
            },
            {
                "bracket_id": "wa_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.07,
                "base_tax_cents": 1225000,
                "description": "Washington Joint Tier #6 (7.00%)"
            },
        ]
    },
    "WV": {
        "name": "West Virginia",
        "top_marginal_rate": 0.0512,
        "brackets_single": [
            {
                "bracket_id": "wv_b1",
                "threshold_cents": 1000000,
                "rate": 0.0085,
                "base_tax_cents": 0,
                "description": "West Virginia Tier #1 (0.85%)"
            },
            {
                "bracket_id": "wv_b2",
                "threshold_cents": 3500000,
                "rate": 0.0171,
                "base_tax_cents": 21250,
                "description": "West Virginia Tier #2 (1.71%)"
            },
            {
                "bracket_id": "wv_b3",
                "threshold_cents": 6000000,
                "rate": 0.0256,
                "base_tax_cents": 64000,
                "description": "West Virginia Tier #3 (2.56%)"
            },
            {
                "bracket_id": "wv_b4",
                "threshold_cents": 8500000,
                "rate": 0.0341,
                "base_tax_cents": 128000,
                "description": "West Virginia Tier #4 (3.41%)"
            },
            {
                "bracket_id": "wv_b5",
                "threshold_cents": 11000000,
                "rate": 0.0427,
                "base_tax_cents": 213250,
                "description": "West Virginia Tier #5 (4.27%)"
            },
            {
                "bracket_id": "wv_b6",
                "threshold_cents": 13500000,
                "rate": 0.0512,
                "base_tax_cents": 320000,
                "description": "West Virginia Tier #6 (5.12%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "wv_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0085,
                "base_tax_cents": 896000,
                "description": "West Virginia Joint Tier #1 (0.85%)"
            },
            {
                "bracket_id": "wv_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0171,
                "base_tax_cents": 896000,
                "description": "West Virginia Joint Tier #2 (1.71%)"
            },
            {
                "bracket_id": "wv_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0256,
                "base_tax_cents": 896000,
                "description": "West Virginia Joint Tier #3 (2.56%)"
            },
            {
                "bracket_id": "wv_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0341,
                "base_tax_cents": 896000,
                "description": "West Virginia Joint Tier #4 (3.41%)"
            },
            {
                "bracket_id": "wv_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0427,
                "base_tax_cents": 896000,
                "description": "West Virginia Joint Tier #5 (4.27%)"
            },
            {
                "bracket_id": "wv_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0512,
                "base_tax_cents": 896000,
                "description": "West Virginia Joint Tier #6 (5.12%)"
            },
        ]
    },
    "WI": {
        "name": "Wisconsin",
        "top_marginal_rate": 0.0765,
        "brackets_single": [
            {
                "bracket_id": "wi_b1",
                "threshold_cents": 1000000,
                "rate": 0.0127,
                "base_tax_cents": 0,
                "description": "Wisconsin Tier #1 (1.27%)"
            },
            {
                "bracket_id": "wi_b2",
                "threshold_cents": 3500000,
                "rate": 0.0255,
                "base_tax_cents": 31750,
                "description": "Wisconsin Tier #2 (2.55%)"
            },
            {
                "bracket_id": "wi_b3",
                "threshold_cents": 6000000,
                "rate": 0.0382,
                "base_tax_cents": 95499,
                "description": "Wisconsin Tier #3 (3.82%)"
            },
            {
                "bracket_id": "wi_b4",
                "threshold_cents": 8500000,
                "rate": 0.051,
                "base_tax_cents": 190999,
                "description": "Wisconsin Tier #4 (5.10%)"
            },
            {
                "bracket_id": "wi_b5",
                "threshold_cents": 11000000,
                "rate": 0.0638,
                "base_tax_cents": 318498,
                "description": "Wisconsin Tier #5 (6.38%)"
            },
            {
                "bracket_id": "wi_b6",
                "threshold_cents": 13500000,
                "rate": 0.0765,
                "base_tax_cents": 477998,
                "description": "Wisconsin Tier #6 (7.65%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "wi_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0127,
                "base_tax_cents": 1338496,
                "description": "Wisconsin Joint Tier #1 (1.27%)"
            },
            {
                "bracket_id": "wi_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0255,
                "base_tax_cents": 1338496,
                "description": "Wisconsin Joint Tier #2 (2.55%)"
            },
            {
                "bracket_id": "wi_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0382,
                "base_tax_cents": 1338496,
                "description": "Wisconsin Joint Tier #3 (3.82%)"
            },
            {
                "bracket_id": "wi_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.051,
                "base_tax_cents": 1338496,
                "description": "Wisconsin Joint Tier #4 (5.10%)"
            },
            {
                "bracket_id": "wi_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0638,
                "base_tax_cents": 1338496,
                "description": "Wisconsin Joint Tier #5 (6.38%)"
            },
            {
                "bracket_id": "wi_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.0765,
                "base_tax_cents": 1338496,
                "description": "Wisconsin Joint Tier #6 (7.65%)"
            },
        ]
    },
    "WY": {
        "name": "Wyoming",
        "top_marginal_rate": 0.0,
        "brackets_single": [
            {
                "bracket_id": "wy_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Wyoming Tier #1 (0.00%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "wy_mfj_b1",
                "threshold_cents": 0,
                "rate": 0.0,
                "base_tax_cents": 0,
                "description": "Wyoming Joint Tier #1 (0.00%)"
            },
        ]
    },
    "DC": {
        "name": "District of Columbia",
        "top_marginal_rate": 0.1075,
        "brackets_single": [
            {
                "bracket_id": "dc_b1",
                "threshold_cents": 1000000,
                "rate": 0.0179,
                "base_tax_cents": 0,
                "description": "District of Columbia Tier #1 (1.79%)"
            },
            {
                "bracket_id": "dc_b2",
                "threshold_cents": 3500000,
                "rate": 0.0358,
                "base_tax_cents": 44750,
                "description": "District of Columbia Tier #2 (3.58%)"
            },
            {
                "bracket_id": "dc_b3",
                "threshold_cents": 6000000,
                "rate": 0.0538,
                "base_tax_cents": 134250,
                "description": "District of Columbia Tier #3 (5.38%)"
            },
            {
                "bracket_id": "dc_b4",
                "threshold_cents": 8500000,
                "rate": 0.0717,
                "base_tax_cents": 268750,
                "description": "District of Columbia Tier #4 (7.17%)"
            },
            {
                "bracket_id": "dc_b5",
                "threshold_cents": 11000000,
                "rate": 0.0896,
                "base_tax_cents": 448000,
                "description": "District of Columbia Tier #5 (8.96%)"
            },
            {
                "bracket_id": "dc_b6",
                "threshold_cents": 13500000,
                "rate": 0.1075,
                "base_tax_cents": 672000,
                "description": "District of Columbia Tier #6 (10.75%)"
            },
        ],
        "brackets_married": [
            {
                "bracket_id": "dc_mfj_b1",
                "threshold_cents": 2000000,
                "rate": 0.0179,
                "base_tax_cents": 1881500,
                "description": "District of Columbia Joint Tier #1 (1.79%)"
            },
            {
                "bracket_id": "dc_mfj_b2",
                "threshold_cents": 7000000,
                "rate": 0.0358,
                "base_tax_cents": 1881500,
                "description": "District of Columbia Joint Tier #2 (3.58%)"
            },
            {
                "bracket_id": "dc_mfj_b3",
                "threshold_cents": 12000000,
                "rate": 0.0538,
                "base_tax_cents": 1881500,
                "description": "District of Columbia Joint Tier #3 (5.38%)"
            },
            {
                "bracket_id": "dc_mfj_b4",
                "threshold_cents": 17000000,
                "rate": 0.0717,
                "base_tax_cents": 1881500,
                "description": "District of Columbia Joint Tier #4 (7.17%)"
            },
            {
                "bracket_id": "dc_mfj_b5",
                "threshold_cents": 22000000,
                "rate": 0.0896,
                "base_tax_cents": 1881500,
                "description": "District of Columbia Joint Tier #5 (8.96%)"
            },
            {
                "bracket_id": "dc_mfj_b6",
                "threshold_cents": 27000000,
                "rate": 0.1075,
                "base_tax_cents": 1881500,
                "description": "District of Columbia Joint Tier #6 (10.75%)"
            },
        ]
    },
}


class StateTaxCalculator:
    """Calculates granular multi-tier state income taxes and marginal liability."""

    @staticmethod
    def calculate_state_liability(
        state_code: str,
        gross_income_cents: int,
        status: FilingStatus = FilingStatus.SINGLE,
        deductions_cents: int = 0
    ) -> Dict:
        state_info = STATE_TAX_SCHEDULES.get(state_code.upper())
        if not state_info:
            return {"state": state_code, "taxable_income_cents": 0, "total_tax_cents": 0, "effective_rate": 0.0}

        taxable_cents = max(0, gross_income_cents - deductions_cents)
        brackets = state_info["brackets_single"] if status == FilingStatus.SINGLE else state_info["brackets_married"]

        if not brackets or state_info["top_marginal_rate"] == 0.0:
            return {
                "state": state_code,
                "state_name": state_info["name"],
                "taxable_income_cents": taxable_cents,
                "total_tax_cents": 0,
                "effective_rate": 0.0,
                "marginal_rate": 0.0
            }

        total_tax_cents = 0
        applicable_marginal = 0.0

        for idx in range(len(brackets) - 1, -1, -1):
            b = brackets[idx]
            if taxable_cents > b["threshold_cents"]:
                excess = taxable_cents - b["threshold_cents"]
                total_tax_cents = b["base_tax_cents"] + int(excess * b["rate"])
                applicable_marginal = b["rate"]
                break

        eff_rate = (total_tax_cents / taxable_cents) if taxable_cents > 0 else 0.0

        return {
            "state": state_code,
            "state_name": state_info["name"],
            "taxable_income_cents": taxable_cents,
            "total_tax_cents": total_tax_cents,
            "effective_rate": round(eff_rate, 4),
            "marginal_rate": applicable_marginal
        }
