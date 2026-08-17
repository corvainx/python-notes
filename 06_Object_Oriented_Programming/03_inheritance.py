# Lesson 03: Inheritance (Single Inheritance)
# A child class inherits attributes and methods from a parent class.

class Animal:
    def __init__(self, name: str):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.eat()
dog.bark()
cat.sleep()
cat.meow()
