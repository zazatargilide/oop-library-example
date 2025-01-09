class Book:
    def __init__(self, title, author, id_number, category, price):
        self.title = title
        self.author = author
        self.id_number = id_number
        self.category = category
        self.__price = price  # Private attribute for price

    def get_price(self):
        """Getter for the private price attribute."""
        return self.__price

    def set_price(self, new_price):
        """Setter for the private price attribute."""
        if new_price >= 0:
            self.__price = new_price
        else:
            raise ValueError("Price cannot be negative.")

    def __str__(self):
        """String representation of a Book object."""
        return f"Book(title='{self.title}', author='{self.author}', id='{self.id_number}', category='{self.category}', price={self.get_price()})"


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []  # List to store Book objects

    def add_book(self, book):
        """Adds a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book objects can be added to the library.")

    def display_books(self):
        """Displays all books in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def __str__(self):
        """String representation of a Library object."""
        return f"Library(name='{self.name}', address='{self.address}', total_books={len(self.books)})"


# Creating a Library with 3 books
book1 = Book("1984", "George Orwell", "001", "Fiction", 150)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "002", "Fiction", 200)
book3 = Book("A Brief History of Time", "Stephen Hawking", "003", "Science", 300)

my_library = Library("Central Library", "123 Main St")
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# Display library and books
print(my_library)
my_library.display_books()