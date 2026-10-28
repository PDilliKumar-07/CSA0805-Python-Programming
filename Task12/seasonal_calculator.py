# ASSIGNMENT 1 - TASK 12: Adapted design for seasonal rates, two-decimal readings and volume bonus.
"""Task 12: seasonal rate card and ten-day bonus."""
from decimal import Decimal as D, ROUND_HALF_UP

RATE_CARDS = {
    "regular": {"base": D("30.00"), "fat": D("0.40"), "snf": D("0.30")},
    "apr_jun": {"base": D("32.00"), "fat": D("0.45"), "snf": D("0.30")},
}


def rate_per_litre(fat, snf, season):
    """Return the seasonal rate for one litre."""
    card = RATE_CARDS[season]
    fat_steps = ((fat - D("3.5")) / D("0.1")).quantize(D("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - D("8.5")) / D("0.1")).quantize(D("1"), rounding=ROUND_HALF_UP)
    return (card["base"] + fat_steps * card["fat"] + snf_steps * card["snf"]).quantize(D("0.01"))


def ten_day_total(entries, season):
    """Add individual payments and apply bonus if litres exceed 500."""
    litres_total = sum((litres for litres, _, _ in entries), D("0"))
    payment_total = sum((litres * rate_per_litre(fat, snf, season) for litres, fat, snf in entries), D("0"))
    bonus = litres_total * D("0.50") if litres_total > D("500") else D("0")
    return (payment_total + bonus).quantize(D("0.01"), rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    print("Regular base rate:", rate_per_litre(D("3.5"), D("8.5"), "regular"))
    print("April-June base rate:", rate_per_litre(D("3.5"), D("8.5"), "apr_jun"))
    print("April-June rate at fat 4.25:", rate_per_litre(D("4.25"), D("8.5"), "apr_jun"))
    entries = [(D("250.01"), D("3.5"), D("8.5")), (D("250"), D("3.5"), D("8.5"))]
    print("Total with bonus:", ten_day_total(entries, "apr_jun"))


