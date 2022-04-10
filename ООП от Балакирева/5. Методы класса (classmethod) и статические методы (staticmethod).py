# Методы класса (classmethod) и статические методы (staticmethod)
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(Vector.norm2(self.x, self.y))


    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y  #+ Vector.MAX_COORD

v = Vector(10, 20)
res = Vector.get_coord(v)
print(res)

# Методы класса - @classmethod - работает исключительно с атрибутами этого класса, но не к локальным
# атрибутам экземплятор класса
print("Методы класса - @classmethod")
print(Vector.validate(5))
# Статические методы - @staticmethod - не имеют доступа ни к атрибутам класса, ни к атрибутам его
# экземпляров
print("Статические методы - @staticmethod")
print(Vector.norm2(5, 6))


