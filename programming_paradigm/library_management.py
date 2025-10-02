class Book:
    """A book class with attributes title, author, and _is_checked_out."""

    def __init__(self, title, author):
        """Initialize a Book instance with title, author, and _is_checked_out."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False


class Library:
    """A library class that manages a collection of books."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book with the given title."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return
        raise ValueError(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book with the given title."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return
        raise ValueError(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book.title for book in self._books if not book._is_checked_out]
        print("\n".join(available_books))