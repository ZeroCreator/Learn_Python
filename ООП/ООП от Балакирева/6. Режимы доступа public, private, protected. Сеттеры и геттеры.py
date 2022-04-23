# Режимы доступа public, private, protected. Сеттеры и геттеры
# Механизм инкапсуляции - ограничения доступа к данным и методам класса извне
from accessify import private, protected
class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = self.y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

#    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        #if type(x) in (int, float) and type(y) in (int, float):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y

pt = Point(1, 2)
#pt.x = 200
#pt.y = "coord_y"
#print(pt.__x, pt.__y)
pt.set_coord(10, 20)
print(pt.get_coord())

# attribute (без одного или двух подчеркиваний вначале) – публичное свойство (public).
# _attribute (с одним подчеркиванием) – режим доступа protected (служит для обращения внутри класса и во всех
# его дочерних классах).
# __attribute (с двумя подчеркиваниями) – режим доступа private (служит для обращения только внутри класса).\
print(dir(pt))
print(pt._Point__x)
print(pt._Point__y)

# Модуль accessify
# pip install accessify
#pt.check_value(5)
pt._Point__check_value(5) # Обойти защиту к доступу к приватным методам
