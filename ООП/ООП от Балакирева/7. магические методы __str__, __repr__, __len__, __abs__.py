# Магические методы __str__, __repr__, __len__, __abs__
# dunder - методы (double underscore)
# __str__() - магический метод для отображения информации об объекте класса для пользователей
# (например, для функции print, str)
# __repr__() - магический метод для отображения информации об объекте класса в режиме отладки
# (для разработчиков)
# __len__() - позволяет применять функцию len() к экземплярам класса
# __abs__() - позволяет применять функцию abs() к экземплярам класса
class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"

cat = Cat("Васька")
cat
str(cat)
print(cat)
print(str(cat))

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, 2, -3)
print(len(p))
print(abs(p))

class Point:
    MIN_COORD = 10
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

pt1 = Point(1, 2)
pt2 = Point(10, 20)
print(pt1.MAX_COORD)
pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.__dict__)
