class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Товар: {self.name}, цена: {self.price}, остаток: {self.quantity}'
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.price == other.price
    
    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        if self.name == other.name:
            obj = Product(self.name, self.price, self.quantity + other.quantity)
            return obj
        else:
            return None
        
    def __len__(self):
        return self.quantity
    
    def __bool__(self):
        return self.quantity > 0


stock = []

def valid(text_value, text_valid, e=int):
    while True:
        try:
            value = e(input(text_value))
            return value
        except ValueError:
            print(text_valid)

while True:
    print('1. Добавить товар')
    print('2. Показать все товары')
    print('3. Выход')
    num = int(input('Выберите действие: '))

    if num == 1:
        name = valid('Введите название товара: ', 'Название не может быть пустым', str)
        price = valid('Введите цену товара: ', 'Цена должна быть числом', float)
        qty = valid('Введите количество товара: ', 'Количество должно быть числом', int)
        obj = Product(name, price, qty)
        for i, existing in enumerate(stock):
            if existing == obj:
                stock[i] = existing + obj
                break
        else:
            stock.append(obj)

    elif num == 2:
        if not stock:
            print('Склад пуст')
            continue
        for t in stock:
            print(t)