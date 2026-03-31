from datetime import datetime
FILE = 'sale.txt'
LINE_WIDTH = 45

class Sale:
    def __init__(self, date, product, category, amount):
        self.date = date
        self.product = product
        self.category = category
        self.amount = amount
    
    def __str__(self):
        return f'{self.date.strftime("%Y-%m-%d")}|{self.product}|{self.amount}'

def get_date(prompt):
    date_str = input(prompt)
    if not date_str:
        return datetime.now()
    try:
        res = datetime.strptime(date_str, "%Y-%m-%d")
        return res
    except ValueError:
        print("Ошибка! Используйте формат ГГГГ-ММ-ДД (или Enter для сегодня)")
        return get_date(prompt)

def read_lines(filename):
    with open(filename, encoding='utf-8') as file:
        for sale in file:
            sale_list = sale.split('|')
            date = datetime.strptime(sale_list[0], '%Y-%m-%d')
            product = sale_list[1]
            category = sale_list[2] if sale_list[2] else None
            amount = float(sale_list[3].strip())
            obj = Sale(date, product, category, amount)
            yield obj

def filter_sales(sales, start, end, category):
    for sale in sales:
        if sale.date < start or sale.date > end:
            continue
        if category and sale.category != category:
            continue
        yield sale

def valid(text_value, text_valid, e=str):
    while True:
        try:
            value = e(input(text_value))
            if value:
                return value
            else:
                print(text_valid)
        except ValueError:
            print(text_valid)

print('=' * LINE_WIDTH)
print('УЧЁТ ПРОДАЖ')
print('=' * LINE_WIDTH)
while True:
    print('\n1. Добавить продажу')
    print('2. Показать отчёт')
    print('3. Выход')
    num = valid('Выберите действие (1-3): ', 'Введите число от 1 до 3', int)
    if num not in [1, 2, 3]:
        print('Число должно быть от 1 до 3')
        continue

    if num == 1:
        date = get_date('Дата (ГГГГ-ММ-ДД):')
        product = valid('Товар: ', 'Товар не может быть пустым').lower()
        category = input('Категория (Enter для всех): ').strip().lower() or None
        amount = valid('Сумма: ', 'Сумма должна быть числом', float)
        with open(FILE, 'a', encoding='utf-8') as file:
            file.write(f"{date.strftime('%Y-%m-%d')}|{product}|{category}|{amount}\n")
        print('✅ Продажа добавлена')

    elif num == 2:
        start = get_date('Дата начала: ')
        end = get_date('Дата конца: ')
        category = input('Категория (Enter для всех): ').strip().lower() or None
        total = 0
        count = 0
        print()
        for sale in filter_sales(read_lines(FILE), start, end, category):
            print(sale)
            count += 1
            total += sale.amount
        
        print(f'Итого: {count} продаж, сумма: {total}₽')
    
    else:
        break