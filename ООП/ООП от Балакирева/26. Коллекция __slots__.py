# Коллекция __slots__.
# - ограничение создаваемых локальных свойств
# - уменьшение занимаемой памяти
# - ускорение работы с локальными свойствами
import time
import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt = Point(1, 2)
pt.x = 10
pt.y = 20
print(pt.__dict__)

pt.z = 4
print(pt.__dict__)

class Point2D:
    __slots__ = ('x', 'y') # уменьшает объем памяти, занимаемый объектом класса и ускоряет работу
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0

pt2 = Point2D(10, 20)
#print(pt2.__dict__)

#pt2.z = 4
#print(pt2.__dict__)

pt2.x = 50
print(pt2.x)
del pt2.y
pt2.y = 100
print(pt2.y)

print(pt2.MAX_COORD)

print(pt.__sizeof__() + pt.__dict__.__sizeof__())
print(pt2.__sizeof__())

p = Point(1, 2)
p2 = Point2D(10, 20)

t1 = timeit.timeit(p.calc)
t2 = timeit.timeit(p2.calc)
print(t1, t2)

class D:
    __slots__ = ['a', 'b', '__dict__']  # Добавить __dict__ в слоты
    c = 3
    def __init__(self):
        self.d = 4
        self.b = 2

X = D()
print(X.d)
print( X.__dict__)
print(X.__slots__)
print(X.c)
X.a = 1
print(getattr(X, 'a',), getattr(X, 'c'), getattr(X, 'd'))

#for attr in list(X.__dict__) + X.__slots__:
for attr in list(getattr(X,'__dict__', [])) + getattr(X, '__slots__', []):
        print(attr, '= > ', getattr(X, attr))
    #print(attr, '= > ', getattr(X, attr))
