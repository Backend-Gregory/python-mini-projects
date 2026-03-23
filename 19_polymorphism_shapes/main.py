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