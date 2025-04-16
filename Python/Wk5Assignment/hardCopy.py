from bookStore import Book

class HardCopyBook(Book):
    def __init__(self, title, author, pages, cover_type):
        super().__init__(title, author, pages)
        self.cover_type = cover_type
        self.is_available = True