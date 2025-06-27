class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = int(year)


    # Method to return a string representation of the book object
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"


    
    # Method for official representation of the book object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    #Method to delete the book object
    def __del__(self):
        print(f"Deleting {self.title}")

