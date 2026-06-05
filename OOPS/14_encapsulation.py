class Student:
    def __init__(self, name, marks):
        self.name = name      # Public attribute
        self.__marks = marks  # Private attribute

    def get_marks(self):
        # Method to access private data
        return self.__marks


# Create object
s1 = Student("Dexter", 95)

print("Name:", s1.name)
print("Marks:", s1.get_marks())

# This will give an error
# print(s1.__marks)
