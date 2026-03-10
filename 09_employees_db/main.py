import os
import json

FILE = "employees.json"

def save():
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(employees, file, ensure_ascii=False, indent=2)

def add_employees(employees):
    name = input("Имя сотрудника: ")
    department = input("Отдел сотрудника: ")
    salary = int(input("Зарплата сотрудника: "))
    id = len(employees) + 1
    employees[id] = {"name": name, "department": department, "salary": salary}
    

if os.path.exists(FILE):
    with open(FILE, encoding="utf-8") as file:
        employees = json.load(file)
else:
    employees = {}

print("1. Добавить сотрудника")
print("2. Повысить или понизить зарплату в отделе")
print("3. ФОТ по отделу")
print("4. Выход")

num = int(input("Выберите действие: "))
if num == 1:
    add_employees(employees)
    save()
    print("Сотрудник сохранен")

