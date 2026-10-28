# ASSIGNMENT 1 - TASK 9: Automated assert tests for normal, boundary and invalid cases.
"""Task 9 automated tests. Run this file directly."""
from decimal import Decimal as D
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Task07"))
from calculator import ten_day_total, validate_entry
from milkrate import payout, rate_per_litre

assert rate_per_litre(D("3.5"), D("8.5")) == D("30.00")
assert payout(D("10"), D("3.5"), D("8.5")) == D("300.00")
assert payout(D("8.5"), D("4.2"), D("8.7")) == D("283.90")
assert payout(D("12"), D("3.1"), D("8.3")) == D("333.60")
assert ten_day_total([(D("10"), D("3.5"), D("8.5")), (D("8.5"), D("4.2"), D("8.7")), (D("12"), D("3.1"), D("8.3"))]) == D("917.50")
try:
    validate_entry(D("-1"), D("3.5"), D("8.5"))
    raise AssertionError("Negative litres should fail")
except ValueError:
    pass
print("All Task 9 tests passed.")

