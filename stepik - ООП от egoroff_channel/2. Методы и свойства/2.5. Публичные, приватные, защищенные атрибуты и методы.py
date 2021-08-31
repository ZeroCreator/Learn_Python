# 2.5. Публичные, приватные, защищенные атрибуты и методы.
# Уровни доступа к атрибутам класса
# Публичные атрибуты - атрибуты, доступные как внутри класса, так и вне класса
print('Публичные атрибуты')
class BankAccount:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_data(self):
        print(self.name, self.balance, self.passport)

account1 = BankAccount('Bob', 100000, 4526516466555114)
account1.print_data()  # Метод класса


print(account1.name)
print(account1.balance)
print(account1.passport)

# Изменение уровня доступа к атрибутам класса
# Защищенные атрибуты и методы