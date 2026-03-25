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
        return self.name == other.name
    
    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        if self.name == other.name:
            obj = Product(self.name, self.price, self.quantity + other.quantity)
            return obj
        else:
            return None