# Lesson 04: Multiple Inheritance
# A child class inherits from multiple parent classes simultaneously.

class Prey:
    def flee(self):
        print("This animal is fleeing from danger!")

class Predator:
    def hunt(self):
        print("This animal is hunting for food!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    """Fish can both hunt smaller creatures and flee from larger ones."""
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

print("--- Animal Behaviors ---")
rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
