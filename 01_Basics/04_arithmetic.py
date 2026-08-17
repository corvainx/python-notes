# Lesson 04: Arithmetic Operators and Augmented Assignment

# Basic Operators:
# + Addition, - Subtraction, * Multiplication, / Division (float), // Floor Division (int), % Modulo, ** Exponentiation

friends = 10

# Augmented Assignment
friends += 2   # friends = friends + 2 -> 12
friends -= 1   # friends = friends - 1 -> 11
friends *= 3   # friends = friends * 3 -> 33
friends /= 2   # friends = friends / 2 -> 16.5 (always float)
friends **= 2  # friends = friends ** 2 -> 272.25

print(f"Computed friends value: {friends}")

# Modulo operator (%) returns the remainder of division
dividend = 14
divisor = 3
remainder = dividend % divisor
quotient_int = dividend // divisor

print(f"{dividend} divided by {divisor} is {quotient_int} with remainder {remainder}")
