"""
Задание 5

Напишите программу, которая ищет общие и уникальные элементы заданных
множеств A и B, отсортированные в обратном порядке.

Тест 1
10 2 7 65 1 33
5 90 2 8 32 10

10 2
90 65 33 32 8 7 5 1
"""

set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))

print(" ".join(map(str, sorted(set_1 & set_2, reverse=True))))
print(" ".join(map(str, sorted(set_1 ^ set_2, reverse=True))))
