import json
import os
LINE_WIDTH = 45
FILE = 'grades.json'

def add_grade(grades):
    name = input('Имя студента: ').strip()
    lesson = input('Урок оценивания: ').strip()
    try:
        grade = int(input('Оценка: ').strip())
        if not(1 <= grade <= 5):
            print('Оценка должна быть от 1 до 5')
            return
    except ValueError:
        print('Оценка должна быть числом')
        return
    if not name or not lesson or not grade:
        print('Ввод не должен быть пустым.')
        return

    grades.setdefault(name, {})
    grades[name].setdefault(lesson, []).append(int(grade))

    try:
        with open(FILE, 'w', encoding='utf-8') as f:
            json.dump(grades, f, ensure_ascii=False, indent=2)
        print('Оценка сохранена.')
    except Exception:
        print('Что то пошло не так.')

def print_students(grades, e=2):
    for name in grades:
        print()
        print(f'{name}:')
        for lesson in grades[name]:
            grade = grades[name][lesson]
            gr = ','.join(map(str, grade))
            average = sum(grade) / len(grade)
            print(f'   {lesson}:', end=' ')
            if e == 2:
                print(gr, end='')
            print(f' [{average:.2f}]')

def get_student_average(grades, student):
    count = 0
    sm = 0
    if student in grades:
        name = grades[student]
        for lesson in name:
            grade = grades[student][lesson]
            count += len(grade)
            sm += sum(grade)
        average = sm / count
        return average
    else:
        return None

def average_score(grades):
    student = input('Имя студента: ')
    avg = get_student_average(grades, student)
    print()
    if avg is None:
        print(f'Студент {student} или нет оценок.')
    else:
        print(f'Средний балл студента {student}: {avg:.2f}')

def student_rating(grades):
    if not grades:
        return
    rating = []
    for student in grades:
        avg = get_student_average(grades, student)
        if avg is not None:
            rating.append((student, avg))
    rating.sort(key=lambda x: x[1], reverse=True)
    print()
    print('РЕЙТИНГ СТУДЕНТОВ:')
    for place, (student, avg) in enumerate(rating, 1):
        print(f'{place}. {student}: {avg:.2f}')


if os.path.exists(FILE):
    try:
        with open(FILE, encoding='utf-8') as f:
            grades = json.load(f)
    except json.JSONDecodeError:
        print('Файл повреждён. Создаю новый.')
        grades = {}
else:
    grades = {}

print('=' * LINE_WIDTH)
print('СИСТЕМА ОЦЕНОК СТУДЕНТОВ')
print('=' * LINE_WIDTH)

while True:
    print()
    print('1. Добавить оценку')
    print('2. Показать всех студентов')
    print('3. Средние по предметам')
    print('4. Общий средний балл студента')
    print('5. Рейтинг студентов')
    print('6. Выход')
    try:
        num = int(input('Выберите действие (1-6): '))
        if not (1 <= num <= 6):
            print('Ошибка! Введите число от 1 до 6')
    except ValueError:
        print('Ошибка! Введите число от 1 до 6')
        continue

    if num == 1:
        add_grade(grades)

    elif num == 2:
        print_students(grades)

    elif num == 3:
        print_students(grades, 3)

    elif num == 4:
        average_score(grades)

    elif num == 5:
        student_rating(grades)
    elif num == 6:
        break