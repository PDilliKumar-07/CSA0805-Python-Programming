# ASSIGNMENT 1 - TASK 9: Complete validated milk-payment calculator and ten-day total.
"""Task 9: complete validated calculator."""
from decimal import Decimal as D, InvalidOperation
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Task07"))
from milkrate import MIN_FAT, MAX_FAT, payout


def validate_entry(litres, fat, snf):
    """Raise ValueError if a delivery entry is not acceptable."""
    if litres <= 0:
        raise ValueError("Litres must be greater than zero.")
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError(f"Fat must be between {MIN_FAT} and {MAX_FAT}.")
    if not D("6.0") <= snf <= D("12.0"):
        raise ValueError("SNF must be between 6.0 and 12.0.")


def ten_day_total(entries):
    """Return the sum of rounded payments for valid entries."""
    total = D("0.00")
    for litres, fat, snf in entries:
        validate_entry(litres, fat, snf)
        total += payout(litres, fat, snf)
    return total


def read_decimal(prompt):
    """Read a decimal number, retrying after invalid input."""
    while True:
        try:
            return D(input(prompt).strip())
        except InvalidOperation:
            print("Enter a number using a decimal point, for example 8.5.")


if __name__ == "__main__":
    entries = []
    print("Enter milk deliveries. Type done as farmer ID to finish.")
    while True:
        farmer_id = input("Farmer ID: ").strip()
        if farmer_id.lower() == "done":
            break
        litres = read_decimal("Litres: ")
        fat = read_decimal("Fat percentage: ")
        snf = read_decimal("SNF percentage: ")
        try:
            validate_entry(litres, fat, snf)
            amount = payout(litres, fat, snf)
            entries.append((litres, fat, snf))
            print(f"{farmer_id:10} rate {amount / litres:6.2f}  payment Rs {amount:8.2f}")
        except ValueError as error:
            print("Invalid entry:", error)
    print(f"Ten-day total: Rs {ten_day_total(entries):.2f}")

