from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            return f"Book '{book.title}' added to the library."
        return "Invalid book."

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Book '{title}' removed from the library."
        return f"Book '{title}' not found in the library."

    def list_books(self):
        if not self.books:
            return "No books available in the library."
        return [book.get_details() for book in self.books]
    
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return f"Book '{title}' not found in the library."