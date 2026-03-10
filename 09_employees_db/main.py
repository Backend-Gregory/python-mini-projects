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
        print(f'{name} ({department}) - {salary}')
    print()

def add_employees(employees):
    name = input("Имя сотрудника: ")
    department = input("Отдел сотрудника: ")
    salary = int(input("Зарплата сотрудника: "))
    id = max(int(id) for id in employees) + 1 if employees else 1
    employees[id] = {"name": name, "department": department, "salary": salary}

def remove_employee(employees):
    id = int(input("Введите id сотрудника которого требуется удалить: "))
    del employees[id]
    print("Сотрудник удален")

def raise_salary_by_department(employees):
    print("1. Повысить зарплату отделу")
    print("2. Понизить зарплату отделу")
    raise_or_lower = int(input("Выберите действие (1-2): "))
    percent = int(input("На сколько процентов (Введите цифру): "))
    department = input("Какому отделу: ")
    for emp_id, employee in employees.items():
        if employee["department"] == department:
            employee["salary"] = int(employee["salary"] * ((1 + percent / 100) if raise_or_lower == 1 else (1 - percent / 100)))

def fot_by_department(employees):
    department = input("ФОТ какого отдела вы хотите узнать: ")
    total = 0
    for emp_id, employee in employees.items():
        if employee["department"] == department:
            total += employee["salary"]
    print(f"ФОТ отдела {department} {total} руб.")

if os.path.exists(FILE):
    with open(FILE, encoding="utf-8") as file:
        employees = json.load(file)
else:
    employees = {}

print_all(employees)

while True:
    print("1. Добавить сотрудника")
    print("2. Удалить сотрудника")
    print("3. Повысить или понизить зарплату в отделе")
    print("4. ФОТ по отделу")
    print("5. Выход")

    num = int(input("Выберите действие (1-5): "))
    if num == 1:
        add_employees(employees)
        save()
        print("Сотрудник сохранен")
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