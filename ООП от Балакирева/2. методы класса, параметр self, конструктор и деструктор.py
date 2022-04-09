# методы класса, параметр self, конструктор и деструктор.

class Point:
    color = "red"
    circle = 2
    x = 1; y = 1

    def set_coords(self, x, y):
        print("вызов метода set_coords")
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
# Point.set_coords() # Ошибка
pt.set_coords(1, 2)
print(pt.__dict__)

pt2 = Point()
pt2.x = 5
pt2.y = 10
pt2.set_coords(5, 10)
Point.set_coords(pt2, 5, 10)
print(pt.get_coords())
print(pt2.__dict__)
f = getattr(pt, "get_coords")
print(f())

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