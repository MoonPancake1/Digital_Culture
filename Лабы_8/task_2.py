"""
Задача 2:

Напишите функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
третий - операция, которая должна быть произведена над ними. Если третий
аргумент +, сложить их; если -, то вычесть из первого второе; * — умножить; / —
разделить (первое на второе обычным делением). В остальных случаях вернуть
строку "Неизвестная операция".
Если делим на 0, то выводить «Деление на 0 запрещено».
На вход принимаются значения через запятую.

Входные данные:
10,4,*

Выходные данные:
40
"""

import unittest

def arithmetic(a: int, b: int, op: str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        try:
            return a / b
        except ZeroDivisionError:
            return "Деление на ноль запрещено!"

class TestArithmeticFunction(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(arithmetic(5, 3, "+"), 8)

    def test_subtraction(self):
        self.assertEqual(arithmetic(10, 4, "-"), 6)

    def test_multiplication(self):
        self.assertEqual(arithmetic(7, 6, "*"), 42)

    def test_division(self):
        self.assertEqual(arithmetic(20, 4, "/"), 5.0)

    def test_division_float_result(self):
        self.assertEqual(arithmetic(7, 2, "/"), 3.5)

    def test_zero_division(self):
        self.assertEqual(arithmetic(10, 0, "/"), "Деление на ноль запрещено!")

    def test_zero_addition(self):
        self.assertEqual(arithmetic(0, 10, "+"), 10)

    def test_negative_numbers(self):
        self.assertEqual(arithmetic(-3, -7, "*"), 21)

    def test_mixed_signs(self):
        self.assertEqual(arithmetic(-8, 2, "-"), -10)

    def test_invalid_operator(self):
        self.assertIsNone(arithmetic(3, 4, "^"))  # Оператор не предусмотрен — вернёт None

if __name__ == '__main__':
    unittest.main()
