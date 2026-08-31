"""
Merchant Name Normalization & Cleansing Engine.
Strips terminal numbers, store IDs, locations, payment gateways (Square, Stripe),
and maps noisy raw transaction strings to canonical merchant identities.
"""

import re
from typing import Dict, Optional


class MerchantNormalizer:
    """
    Cleans noisy bank descriptions (e.g. 'SQ *BLUE BOTTLE COFFEE #120 SAN FRANCISCO CA')
    into canonical brand names ('Blue Bottle Coffee').
    """

    CLEANUP_REGEXES = [
        re.compile(r"^(sq\s*\*|tst\s*\*|sp\s*\*|paypal\s*\*|stripe\s*\*|apple\.com\/bill\s*)", re.IGNORECASE),
        re.compile(r"#\s*\d+", re.IGNORECASE),
        re.compile(r"(store|loc|terminal|pos|dept)\s*\d+", re.IGNORECASE),
        re.compile(r"[A-Z]{2}\s+\d{5}(-\d{4})?"),  # State + Zip code
        re.compile(r"\d{2,}"),  # Sequences of standalone numbers
    ]

    CANONICAL_BRANDS: Dict[str, str] = {
        "amzn": "Amazon",
        "amazon": "Amazon",
        "prime video": "Amazon Prime",
        "uber": "Uber",
        "uber *eats": "Uber Eats",
        "lyft": "Lyft",
        "nflx": "Netflix",
        "netflix": "Netflix",
        "spot": "Spotify",
        "spotify": "Spotify",
        "tgt": "Target",
        "target": "Target",
        "wmt": "Walmart",
        "walmart": "Walmart",
        "wfm": "Whole Foods Market",
        "wholefds": "Whole Foods Market",
        "sbux": "Starbucks",
        "starbucks": "Starbucks",
        "trader joe": "Trader Joe's",
        "blue bottle": "Blue Bottle Coffee",
        "apple": "Apple",
        "google": "Google",
    }

    @classmethod
    def normalize(cls, raw_description: str) -> str:
        """
        Returns normalized merchant name.
        """
        cleaned = raw_description.strip()

        # Check known canonical patterns first
        lower_desc = cleaned.lower()
        for pattern, canonical in cls.CANONICAL_BRANDS.items():
            if pattern in lower_desc:
                return canonical

        # Apply regex cleanup
        for pattern in cls.CLEANUP_REGEXES:
            cleaned = pattern.sub(" ", cleaned)

        # Normalize whitespace and title-case
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        return cleaned.title() if cleaned else "Unknown Merchant"
