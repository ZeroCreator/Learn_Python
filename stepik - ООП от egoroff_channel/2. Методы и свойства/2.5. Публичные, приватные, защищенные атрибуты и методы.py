# 2.5. Публичные, приватные, защищенные атрибуты и методы.
# Уровни доступа к атрибутам класса
# Публичные атрибуты - атрибуты, доступные как внутри класса, так и вне класса
'''
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
'''
# Инкапсуляция. Геттеры и сеттеры.
'''
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x; self.y = y

pt = Point(1, 2)
print(pt.x, pt.y)
pt.x = 100
pt.y = 'abc'
print(pt.x, pt.y)
'''
# Чтобы не было возможности менять атрибуты извне - их надо делать закрытыми
# 3 типа доступа:
# 1. public - публичное
# 2. _protected - можно обращаться только внутри класса и во всех его дочерних классах
# 3. __private - можно обращаться только внутри класса
'''
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    def setCoords(self, x, y): # сеттеры
        # Проверка x, y - числа
        if (isinstance(x, int) or isinstance(x, float)) and \
                (isinstance(y, int) or isinstance(y, float)):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def getCoords(self): # геттеры
        return self.__x, self.__y

pt = Point(1, 2)
print(pt.getCoords())
pt.setCoords(10, 20)
print(pt.getCoords())
pt.setCoords("10", 20)
print(pt.getCoords())
'''
# Создадим метод, который будет проверять значения x и y --> (if (isinstance(x, int) or isinstance(x, float)) and \
#                 (isinstance(y, int) or isinstance(y, float))
'''
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    def __checkValue(x): # Приватный метод внутри класса
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y): # Использование приватного метода
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def getCoords(self):
        return self.__x, self.__y

pt = Point(1, 2)
print(pt.getCoords())
pt.setCoords(10, 20)
print(pt.getCoords())
pt.setCoords("10", 20)
print(pt.getCoords())

# Обратиться к закрытым методам и к закрытым переменным:
# _Имя класса__имя переменной (_Point__x)
# _Имя класса__имя метода
print(pt._Point__x)
print(pt._Point__y)
Point._Point__checkValue(4)
'''
# Перегрузка методов:
# __setattr(self, key, value)__ - автоматически вызывается при изменении свойства key класса;
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item$
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса;
# __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно, существует оно или нет).
'''
class Point:
    WIDTH = 5 # Глобальная константа, которую нельзя менять

    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    def __checkValue(x): # Приватный метод внутри класса
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y): # Использование приватного метода
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def getCoords(self):
        return self.__x, self.__y

    def __getattribute__(self, item):
        if item == "_Point__x":
            return "Частная переменная"
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value): # Метод, запрещающий изменения глобальной константы
        if key == "WIDTH":
            raise AttributeError
        else:
            self.__dict__[key] = value # Если необходимо менять локальные свойства - это надо делать через __dict__

    def __getattr__(self, item):
        print("__getattr__:" + item)

    def __delattr__(self, item):
        print("__delattr__:" + item)



pt = Point(1, 2)
print(pt._Point__x)
print(pt._Point__y)
print(pt.getCoords())
print(pt._Point__x)
# pt.WIDTH = 5 # AttributeError

pt.c = 1
del pt.z
'''
# разрешенные свойства локальных экземпляров классов, прописать в коллекцию:
class Point:
    WIDTH = 5 # Глобальная константа, которую нельзя менять
    __slots__ = ["__x", "__y", "z"]

    def __init__(self, x = 0, y = 0):
        self.__x = x; self.__y = y

    def __checkValue(x): # Приватный метод внутри класса
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y): # Использование приватного метода
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def getCoords(self):
        return self.__x, self.__y

pt = Point(1, 2)
pt.z = 5 # AttributeError: 'Point' object has no attribute 'z'
