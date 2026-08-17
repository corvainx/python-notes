# Lesson 13: Variable Scope — Built-in Scope
# Built-in names (e.g. len, range, min, max, print) are preloaded in Python's standard library.
from math import e

def calculate_log_base_e(val):
    # 'e' comes from imported module, 'min' is built-in
    clamped = max(val, 0.0001)
    print(f"Euler's constant e: {e}")
    print(f"Clamped value: {clamped}")

calculate_log_base_e(5.0)
