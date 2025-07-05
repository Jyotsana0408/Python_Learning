class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f" '{self.title}' by {self.author} — {status}")


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def display_user(self):
        print(f"\n User: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"  - {book.title} by {book.author}")
        else:
            print("No books borrowed.")


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def register_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def borrow_book(self, user, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                user.borrowed_books.append(book)
                print(f" '{title}' borrowed by {user.name}")
                return
        print(f" '{title}' is not available.")

    def return_book(self, user, title):
        for book in user.borrowed_books:
            if book.title == title:
                book.is_available = True
                user.borrowed_books.remove(book)
                print(f" '{title}' returned by {user.name}")
                return
        print(f" '{title}' not found in {user.name}'s borrowed list.")

    def display_books(self):
        print("\n Library Books:")
        if not self.books:
            print("No books in library.")
        for book in self.books:
            book.display()



lib = Library()
lib.add_book("Python Basics", "Jyotsna Sahu")
lib.add_book("OOP Design", "Robert Martin")

user1 = lib.register_user("Amit")

lib.display_books()

lib.borrow_book(user1, "Python Basics")
user1.display_user()

lib.return_book(user1, "Python Basics")
lib.display_books()


