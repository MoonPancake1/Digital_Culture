"""
Задача 4:

Напишите программу, которая моделирует работу банковского счета с
различными проверками. Должны быть реализованы классы и методы:

• Account — основной класс, представляющий банковский счет (по
умолчанию начальная сумма = 0):
    o Методы:
        o deposit – пополнение счета на сумму. Сумма должна быть больше 0.
        o withdraw – снятие наличных. Сумма должна быть больше 0 и средств
            на счете должно быть достаточно.
        o transfer_c2a – перевод средств со счета. Сумма должна быть больше
            0 и средств на счете должно быть достаточно.
        o transfer_a2c - перевод средств на счет. Сумма должна быть больше 0.
        o get_balance – возвращает текущий баланс счета.
        o show_transactions – возвращает список совершенных транзакций по
            счету.

• Transaction — хранит записи транзакций с суммой и типом (deposit,
    withdraw, transfer_c2a, transfer_a2c).

Пример:
account = Account(1000) # Счет с ненулевой начальной суммой
account.deposit(500) # Пополнение счета на 500
account.withdraw(200) # Снятие 200
print(account.get_balance()) # 1300
"""

from typing import Optional
from datetime import datetime
from uuid import uuid4

class Account():
    
    def __init__(self, curr_balance: int = 0):
        self.uuid = uuid4()
        self.transactions = []
        self.__balance = curr_balance

    def get_balance(self) -> str:
        return self.__balance
    
    def deposit(self, money: int) -> None:
        transaction = Transaction(
                type_transaction='Депозит',  
                money=money, 
                uuid_user=self.uuid
        )
        if not isinstance(money, int):
            print("Ошибка: сумма транзации не является числом!")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if money <= 0:
            print("Ошибка: сумма пополнения должна быть положительной")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        self.__balance += money
        transaction.complete = True
        self.transactions.append(transaction)
        print(f"Пополнение счета: {money}. Текущий баланс: {self.get_balance()}")
        return True
    
    def withdraw(self, money: int) -> None:
        transaction = Transaction(
                type_transaction='Вывод',  
                money=money, 
                uuid_user=self.uuid
        )
        if not isinstance(money, int):
            print("Ошибка: сумма транзации не является числом!")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if money < 0:
            print("Ошибка: сумма снятия должна быть положительной")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if self.__balance >= money:
            self.__balance -= money
            print(f"Снятие со счета: {money}. Текущий баланс: {self.get_balance()}")
            transaction.complete = True
            self.transactions.append(transaction)
            return True
        else:
            print(f"На счёте недостаточно средств. Текущий баланс: {self.get_balance()}")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
    
    def transfer_c2a(self, client: Optional['Account'], money: int) -> None:
        transaction = Transaction(
                type_transaction='Перевод от клиента на счёт',  
                money=money, 
                uuid_user=client.uuid,
                uuid_recipient=self.uuid
        )
        if not isinstance(money, int):
            print("Ошибка: сумма транзации не является числом!")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if not isinstance(client, Account):
            print("Ошибка: указан неверный счёт для перевода")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if money < 0:
            print("Ошибка: сумма перевода должна быть положительной")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if client.get_balance() >= money:
            client.withdraw(money)
            self.deposit(money)
            print(f"Перевод {money} успешно выполнен. Текущий баланс: {client.get_balance()}")
            transaction.complete = True
            self.transactions.append(transaction)
            return True
        else:
            print(f"Недостаточно средств для перевода. {client.get_balance()}")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
    
    def transfer_a2c(self, client: Optional['Account'], money: int) -> None:
        if not client:
            return False
        transaction = Transaction(
                type_transaction='Перевод со счёта к клиенту',  
                money=money, 
                uuid_user=self.uuid,
                uuid_recipient=client.uuid
        )
        if not isinstance(money, int):
            print("Ошибка: сумма транзации не является числом!")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if not isinstance(client, Account):
            print("Ошибка: указан неверный счёт для перевода")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if money < 0:
            print("Ошибка: сумма перевода должна быть положительной")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
        if self.get_balance() >= money:
            self.withdraw(money)
            client.deposit(money)
            print(f"Перевод {money} успешно выполнен. Текущий баланс: {self.get_balance()}")
            transaction.complete = True
            self.transactions.append(transaction)
            return True
        else:
            print(f"Недостаточно средств для перевода. {self.get_balance()}")
            transaction.complete = False
            self.transactions.append(transaction)
            return False
            
    def show_transactions(self) -> list['Transaction']:
        print(f"Транзакции пользователя: {self.uuid}:\n")
        [print(transaction) for transaction in self.transactions]
        return True
            

