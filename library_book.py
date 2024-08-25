"""Define a class called Library that manages a collection of books. Each book should have a title, an author, and an ISBN number. The Library class should have methods to:

Add a Book: Add a new book to the library.
Remove a Book: Remove a book from the library using the ISBN number.
List All Books: List all the books currently in the library.
Include appropriate methods for initialization and representation of the classes.

Provide the implementation of the Library class along with a Book class that will be used by the Library class."""

#Implementation

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        # Provides a string representation of the book, including the author
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            print(f"Added: {book}")
        else:
            print("Book already exists in the library.")

    def remove_book(self, isbn):
        if isbn in self.books:
            removed_book = self.books.pop(isbn)
            print(f"Removed: {removed_book}")
        else:
            print("Book not found.")

    def list_books(self):
        if not self.books:
            return "No books in the library."
        # Joins the string representations of all books in the library
        return "\n".join(str(book) for book in self.books.values())

# Example Usage
my_library = Library()

# Add books
my_library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780060935467"))
my_library.add_book(Book("1984", "George Orwell", "9780451524935"))

# List all books
print(my_library.list_books())

# Remove a book
my_library.remove_book("9780451524935")

# List all books again
print(my_library.list_books())
