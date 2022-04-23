# Парадигма ООП, классы, экземпляры классов, атрибуты.
# Наследование - образование новых классов на основе ранее созданных.
# Полиморфизм - вызов методов базового класса из дочерних.
# Инкапсуляция - это возможность закрывать данные и методы класса от внешнего вмешательства.
class Point:
    """ Класс для представления координат точек на плоскости
    """
    x = 1
    y = 1

print(Point.__doc__)
print(Point.__name__)
print(dir(Point))

pt = Point() # Создаем экземпляр класса - пространство имен
print(pt.__dict__)
Point.x = 100
print(pt.x, pt.y)
print(id(pt), id(Point), sep="\n")

pt.x = 5
pt.y = 10
print(pt.x, Point.x)
# Узнать, какие переменные есть в классе: .__dict__:
print("Узнать, какие локальные переменные есть в классе и их значения: .__dict__:")

print(pt.__dict__)

# Переменные внутри класса или экземпляров класса называются атрибутами (свойствами) класса.
# Функции для работы с атрибутами:
# getattr(obj, name [, default]) - возвращает значение атрибута объекта;
# hassttr(obj, name) - проверяет на наличие атрибута name в obj;
# setattr(obj, name, value) - задает значение атрибута (если атрибут не существует, то он создается),
# delattr(obj, name) - удаляет атрибут с именем name.
print(getattr(pt, "x"))
print(getattr(pt, "z", False)) # Прописываем значение, которое будет возвращаться, если атрибут не существует
print(hasattr(pt, "y"))
setattr(pt, "z", 7)
print(pt.__dict__)
delattr(pt, "z")
print(pt.__dict__)

# Те же действия можно производить и с классом:
setattr(Point, "z", 7)
print(Point.__dict__)

Point.z = 100
pt.msg = "hello"
res = getattr(pt, "sss", False)
del pt.x

# Проверка принадлежности экземпляра классу - функция isinstance:
print("Проверка принадлежности экземпляра классу - функция isinstance:")
print(isinstance(pt, Point))

# Встроенные переменные:
# __doc__ - содержит строку с описанием класса;
# __name__ - содержит строку с именем класса;
# __dict__ - содержит набор атрибутов экземпляра класса.

class Point3D:
    x = 10
    y = 1
    z = 1


sx = Point3D()
sy = Point3D()
sz = Point3D()

print(sx.x)
print(sy.y)
print(sz.z)

sz.z = 50
print(Point3D.__dict__)
Point3D.z = 50
print(Point3D.__dict__)
