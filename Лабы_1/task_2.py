"""
Задача 2.

Напишите программу, которая принимает от пользователя три значения, а затем
выводит информацию о типе каждого введенного значения
"""


def print_type(value: str):
    value = value.lower()
    if '.' in value:
        try:
            # float
            print(f'Значение: {value} – {type(float(value)).__name__}')
        except Exception as e:
            # string
            print(f'Значение: {value} – {type(value).__name__}')
        return True
    elif value in ['true', 'false']:
        # bool
        print(f'Значение: {value} – bool')
        return True
    elif value.isdigit():
        # integer
        print(f'Значение: {value} – int')
        return True
    else:
        print(f'Значение: {value} – str')
    
    
print_type(input())
print_type(input())
print_type(input())