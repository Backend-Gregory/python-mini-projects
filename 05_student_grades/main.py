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
            print(f' [{average}]')
            

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
print('3. Средние по предметам (студент)')
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