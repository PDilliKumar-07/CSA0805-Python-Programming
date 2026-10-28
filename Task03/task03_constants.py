# ASSIGNMENT 1 - TASK 3: Define well-named constants and demonstrate dynamic typing and multiple assignment.
# Constants use UPPER_CASE by convention. Python does not enforce constants, so code must not reassign them.
from decimal import Decimal as D

BASE_RATE = D("30.00")
FAT_STEP_VALUE = D("0.40")
SNF_STEP_VALUE = D("0.30")
RATE_CARD = {"base": BASE_RATE, "fat": FAT_STEP_VALUE, "snf": SNF_STEP_VALUE}

value = 10
print("value:", value, type(value))
value = "ten"
print("value:", value, type(value))
a, b = "AM", "PM"
a, b = b, a
print("Swapped shifts:", a, b)
print("Rate card:", RATE_CARD)
