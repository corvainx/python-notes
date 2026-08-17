# Helper Module: math_helper.py
# Contains reusable mathematical utility functions.

PI = 3.141592653589793
E = 2.718281828459045

def square(x: float) -> float:
    return x ** 2

def cube(x: float) -> float:
    return x ** 3

def circumference(radius: float) -> float:
    return 2 * PI * radius

def circle_area(radius: float) -> float:
    return PI * (radius ** 2)
