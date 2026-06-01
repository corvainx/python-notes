# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class child(Parent)

class Animal:
    def __init__(self, name, is_alive=True):
        self.name = name
        self.is_alive = is_alive

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Goat(Animal):
    def speak(self):
        print("FLASHING LIGHTS")

dog = Dog("Vinnie")
cat = Cat("Garfield")
goat = Goat("Kanye")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

