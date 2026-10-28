# ASSIGNMENT 1 - TASK 10: Compare float and Decimal totals and measure execution time for three data sizes.
# Results depend on your computer. Run this file yourself and paste the output into the report.
from decimal import Decimal
from time import perf_counter


def benchmark(count):
    values = ["33.40"] * count
    start = perf_counter(); float_total = sum(float(x) for x in values); float_time = perf_counter() - start
    start = perf_counter(); decimal_total = sum((Decimal(x) for x in values), Decimal("0")); decimal_time = perf_counter() - start
    print(f"n={count:6} | float={float_total} ({float_time:.6f}s) | Decimal={decimal_total} ({decimal_time:.6f}s)")

for size in (300, 6000, 150000):
    benchmark(size)
