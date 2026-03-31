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
    
print('=' * LINE_WIDTH)
print('УЧЁТ ПРОДАЖ')
print('=' * LINE_WIDTH)

print('\n1. Добавить продажу')
print('2. Показать отчёт')
print('3. Выход')
num = int(input('Выберите действие (1-3): '))