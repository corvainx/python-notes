# Lesson 11: Aggregation (HAS-A Relationship, Weak Coupling)
# An aggregate object contains references to independent objects that exist outside it.

class Book:
    def __init__(self, title: str):
        self.title = title

class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_inventory(self):
        print(f"Library: {self.name}")
        for b in self.books:
            print(f" - {b.title}")

# Books exist independently of the library
book1 = Book("The Pragmatic Programmer")
book2 = Book("Design Patterns")

city_library = Library("Metro Public Library")
city_library.add_book(book1)
city_library.add_book(book2)

city_library.list_inventory()
