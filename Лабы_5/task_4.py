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
        

# Создание пользователей
user_a = Account(5_000)
user_b = Account(10_000)
user_c = Account(0)
user_d = Account(1_000_000)

# Проверка пополнения счёта
user_a.deposit(1_000)
user_b.deposit(0)
user_c.deposit(-90)
user_d.deposit("sss")

# Проверка снятия со счёта
user_a.withdraw(1_000)
user_b.withdraw(0)
user_c.withdraw(-90)
user_d.withdraw("sss")

# Проверка перевода от клиента на счёт другого клиента
user_a.transfer_a2c(user_b, 1_000)
user_c.transfer_a2c(user_d, 1_000)
user_d.transfer_a2c(user_c, 50_000)
user_b.transfer_a2c(user_a, -100)
user_a.transfer_a2c(user_a, 100)

# Проверка перевода от другого клиента на счёт клиента
user_a.transfer_c2a(user_b, 1_000)
user_c.transfer_c2a(user_d, 1_000)
user_b.transfer_c2a(user_c, 50_000)
user_d.transfer_c2a(user_b, 50_000)
user_d.transfer_c2a(user_c, 50_000)

# Проверка счёта клиентов
user_a.get_balance()
user_b.get_balance()
user_c.get_balance()
user_d.get_balance()

# Просмотр транзакций
user_a.show_transactions()
user_b.show_transactions()