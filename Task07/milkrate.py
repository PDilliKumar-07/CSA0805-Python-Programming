# ASSIGNMENT 1 - TASK 7: Reusable milk-rate module with rate_per_litre() and payout().
"""Rate card of the village milk co-operative (used as a module)."""
from decimal import Decimal, ROUND_HALF_UP

D = Decimal
PAISA = D("0.01")
BASE_RATE = D("30.00")
BASE_FAT = D("3.5")
BASE_SNF = D("8.5")
FAT_STEP_VALUE = D("0.40")
SNF_STEP_VALUE = D("0.30")
STEP = D("0.1")
MIN_FAT = D("2.0")
MAX_FAT = D("7.0")


def rate_per_litre(fat, snf):
    """Return the price per litre rounded to two decimal places."""
    fat_steps = ((fat - BASE_FAT) / STEP).quantize(D("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - BASE_SNF) / STEP).quantize(D("1"), rounding=ROUND_HALF_UP)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return rate.quantize(PAISA, rounding=ROUND_HALF_UP)


def payout(litres, fat, snf):
    """Return amount payable to the farmer rounded to two decimal places."""
    return (litres * rate_per_litre(fat, snf)).quantize(PAISA, rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    for litres, fat, snf in [(D("10"), D("3.5"), D("8.5")), (D("8.5"), D("4.2"), D("8.7")), (D("12"), D("3.1"), D("8.3"))]:
        rate, pay = rate_per_litre(fat, snf), payout(litres, fat, snf)
        print(f"{litres:5} L  fat {fat}  snf {snf}  rate {rate:6.2f}  pay {pay:8.2f}")

