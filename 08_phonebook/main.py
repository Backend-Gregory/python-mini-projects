import json
import os
import logging

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s,",
    encoding='utf-8'
)

class ContactNotFoundError(Exception):
    pass

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

def add_contact(contacts: list[dict]) -> None:
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
    except PermissionError as e:
        print("Ошибка: Нет прав на запись в файл")
        logging.error(f'Ошибка записи в {FILE}: {e}')
    except OSError as e:
        print(f"Ошибка записи: {e}")
        logging.error(f'Ошибка записи в {FILE}: {e}')
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        logging.error(f'Неизвестная ошибка: {e}')

def find_by_name_or_number(contacts: list[dict], value: str, key: str) -> None:
    if not contacts:
        raise ContactNotFoundError('Список контактов пуст')
    
    found = False
    for ch in contacts:
        if ch[key].lower() == value.lower():
            print(f"{ch['name']}: {ch['number']}")
            found = True
    if not found:
        raise ContactNotFoundError('Контакт не найден.')

def print_contacts(contacts: list[dict]) -> None:
    if not contacts:
        raise ContactNotFoundError("У вас нет ни одного контакта.")
    print()
    for ch in contacts:
        print(f"{ch['name']}: {ch['number']}")

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
        try:
            find_by_name_or_number(contacts, name, by)
        except ContactNotFoundError as e:
            print(e)

    elif num == 3:
        number = input("Введите номер: ")
        by = 'number'
        try:
            find_by_name_or_number(contacts, number, by)
        except ContactNotFoundError as e:
            print(e)

    elif num == 4:
        try:
            print_contacts(contacts)
        except ContactNotFoundError as e:
            print(e)
    elif num == 5:
        break