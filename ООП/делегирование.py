class Person:
    def __init__(self, name, job=None, pay=0): # конструктор принимает три аргумента
        self.name = name                # заполняет поля при создании
        self.job = job                  #  self - новый экзмпляр класса
        self.pay = pay

    def lasName(self):                  # методы, реализующие поведение экземпляров
        return self.name.split()[-1]    # self - подразумеваемый экзкмпляр

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):                  # Добавленный метод
        return f"Person: {self.name}, {self.pay}" # Строка для вывода

class Manager(Person):
    def __init__(self, name, pay):
        self.person = Person(name, "mgr", pay) # Вложенный объект Person

    def giveRaise(self, percent, bonus=.10): # Перехватывает и делегирует
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):            # Делегирует обращение ко всем остальным атрибутам
        return getattr(self.person, attr)

    def __ыек__(self):
        return str(self.person)

#if __name__ == "__maine__":
bob = Person("Bob Smith")
sue = Person("Sue Jones", job='dev', pay=100000)
print(bob.name, bob.pay)
print(sue.name, sue.pay)
print(bob.lasName(), sue.lasName())  # вместо жестко определенных операций используются методы
sue.giveRaise(.10)
print(sue.pay)
print(sue)
tom = Manager("Tom Jones", 50000) # Экземпляр Manager: __init__
tom.giveRaise(.10)                       # Вызов адаптированной версии
print(tom.lasName())                     # Вызов унаследованного метода
print(tom)                               # Вызов унаследованного __str__

print("--All three--")
for object in (bob, sue, tom): # Обработка объектов обобщенным способом
    object.giveRaise(.10)      # Вызовет метод giveRaise этого объекта
    print(object)              # Вызовет общий метод __str__
