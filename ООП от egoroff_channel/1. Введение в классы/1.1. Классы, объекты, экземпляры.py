# Классы, объекты, экземпляры.
# Объект - контейнер, состоящий из:
# 1. данных и состояния (атрибуты класса)
# 2. поведения (методы класса)

print(isinstance(4, int))
print(isinstance(4, float))
print(isinstance(4, object))
print(type(int))

# Класс - шаблон создания объектов.
print('Создание класса:')
class Car:
    pass

a = Car()
print(type(a))

b = Car()

class Car:
    model = 'BMW'
    engine = 1.6

c = Car()



