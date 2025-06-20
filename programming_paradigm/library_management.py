class Book:
    def __Init__ (self, title, author):
        self.title = title
        self.author = author 
        self_is_checked_out = False # Initialize the book as available


    
    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out: # Check if the book is checked out
            self._is_checked_out = True
        return False  # If the book is not checked out, return False
    

    def check_out (self):
        """Check out the book from the library."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        
    

class Library:
    def __init__(self):
        self._books = []


    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} by {book.author} to the library.")


    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = True
                self._books.remove(book)
                print(f"Checked out {book.title} by {book.author}.")
                return True
            
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out==True: 
                book._is_checked_out = False
                self._books.append(book)
                return True
            return False
    
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title}")  
    
