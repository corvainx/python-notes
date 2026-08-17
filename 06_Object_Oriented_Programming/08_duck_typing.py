# Lesson 08: Duck Typing
# "If it walks like a duck and quacks like a duck, it's a duck."
# Type is determined by methods/capabilities, not explicit inheritance.

class Duck:
    def walk(self):
        print("This duck is waddling.")

    def talk(self):
        print("This duck is quacking.")

class Person:
    def walk(self):
        print("This person is imitating a duck walk.")

    def talk(self):
        print("This person is saying 'quack'!")

def make_it_quack(entity):
    # Expects entity to support walk() and talk()
    entity.walk()
    entity.talk()

make_it_quack(Duck())
print()
make_it_quack(Person())
