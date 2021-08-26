# Практика создания класса и его методов.
# Класс Point.
class Point:

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


p1 = Point(3, 4)
p2 = Point(-54, 32)

#
print('Tasks')
# Создайте класс Dog, у которого есть:
# конструктор __init__, принимающий 2 аргумента: name, age.
# метод description, который возвращает строку в виде "<name> is <age> years old"
# метод speak принимающий один аргумент, который возвращает строку вида "<name> says <sound>";
# jack = Dog("Jack", 4)
# print(jack.description()) # распечатает 'Jack is 4 years old'
# print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
# print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'
    def speak(self, sound):
        return f'{self.name} says {sound}'



# В этом задании вам предстоит реализовать свой стек(stack) -  это упорядоченная коллекция элементов, организованная по
# принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
# Ваша задача реализовать класс Stack, у которого есть:
# метод __init__  создаёт новый пустой стек. Параметры данный метод не принимает. Создает атрибут экземпляра values,
# где будут в дальнейшем хранятся элементы стека в виде списка (list), изначально при инициализации задайте значение
# атрибуту values равное пустому списку;
# метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает.
# метод pop() удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент. Стек изменяется.
# Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение "Empty Stack";
# метод peek() возвращает верхний элемент стека, но не удаляет его. Параметры не требуются, стек не модифицируется.
# Если элементов в стеке нет, распечатайте сообщение "Empty Stack", верните None после этого;
# метод is_empty() проверяет стек на пустоту. Параметры не требуются, возвращает булево значение.
# метод size() возвращает количество элементов в стеке. Параметры не требуются, тип результата - целое число.
class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        return self.values.pop() if self.values else print("Empty Stack")

    def peek(self):
        return self.values[-1] if self.values else print("Empty Stack")

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)


s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2


#
class Stack(list):
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values):
            return self.values.pop()
        else:
            print('Empty Stack')

    def peek(self):
        if self.is_empty():
            print('Empty Stack')
        else:
            return self.values[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.values)


#
class Stack:
    def __init__(self):
        """ создаёт новый пустой стек. Параметры данный метод не принимает.
            Создает атрибут экземпляра values, где будут в дальнейшем хранятся элементы стека в виде списка (list),
            изначально при инициализации задайте значение атрибуту values равное пустому списку;"""
        self.values = []
        self.item = None

    def push(self, item):
        """ добавляет новый элемент на вершину стека, метод ничего не возвращает."""
        self.item = item
        self.values.append(self.item)

    def pop(self):
        """ удаляет верхний элемент из стека. Параметры не требуются, метод возвращает элемент. Стек изменяется.
            Если пытаемся удалить элемент из пустого списка, необходимо вывести сообщение "Empty Stack";"""
        if not self.is_empty():
            return self.values.pop()
        else:
            print('Empty Stack')

    def peek(self):
        """ возвращает верхний элемент стека, но не удаляет его.
            Параметры не требуются, стек не модифицируется.
            Если элементов в стеке нет, распечатайте сообщение "Empty Stack", верните None после этого;"""
        if not self.is_empty():
            return self.values[-1]
        else:
            print('Empty Stack')

    def is_empty(self):
        """  проверяет стек на пустоту. Параметры не требуются, возвращает булево значение."""
        if not self.values:
            return True
        else:
            return False

    def size(self):
        """ возвращает количество элементов в стеке.
            Параметры не требуются, тип результата - целое число."""
        return len(self.values)

#
