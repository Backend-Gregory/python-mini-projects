from decimal import Decimal, ROUND_HALF_UP as R

def Calculate(amount, percent):
    res = amount * (percent / 100)
    rounded = res.quantize(Decimal("0.01"), rounding=R)
    print(rounded)

LINE_WIDTH = 45

print('=' * LINE_WIDTH)
print('БУХГАЛТЕРСКИЙ КАЛЬКУЛЯТОР')
print('=' * LINE_WIDTH)
print()
print('1. Рассчитать НДФЛ (13%): ')
print('2. Рассчитать страховые взносы (30%): ')
print('3. Рассчитать сумму "грязными" (указывай чистыми): ')
print('4. Выход')
num = int(input('Выберите действие (1-4): '))
if num == 1:
    amount = Decimal(input("Введите зарплату (грязными): "))
    percent = Decimal('13')
    Calculate(amount, percent)