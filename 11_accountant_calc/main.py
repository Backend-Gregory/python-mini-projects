from decimal import Decimal, ROUND_HALF_UP as R, InvalidOperation, DivisionByZero

def get_amount_and_calculate(percent_value, e="грязными"):
    try:
        amount = Decimal(input(f"Введите зарплату ({e}): "))
        percent = Decimal(percent_value)
        
        if not amount:
            print("Сумма не может быть пустой")
            return

        if e == "грязными":
            res = amount * (percent / 100)
        else:
            res = amount * 100 / (100 - percent)

    except InvalidOperation:
        print("Ошибка! Введите число, используя точку (например 100.50)")
        return
    except DivisionByZero:
        print("Ошибка! Деление на ноль")
        return
    
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

    try:
        num = int(input('Выберите действие (1-4): '))
        if not (1 <= num <= 4):
            print("Число должо быть от 1 до 4")
            continue
    except ValueError:
        print("Введите число")
        continue

    if num == 1:
        get_amount_and_calculate('13')
    elif num == 2:
        get_amount_and_calculate('30')
    elif num == 3:
        get_amount_and_calculate('13', "чистыми")
    elif num == 4:
        break
