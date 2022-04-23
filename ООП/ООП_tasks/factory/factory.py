# функция-генератор объектов с именем factory.Она ожидает получить объект класса (любого) вместе с одним или
# более аргументами конструктора класса. Функция использует специальный синтаксис
# вызова с переменным числом аргументов, чтобы создать и вернуть экземпляр.

def factory(aClass, *args, **kwargs): # Кортеж с переменным числом аргументов
    return aClass(*args, **kwargs) # Вызов aClass


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job


object1 = factory(Spam) # Создать объект Spam
object2 = factory(Person, "Guido", "guru") # Создать объект Person
print(object1)
print(object2)