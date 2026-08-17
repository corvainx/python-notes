# Lesson 10: Class Methods (@classmethod)
# Methods that operate on the class ('cls') itself rather than instances ('self').

class Book:
    total_books = 0

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def get_inventory_count(cls) -> int:
        return cls.total_books

    @classmethod
    def from_raw_string(cls, data_str: str):
        """Alternative constructor factory parsing 'Title;Author'."""
        title, author = data_str.split(";")
        return cls(title.strip(), author.strip())

b1 = Book("Clean Code", "Robert C. Martin")
b2 = Book.from_raw_string("Fluent Python ; Luciano Ramalho")

print(f"Total Books in Library: {Book.get_inventory_count()}")
print(f"Parsed Book: '{b2.title}' by {b2.author}")
