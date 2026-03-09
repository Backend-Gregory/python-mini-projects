import json
LINE_WIDTH = 45
FILE = 'friends.json'
print('=' * LINE_WIDTH)
print('ПОИСК ДРУЗЕЙ В СОЦСЕТИ')
print('=' * LINE_WIDTH)
print('Введите имя и после ":" друзей через запятую (или "стоп" для завершения):')
dcit_friends = {}
while True:
    s = input()
    if 'стоп' in s.lower():
        break
    name, friends = s.split(":")
    friends = [friend.strip() for friend in friends.split(",")]
    dcit_friends[name] = friends
with open(FILE, 'w', encoding='utf-8') as file:
    json.dump(dcit_friends, file, ensure_ascii=False, indent=2)
