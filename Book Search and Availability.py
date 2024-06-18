class Library:
    def __init__(self):
        self.books = [
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "copies": 4},
            {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "copies": 2},
            {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "copies": 5},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "copies": 3},
            {"title": "Moby Dick", "author": "Herman Melville", "genre": "Adventure", "copies": 1},
            {"title": "The Secret", "author": "Rhonda Byrne", "genre": "Non-Fiction", "copies": 3},
            {"title": "Little Women", "author": "Louisa May Alcott", "genre": "classic", "copies": 2},
        ]

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books:
            if title and title.lower() not in book["title"].lower():
                continue
            if author and author.lower() not in book["author"].lower():
                continue
            if genre and genre.lower() not in book["genre"].lower():
                continue
            results.append(book)
        return results

    def display_books(self, books):
        if not books:
            print("No books found.")
        else:
            for book in books:
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Genre: {book['genre']}")
                print(f"Copies Available: {book['copies']}")
                print("-" * 40)

def main():
    library = Library()

    while True:
        print("Search for books by Title, Author, or Genre")
        search_type = input("Enter search type (title, author, genre or 'exit' to quit): ").strip().lower()
        
        if search_type == "exit":
            break

        search_query = input(f"Enter the {search_type}: ").strip()

        if search_type == "title":
            books_found = library.search_books(title=search_query)
        elif search_type == "author":
            books_found = library.search_books(author=search_query)
        elif search_type == "genre":
            books_found = library.search_books(genre=search_query)
        else:
            print("Invalid search type. Please try again.")
            continue

        library.display_books(books_found)

if __name__ == "__main__":
    main()
