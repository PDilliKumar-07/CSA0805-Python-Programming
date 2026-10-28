# ASSIGNMENT 1 - TASK 6: Organise calculation logic into functions with parameters, return values and docstrings.
# Functions return values rather than print them, so results can be reused and tested.
from decimal import Decimal as D


def rate_per_litre(fat, snf):
    """Return rate for given fat and SNF values."""
    fat_steps = round((fat - D("3.5")) / D("0.1"))
    snf_steps = round((snf - D("8.5")) / D("0.1"))
    return D("30.00") + fat_steps * D("0.40") + snf_steps * D("0.30")


def payout(litres, fat, snf):
    """Return payment for one delivery."""
    return (litres * rate_per_litre(fat, snf)).quantize(D("0.01"))

print("Payment:", payout(D("8.5"), D("4.2"), D("8.7")))
