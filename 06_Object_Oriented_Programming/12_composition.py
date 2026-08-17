# Lesson 12: Composition (PART-OF Relationship, Strong Coupling)
# A composite object manages the full lifecycle of its components.

class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine ({self.horsepower} HP) started.")

class Car:
    def __init__(self, make: str, horsepower: int):
        self.make = make
        # Engine is created internally and tied directly to Car lifecycle
        self.engine = Engine(horsepower)

    def start(self):
        print(f"Starting {self.make}...")
        self.engine.start()

car = Car("Ford Mustang", 450)
car.start()
