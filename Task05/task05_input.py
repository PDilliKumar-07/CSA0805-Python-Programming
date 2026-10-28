# ASSIGNMENT 1 - TASK 5: Read text input, convert it safely to Decimal, handle invalid entries and format output.
# input() always returns str, so decimal conversion is protected by try/except.
from decimal import Decimal, InvalidOperation


def parse_number(text):
    """Return a Decimal or None for invalid text."""
    try:
        return Decimal(text.strip())
    except InvalidOperation:
        return None

for text in ["8.5", " 8.5 ", "8,5", "eight"]:
    value = parse_number(text)
    print(f"{text!r:10} -> {value}")
amount = Decimal("283.90")
print(f"Formatted amount: Rs {amount:8.2f}")
