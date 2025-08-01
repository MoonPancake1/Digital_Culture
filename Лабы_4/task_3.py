"""
Задача 3:

Напишите программу, которая открывает файл, считывает его содержимое и
обрабатывает возможные исключения, такие как отсутствие файла или
неправильный формат данных. Если файл открывается успешно, программа
должна посчитать сумму всех чисел в файле и вывести результат. Если возникают
ошибки, программа должна корректно обработать их и вывести соответствующие
сообщения:
Если файла не существует: Не удалось открыть файл
Если данные некорректные: Данные в файле некорректны

Входные данные:
12
13
14
15

Выходные данные:
54
"""

try:
    with open('input_3.txt', "r+") as f:
        try:
            print(sum(map(int, f.readlines())))
        except ValueError as VE:
            print(f"[ERROR] Данные в файле некорректны")
except FileExistsError as FEE:
    print(f"[ERROR] Не удалось открыть файл")