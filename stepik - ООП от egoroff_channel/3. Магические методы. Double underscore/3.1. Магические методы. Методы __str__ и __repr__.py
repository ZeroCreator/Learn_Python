# 3.1 Магические методы. Методы __str__ и __repr__
# Отвечают за текстовое отображение объекта в системе.
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self): # Отображение объекта внутри системы (для разработчиков)
        return f"The object Lion - {self.name}"

    def  __str__(self): # Отображение объекта для пользователя
        return f"Lion - {self.name}"


q = Lion("Bob")
s = Lion("Simba")
print(q)
print(str(s))


#
print("Tasks")
# Создайте класс Person, у которого есть:
# конструктор __init__, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только
# 2 значения: "male" и "female", по умолчанию "male". Если в атрибут gender передается любое другое значение,
# печатать сообщение: "Не знаю, что вы имели ввиду? Пусть это будет мальчик!" и проставить атрибут gender значением "male"
# переопределить метод __str__ следующим образом:
# если объект - мужчина (атрибут gender = "male"), возвращать строку "Гражданин <Фамилия> <Имя>
# если объект - женщина (атрибут gender = "female"), возвращать строку "Гражданка <Фамилия> <Имя>
# p1 = Person('Chuck', 'Norris')
# print(p1) # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"
class Person:
    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        if gender not in ["male", "female"]:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = "male"
        else:
            self.gender = gender

    def __str__(self):
        if self.gender == "male":
            return f"Гражданин {self.surname} {self.name}"
        return f"Гражданка {self.surname} {self.name}"

p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3) # печатает "Гражданин Кеноби Оби-Ван"


#
class Person:
    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        if gender not in ["male", "female"]:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = "male"
        else:
            self.gender = gender

    def __str__(self):
        if self.gender == "male":
            return f"Гражданин {self.surname} {self.name}"
        return f"Гражданка {self.surname} {self.name}"


#
class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender in ('male', 'female'):
            self.gender = gender
        else:
            self.gender = 'male'
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')

    def __str__(self):
        if self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'
        return f'Гражданин {self.surname} {self.name}'

#
class Person:
    def __init__(self, name, surname, gender='male'):
        self.name, self.surname = name, surname
        if gender not in ('male', 'female'):
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            gender = 'male'
        self.gender = gender

    def __str__(self):
        return f"Граждан{('ка', 'ин')[self.gender == 'male']} {self.surname} {self.name}"


# Создайте класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
# конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо
# оставить только целые числа и сохранить их в атрибут values в виде списка;
# переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
# "Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по
# возрастанию (будьте аккуратнее с пробелами, они стоят только после запятых, см. пример ниже);
# "Пустой вектор", если наш вектор не хранит в себе значения
# v1 = Vector(1,2,3)
# print(v1) # печатает "Вектор(1, 2, 3)"
# v2 = Vector()
# print(v2) # печатает "Пустой вектор"
class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return f'Пустой вектор'


#
class Vector:
    def __init__(self, *args):
        self.values = [x for x in args if isinstance(x, int)]

    def __str__(self):
        if self.values:
            return f'Вектор{(*sorted(self.values),)}'
        else:
            return 'Пустой вектор'