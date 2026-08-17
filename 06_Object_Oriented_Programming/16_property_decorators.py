# Lesson 16: Property Decorators (@property, @setter, @deleter)
# Provides Pythonic getters and setters with validation.

class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        """Getter for width."""
        return self._width

    @width.setter
    def width(self, val: float):
        """Setter with validation."""
        if val > 0:
            self._width = val
        else:
            raise ValueError("Width must be strictly positive.")

    @property
    def height(self) -> float:
        """Getter for height."""
        return self._height

    @height.setter
    def height(self, val: float):
        """Setter with validation."""
        if val > 0:
            self._height = val
        else:
            raise ValueError("Height must be strictly positive.")

    @property
    def area(self) -> float:
        """Computed dynamic property."""
        return self._width * self._height

rect = Rectangle(10.0, 5.0)
print(f"Dimensions: {rect.width} x {rect.height}")
print(f"Area: {rect.area}")

rect.width = 15.0
print(f"Updated Dimensions: {rect.width} x {rect.height}")
print(f"Updated Area: {rect.area}")
