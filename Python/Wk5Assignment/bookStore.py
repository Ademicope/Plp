class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
