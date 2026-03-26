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
    
    def _find_user(self, name):
        return next((u for u in self.users if u.name == name), None)

    def _find_book(self, title):
        return next((b for b in self.books if b.title == title), None)
    
    def borrow_book(self, title_book, user_name):
        user = self._find_user(user_name)
        book = self._find_book(title_book)
        if not user:
            print("Пользователь не найден")
            return
        if not book:
            print("Книга не найдена")
            return
        
        for user in self.users:
            if book in user.borrowed:
                print(f'Книга {title_book} уже выдана')
                return
        user.borrow(book)
        print(f'Книга выдана пользователю: {user.name}')
    
    def return_book(self, title_book, user_name):
        user = self._find_user(user_name)

        if not user:
            print("Пользователь не найден")
            return
        
        book = next((book for book in user.borrowed if title_book == book.title), None)

        if not book:
            print("Книга не найдена")
            return

        user.borrowed.remove(book)
        print('Книга сдана')