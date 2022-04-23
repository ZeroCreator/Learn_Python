# Classmethod and staticmethod.
'''
class Example:

    def hello():
        print("hello")
        # Можем вызвать от класса, но не можем вызывать от экземпляоа класса (instance)

    def instance_hello(self):
        print(f"instance_hello {self}")
        # Можем вызвать от экземпляоа класса (instance), но не можем вызывать от класса

Example.hello
Example.hello()

p = Example()
print(p.hello) # Можно вызвать от класса
# print(p.hello()) # Нельзя вызвать от экземпляра: TypeError: hello() takes 0 positional arguments but 1 was given

q = Example()
q.instance_hello()
print(q)
# Example.instance_hello() # TypeError: instance_hello() missing 1 required positional argument: 'self'
'''
# декоратор staticmethod - не привязывается ни к клссу, ни к экземпляру класса, поэтому его можно
# вызвать обоими способами
print("декоратор staticmethod")
class Example:
    def hello():
        print("hello")

    def instance_hello(self):
        print(f"instance_hello {self}")

    @staticmethod
    def static_hello():
        print("static_hello")

Example.static_hello()
y = Example()
y.static_hello()

# декоратор classcmethod - когда нужна обработка не экземплятор класса, а целого класса.
print("декоратор classcmethod")

class Example:
    def hello():
        print("hello")

    def instance_hello(self):
        print(f"instance_hello {self}")

    @staticmethod
    def static_hello():
        print("static_hello")

    @classmethod
    def class_hello(cls):
        print(f"instance_hello {cls}")

c = Example.class_hello()
print(c)

a = Example()
g = a.class_hello()
print(g)

print(a.__class__)

#
print("Tasks")
# Создайте класс Robot, у которого есть:
# атрибут класса population. В этом атрибуте будет хранится общее количество роботов, изначально принимает значение 0;
# конструктор __init__, принимающий 1 аргумент name. Данный метод должен сохранять атрибут name и печатать сообщение
# вида "Робот <name> был создан". Помимо инициализации робота данный метод должен увеличивать популяцию роботов на единицу;
# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"
# метод say_hello, которой печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"
# метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"
# r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
# r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
# Robot.how_many() # печатает "1, вот сколько нас еще осталось"
# r2.destroy() # печатает "Робот R2-D2 был уничтожен"

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")


r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"


#
class Robot:
    population = 0

    def __init__(self, name):
        self.name=name
        print(f'Робот {self.name} был создан')
        Robot.population += 1


    def destroy(self):
        Robot.population -= 1
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @staticmethod
    def how_many():
        print(f'{Robot.population}, вот сколько нас еще осталось')
