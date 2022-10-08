from book_library.details.writer import Writer

class Book:

    def __init__(self, book_name, writer:Writer, published_year) -> None:
        self.book_name = book_name
        self.writer = writer
        self.published_year = published_year


    def __str__(self) -> str:
        return f"The book '{self.book_name}' was written by '{self.writer}' in {self.published_year}."

writer1 = Writer("JK", "Rowling")
writer2 = Writer("John Ronald Reuel", "Tolkien")
    
book1 = Book("Harry Potter", writer1, 1997)
book2 = Book("The Lord of The Rings",writer2, 1954)
print(book1)
print(book2)

