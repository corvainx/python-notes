# Project 11: Variable Swapping Techniques
# Demonstrating Pythonic tuple packing vs traditional temporary variable swap.

a = 10
b = 25
print(f"Original: a = {a}, b = {b}")

# Method 1: Pythonic Tuple Unpacking (Zero temporary memory)
a, b = b, a
print(f"After Pythonic Swap (a, b = b, a): a = {a}, b = {b}")

# Method 2: Arithmetic Swap (without temp variable)
a = a + b
b = a - b
a = a - b
print(f"After Arithmetic Swap: a = {a}, b = {b}")
