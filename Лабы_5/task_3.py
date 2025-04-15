"""
Задача 3:

Создайте класс FibonacciGenerator, который генерирует последовательность
чисел Фибоначчи. Используйте метод next() для получения следующего числа
последовательности.

Пример:
fib_gen = FibonacciGenerator()

for i in range(10):
    print(fib_gen.next())
"""

class FibonacciGenerator:
    def __init__(self):
        self.a = 0
        self.b = 1
    
    def next(self):
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        return current


fib_gen = FibonacciGenerator()

for i in range(10):
    print(fib_gen.next())
