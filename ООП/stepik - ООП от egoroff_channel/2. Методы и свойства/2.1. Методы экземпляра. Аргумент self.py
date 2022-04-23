# Методы экземпляра. Аргумент self.
class Cat:
    def hello():
        print("Hello world from kitty")


# Cat.hello - функция - <function __main__.Cat.hello()>
# bob.hello - Метод - <bound method Cat.hello of <__main__.Cat object at 0x000001B0460F2DC8>>

# 1. Метод - это функция, объявленная внутри класса.
# 2. Метод - привязан к конкретному объекту и связан с ним.
# Функция не связана с отдельным объектом.
# 3. При вызове метода, тот объект, с которым он связан, будет автоматически подстовляться в аргумент функции.

class Cat:
    def hello(*args):
        print("Hello world from kitty", args)

jim = Cat()
print(jim.hello())  # Hello world from kitty (<__main__.Cat object at 0x00000206B9A0A248>,) где 0x206b9a0a248 - адрес памяти

#
class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

walt = Cat()
print(walt.show_breed())        # 'my breed is pers'

walt.breed = 'siam'
print(walt.show_breed())        # 'my breed is siam'

bob = Cat()
print(bob.show_breed())         # 'my breed is pers'

#
class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f'my name is {instance.name}')
        else:
            print('nothing')


mary = Cat()
mary.name = 'MARY'
print(mary.show_name())         # 'my name is MARY'

# Метод для создания атрибутов:
print('Метод для создания атрибутов:')
class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

    def show_name(instance):
        if hasattr(instance, 'name'):
            print(f'my name is {instance.name}')
        else:
            print('nothing')

    def set_value(koshka, value, age=0):
        koshka.name = value
        koshka.age = age

tom = Cat()
print(tom.show_name()) # nothing

tom.set_value('Tom')
print(tom.name) # Tom
print(tom.show_name) # my name is Tom

jerry = Cat()
jerry.set_value('Jarry', 15)

# Аргумент self
print('Аргумент self')
# self - общепринятое название объекта, у которого был вызван метод.

class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed(self):
        print(f'my breed is {self.breed}')

    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def new_method(self):


#
print('Tasks')
# Создайте класс Lion. В нем должен быть метод roar, который печатает на экран "Rrrrrrr!!!"
# Пример работы с классом Lion
# simba = Lion()
# simba.roar() # печатает Rrrrrrr!!!
class Lion:

    def roar(self):
        print('Rrrrrrr!!!')

#
class Lion:
    @staticmethod
    def roar():
        print('Rrrrrrr!!!')


# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
# В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент - значение,
# с которого начинается подсчет, по умолчанию равно 0
# Также нужно создать метод increment, который увеличивает счетчик на 1.
# Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>" и метод reset,
# который обнуляет экземпляр счетчика
# Пример работы с классом Counter:
# c1 = Counter()
# c1.start_from()
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 1"
# c1.increment()
# c1.display() # печатает "Текущее значение счетчика = 2"
# c1.reset()
# c1.display() # печатает "Текущее значение счетчика = 0"
#
# c2 = Counter()
# c2.start_from(3)
# c2.display() # печатает "Текущее значение счетчика = 3"
# c2.increment()
# c2.display() # печатает "Текущее значение счетчика = 4"

class Counter:

    def  start_from(self, count=0):
        self.count = count

    def  increment(self):
        self.count += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.count}')

    def reset(self):
        self.count = 0


# Создайте класс Point. У этого класса должны быть:
# метод set_coordinates, который принимает координаты по x и по y, и сохраняет их в экземпляр класса соответственно в атрибуты x и y
# метод get_distance, который обязательно принимает экземпляр класса Point и возвращает расстояние между двумя точками по теореме Пифагора. В случае, если в данный метод передается не экземпляр класса Point необходимо вывести сообщение "Передана не точка"
# Пример работы с классом Point:
# p1 = Point()
# p2 = Point()
# p1.set_coordinates(1, 2)
# p2.set_coordinates(4, 6)
# d = p1.get_distance(p2) # вернёт 5.0
# p1.get_distance(10) # Распечатает "Передана не точка"
class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, arg):
        if isinstance(arg, Point):
            return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
        else:
            print(f'Передана не точка')


#
class Point():

    def set_coordinates(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_distance(self, point):
        try:
            return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        except:
            print("Передана не точка")

#
class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other):
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        print('Передана не точка')

#

