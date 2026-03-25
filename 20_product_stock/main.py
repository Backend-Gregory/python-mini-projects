class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Товар: {self.name}, цена: {self.price}, остаток: {self.quantity}'