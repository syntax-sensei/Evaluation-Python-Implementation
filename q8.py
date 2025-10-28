class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def borrow(self):
        self.copies -= 1

    def return_book(self):
        self.copies += 1


class EBook(Book):
    def __init__(self, title, author, isbn, copies, file_size):
        super.__init__(title, author, isbn, copies)
        self.file_size = file_size

    def borrow(self):
        print("Unlimited")


class Library:
    def __init__(self):
        self.__books = []
