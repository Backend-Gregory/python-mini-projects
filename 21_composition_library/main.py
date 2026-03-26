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