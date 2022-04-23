# Вычисляемые свойства.
class Square:

    def __init__(self, s):
        self.side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            print("calculate area")
            self.__area = self.side**2
        return self.__area

#a = Square(5)
#print(a.area())

b = Square(6)
b.area
#print(b.area())

b.side = 100
print(b.area)

c = Square(11)
print(c.area)
print(c.area)

c.side = 4
print(c.area)

d = Square(7)
print(d.area)

d.side = 3
print(d.area)
