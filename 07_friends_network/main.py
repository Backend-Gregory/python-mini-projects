import json
import os

LINE_WIDTH = 45
FILE = 'friends.json'
print('=' * LINE_WIDTH)
print('ПОИСК ДРУЗЕЙ В СОЦСЕТИ')
print('=' * LINE_WIDTH)

if not os.path.exists(FILE):
    print('Введите имя и после ":" друзей через запятую (или "стоп" для завершения):')
    dcit_friends = {}
    while True:
        s = input()
        if 'стоп' in s.lower():
            break
        name, friends = s.split(":")
        friends = [friend.strip() for friend in friends.split(",")]
        dcit_friends[name] = list(set(friends))
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(dcit_friends, file, ensure_ascii=False, indent=2)

else:
    with open(FILE, encoding='utf-8') as file:
        dcit_friends = json.load(file)

users = ', '.join(dcit_friends.keys())
print(f'Доступные пользователи: {users}')

print('1. Найти общих друзей')
print('2. Найти взаимных друзей')
print('3. Получить рекомендации')
print('4. Выход')
num = int(input("Выберите действие: "))
