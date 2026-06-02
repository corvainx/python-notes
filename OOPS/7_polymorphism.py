# polymorphism = Greek word that means to "many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):

class Circle(Shape):
    pass

class Square(Shape):
    pass

class Triangle(Shape):
    pass

shapes = [Circle(), Square(), Triangle()]
