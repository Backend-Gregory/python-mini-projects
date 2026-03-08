import json
import os

FILE = "contacts.json"

if os.path.exists(FILE):
    with open(FILE, "r", encoding="utf-8") as f:
        contacts = json.load(f)
else:
    contacts = []

def add_contact(contacts):
    name = input("Имя контакта: ")
    number = input("Номер контакта: ")
    contact = {"name": name, "number": number}
    contacts.append(contact)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    print("Контакт сохранен")

def find_by_name(contacts):
    name = input("Введите имя: ")
    if contacts:
        for ch in contacts:
            if ch['name'] == name:
                print(f'{name}: {ch['number']}')
                break
        else:
            print('Контакт не найден')
    else:
        print("У вас нет ни одного контакта.")

def print_contacts(contacts):
    if contacts:
        for ch in contacts:
            print(f'{ch['name']}: {ch['number']}')
    else:
        print("У вас нет ни одного контакта.")

print("1. Добавить контакт")
print("2. Найти по имени")
print("3. Найти по номеру")
print("4. Показать все контакты")
print("5. Выход")
num = int(input("Выберите действие: "))

if num == 1:
    add_contact(contacts)

elif num == 2:
    find_by_name(contacts)

elif num == 4:
    print_contacts(contacts)