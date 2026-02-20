import os
import time

BLOCK_TIME = 900
AUTH_FILE = 'auth.txt'
LOCK_FILE = 'lockout.txt'
LINE_WIDTH = '=' * 45

if os.path.exists(AUTH_FILE):
    print(LINE_WIDTH)
    print('ВХОД В СИСТЕМУ')
    print(LINE_WIDTH)

    if os.path.exists(LOCK_FILE):
        with open(LOCK_FILE, encoding='utf-8') as lock:
            unlock_time = float(lock.read())

        if time.time() < unlock_time:
            time_ost = int((unlock_time - time.time()) / 60)
            print(f'До разблокировки осталось {time_ost} минут')
            exit()
        else:
            os.remove(LOCK_FILE)

    with open(AUTH_FILE, encoding='utf-8') as auth:
        attempts = 3
        while True:
            login = input('Логин: ')
            password = input('Пароль: ')
            status = None
            auth.seek(0)

            if login == auth.readline().strip() and \
            password == auth.readline().strip():
                status = True
                print(f"Статус: {status}")
                print('Добро пожаловать!')
                break

            else:
                if attempts > 0:
                    status = False
                    print(f"Статус: {status}")
                    print(f'Неверно! Осталось {attempts} попыток.')
                    attempts -= 1

                else:
                    unlock_time = time.time() + BLOCK_TIME
                    with open(LOCK_FILE, 'w', encoding='utf-8') as lockout:
                        lockout.write(str(unlock_time))
                        print(f'Попыток не осталось! Вы заблокированы на 15 минут.')
                            
            
else:
    print(LINE_WIDTH)
    print('ДОБРО ПОЖАЛОВАТЬ!')
    print(LINE_WIDTH)
    print('Это ваш первый запуск.')
    print('Необходимо зарегистрироваться.')
    print()
    
    with open(AUTH_FILE, 'a', encoding='utf-8') as auth:
        login = input('Придумайте логин: ')
        password = input('Придумайте пароль: ')
        auth.write(login + '\n')
        auth.write(password)