class Transaction():
    
    def __init__(self, 
                 type_transaction: str,
                 money: int,
                 uuid_user: str,
                 complete: bool = False,
                 uuid_recipient: str | None = None):
        self.uuid_user = uuid_user
        self.uuid_recipient = uuid_recipient
        self.type_transaction = type_transaction
        self.complete = complete
        self.money = money
        self.create_at = datetime.now()
        self.update_at = datetime.now()
        
    def __repr__(self):
        c = f", к получателю: {self.uuid_recipient}" if self.uuid_recipient else ""
        t = "Успешно" if self.complete else "Не успешно"
            
        return f"Транзакция: {self.type_transaction}. " + \
            f"Тип: {t}. " + \
            f"От пользователя: {self.uuid_user}{c}. " + \
            f"Время транзакции: {self.create_at}. " + \
            f"Сумма транзакции: {self.money}."
            
            
##########################################################################
# ТЕСТЫ
##########################################################################


import unittest

class TestAccountSystem(unittest.TestCase):

    def test_initial_balance(self):
        acc = Account(100)
        self.assertEqual(acc.get_balance(), 100)

    def test_deposit_success(self):
        acc = Account()
        result = acc.deposit(50)
        self.assertTrue(result)
        self.assertEqual(acc.get_balance(), 50)
        self.assertTrue(acc.transactions[-1].complete)

    def test_deposit_negative(self):
        acc = Account()
        result = acc.deposit(-20)
        self.assertFalse(result)
        self.assertEqual(acc.get_balance(), 0)
        self.assertFalse(acc.transactions[-1].complete)

    def test_deposit_invalid_type(self):
        acc = Account()
        result = acc.deposit("100")  # строка вместо числа
        self.assertFalse(result)
        self.assertEqual(acc.get_balance(), 0)
        self.assertFalse(acc.transactions[-1].complete)

    def test_withdraw_success(self):
        acc = Account(100)
        result = acc.withdraw(40)
        self.assertTrue(result)
        self.assertEqual(acc.get_balance(), 60)
        self.assertTrue(acc.transactions[-1].complete)

    def test_withdraw_insufficient_funds(self):
        acc = Account(30)
        result = acc.withdraw(50)
        self.assertFalse(result)
        self.assertEqual(acc.get_balance(), 30)
        self.assertFalse(acc.transactions[-1].complete)

    def test_transfer_c2a_success(self):
        sender = Account(200)
        receiver = Account(50)
        result = receiver.transfer_c2a(sender, 100)
        self.assertTrue(result)
        self.assertEqual(sender.get_balance(), 100)
        self.assertEqual(receiver.get_balance(), 150)
        self.assertTrue(receiver.transactions[-1].complete)

    def test_transfer_c2a_insufficient_funds(self):
        sender = Account(10)
        receiver = Account()
        result = receiver.transfer_c2a(sender, 100)
        self.assertFalse(result)
        self.assertEqual(sender.get_balance(), 10)
        self.assertEqual(receiver.get_balance(), 0)
        self.assertFalse(receiver.transactions[-1].complete)

    def test_transfer_a2c_success(self):
        acc1 = Account(300)
        acc2 = Account(100)
        result = acc1.transfer_a2c(acc2, 150)
        self.assertTrue(result)
        self.assertEqual(acc1.get_balance(), 150)
        self.assertEqual(acc2.get_balance(), 250)
        self.assertTrue(acc1.transactions[-1].complete)

    def test_transfer_a2c_invalid_recipient(self):
        acc = Account(100)
        result = acc.transfer_a2c(None, 50)
        self.assertFalse(result)
        self.assertEqual(acc.get_balance(), 100)

if __name__ == '__main__':
    unittest.main()
