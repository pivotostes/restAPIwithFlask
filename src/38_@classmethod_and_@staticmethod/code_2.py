class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        """
        docstring
        """
        return Book(name, Book.TYPES[1], page_weight)


book = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("Python 101", 1500)

print(book)
print(book2)
