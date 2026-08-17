# Lesson 02: Class Variables vs Instance Variables
# Class variables are shared across ALL instances of a class.

class Student:
    graduating_year = 2026   # Class Variable
    total_students = 0       # Class Variable Counter

    def __init__(self, name: str, age: int):
        self.name = name     # Instance Variable
        self.age = age       # Instance Variable
        Student.total_students += 1

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Dexter", 24)

print(f"Total Enrolled Students: {Student.total_students}")
print(f"Graduating Class: {Student.graduating_year}")
print(f"Student 1: {student1.name} (Age {student1.age})")
