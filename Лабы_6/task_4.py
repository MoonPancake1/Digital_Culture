"""
Задача 4:

Реализуйте класс Vector для работы с векторами:

    • Методы:
        o __add__ (сложение векторов)
        o __sub__ (вычитание векторов)
        o __mul__ (умножение на число)
        o __eq__ (сравнение векторов)

Пример: Vector(1, 2) + Vector(3, 4) -> Vector(4, 6)

    • Требования:
        o Поддержка операций с числами и другими векторами
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Операция поддерживается только между векторами")
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Операция поддерживается только между векторами")
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Вектор можно умножать только на число")
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)

v4 = v2 - v1
print(v4)

v5 = v1 * 3
print(v5)

v6 = 2 * v2
print(v6)

print(v1 == Vector(1, 2))
print(v1 == v2)