"""
Задача 3:

Напишите программу, которая фильтрует список чисел, оставляя только те,
которые делятся на 3 и возводят в квадрат каждое из оставшихся чисел, используя
lambda-выражения и встроенные функции filter и map.

Входные данные:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Выходные данные:
9, 36, 81
"""

import unittest

def foo(a: list):
    return ' '.join(map(lambda x: str(x**2), filter(lambda x: not x % 3, a)))

class TestFooFunction(unittest.TestCase):

    def test_all_divisible_by_3(self):
        self.assertEqual(foo([3, 6, 9]), "9 36 81")

    def test_none_divisible_by_3(self):
        self.assertEqual(foo([1, 2, 4, 5, 7]), "")

    def test_mixed_numbers(self):
        self.assertEqual(foo([1, 3, 4, 6, 8]), "9 36")

    def test_with_zero(self):
        self.assertEqual(foo([0, 3, 6]), "0 9 36")  # 0 делится на 3

    def test_negative_numbers(self):
        self.assertEqual(foo([-3, -6, 2]), "9 36")

    def test_empty_list(self):
        self.assertEqual(foo([]), "")

    def test_single_element_divisible(self):
        self.assertEqual(foo([9]), "81")

    def test_single_element_not_divisible(self):
        self.assertEqual(foo([10]), "")

    def test_large_numbers(self):
        self.assertEqual(foo([30, 60]), "900 3600")

    def test_repeated_values(self):
        self.assertEqual(foo([3, 3, 3]), "9 9 9")

if __name__ == '__main__':
    unittest.main()
