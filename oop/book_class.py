class Book:
    """
    A class to represent a book, including its title, author, and publication year.
    """
    def __init__(self, title, author, year):
        """
        Initializes a Book instance with a title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
