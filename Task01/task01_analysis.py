# ASSIGNMENT 1 - TASK 1: Understand the payment problem and identify input, output, constants, types, rules and assumptions.
# Inputs: farmer ID, litres, fat percentage, SNF percentage and shift.
# Outputs: rate per litre, one payment and ten-day total.
# This file shows one entry represented as a tuple, which scales better than separate variables.
from decimal import Decimal as D

entry = ("F001", D("10.0"), D("3.5"), D("8.5"), "AM")
farmer_id, litres, fat, snf, shift = entry
print(f"Farmer={farmer_id}, litres={litres}, fat={fat}, SNF={snf}, shift={shift}")
print("Rules: litres > 0 and 2.0 <= fat <= 7.0")
