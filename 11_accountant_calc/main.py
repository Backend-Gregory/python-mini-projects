from decimal import Decimal, ROUND_HALF_UP as R

def get_amount_and_calculate(percent_value, e="грязными"):
    amount = Decimal(input(f"Введите зарплату ({e}): "))
    percent = Decimal(percent_value)
    if e == "грязными":
        res = amount * (percent / 100)
    else:
        res = amount * 100 / (100 - percent)
    rounded = res.quantize('0.01', rounding=R)
    print(f"{rounded}₽")

LINE_WIDTH = 45

print('=' * LINE_WIDTH)
print('БУХГАЛТЕРСКИЙ КАЛЬКУЛЯТОР')
print('=' * LINE_WIDTH)
while True:
    print()
    print('1. Рассчитать НДФЛ (13%): ')
    print('2. Рассчитать страховые взносы (30%): ')
    print('3. Рассчитать сумму "грязными" (указывай чистыми): ')
    print('4. Выход')

    num = int(input('Выберите действие (1-4): '))
    if num == 1:
        get_amount_and_calculate('13')
    elif num == 2:
        get_amount_and_calculate('30')
    elif num == 3:
        get_amount_and_calculate('13', "чистыми")
    elif num == 4:
        break
