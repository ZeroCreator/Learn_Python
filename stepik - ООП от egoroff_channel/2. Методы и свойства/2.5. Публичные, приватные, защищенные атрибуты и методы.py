# 2.5. Публичные, приватные, защищенные атрибуты и методы.
# Уровни доступа к атрибутам класса
# Публичные атрибуты - атрибуты, доступные как внутри класса, так и вне класса
print('Публичные атрибуты')
class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)

account1 = BankAccount('Bob', 100000, 4526516466555114)
account1.print_public_data()  # Метод класса

print(account1.name)
print(account1.balance)
print(account1.passport)

# Изменение уровня доступа к атрибутам класса
# Защищенные атрибуты и методы _.
print('Защищенные атрибуты и методы _.')
# Лучше не использовать вне класса
class BankAccount:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

account2 = BankAccount('Tim', 500000, 4526515414848)
account2.print_protected_data()  # Метод класса

print(account2._name)
print(account2._balance)
print(account2._passport)

# Приватные переменные __.
print('Приватные переменные __.')
# Сокрытие обработки защищенных атрибутов (инкапсуляция).

class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_privat_data(self):
        print(self.__name, self.__balance, self.__passport)

account3 = BankAccount('Nic', 5000, 856321485)
account3.print_privat_data()  # Метод класса

# print(account3.__name)
# print(account3.__balance)
# print(account3.__passport)

# Метод тоже можно скрыть (инкапсулировать):
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.__print_privat_data()

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    def __print_privat_data(self):
        print(self.__name, self.__balance, self.__passport)

account4 = BankAccount('Ы', 5, 2)
# account4.__print_privat_data()  # Будет ошибка
account4.print_public_data()
print(dir(account4))
account4._BankAccount__print_privat_data()
print(account4._BankAccount__balance)

# Модуль accessify для сокрытия данных