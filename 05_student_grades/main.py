import json
import os
LINE_WIDTH = 45
FILE = 'grades.json'

def add_grade(grades):
    name = input('Имя студента: ')
    lesson = input('Урок оценивания: ')
    grade = input('Оценка: ')

    grades.setdefault(name, {})
    grades[name].setdefault(lesson, []).append(int(grade))

    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(grades, f, ensure_ascii=False, indent=2)
    print('Оценка сохранена.')

def print_students(grades, e=2):
    for name in grades:
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
    student = input('Средний балл студента: ')
    avg = get_student_average(grades, student)
    if avg is None:
        print(f'Студент {student} или нет оценок.')
    else:
        print(f'Средний балл студента {student}: {avg:.2f}')

def student_rating(grades):
    rating = []
    for student in grades:
        avg = get_student_average(grades, student)
        if avg is not None:
            rating.append((student, avg))
    rating.sort(key=lambda x: x[1], reverse=True)
    print('РЕЙТИНГ СТУДЕНТОВ')
    for place, (student, avg) in enumerate(rating, 1):
        print(f'{place}. {student}: {avg:.2f}')


if os.path.exists(FILE):
    with open(FILE, encoding='utf-8') as f:
        grades = json.load(f)
else:
    grades = {}

print('=' * LINE_WIDTH)
print('СИСТЕМА ОЦЕНОК СТУДЕНТОВ')
print('=' * LINE_WIDTH)
print()
print('1. Добавить оценку')
print('2. Показать всех студентов')
print('3. Средние по предметам')
print('4. Общий средний балл студента')
print('5. Рейтинг студентов')
print('6. Выход')
num = int(input('Выберите действие (1-6): '))

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