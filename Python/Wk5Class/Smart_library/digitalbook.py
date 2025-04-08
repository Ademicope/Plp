from book import Book

class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size  # in MB

    def stream(self):
        """
        simulates streaming of digital book
        """
        return f"Streaming '{self.title}' in {self.file_size} file_size."

    def borrow(self):
        """
        Overriding the borrow method to include digital availability
        """
        return f"{self.title} is a digital book. No need to borrow, stream anytime."

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, File Size: {self.file_size}MB, file_size: {self.file_size}"

    def download(self):
        return f"Downloading '{self.title}' in {self.file_size} file_size."

    def upload(self):
        return f"Uploading '{self.title}' in {self.file_size} file_size."