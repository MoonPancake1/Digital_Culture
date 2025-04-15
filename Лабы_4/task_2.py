"""
Задача 2:

Напишите программу, которая сортирует список словарей по каждому значению
ключей с использованием lambda-выражения.

Входные данные:

data = [
    {"name": "Alice", "age": 25},
    {"name": "David", "age": 29},
    {"name": "Bob", "age": 32},
    {"name": "Charlie", "age": 28}
]

Выходные данные:

Сортируем по первому ключу:
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 32},
    {"name": "Charlie", "age": 28},
    {"name": "David", "age": 29}
]

Сортируем по второму ключу:
data = [
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 28},
    {"name": "David", "age": 29},
    {"name": "Bob", "age": 32}
]
"""

data = [{"name": input(f"Введите имя для {i + 1} человека: "), "age": int(input(f"Введите возраст для {i + 1} человека: "))} for i in range(int(input("Введите кол-во людей: ")))]
print(f'{sorted(data, key=lambda x: x["name"])}\n{sorted(data, key=lambda x: x["age"])}')