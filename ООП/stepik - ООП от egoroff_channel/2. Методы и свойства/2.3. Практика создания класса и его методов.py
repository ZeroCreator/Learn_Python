# Практика создания класса и его методов.
# Класс Point(x,y).
class Point:

    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y

# перемещение точек по координатной плоскости:
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

# возвращение в начало координат
    def go_home(self):
        self.x = 0
        self.y = 0


p1 = Point(3, 4)
p2 = Point(-54, 32)
p3 = Point()
p3.move_to(4, 5)
p3.move_to(-90, 5)

# Редактирование кода:
from math import sqrt
class Point:

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f"Точка с координатами ({self.x}, {self.y})")

# метод для работы с несколькими экземплярами:
    # рассчитать дистанцию между двумя точками:
    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Точка")
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)


p4 = Point(4)
p4.move_to(4, 8)
p4.move_to(8, 8)
p4.go_home()

p5 = Point()
p5.print_point()
p5.move_to(7, 43)
p5.print_point()

p6 = Point()
p6.print_point()

p7 = Point(6, 0)
p8 = Point(0, 8)
p7.calc_distance(p8)

# Создание аттрибута, который распространяется на весь класс:
from math import sqrt
class Point:

    list_points = []

    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x, coord_y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Аргумент должен принадлежать классу Точка")
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)


p11 = Point()
print(p11)
p12 = Point(4, 5)
print(Point.list_points)
print(Point.list_points[1])
print(Point.list_points[1].x)
print(Point.list_points[1].y)


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
