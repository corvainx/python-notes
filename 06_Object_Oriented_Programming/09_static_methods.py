# Lesson 09: Static Methods (@staticmethod)
# Methods that belong to a class namespace but do not access 'self' or 'cls'.

class MathOperations:
    @staticmethod
    def is_even(num: int) -> bool:
        return num % 2 == 0

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

print(f"Is 10 even?: {MathOperations.is_even(10)}")
print(f"Is 7 even?: {MathOperations.is_even(7)}")
print(f"Static add: {MathOperations.add(14.5, 5.5)}")
