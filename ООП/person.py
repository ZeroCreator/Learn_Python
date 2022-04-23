from ООП.classtools import AttrDisplay # Импортирует обобщенный инструмент

class Person(AttrDisplay):
    """
    Создает и обрабатывает записи с информацией о людях
    """
    def __init__(self, name, job=None, pay=0): # конструктор принимает три аргумента
        self.name = name                # заполняет поля при создании
        self.job = job                  #  self - новый экзмпляр класса
        self.pay = pay

    def lastName(self):                  # методы, реализующие поведение экземпляров
        return self.name.split()[-1]    # self - подразумеваемый экзкмпляр

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __str__(self):                  # Добавленный метод
    #     return f"Person: {self.name}, {self.pay}" # Строка для вывода

class Manager(Person):      # Определение подкласса класса Person
    """
    Версия класса Person, адаптированная в соответсвии со специальными требованиями
    """
    def __init__(self, name, pay):              # Переопределенный конструктор
        Person.__init__(self, name, "mgr", pay) # Вызов оригинального конструктора со значением "mgr" в аргументе job

    def giveRaise(self, percent, bonus=.10): # переопределение метода
        Person.giveRaise(self, percent + bonus) # вызов версии из класса Person

    # def someThingElse(self):
    #     pass

# Объединение объектов в составной объект

# class Department:
#     def __init__(self, *args):
#         self.members = list(args)
#     def addMember(self, person):
#         self.members.append(person)
#     def giveRaises(self, percent):
#         for person in self.members:
#             person.giveRaise(percent)
#     def showAll(self):
#         for person in self.members:
#             print(person)

if __name__ == "__main__": # только когда файл запускается для тестирования
    # реализация самотестирования
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())  # вместо жестко определенных операций используются методы
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue)
    tom = Manager("Tom Jones", 50000) # Экземпляр Manager: __init__
    tom.giveRaise(.10)                       # Вызов адаптированной версии
    print(tom.lastName())                     # Вызов унаследованного метода
    print(tom)                               # Вызов унаследованного __str__

    # print("--All three--")
    # for object in (bob, sue, tom): # Обработка объектов обобщенным способом
    #     object.giveRaise(.10)      # Вызовет метод giveRaise этого объекта
    #     print(object)              # Вызовет общий метод __str__


"""
class Manager(Person): # Наследование
def giveRaise(self, ...): ... # Адаптация
def someThingElse(self, ...): ... # Расширение
tom = Manager()
tom.lastName() # Унаследованный метод
tom.giveRaise() # Адаптированная версия
tom.someThingElse() # Дополнительный метод
print(tom) # Унаследованный метод перегрузки
"""

# Объединение объектов в составной объект
#
# development = Department(bob, sue) # Встраивание объектов в составной объект
# development.addMember(tom)
# development.giveRaises(.10) # Вызов метода giveRaise вложенных объектов
# development.showAll() # Вызов метода __str__ вложенных объектов