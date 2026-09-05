"""
SYZYGY Anti-Slop Text Auditor: ASD-STE100 Simplified Technical English
Enforces unambiguous, concise vocabulary and flags generic AI marketing filler.
"""

import re
from typing import Dict, Any, List

AI_SLOP_LIST = [
    "game changer", "revolutionize", "delve", "testament", "seamlessly integrate",
    "leverage the power of", "in conclusion", "it is important to remember",
    "tapestry", "beacon", "cutting-edge solutions", "unparalleled", "plethora"
]

class STE100Validator:
    @staticmethod
    def audit_text(text: str) -> Dict[str, Any]:
        detected_slop = []
        for word in AI_SLOP_LIST:
            if re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE):
                detected_slop.append(word)

        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        long_sentences = [s for s in sentences if len(s.split()) > 25]

        is_compliant = len(detected_slop) == 0 and len(long_sentences) == 0

        return {
            "compliant": is_compliant,
            "slopWordsFound": detected_slop,
            "longSentenceCount": len(long_sentences),
            "score": max(0, 100 - (len(detected_slop) * 20) - (len(long_sentences) * 10))
        }
