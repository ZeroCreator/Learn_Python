# методы класса - @classmethod и статические методы - @staticmethod.
# Чем отличаются методы, объявленные через декоратор @classmethod от статических методов,
# объявленных через @staticmethod.
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def setCoords(self, x, y):
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y
            return x, y

    @classmethod
    def validate(cls, arg):
        if arg >= cls.MIN_COORD and arg <= cls.MAX_COORD:
            return True
        return False


    @staticmethod
    def norm2(x, y):
        return x*x + y*y


c = Vector.validate(5)
print(c)

c = Vector.validate(500)
print(c)

t = Vector.norm2(1, 2)
print(t)


v = Vector()
v.setCoords(1, 2)
print(v)

g = Vector.setCoords(v, 10, 20)
print(g)

# 1. Если нам нужен метод, который бы работал с атрибутами экземпляров классов, то это однозначно обычный метод класса
# с первым параметром self, который указывает на текущий объект.
# 2. Если нам нужен метод, который можно вызывать непосредственно из класса (или экземпляра) и который бы имел доступ к
# свойствам и методам этого класса, то его следует объявить как метод класса через декоратор @classmethod.
# 3. Если нам нужен метод, который можно вызывать непосредственно из класса, но доступ к его атрибутам не предполагаете,
# то достаточно его объявить как статический через декоратор @staticmethod.