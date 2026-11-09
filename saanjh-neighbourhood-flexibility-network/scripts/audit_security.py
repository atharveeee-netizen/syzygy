#!/usr/bin/env python3
"""SYZYGY Pre-Flight Security Audit Harness (Strix Pentester)"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from core.pentest import StrixPentestAgent

if __name__ == "__main__":
    auditor = StrixPentestAgent()
    res = auditor.run({"target": "http://localhost:3000"})
    print("Audit Result:", res)
