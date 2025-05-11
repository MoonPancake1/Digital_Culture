"""
Задача 2:

Создайте иерархию классов животных с разными звуками:

    • Базовый класс Animal с методом make_sound() (возвращает
    "Неизвестный звук").

    • Наследники:
        o Dog (переопределяет make_sound() -> «Гав!»)
        o Cat (переопределяет make_sound() -> «Мяу!»)
        o Bird (переопределяет make_sound() -> «Чирик!»)
        o Добавьте на свое усмотрение еще 2 наследника

    • Требования:
        o Использовать наследование
        o Каждый дочерний класс должен переопределять метод
        make_sound()
        o Реализовать функцию animal_concert(), которая принимает
список животных и вызывает их звуки (функция вне классов)
"""

class Animal:
    def make_sound(self):
        return "Неизвестный звук"

class Dog(Animal):
    def make_sound(self):
        return "Гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

class Bird(Animal):
    def make_sound(self):
        return "Чирик!"

class Cow(Animal):
    def make_sound(self):
        return "Муу!"

class Frog(Animal):
    def make_sound(self):
        return "Ква-ква!"

def animal_concert(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Dog(), Cat(), Bird(), Cow(), Frog()]
animal_concert(animals)