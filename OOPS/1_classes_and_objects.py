# object = A "bundle" of related attributes (variables) and methods (functions)
#          Eg: phone, cup, book, etc
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("McLarren", 2026, "yellow", True)

print(car1.model)
print(car1.year)
print(car1.colour)
print(car1.for_sale)
print()

print(car2.model)
print(car2.year)
print(car2.colour)
print(car2.for_sale)
print()

print(car3.model)
print(car3.year)
print(car3.colour)
print(car3.for_sale)
print()

