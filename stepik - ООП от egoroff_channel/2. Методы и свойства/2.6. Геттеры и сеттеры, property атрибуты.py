# Геттеры и сеттеры, property атрибуты.
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self): # Вернет значение
        return self.__balance

    def set_balance(self, value): # Проставит значение
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value
'''
a = BankAccount('Ivan', 100)
print(a.balance)
print(a.name)
a.balance = 'hello'
print(a.balance)
'''
# Ограничение доступа к переменной

b = BankAccount('Vasya', 200)
print(b.get_balance())
b.set_balance(400)
print(b.get_balance())
print(b.__dict__)

c = BankAccount('Tanya', 300)
#c.set_balance('he')
print(c.get_balance())
c.set_balance(500)
print(c.get_balance())
print(c.__dict__)

# property - свойство
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self): # Вернет значение
        print('get balance')
        return self.__balance

    def set_balance(self, value): # Проставит значение
        print('set balance', value)
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

d = BankAccount('Misha', 400)
d.balance # не атрибут, а свойство
print(d.balance)
d.balance = 777
print(d.balance)

# del d.balance
# print(d.balance) # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'

d.balance = 789
print(d.balance)
