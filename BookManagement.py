class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} written by {self.author}"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn, genre, quantity):
        new_book = Book(title, author, isbn, genre, quantity)
        self.books.append(new_book)
        print(f"Added {title} written by {author} to the library.")

    def update_book_quantity(self, isbn, new_quantity):
        for book in self.books:
            if book.isbn == isbn:
                book.update_quantity(new_quantity)
                print(f"Updated quantity of {book.title} to {new_quantity}.")
                return
        print(f"Book with ISBN {isbn} not found.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed {book.title} written by {book.author} from the library.")
                return
        print(f"Book with ISBN {isbn} not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")


library = Library()

# Adding books
library.add_book("The Secret", "Rhonda Byrne", "9781416554998", "non-Fiction", 5)
library.add_book("Atomic Habits", "James Clear", "9783442178582", "non-Fiction", 3)
library.add_book("Rich Dad Poor Dad", "Robert Kiyosaki", "9780446677455", "Personal Finance Classic", 2)
library.add_book("The Girl on the Train", "Paula Hawkins", "9780735219755", "Fiction", 3)
library.add_book("Little Women", "Louisa May Alcott", "9780886463151", "classic", 3)

# Display all books
library.display_books()

# Updating quantity of a book
library.update_book_quantity("9781416554998", 7)

# Removing a book by isbn
library.remove_book("9783442178582")

# Display all books after modifications
library.display_books()
