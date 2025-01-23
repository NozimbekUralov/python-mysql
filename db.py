
class Library:
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()

    def create_books_table(self):
        """
        Create a 'books' table in the database if it doesn't exist.
        """
        self.__cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY not null,
                title VARCHAR(255) not null,
                author VARCHAR(255) not null,
                published_year INT not null,
                genre VARCHAR(255) not null,
                price DECIMAL(10, 2) not null,
                available BOOLEAN not null
            )
            """
        )

    def insert_book(self, title, author, published_year, genre, price, available=True):
        """
        Insert a new book into the 'books' table.
        """
        self.__cursor.execute(
            """
            INSERT INTO books (title, author, published_year, genre, price, available)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (title, author, published_year, genre, price, available)
        )
        
        self.__connection.commit()
        self.show_all_books()

    def update_book_price(self, book_id, new_price):
        """
        Update the price of a specific book.
        """
        self.__cursor.execute(
            "UPDATE books SET price = %s WHERE id = %s",
            (new_price, book_id)
        )
        self.__connection.commit()
        self.show_all_books()

    def update_book_availability(self, book_id, available):
        """
        Update the availability of a specific book.
        """
        self.__cursor.execute(
            "UPDATE books SET available = %s WHERE id = %s",
            (available, book_id)
        )

        self.__connection.commit()
        self.show_all_books()

    def delete_book(self, book_id):
        """
        Delete a specific book from the 'books' table.
        """
        self.__cursor.execute(f"DELETE FROM books WHERE id = {book_id}")
        self.__connection.commit()
        self.show_all_books()

    def show_all_books(self):
        """
        Retrieve and display all books from the 'books' table.
        """
        self.__cursor.execute("SELECT * FROM books")
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)

    def search_books_by_author_or_genre(self, search_type, search_value):
        """
        Search for books by author or genre.
        """
        self.__cursor.execute(
            f"SELECT * FROM books WHERE {search_type} = {search_value}"
        )

        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)

    def sort_books_by_year(self, order="ASC"):
        """
        Retrieve books sorted by published year.
        """
        self.__cursor.execute(f"SELECT * FROM books ORDER BY published_year {order}")

        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)

    def count_books(self):
        """
        Count the total number of books in the 'books' table.
        """
        self.__cursor.execute("SELECT COUNT(*) FROM books")
        rows = self.__cursor.fetchall()
        for row in rows:
            print(row)

    def price_statistics(self):
        """
        Display min, max, and average price of books.
        """
        self.cursor.execute(
            "SELECT MIN(price), MAX(price), AVG(price) FROM books"
        )

        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

