# ASSIGNMENT 1 - TASK 4: Calculate fat/SNF steps, rate and payment; demonstrate operator behaviour.
# round() is used because float expressions such as (4.2 - 3.5) / 0.1 can contain tiny binary errors.
import math

fat, snf, litres = 4.2, 8.7, 8.5
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = round(30.00 + fat_steps * 0.40 + snf_steps * 0.30, 2)
amount = round(litres * rate, 2)
print("steps:", fat_steps, snf_steps, "rate:", rate, "amount:", amount)
print("-2**2 =", -2**2, "; (-2)**2 =", (-2)**2)
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("int(-1.9) =", int(-1.9), "; floor(-1.9) =", math.floor(-1.9))
