# Lesson 15: Magic / Dunder Methods (__str__, __repr__, __eq__, __add__, __len__)

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    # Readable string for end users (print / str)
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Unambiguous representation for debugging (repr)
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    # Length protocol len(book)
    def __len__(self):
        return self.pages

    # Equality check (book1 == book2)
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    # Addition overload (book1 + book2) -> Total pages
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)
book3 = Book("1984", "George Orwell", 328)

print(f"print(book1): {book1}")
print(f"repr(book1): {repr(book1)}")
print(f"len(book1): {len(book1)} pages")
print(f"book1 == book3: {book1 == book3}")
print(f"Combined page count (book1 + book2): {book1 + book2}")
