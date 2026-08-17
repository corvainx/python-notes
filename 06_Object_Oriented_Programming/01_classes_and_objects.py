# Lesson 01: Classes and Objects
# - Class: A blueprint/template defining attributes and methods.
# - Object: A concrete instance created from a class.

class Car:
    def __init__(self, model: str, year: int, colour: str, for_sale: bool):
        # Instance attributes
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.colour} {self.model}.")

    def stop(self):
        print(f"You stop the {self.colour} {self.model}.")

    def describe(self):
        status = "Available" if self.for_sale else "Sold"
        print(f"Vehicle: {self.year} {self.colour} {self.model} | Status: {status}")

# Instantiating objects
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

car1.describe()
car2.describe()

car1.drive()
car2.stop()
