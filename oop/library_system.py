# Library System with Book, EBook, PrintBook, and Library classes
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author





class EBook(Book):
    def __init__(self, title, author, file_size):
        self.file_size = int (file_size)
        super().__init__(title, author)

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, Size: {self.file_size}MB"





class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.page_count = int(page_count)
        super().__init__(title, author)

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.page_count}"





class Library:
    def __init__(self):
        self.books = []


    def add_book(self, book):
        self.books.append(book)


    def list_books(self):
        # List all books in the library
        for book in self.books:
            # Check the type of book and print accordingly
            if isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            else:
                print(f"Book: {book.title} by {book.author}")






