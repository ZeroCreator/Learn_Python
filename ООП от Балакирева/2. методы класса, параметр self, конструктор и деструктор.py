# методы класса, параметр self, конструктор и деструктор.

class Point:
    x = 1; y = 1
    def setCoords(self, x, y):
        self.x = x
        self.y = y

pt = Point()
# pt.x = 5
# pt.y = 10
# pt.setCoords(5, 10)
Point.setCoords(pt, 5, 10)
print(pt.__dict__)


# Метод __init__() - инициализатор (конструктор - это метод __new__()), а метод __del__() - финализатор.
print("Метод __init__() - инициализатор")
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print("Создание экземпляра класса Point")

    x = 1
    y = 1
    def setCoords(self, x, y):
        self.a = x
        self.b = y

pt = Point()
pt2 = Point(5)
pt3 = Point(5, 10)
print(pt.__dict__, pt2.__dict__, pt3.__dict__, sep="\n")

print("метод __del__() - финализатор")
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print("Создание экземпляра класса Point")

    def __del__(self):
        print("Удаление экземпляра: " + self.__str__())

    x = 1
    y = 1
    def setCoords(self, x, y):
        self.a = x
        self.b = y

pt = Point()
pt2 = Point(5)
pt3 = Point(5, 10)
print(pt.__dict__, pt2.__dict__, pt3.__dict__, sep="\n")