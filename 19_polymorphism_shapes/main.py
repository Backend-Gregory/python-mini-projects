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
    
    def info():
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