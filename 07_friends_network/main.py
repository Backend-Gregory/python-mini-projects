import json
import os

LINE_WIDTH = 45
FILE = 'friends.json'

def get_friends_sets(dict_friends):
    friends_set = {}
    for user in dict_friends:
        friends_set[user] = set(dict_friends[user])
    return friends_set

def mutual_friends(dict_friends, user1, user2):
    if user1 not in dict_friends or user2 not in dict_friends:
        print("Ошибка! Одного из пользователей нет в списке")
        return
    
    user1_friends = set(dict_friends[user1])
    user2_friends = set(dict_friends[user2])
    mutual_friends = user1_friends & user2_friends

    if not mutual_friends:
        print('Общих друзей нет')
    else:
        res = ', '.join(mutual_friends)
        print(f"Общие друзья: {res}")

def find_mutual(dict_friends):
    print()
    print('Взаимные друзья:')
    friends_set = get_friends_sets(dict_friends)
    
    for user1 in friends_set:
        for user2 in friends_set[user1]:
            if user2 in friends_set and user1 in friends_set[user2] and user1 < user2:
                print(f"{user1.capitalize()} и {user2.capitalize()}")

def recommendation(dict_friends, user):
    if user not in dict_friends:
        print(f"Пользователь {user} не найден")
        return
    friends_set = get_friends_sets(dict_friends)

    res = set()
    for friend in friends_set[user]:
        if friend in friends_set:
            res |= friends_set[friend]
    res -= friends_set[user]
    res.discard(user)
    user = user.capitalize()
    if res:
        print(f'Рекомендации для пользователя {user}: {", ".join(r.capitalize() for r in res)}')
    else:
        print(f'Для пользователя {user} нет рекомендаций')

print('=' * LINE_WIDTH)
print('ПОИСК ДРУЗЕЙ В СОЦСЕТИ')
print('=' * LINE_WIDTH)

if not os.path.exists(FILE):
    print('Введите имя и после ":" друзей через запятую (или "стоп" для завершения):')
    dict_friends = {}
    while True:
        s = input().strip()
        if not s:
            print("Ввод не может быть пустым")
            continue
        if 'стоп' in s.lower():
            break
        if ":" not in s:
            print("Ошибка! Неправильный формат ввода (имя: друзья через ',')")
            continue
        name, friends = s.split(":", 1)
        if not name:
            print("Имя не может быть пустым")
            continue
        name = name.lower()
        friends = [friend.strip().lower() for friend in friends.split(",")]
        dict_friends[name] = list(set(friends))
    with open(FILE, 'w', encoding='utf-8') as file:
        json.dump(dict_friends, file, ensure_ascii=False, indent=2)
else:
    try:
        with open(FILE, encoding='utf-8') as file:
            dict_friends = json.load(file)
    except json.JSONDecodeError:
        print("⚠️ Файл повреждён. Создаю новый.")
        dict_friends = {}


users = ', '.join(dict_friends.keys()) or "нет пользователей"
while True:
    print()
    print(f'Доступные пользователи: {users}')

    print()
    print('1. Найти общих друзей')
    print('2. Найти взаимных друзей')
    print('3. Получить рекомендации')
    print('4. Выход')
    try:
        num = int(input("Выберите действие (1-4): "))
        if not(1 <= num <= 4):
            print("Ошибка! Введите число от 1 до 4")
            continue
    except ValueError:
        print("Ошибка! Введите число")
        continue

    if num == 1:
        user1 = input("Введите первого пользователя: ").strip().lower()
        user2 = input("Введите второго пользователя: ").strip().lower()
        mutual_friends(dict_friends, user1, user2)

    elif num == 2:
        find_mutual(dict_friends)

    elif num == 3:
        user = input('Введите пользователя: ').lower()
        recommendation(dict_friends, user)

    elif num == 4:
        break