# Инициализация объекта. Метод init.
# Магические методы: __xxx__
class Cat:
    breed = 'pers'

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

    def __init__(self):
        print('hello new object is', self)

Cat()
tom = Cat()
jerry = Cat()
print(tom.__dict__)


class Cat:

    def __init__(self, name, breed='pers', age=1, color='white'):
        print('hello new object is', self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

# self.xxx - имена аттрибутов
# age =  - входящие значения - аргументы функции

walt = Cat('Walt')
kelly = Cat('Kelly', age = 4)

Cat('Tom', 'siam', 40, 'black')

#
print('Tasks')
# Создайте класс Laptop, у которого есть:
# конструктор __init__, принимающий 3 аргумента: бренд, модель и цену ноутбука. На основании этих аргументов нужно для экземпляра создать атрибуты brand, model, price и также атрибут laptop_name - строковое значение, вида "<brand> <model>"
# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.price) # выводит 57000
# print(hp.laptop_name) # выводит "hp 15-bw0xx"
class  Laptop:

    def  __init__(self, brand,  model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'

laptop1=Laptop('Asus', '18-bdfx', 37000)
laptop2=Laptop('Samsung', '13-bsdf0xx', 47000)


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name)

#
class Laptop():
    def __init__(self, brand, model, price):
        self.laptop_name = brand + " " + model

#
class Laptop():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + " " + model


# Создайте класс SoccerPlayer, у которого есть:
# конструктор __init__, принимающий 2 аргумента: name, surname. Также во время инициализации необходимо создать
# 2 атрибута экземпляра: goals и assists - общее количество голов и передач игрока, изначально оба значения должны быть 0
# метод score, который принимает количество голов, забитых игроком, по умолчанию данное значение равно единице.
# Метод должен увеличить общее количество забитых голов игрока на переданное значение;
# метод make_assist, который принимает количество передач, сделанных игроком за матч, по умолчанию данное значение равно
# единице. Метод должен увеличить общее количество сделанных передач игроком на переданное значение;
# метод statistics, который вывод на экран статистику игрока в виде:
# <Фамилия> <Имя> - голы: <goals>, передачи: <assists>
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"
class  SoccerPlayer:

    def  __init__(self,  name,  surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"


# Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы "Полоска белая",
# "Полоска черная", начиная именно с фразы "Полоска белая"
# Пример работы с классом Zebra
# z1 = Zebra()
# z1.which_stripe() # печатает "Полоска белая"
# z1.which_stripe() # печатает "Полоска черная"
# z1.which_stripe() # печатает "Полоска белая"
# z2 = Zebra()
# z2.which_stripe() # печатает "Полоска белая"
class Zebra():

    def __init__(self,count = 0):
        self.count = count

    def which_stripe(self):
        self.count += 1
        if self.count % 2 == 0:
            print("Полоска черная")
        else:
            print("Полоска белая")


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"

#
class Zebra:
    flag = True
    def which_stripe(self):
        print('Полоска белая' if self.flag else 'Полоска черная')
        self.flag = not self.flag


#
class Zebra:
    stripe = 'Полоска белая'
    stripe1 = 'Полоска черная'
    def which_stripe(self):
        print(self.stripe)
        self.stripe, self.stripe1 = self.stripe1, self.stripe


#
'''
Если кто-то не понял условия if not self.cnt % 2 поясню:

False эквивалентно значению 0

True эквивалентно значению 1

Т.к. в начале атрибут self.cnt = 0, а 0 % 2 == 0, то это значит, что 0 % 2 == False.
Само выражение if self.cnt % 2 без знака == подразумевает значение True. То есть мы как бы говорим программе: напечатай 
"Белая", если 0 % 2 == True. Но мы уже выяснили, что 0 % 2 == False, для этого мы и добавляем союз not, т.к. not True == False
'''
class Zebra():

    def __init__(self, cnt=0):
        self.cnt = cnt

    def which_stripe(self):
        print("Полоска белая") if not self.cnt % 2 else print("Полоска черная")
        self.cnt += 1


# Создайте класс Person, у которого есть:

# 1. конструктор __init__, принимающий 3 аргумента: first_name, last_name, age.
# 2. метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
# 3. метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;
# p1 = Person('Jimi', 'Hendrix', 55)
# print(p1.full_name())  # выводит "Hendrix Jimi"
# print(p1.is_adult()) # выводит "True"

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return self.last_name + ' ' + self.first_name

    def is_adult(self):
        if self.age >= 18:
            return True
        return False

p1 = Person('Jimi', 'Hendrix', 17)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"


#
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return self.age > 17


