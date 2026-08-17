# Lesson 06: Python 'math' Module and Geometry Calculations
import math

print(f"Value of Pi (math.pi): {math.pi}")
print(f"Euler's number (math.e): {math.e}")

# Common math functions
num = 9.1
print(f"Square root of 25: {math.sqrt(25)}")
print(f"math.ceil({num}): {math.ceil(num)}")    # Always rounds UP
print(f"math.floor({num}): {math.floor(num)}")  # Always rounds DOWN

# Practical Example: Circumference and Area of a Circle
radius = float(input("\nEnter radius of a circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"Circumference: {round(circumference, 2)}")
print(f"Area: {round(area, 2)}")
