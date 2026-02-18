from datetime import datetime
while True:
    print('1. Записать новую запись')
    print('2. Показать все записи')
    print('3. Найти запись по дате')
    print('4. Выход')
    num = int(input('Выберите действие(1-4): '))
    if num == 1:
        with open('diary.txt', 'a', encoding='utf-8') as diary:
            now = datetime.now()
            now_f = now.strftime('%Y-%m-%d %H:%M')
            record = input('Введите запись: ')
            diary.write(f"[{now_f}] {record}\n")
    elif num == 2:
        with open('diary.txt', encoding='utf-8') as diary:
            file = diary.read()
            print(file)
    elif num == 4:
        break