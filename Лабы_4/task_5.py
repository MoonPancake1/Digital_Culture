"""
Задача 5:

Напишите программу, которая принимает от пользователя строку,
представляющую математическое выражение, и вычисляет его значение.
Программа должна проверять правильность ввода и обрабатывать возможные
ошибки, если они произойдут.

Входные данные:
2+2

Выходные данные:
4

Входные данные:
2+5о

Выходные данные:
Ошибка: недопустимый символ в выражении (например)
"""


expression = input("Введите математическое выражение: ")

try:
    allowed_chars = set('0123456789+-*/(). ')
    if not all(char in allowed_chars for char in expression):
        invalid_chars = [char for char in expression if char not in allowed_chars]
        raise ValueError(f"Недопустимый символ в выражении: {invalid_chars}")
    
    if not expression.strip():
        raise ValueError("Выражение не может быть пустым")
    
    result = eval(expression)
    
    print(result)

except SyntaxError:
    print("Ошибка: некорректный синтаксис выражения")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
except ValueError as ve:
    print(f"Ошибка: {ve}")
except Exception as e:
    print(f"Ошибка при вычислении: {e}")
