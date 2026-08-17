# Practice Task 05: Right-Angled Triangle Hypotenuse (Pythagorean Theorem)
# Formula: c = sqrt(a^2 + b^2)
import math

side_a = float(input("Enter length of side A (cm): "))
side_b = float(input("Enter length of side B (cm): "))

hypotenuse = math.hypot(side_a, side_b)

print(f"Hypotenuse (Side C): {hypotenuse:.2f} cm")
