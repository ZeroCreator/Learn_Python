# Декоратор Property.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get_balance')
        return self.__balance

    #my_property_balance = my_balance
    @my_balance.setter
    def my_balance(self, value): #  было set_balance
        print('set_balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value


    @my_balance.deleter
    def my_balance(self):   #  было delete_balance
        print("delete balanse")
        del self.__balance
    #my_balance = my_property_balance.setter(set_balance)
    #def del_balance(self):
        ##del self.__balance

    #my_balance = property()
   # my_balance = property(my_balance)
    #my_balance = my_balance.setter(set_balance)
    #my_balance = my_balance.deleter(del_balance)
    #balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)

a = BankAccount('lol',200)
a.set_balance =300
print(a.my_balance)

a.set_balance = 500
print(a.name)
'''

# Объекты - свойства (property)
print('Объекты - свойства (property)')
'''
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def __checkValue(x):  # Приватный метод внутри класса
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def __getCoordX(self):
        #print("вызов __getCoordx")
        return self.__x

    def __setCoordX(self, x):
        #print("вызов __setCoordx")
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")

    def __delCoordX(self):
        print("Удаление свойства")
        del self.__x

    coordX = property(__getCoordX, __setCoordX, __delCoordX)

pt = Point(1, 2)
pt.coordX = 100 # запись значения
x = pt.coordX # чтение значения

print(x)
#pt.coordX = "100"
#print(x)

del pt.coordX # Сам объект coordX не удалаем, удаляем приватную переменную х (локальное свойство) из нашего экземпляра класса pt.

pt.coordX = 7
pt.coordX
'''

# использование декоратора @property
print("использование декоратора @property")
'''
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def __checkValue(x):  # Приватный метод внутри класса
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property
    def coordX(self):
        return self.__x

    @coordX.setter
    def coordX(self, x):
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")

    @coordX.deleter
    def coordX(self):
        print("Удаление свойства")
        del self.__x

pt = Point(1, 2)
pt.coordX = 100
x = pt.coordX
print(x)
del pt.coordX
pt.coordX = 7
pt.coordX
'''
# Дескрипторы.
print("Дескрипторы")
# Специальный класс, в котором определены методы:
# - __get__
# - __set__
# - __delet__
class CoordValue:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        self.__value = value

    def __delete__(self, obj):
        del self.__value


class Point:
    coordX = CoordValue() # дескриптор
    coordY = CoordValue() # дескриптор

    def __init__(self, x = 0, y = 0):
        self.coordX = x
        self.coordY = y

# Использование дескрипторов как обычных свойств.
pt = Point(1, 2)
pt.coordX = 5
print(pt.coordX, pt.coordY)

'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value,(int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance
'''