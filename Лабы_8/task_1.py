"""
Задача 1:

Напишите функцию с двумя параметрами: первый будет делиться на 10
целочисленным делением, а второй – на 5 обычным делением (округлить до 2
цифр после запятой).

На вход принимаются значения через запятую. На выходе выводятся значения
через запятую.

Входные данные:
7,18

Выходные данные:
0,3.60
"""

import unittest

def foo(a: int, b: int) -> tuple:
    if isinstance(a, int) and isinstance(b, int):
        return a // 10, round(b / 5, 2)
    return "Введи норм данные)"

class TestFooFunction(unittest.TestCase):

    def test_1(self):
        self.assertEqual(foo(10, 5), (1, 1.0))  # базовый случай

    def test_2(self):
        self.assertEqual(foo(0, 0), (0, 0.0))  # нули

    def test_3(self):
        self.assertEqual(foo(-10, 5), (-1, 1.0))  # отрицательное a

    def test_4(self):
        self.assertEqual(foo(10, -5), (1, -1.0))  # отрицательное b

    def test_5(self):
        self.assertEqual(foo(-25, -15), (-3, -3.0))  # оба отрицательные

    def test_6(self):
        self.assertEqual(foo(99, 12), (9, 2.4))  # округление дробного числа

    def test_7(self):
        self.assertEqual(foo(5, 2), (0, 0.4))  # округление вниз

    def test_8(self):
        self.assertEqual(foo(123, 456), (12, 91.2))  # большие числа

    def test_9(self):
        self.assertEqual(foo(1, 1), (0, 0.2))  # маленькие значения

    def test_10(self):
        self.assertEqual(foo(20, 13), (2, 2.6))  # обычный случай с нецелым делением b

    def test_11(self):
        self.assertEqual(foo("La-La. I'm Semen Lobanov", "U menya golova iz kartoshki"), ("Введи норм данные)"))  # текст вместо чисел

if __name__ == '__main__':
    unittest.main()
