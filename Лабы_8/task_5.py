"""
Задача 5:

Реализуйте класс User с защищенными данными профиля:

    • Приватные атрибуты:
        o __username (логин, минимум 5 символов),
        o __password (пароль, минимум 8 символов).

    • Публичные методы:
        o update_password(old_pass, new_pass) (смена пароля при
        условии правильного старого).
        o show_info() (возвращает логин и пароль, но скрывает пароль:
        логин: user123, пароль: ********)

    • Ошибки:
        o Неверный старый пароль -> ValueError("Неверный пароль")
        o Слабый новый пароль (меньше 8 символов) ->
        ValueError("Пароль слишком короткий")
        o Слабый логин (меньше 5 символов) -> ValueError("Логин
        слишком короткий")

    • Требования:
        o Инкапсуляция через приватные атрибуты
        o Валидация входных данных в методах
        o Запретить прямой доступ к __username,__password
"""

class User:
    def __init__(self, username, password):
        self.__username = None
        self.__password = None
        self.set_username(username)
        self.set_password(password)
    
    def set_username(self, username):
        if len(username) < 5:
            raise ValueError("Логин слишком короткий")
        self.__username = username
    
    def set_password(self, password):
        if len(password) < 8:
            raise ValueError("Пароль слишком короткий")
        self.__password = password
    
    def update_password(self, old_pass, new_pass):
        if old_pass != self.__password:
            raise ValueError("Неверный пароль")
        if len(new_pass) < 8:
            raise ValueError("Пароль слишком короткий")
        self.__password = new_pass
    
    def show_info(self):
        return f"логин: {self.__username}, пароль: {'*' * len(self.__password)}"
    
    def get_username(self):
        return self.__username
    
    def check_password(self, password):
        return password == self.__password

try:
    user = User("user123", "My_very_cool_password")
    print(user.show_info())
    
    user.update_password("My_very_cool_password", "PrO_100_Password")
    print(user.show_info())
    
    bad_user = User("usr", "password")
except ValueError as e:
    print(f"Ошибка: {e}")

##########################################################################
# ТЕСТЫ
##########################################################################

import unittest

class TestUser(unittest.TestCase):

    def test_valid_user_creation(self):
        user = User("validUser", "StrongPass123")
        self.assertEqual(user.get_username(), "validUser")
        self.assertTrue(user.check_password("StrongPass123"))

    def test_short_username_raises(self):
        with self.assertRaises(ValueError) as cm:
            User("usr", "StrongPass123")
        self.assertEqual(str(cm.exception), "Логин слишком короткий")

    def test_short_password_raises(self):
        with self.assertRaises(ValueError) as cm:
            User("validUser", "12345")
        self.assertEqual(str(cm.exception), "Пароль слишком короткий")

    def test_update_password_success(self):
        user = User("user123", "password123")
        user.update_password("password123", "newPassword456")
        self.assertTrue(user.check_password("newPassword456"))

    def test_update_password_wrong_old(self):
        user = User("user123", "password123")
        with self.assertRaises(ValueError) as cm:
            user.update_password("wrongOld", "newPassword456")
        self.assertEqual(str(cm.exception), "Неверный пароль")

    def test_update_password_too_short(self):
        user = User("user123", "password123")
        with self.assertRaises(ValueError) as cm:
            user.update_password("password123", "short")
        self.assertEqual(str(cm.exception), "Пароль слишком короткий")

    def test_show_info_masked_password(self):
        user = User("myuser", "supersecure")
        info = user.show_info()
        self.assertIn("логин: myuser", info)
        self.assertIn("***********", info)  # 11 звёздочек для "supersecure"

    def test_check_password_correct(self):
        user = User("admin", "adminpass")
        self.assertTrue(user.check_password("adminpass"))

    def test_check_password_incorrect(self):
        user = User("admin", "adminpass")
        self.assertFalse(user.check_password("wrongpass"))

    def test_get_username(self):
        user = User("tester", "testpass123")
        self.assertEqual(user.get_username(), "tester")

if __name__ == '__main__':
    unittest.main()
