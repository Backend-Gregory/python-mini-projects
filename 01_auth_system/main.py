import os
if os.path.exists('auth.txt'):
    print('=' * 45)
    print('ВХОД В СИСТЕМУ')
    print('=' * 45)
else:
    print('=' * 45)
    print('ДОБРО ПОЖАЛОВАТЬ!')
    print('=' * 45)
    print('Это ваш первый запуск.')
    print('Необходимо зарегистрироваться.')
    print()
    with open('auth.txt', 'a', encoding='utf-8') as auth:
        login = input('Придумайте логин: ')
        password = input('Придумайте пароль: ')
        auth.write(login + '\n')
        auth.write(password)