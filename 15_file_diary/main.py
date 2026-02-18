from datetime import datetime
def get_choice():
    while True:
        try:
            value = int(input('Выберите действие(1-4): '))
            if 1 <= value <= 4:
                return value
            else:
                print("Ошибка! Число должно быть от 1 до 4")
        except ValueError:
            print("Ошибка! Введите число, а не текст")

while True:
    print('1. Записать новую запись')
    print('2. Показать все записи')
    print('3. Найти запись по дате')
    print('4. Выход')

    num = get_choice()
    if num == 1:
        with open('diary.txt', 'a', encoding='utf-8') as diary:
            now = datetime.now()
            now_f = now.strftime('%Y-%m-%d %H:%M')
            record = input('Введите запись: ')
            diary.write(f"[{now_f}] {record}\n")
    elif num == 2:
        try:
            with open('diary.txt', encoding='utf-8') as diary:
                file = diary.read()
                print(file)
        except FileNotFoundError:
            print('Ошибка! Файл не найден')
    elif num == 3:
        try:
            with open('diary.txt', encoding='utf-8') as diary:
                flag = False
                data = input("Введите дату (ГГГГ-ММ-ДД): ")
                for line in diary:
                    if line.startswith(f'[{data}'):
                        print(line.strip())
                        flag = True
                
                if not flag:
                    print("Записей на эту дату нет")
        except FileNotFoundError:
            print('Ошибка! Файл не найден')
    elif num == 4:
        break