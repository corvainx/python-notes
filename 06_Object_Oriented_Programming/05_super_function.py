# Lesson 05: The 'super()' Function
# Invokes methods and constructors of the parent class to extend functionality.
import math

class Shape:
    def __init__(self, color: str, is_filled: bool):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        status = "filled" if self.is_filled else "hollow"
        print(f"Shape: Color={self.color}, Style={status}")

class Circle(Shape):
    def __init__(self, color: str, is_filled: bool, radius: float):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        area = math.pi * (self.radius ** 2)
        print(f"  Type: Circle | Radius={self.radius} | Area={area:.2f}")

class Rectangle(Shape):
    def __init__(self, color: str, is_filled: bool, width: float, height: float):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        area = self.width * self.height
        print(f"  Type: Rectangle | Dimensions={self.width}x{self.height} | Area={area:.2f}")

circle = Circle("red", True, 5.0)
rect = Rectangle("blue", False, 4.0, 6.0)

circle.describe()
print()
rect.describe()
