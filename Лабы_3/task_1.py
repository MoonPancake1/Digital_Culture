"""

Задача 1:

Напишите функцию sum_range(start, end), которая суммирует все четные числа от
значения «start» до величины «end» включительно, а нечетные – считает.

Если пользователь задаст первое число большее чем второе, просто поменяйте их
местами.

На вход принимаются значения через запятую. На выходе выводятся значения
через запятую.

Входные данные:
20,2

Выходные данные:
110,9

"""

def sum_range(start: int, end: int) -> tuple:
    if end <= start:
        start, end = end, start        
    
    cnt = 0
    sm = 0
    for i in range(start, end + 1):
        if i % 2:
            cnt += 1
        else:
            sm += i
    return sm, cnt


# print(*sum_range(20, 2))
print(*sum_range(int(input()), int(input())))