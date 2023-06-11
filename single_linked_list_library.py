class Book:
    def __init__(self, title):
        self.title = title
        self.next_book = None


class Visitor:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = None

    def borrow_book(self, title):
        new_book = Book(title)
        if self.borrowed_books is None:
            self.borrowed_books = new_book
        else:
            current_book = self.borrowed_books
            while current_book.next_book is not None:
                current_book = current_book.next_book
            current_book.next_book = new_book

    def print_borrowed_books(self):
        if self.borrowed_books is None:
            print("Tidak ada buku yang dipinjam oleh", self.name)
        else:
            print("Buku yang dipinjam oleh", self.name, ":")
            current_book = self.borrowed_books
            while current_book is not None:
                print("-", current_book.title)
                current_book = current_book.next_book


# Contoh penggunaan program
visitor1 = Visitor("Mika")
visitor1.borrow_book("Judul Buku :" "Harry Potter")
visitor1.borrow_book("Daftar Buku :" "MPK01")

visitor2 = Visitor("Arga")
visitor2.borrow_book("Judul Buku:" "The Great Gatsby")
visitor2.borrow_book("Daftar Buku :" "MPK03")

visitor3 = Visitor("Charlie")
visitor3.borrow_book("Judul Buku :" "To Kill a Mockingbird")
visitor3.borrow_book("Daftar Buku :" "MPK05")

visitor1.print_borrowed_books()
visitor2.print_borrowed_books()
visitor3.print_borrowed_books()
 