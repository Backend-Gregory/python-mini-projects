from math import pi
class Shape():
    def area(self):
        return 0
    
    def info(self):
        return 'Фигура'
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        res = pi * (self.radius ** 2)
        return res
    
    def info(self):
        return 'Круг'
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        res = self.width * self.height
        return res
    
    def info(self):
        return 'Прямоугольник'
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        res = 0.5 * self.base * self.height
        return res
    
    def info(self):
        return 'Треугольник'

def print_area(obj):
    print(f'{obj.info()}: площадь: {obj.area()}')

def valid(text_value, e=float):
    while True:
        try:
            value = e(input(text_value))
            return value
        except ValueError:
            print('Введите число')
while True:
    print('\n1. Круг')
    print('2. Прямоугольник')
    print('3. Треугольник')
    print('4. Выход')
    num = valid('Выберите фигуру (1-4): ', int)
    if num == 1:
        radius = valid('Введите радиус: ')
        obj = Circle(radius)
        print_area(obj)
    elif num == 2:
        width = valid('Введите ширину: ')
        height = valid('Введите высоту: ')
        obj = Rectangle(width, height)
        print_area(obj)
    elif num == 3:
        base = valid('Введите длинну основания: ')
        height = valid('Введите высоту: ')
        obj = Triangle(base, height)
        print_area(obj)
    else:
        break