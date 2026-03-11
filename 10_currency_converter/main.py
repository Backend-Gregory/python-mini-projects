import requests

def get_rate(base, target, sm):
    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if target in data["rates"]:
                res = data["rates"][target] * sm
                print(f"{sm} {base} - {res:.2f} {target}")
            else:
                print(f"Валюта {target} не найдена")
        else:
            print(f"Ошибка сервера: {response.status_code}")
    except requests.ConnectionError:
        print("Нет подключения к интернету")
    except requests.Timeout:
        print("Сервер слишком долго отвечает")
    except Exception as e:
        print(f"Неизвестная ошибка {e}")

LINE_WIDTH = 45
print('=' * LINE_WIDTH)
print('КОНВЕРТЁР ВАЛЮТ')
print('=' * LINE_WIDTH)

while True:
    currency1 = input("Введите исходную валюту (например USD): ").upper()
    currency2 = input("Введите целевую валюту (например RUB): ").upper()
    if not currency1 or not currency2:
        print("Валюты не могут быть пустыми")
        continue
    try:
        amount = float(input(f"Сколько {currency1} конвертируем в {currency2}?: "))
        if amount <= 0:
            print("Сумма конвертации должна быть больше 0")
            continue
    except ValueError:
        print("Сумма конвертации должна состоять из цифр")
        continue

    get_rate(currency1, currency2, amount)

    exit_true = False
    while True:
        exit = input("Хотите конвертировать ещё что нибудь? (да/нет): ").lower()
        if exit != "нет" and exit != "да":
            print("Ошибка! введите да или нет")
            continue
        if exit == 'нет':
            exit_true = True
            break
        else:
            break
    
    if exit_true:
        break