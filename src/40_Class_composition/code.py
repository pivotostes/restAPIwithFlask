class BookShelf:
    def __init__(self, *books) -> None:
        self.books = books

    def __str__(self) -> str:
        return f'BookShelf with {len(self.books)} books.'


class Book:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'Book: {self.name}'


book_1 = Book('Harry Potter')
book_2 = Book('Python 101')

books = [book_1, book_2]

shelf = BookShelf(*books)
shelf_2 = BookShelf(book_1, book_2)
print(shelf)
print(shelf_2)
