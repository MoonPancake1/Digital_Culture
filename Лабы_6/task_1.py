"""
Задача 1:

Создайте иерархию классов для моделирования транспортных средств:

    • Базовый класс Transport с методами:
        o start_engine() (возвращает «Двигатель запущен»)
        o stop_engine() (возвращает «Двигатель остановлен»)
        o move() (базовый метод -> «Производится движение»)

    • Наследники:
        o Car (переопределяет move() -> «Едет по дороге»)
        o Airplane (переопределяет move() -> «Летит по воздуху»)
        o Boat (переопределяет move() -> «Плывет по воде»)

Требования:
    • Использовать наследование
    • Каждый дочерний класс должен переопределять метод move()
"""


class Transport():
    
    @staticmethod
    def start_engine() -> str:
        return "Двигатель запущен"
    
    @staticmethod
    def stop_engine() -> str:
        return "Двигатель остановлен"
    
    @staticmethod
    def move() -> str:
        return "Производится движение"


class Car(Transport):
    
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def move() -> str:
        return "Едет по дороге"
    
    
class Airplane(Transport):
    
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def move() -> str:
        return "Летит по воздуху"


class Boat(Transport):
    
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def move() -> str:
        return "Плывет по воде"
    
bmw_m5 = Car()
print(bmw_m5.start_engine())
print(bmw_m5.move())