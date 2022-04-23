# объекты свойства (property) и дескрипторы классов.
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __checkValue(x):
        return isinstance(x, (int, float))

    def __getCoordX(self):
        # print("вызов __getCoordX")
        return self.__x

    def __setCoordX(self, x):
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError("Неверный формат данных")

    def __delCoordX(self):
        print("Удаление свойства")
        del self.__x

    coordX = property(__getCoordX, __setCoordX, __delCoordX, "Работа с X")

pt = Point(1, 2)
pt.coordX = 100 # запись значения
x = pt.coordX   # чтение значения
print(x)
del pt.coordX
pt.coordX = 7
print(x)
print(pt.coordX)

# Дескрипторы - класс, в котором определены __get__, __set__, __delete__:
print("Дескрипторы:")
class CoordValue:
    # def __init__(self, name):
    #     self.__name = name
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    # def __delete__(self, obj):
    #     del self.__value


class Point:
    coordX = CoordValue() # дескриптор "coordX"
    coordY = CoordValue() # дескриптор "coordY"

    def __init__(self, x = 0, y = 0):
        self.coordX = x
        self.coordY = y


pt = Point(1, 2)
pt2 = Point(10,20)
pt.coordX = 5 # запись значения
print(pt.coordX, pt.coordY)
print(pt2.coordX, pt2.coordY)

# дескрипторы данных (data-descriptor)
# дескрипторы не данных (non-data descriptor) (только метод __get__)