# Магические методы __str__, __repr__, __len__, __abs__
# __str__() - для отображения информации об объекте класса
# для пользователей (например, для функций print, str)
# __repr__() - для отображения информации об объекте класса
# в режиме отладки (для разработчиков).
class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"




cat = Cat("Васька")
print(cat)

# __len__() - позволяет применять функцию len() к экземплярам класса
# __аbs__() -  позволяет применять функцию abs() к экземплярам класса
class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))


p = Point(1, -2, -5)
print(len(p))
print(abs(p))






