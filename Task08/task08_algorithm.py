# ASSIGNMENT 1 - TASK 8: Plan the algorithm with pseudocode, a validation flow and hand trace before final coding.
# This program is a small executable version of the pseudocode. Copy the flowchart and hand trace to the report.
from decimal import Decimal as D

entries = [(D("10"), D("3.5"), D("8.5")), (D("8.5"), D("4.2"), D("8.7")), (D("12"), D("3.1"), D("8.3"))]
total = D("0.00")
for litres, fat, snf in entries:
    fat_steps = round((fat - D("3.5")) / D("0.1"))
    snf_steps = round((snf - D("8.5")) / D("0.1"))
    rate = D("30.00") + fat_steps * D("0.40") + snf_steps * D("0.30")
    payment = (litres * rate).quantize(D("0.01"))
    total += payment
    print(litres, fat, snf, rate, payment, total)
print("Ten-day total:", total)
