"""
Задача 2:

Напишите программу, которая содержит несколько классов фигур: прямоугольник,
круг, треугольник, параллелограмм, ромб, трапеция и добавьте методы для
расчета площади каждой фигуры.

Пример:
rect = Rectangle(5, 10)
circle = Circle(3)
print(rect.area()) # 50
print(circle.area()) # ~28.27
"""

from math import pi, sqrt


class Rectangle():
    
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    
    def area(self) -> int:
        return round(self.a * self.b, 2)
    
    def __repr__(self):
        return f"Это прямоугольник... у него такая площадь: {self.area()}"


class Circle():
    
    def __init__(self, a: int):
        self.a = a
    
    def area(self) -> int:
        return round(pi * self.a**2, 2)
    
    def __repr__(self):
        return f"Это круг... у него такая площадь: {self.area()}"
    
    
class Triangle():
    
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> int:
        p = (self.a + self.b + self.c) / 2
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.b)), 2)
    
    def __repr__(self):
        return f"Это треугольник... у него такая площадь: {self.area()}"
    
    
class Parallelogram():
    
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
    
    def area(self) -> int:
        return round(self.a * self.b, 2)
    
    def __repr__(self):
        return f"Это параллелограмм... у него такая площадь: {self.area()}"
    
    
class Rhomb(Parallelogram):
    
    def __repr__(self):
        return f"Это ромб... у него такая площадь: {self.area()}"


class Trapezoid(Parallelogram):
    
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c
    
    def area(self):
        return round((self.a + self.c) * self.b / 2, 2)

    def __repr__(self):
        return f"Это трапеция... у неё такая площадь: {self.area()}"


# Пример
rect = Rectangle(5, 10)
circle = Circle(3)
print(rect.area()) # 50
print(circle.area()) # ~28.27
