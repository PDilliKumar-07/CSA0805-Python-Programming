# ASSIGNMENT 1 - TASK 11: State and defend the final technical recommendation for the co-operative.
# Recommendation: use Decimal values created from input strings and round every payment to paisa.
# Rate values should be centralised in one module or a validated JSON rate card for safe revisions.
# This file prints the concise recommendation; expand it with measured Task 10 evidence in the report.
recommendation = "Use Decimal, round each payment to 0.01, validate inputs, and keep rates in one rate card."
limitations = "Manual input and policy-dependent validation limits must be controlled operationally."
scale = "Each entry has O(1) work; n entries require O(n) total time."
print(recommendation)
print(limitations)
print(scale)
