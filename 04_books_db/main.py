LINE_WIDTH = 45
LIBRARY = 'library.txt'

def add_book(book, author, year):
    with open(LIBRARY, 'a', encoding='utf-8') as library:
        library.write(f'{book}|{author}|{year}\n')

def search_by_author(author):
    with open(LIBRARY, encoding='utf-8') as library:
        res = []
        for i in library:
            l = tuple(i.strip().split('|'))
            if l[1] == author:
                res.append((l[0], l[2]))
        return res
    
def get_all_books():
    books = []
    with open(LIBRARY, encoding='utf-8') as library:
        for line in library:
            parts = tuple(line.strip().split('|'))
            books.append((parts[0], parts[1], int(parts[2])))
        return books


print("=" * LINE_WIDTH)
print('База данных "Книги"')
print('=' * LINE_WIDTH)
while True:
    print()
    print('1. Добавить книгу')
    print('2. Поиск по автору')
    print('3. Сортировка по году')
    print('4. Показать все')

    num = int(input('Выбери действие (1-4): '))
    if num == 1:
        book = input('Название книги: ')
        author = input('Автор книги: ')
        year = input('Год выпуска: ')
        add_book(book, author, year)
        print('✅ Книга добавлена!')
    elif num == 2:
        author = input('Автор книги: ')
        books = search_by_author(author)
        if books:
            print()
            print(f'Книги автора {author}:')
            for i in books:
                print(f"{i[0]} ({i[1]} год)")
        else:
            print(f'Книги автора {author} не найдены.')
    else:
        books = get_all_books()
        if num == 3:
            books = sorted(books, key=lambda x: x[2])
            print()
            print("Все книги сортированые по году:")
        for book in books:
            print(f"{book[0]} - {book[1]} ({book[2]} год)")
    inp = input('Хотите продолжить? (да/нет)').lower()
    if inp == 'нет':
        break