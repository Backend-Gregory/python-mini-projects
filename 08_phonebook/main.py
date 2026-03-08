import json
import os

LINE_WIDTH = 45
FILE = "contacts.json"

if os.path.exists(FILE):
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            contacts = json.load(f)
    except json.JSONDecodeError:
        print("Файл поврежден! Создаю новый.")
        contacts = []
else:
    contacts = []

def add_contact(contacts):
    name = input("Имя контакта: ")
    number = input("Номер контакта: ")
    if not name or not number:
        print("Имя и номер не могут быть пустыми")
        return
    contact = {"name": name, "number": number}
    contacts.append(contact)

    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=2)
        print("Контакт сохранен")
    except PermissionError:
        print("Ошибка: Нет прав на запись в файл")
    except OSError as e:
        print(f"Ошибка записи: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

def find_by_name_or_number(contacts, value, key):
    if contacts:
        found = False
        for ch in contacts:
            if ch[key].lower() == value.lower():
                print(f"{ch['name']}: {ch['number']}")
                found = True
        if not found:
            print('Контакт не найден.')
    else:
        print("У вас нет ни одного контакта.")

def print_contacts(contacts):
    if contacts:
        print()
        for ch in contacts:
            print(f"{ch['name']}: {ch['number']}")
    else:
        print("У вас нет ни одного контакта.")

print('=' * LINE_WIDTH)
print('Телефонный справочник')
print('=' * LINE_WIDTH)
while True:
    print()
    print("1. Добавить контакт")
    print("2. Найти по имени")
    print("3. Найти по номеру")
    print("4. Показать все контакты")
    print("5. Выход")
    try:
        num = int(input("Выберите действие: "))
        if not (1 <= num <= 5):
            print("Ошибка! Введите число от 1 до 5")
            continue
    except ValueError:
        print("Ошибка! Введите число")
        continue

    if num == 1:
        add_contact(contacts)

    elif num == 2:
        name = input("Введите имя: ")
        by = 'name'
        find_by_name_or_number(contacts, name, by)

    elif num == 3:
        number = input("Введите номер: ")
        by = 'number'
        find_by_name_or_number(contacts, number, by)

    elif num == 4:
        print_contacts(contacts)
    
    elif num == 5:
        break