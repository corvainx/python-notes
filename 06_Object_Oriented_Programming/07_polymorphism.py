# Lesson 07: Polymorphism (Many Forms)
# Different classes can implement methods with identical signatures.

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

animals = [Dog(), Cat(), Duck()]

print("Polymorphic behavior across distinct types:")
for animal in animals:
    print(f"  {type(animal).__name__} says: {animal.speak()}")
