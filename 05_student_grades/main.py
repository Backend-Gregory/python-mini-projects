import json
import os
LINE_WIDTH = 45
FILE = 'grades.json'
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
    name = input('Имя студента: ')
    lesson = input('Урок оценивания: ')
    grade = input('Оценка: ')
    if os.path.exists(FILE):
        with open(FILE, encoding='utf-8') as f:
            grades = json.load(f)
    else:
        grades = {}
    grades.setdefault(name, {})
    grades[name].setdefault(lesson, []).append(int(grade))

    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(grades, f, ensure_ascii=False, indent=2)
    print('Оценка сохранена.')