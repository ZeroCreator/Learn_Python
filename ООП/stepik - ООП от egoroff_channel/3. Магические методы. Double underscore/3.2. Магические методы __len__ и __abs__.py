# Магические методы __len__ и __abs__
print('pet'.__len__())
print(-78.05.__abs__())

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)

b = Person("aa", "bbb")
print(len(b))
#part 1
def __init__(self, name, surname):
    self.name = name
    self.surname = surname


def __len__(self):
    return len(str(self.name) + str(self.surname))


# part 2
class Point():
    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Otrezok():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        t = f"Otrezok(a{str(self.point1)}, b{str(self.point2)})"
        return t

    def __abs__(self):
        import math
        dx = self.point2.x - self.point1.x
        dy = self.point2.y - self.point1.y
        return (dx ** 2 + dy ** 2) ** 0.5


a = Point(0, 0)
b = Point(3, 4)
ab = Otrezok(a, b)
print(abs(ab))
print(ab)



class Otrezok():
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self) # self.__abs__()

    def __abs__(self):
        return abs(self.x2 - self.x1)


a = Point(0, 0)
b = Point(3, 4)
q = Otrezok(3, 9)
w = Otrezok(10, 2)
print(abs(w))
print(len(w))