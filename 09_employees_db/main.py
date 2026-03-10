import os
import json

FILE = "employees.json"

def save():
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(employees, file, ensure_ascii=False, indent=2)

def print_all(employees):
    if not employees:
        print("Сотрудники не найдены")
        return
    
    print("СОТРУДНИКИ:")
    for emp_id in employees:
        employee = employees[emp_id]
        name = employee["name"]
        department = employee["department"]
        salary = employee["salary"]
        print(f'{emp_id}(id): {name} ({department}) - {salary}')
    print()

def add_employees(employees):
    try:
        name = input("Имя сотрудника: ")
        department = input("Отдел сотрудника: ")
        salary = int(input("Зарплата сотрудника: "))
        if not name or not department or not salary:
            print("Имя, отдел и зарплата не должны быть пустыми")
            return
    except ValueError:
        print("Зарплата должна быть числом")
        return
    id = max(int(id) for id in employees) + 1 if employees else 1
    employees[id] = {"name": name, "department": department, "salary": salary}
    print("Сотрудник сохранен")

def remove_employee(employees):
    try:
        id = int(input("Введите id сотрудника которого требуется удалить: "))
        if id in employees:
            del employees[id]
            print("Сотрудник удален")
            return
        else:
            print("Введённое id не найдено")
            return
    except ValueError:
        print("id должно быть числом")
        return

def raise_salary_by_department(employees):
    print("1. Повысить зарплату отделу")
    print("2. Понизить зарплату отделу")
    try:
        raise_or_lower = int(input("Выберите действие (1-2): "))
        if not (1 <= raise_or_lower <= 2):
            print("Число должно быть от 1 до 2")
            return
    except ValueError:
        print("Действие должно быть числом")
        return
    try:
        percent = int(input("На сколько процентов (Введите цифру): "))
    except ValueError:
        print("Процент должен быть числом")
        return
    department = input("Какому отделу: ")
    if not department:
        print("Отдел не должен быть пустым")
        return
    found = False
    for emp_id, employee in employees.items():
        if employee["department"] == department:
            found = True
            employee["salary"] = int(employee["salary"] * ((1 + percent / 100) if raise_or_lower == 1 else (1 - percent / 100)))
    if not found:
        print("Отдел не найден")
        return

def fot_by_department(employees):
    department = input("ФОТ какого отдела вы хотите узнать: ")
    total = 0
    found = False
    for emp_id, employee in employees.items():
        if employee["department"] == department:
            found = True
            total += employee["salary"]
    if found:
        print(f"ФОТ отдела {department} {total} руб.")
    else:
        print("Отдел не найден")

if os.path.exists(FILE):
    try:
        with open(FILE, encoding="utf-8") as file:
            employees = json.load(file)
    except json.JSONDecodeError:
        print("Файл битый! Создаю новый")
        employees = {}
else:
    employees = {}

while True:
    print()
    print_all(employees)
    print()
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Повысить или понизить зарплату в отделе")
    print("4. ФОТ по отделу")
    print("5. Выход")

    try:
        num = int(input("Выберите действие (1-5): "))
        if not (1 <= num <= 5):
            print("Введённое число должно быть от 1 до 5")
            continue
    except ValueError:
        print("Введите число")
        continue

    if num == 1:
        add_employees(employees)
        save()
    elif num == 2:
        remove_employee(employees)
        save()
    elif num == 3:
        raise_salary_by_department(employees)
        save()
    elif num == 4:
        fot_by_department(employees)
    elif num == 5:
        break