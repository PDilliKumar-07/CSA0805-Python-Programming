# ASSIGNMENT 1 - TASK 7: Demonstrates importing payout() from the milkrate module.
"""Task 7: importing a function prevents milkrate's demonstration table from running."""
from decimal import Decimal as D
from milkrate import payout

print("Imported payout() result:", payout(D("8.5"), D("4.2"), D("8.7")))

