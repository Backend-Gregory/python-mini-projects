LINE_WIDTH = 45
LIBRARY = 'library.txt'

def add_book(book, author, year):
    with open(LIBRARY, 'a', encoding='utf-8') as library:
        library.write(f'{book}|{author}|{year}\n')

print("=" * LINE_WIDTH)
print('База данных "Книги"')
print('=' * LINE_WIDTH)
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