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
            date, product, category, amount = datetime.strptime(sale_list[0], '%Y-%m-%d'), sale_list[1], sale_list[2], sale_list[3]
            obj = Sale(date, product, category, amount)
            yield obj

def filter_sales(sales, start, end, category):
    for sale in sales:
        if sale.date < start or sale.date > end:
            continue
        if category and sale.category != category:
            continue
        yield sale

print('=' * LINE_WIDTH)
print('УЧЁТ ПРОДАЖ')
print('=' * LINE_WIDTH)

print('\n1. Добавить продажу')
print('2. Показать отчёт')
print('3. Выход')
num = int(input('Выберите действие (1-3): '))

if num == 1:
    date = get_date('Дата (ГГГГ-ММ-ДД):')
    product = input('Товар: ').strip()
    category = input('Категория: ').strip()
    amount = float(input('Сумма: '))
    with open(FILE, 'a', encoding='utf-8') as file:
        file.write(f'{date}|{product}|{category}|{amount}\n')
    print('✅ Продажа добавлена')