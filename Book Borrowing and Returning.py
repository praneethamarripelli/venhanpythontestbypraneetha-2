import datetime

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower_id = None
        self.due_date = None

    def __str__(self):
        return f"{self.title} written by {self.author} (ISBN: {self.isbn})"

class Borrower:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book, days_to_borrow):
        if book.is_borrowed:
            print(f"Sorry, {book} is already borrowed.")
            return False
        due_date = datetime.date.today() + datetime.timedelta(days=days_to_borrow)
        book.is_borrowed = True
        book.borrower_id = self.membership_id
        book.due_date = due_date
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book}. Due on {due_date}.")
        return True

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            book.borrower_id = None
            book.due_date = None
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book}.")
            return True
        print(f"{self.name} did not borrow {book}.")
        return False

    def check_overdue_books(self):
        today = datetime.date.today()
        overdue_books = [book for book in self.borrowed_books if book.due_date < today]
        return overdue_books

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library.")

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)
        print(f"Added borrower {borrower.name} with ID {borrower.membership_id}.")

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_borrower_by_id(self, membership_id):
        for borrower in self.borrowers:
            if borrower.membership_id == membership_id:
                return borrower
        return None

    def handle_overdue_books(self):
        for borrower in self.borrowers:
            overdue_books = borrower.check_overdue_books()
            if overdue_books:
                print(f"Borrower {borrower.name} has overdue books:")
                for book in overdue_books:
                    print(f"  {book} was due on {book.due_date}")

# Example usage
library = Library()

# Add some books
library.add_book(Book("The Secret", "Rhonda Byrne", "9781416554998"))
library.add_book(Book("Rich Dad Poor Dad", "Robert Kiyosaki", "9780446677455"))

# Add a borrower
praneetha = Borrower("Praneetha", "MID001")
library.add_borrower(praneetha)

# Borrow a book
book = library.find_book_by_isbn("9780446677455")
if book:
    praneetha.borrow_book(book, 7)  # Borrow for 7 days

# Check overdue books (assuming some days have passed)
library.handle_overdue_books()

# Return a book
praneetha.return_book(book)
