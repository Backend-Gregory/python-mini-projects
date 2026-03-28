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

library = Library()
while True:
    print('\n1. Добавить книгу')
    print('2. Добавить читателя')
    print('3. Выдать книгу')
    print('4. Вернуть книгу')
    print('5. Показать книги')
    print('6. Показать читателей')
    print('7. Показать выдачи')
    print('8. Выход')
    num = int(input('Выберите действие: '))
    if num == 1:
        title = input('Введите название книги: ')
        author = input('Введите автора: ')
        year = int(input('Введите год: '))
        book = Book(title, author, year)
        library.add_book(book)
        print('✅ Книга добавлена')
    
    elif num == 2:
        name = input('Введите свое имя: ')
        user = User(name)
        library.add_users(user)
        print('✅ Читатель добавлен')

    elif num == 3:
        name = input('Имя читателя: ')
        title_book = input('Название книги: ')
        library.borrow_book(title_book, name)

    elif num == 4:
        name = input('Имя читателя: ')
        title_book = input('Название книги: ')
        library.return_book(title_book, name)
    
    elif num == 5:
        books = library.show_books()
        print('Книги:')
        for book in books:
            print(book)