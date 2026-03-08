import json
import os

FILE = "contacts.json"

if os.path.exists(FILE):
    with open(FILE, "r", encoding="utf-8") as f:
        contacts = json.load(f)
else:
    contacts = []

print("1. Добавить контакт")
print("2. Найти по имени")
print("3. Найти по номеру")
print("4. Показать все контакты")
print("5. Выход")
num = int(input("Выберите действие: "))

if num == 1:
    contact = {"name": input("Имя контакта: "), "number": input("Номер контакта: ")}
    contacts.append(contact)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
    print("Контакт сохранен")