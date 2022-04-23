# Как работает __slots__ с property и при наследовании
class Point2D:
    __slots__ = ('x', 'y', 'length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x*x + y*y) ** .5

    @property
    def length(self):
        return self.__length



pt = Point2D(1, 2)
print(pt.length)


class D:
    __slots__ = ['a', 'b', '__dict__']  # Добавить __dict__ в слоты
    c = 3
    def __init__(self): self.d = 4

X = D()
print(X.d)
print( X.__dict__)
print(X.__slots__)
print(X.c)
X.a = 1
print(getattr(X, 'a',), getattr(X, 'c'), getattr(X, 'd'))