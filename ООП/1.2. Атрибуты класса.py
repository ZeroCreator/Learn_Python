# Атрибуты класса.
class Person:
    name = 'Ivan'
    age = 30

print(Person.name)
print(Person.age)

print('Посмотреть все атрибуты класса:')
Person.__dict__
print(Person.__dict__)

# or
print(getattr(Person, 'name'))
print(getattr(Person, 'age'))
print(getattr(Person, 'x', 100))    # третий параметр позволяет избежать ошибки

#
print('Изменить значение атрибута:')
Person.name = 'Mosha'
print(Person.name)
Person.x = 100
print(Person.x)

Person.x = [1, 2, 3]
print(Person.x)

#
print(' Встроенная функция setattr(obj, name, value):')
setattr(Person, 'x', 200)
print(Person.x)

#
print('Создание нового атрибута класса:')
setattr(Person, 'y', 10)
print(Person.y)

#
print('Удаление атрибута класса:')
print(Person.__dict__)
del Person.x
print(Person.__dict__)

delattr(Person, 'y')
print(Person.__dict__)

#
print('Вызвать экземпляр класса:')
Person()
print(Person())
a = Person()

Person.z = 100

# Вам необходимо создать класс Cat и внутри него два атрибута: name со значением 'Матроскин' и color со значением
# 'black'
# После этого создайте экземпляр класса и сохраните его в переменную my_cat
class Cat:
    name = 'Матроскин'
    color = 'black'
my_cat = Cat()

class Cat:
    def __init__(self, name='Матроскин', color='black'):
        self.name = name
        self.color = color


my_cat = Cat()

class Cat:
    name, color = "Матроскин", "black"

my_cat = Cat()




