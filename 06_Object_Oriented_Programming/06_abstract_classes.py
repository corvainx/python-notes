# Lesson 06: Abstract Classes & Interfaces (abc Module)
# Abstract classes cannot be instantiated directly; subclasses MUST implement abstract methods.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        """Must be implemented by subclasses."""
        pass

    @abstractmethod
    def stop(self):
        """Must be implemented by subclasses."""
        pass

class Car(Vehicle):
    def go(self):
        print("Car: Driving along the highway.")

    def stop(self):
        print("Car: Applying brakes to stop.")

class Boat(Vehicle):
    def go(self):
        print("Boat: Cruising through the water.")

    def stop(self):
        print("Boat: Dropping anchor to stop.")

vehicles = [Car(), Boat()]
for v in vehicles:
    v.go()
    v.stop()
