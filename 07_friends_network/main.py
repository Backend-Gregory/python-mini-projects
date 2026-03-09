import json
import os

LINE_WIDTH = 45
FILE = 'friends.json'

def mutual_friends(dict_friends, user1, user2):
    if user1 not in dict_friends or user2 not in dict_friends:
        print("Ошибка! Оного из пользователей нету в списке")
        return
    
    user1_friends = set(dict_friends[user1])
    user2_friends = set(dict_friends[user2])
    mutual_friends = user1_friends & user2_friends

    if not mutual_friends:
        print('Общих друзей нет')
    else:
        res = ', '.join(mutual_friends)
        print(f"Общие друзья: {res}")


print('=' * LINE_WIDTH)
print('ПОИСК ДРУЗЕЙ В СОЦСЕТИ')
print('=' * LINE_WIDTH)

if not os.path.exists(FILE):
    print('Введите имя и после ":" друзей через запятую (или "стоп" для завершения):')
    dict_friends = {}
    while True:
        s = input()
        if 'стоп' in s.lower():
            break
        name, friends = s.split(":")
        friends = [friend.strip() for friend in friends.split(",")]
        dict_friends[name] = list(set(friends))
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(dict_friends, file, ensure_ascii=False, indent=2)

else:
    with open(FILE, encoding='utf-8') as file:
        dict_friends = json.load(file)

users = ', '.join(dict_friends.keys())
print(f'Доступные пользователи: {users}')

print()
print('1. Найти общих друзей')
print('2. Найти взаимных друзей')
print('3. Получить рекомендации')
print('4. Выход')
num = int(input("Выберите действие: "))

if num == 1:
    user1 = input("Введите первого пользователя: ").strip()
    user2 = input("Введите второго пользователя: ").strip()
    mutual_friends(dict_friends, user1, user2)
