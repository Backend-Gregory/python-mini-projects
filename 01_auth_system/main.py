import os

if os.path.exists('auth.txt'):
    print('=' * 45)
    print('ВХОД В СИСТЕМУ')
    print('=' * 45)
    if os.path.exists('status.txt'):
        print('Вы заблокированы! Попыток не осталось.')
    else:
        with open('auth.txt', encoding='utf-8') as auth:
            attempts = 3
            while True:
                login = input('Логин: ')
                password = input('Пароль: ')
                status = None
                auth.seek(0)
                if login == auth.readline().strip() and \
                password == auth.readline().strip():
                    status = True
                    print('Добро пожаловать!')
                    break
                else:
                    if attempts > 0:
                        status = False
                        print(f'Неверно! Осталось {attempts} попыток.')
                        attempts -= 1
                    else:
                        with open('status.txt', 'w', encoding='utf-8'):
                            print('Вы заблокированы! Попыток больше не осталось.')
                            break
            
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