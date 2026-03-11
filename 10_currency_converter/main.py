import requests

def get_rate(base, target, sm):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base}")
    data = response.json()
    res = data["rates"][target] * sm
    return res


LINE_WIDTH = 45
print('=' * LINE_WIDTH)
print('КОНВЕРТЁР ВАЛЮТ')
print('=' * LINE_WIDTH)

currency1 = input("Введите исходную валюту (например USD): ")
currency2 = input("Введите целевую валюту (например RUB): ")
amount = float(input(f"Сколько {currency1} конвертируем в {currency2}?: "))

result = get_rate(currency1, currency2, amount)

print(f"{amount} {currency1} - {result} {currency2}")