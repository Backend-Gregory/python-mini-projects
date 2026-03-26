class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} ({self.author}), год: {self.year}'
    
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def borrow(self, book):
        self.borrowed.append(book)

    def __str__(self):
        return f'{self.name}: {len(self.borrowed)} книг'
    
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_users(self, user):
        self.users.append(user)
    
    def show_loans(self):
        res = [user.borrowed for user in self.users]
        return res
    
    def show_books(self):
        return self.books
    
    def show_users(self):
        return self.users