# Ограничение доступа к классам и методам извне (инкапсуляция).
# режимы доступа - public, private, protected. Геттеры и сеттеры.
class Point:
    def __init__(self, x=0, y=0):
        self.x = x; self.y = y

pt = Point(1, 2)
print(pt.x, pt.y)
pt.x = 100
pt.y = 'abc'
print(pt.x, pt.y)

# <имя атрибута> (без одного или двух подчеркиваний в начале) - публичное свойство (public);
# <имя атрибута> (с одним подчеркиванием) - режим доступа protected
# (можно обращаться только внутри класса и во всех его дочерних классах)
# <имя атрибута> (с двумя подчеркиваниями) - режим доступа private (можно обращаться только внутри класса)

class Point:
    WIDTH = 5
    # Разрешенные свойства экземпляров классов:
    __slots__ = ["__x", "__y", "z"]
    def __init__(self, x=0, y=0):
        self.__x = x; self.__y = y

# pt = Point(1, 2)
# print(pt.__x, pt.__y)

# Для изменения знаяений объектов класса методы:
    def __checkValue(x):
        return isinstance(x, (int, float))


    def setCorrds(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(x):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def getCoords(self):
        return self.__x, self.__y
# __setattr(self, key, value)__ - автоматически вызывается при изменении key класса;
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item;
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса;
# __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно существует оно или нет).
#     def __getattribute__(self, item):
#         if item == "_Point__x":
#             return "Частная переменная"
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key =="WIDTH":
#             raise AttributeError
#         else:
#             self.__dict__[key] = value
#             # self.__x = value - нельзя, так как по рекурсии начнет вызывать сам себя до ошибки
#
#     def __getattr__(self, item):
#         print("__getattr__: " + item)
#
#     def __delattr__(self, item):
#         print("__delattr__: " + item)


pt = Point(1, 2)
print(pt.getCoords())
pt.setCorrds(10, 20)
print(pt.getCoords())

# Назначение сеттеров и геттеров - назначать и получать значения приватных свойств класса.

# Доступ к приватным переменным:
# _Имя класса__им переменной _Point__x
# _Имя класса__имя метода
print(pt._Point__x)
print(pt._Point__y)
Point._Point__checkValue(4)

# pt.WIDTH = 5
# pt.zzz # несуществующий метод
# pt.z = 1
# del pt.z
pt.z = 1