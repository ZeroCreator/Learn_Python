# Замыкания в Python. Вложенные функции.
def say_name(name):
    def say_goodbye():
        print("Don't say me godbye, " + name + "!")

    say_goodbye()

say_name("Sergey")


def say_name(name):
    def say_goodbye():
        print("Don't say me godbye, " + name + "!")

    return say_goodbye

f = say_name("Sergey")
f2 = say_name("Python")
f()
f2()

# Функция - счетчик
print("Функция - счетчик")
def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step

c1 = counter(10) # счетчик начинается с 10
c2 = counter() # счетчик начинается с 0
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())


# Удаление ненужных символов в начале и в конце строки
print("Удаление ненужных символов в начале и в конце строки")
def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(" !?,.:")

print(strip1(" hello python! .. "))
print(strip2(" hello python! .. "))


#
print("Tasks")
# Используя замыкания функций, определите вложенную функцию, которая бы увеличивала значение переданного параметра на 5
# и возвращала бы вычисленный результат. При этом внешняя функция должна иметь следующую сигнатуру:
# def counter_add(): ...
# Вызовите функцию counter_add и результат ее работы присвойте переменной с именем cnt. Вызовите внутреннюю функцию
# через переменную cnt со значением k, введенным с клавиатуры:
# k = int(input())
# Выведите результат на экран.

def counter_add():
    def increase_number(cnt):
        cnt += 5
        return cnt
    return increase_number


k = int(input())
cnt = counter_add()
print(cnt(k))


#
def counter_add():
    def counter_in(k):
        return k + 5
    return counter_in


k = int(input())
cnt = counter_add()
print(cnt(k))

# Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение своего аргумента на некоторую
# величину n - параметр внешней функции с сигнатурой:
# def counter_add(n): ...
# Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt. Вызовите
# внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
# k = int(input())
# Выведите результат на экран.
def counter_add(n):
    def increase_number(cnt):
        return cnt + n
    return increase_number

k = int(input())
cnt = counter_add(2)
print(cnt(k))


# Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s (s - строка, параметр
# внутренней функции). Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью реализованного
# замыкания. Результат выведите на экран.
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
def add_tag(str):
    def inner_funk():
        return f"<h1>{str}</h1>"
    return inner_funk

str = input()
p = add_tag(str)
print(p())


#
def counter_add():
    def counter_in(s):
        return f'<h1>{s}</h1>'
    return counter_in

s = input()

print(counter_add()(s))


#  Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s (s - строка, параметр внутренней
#  функции) в произвольный тег, содержащийся в переменной tag - параметре внешней функции.
# Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым. Вторую строку нужно
# поместить в тег из первой строки с помощью реализованного замыкания. Результат выведите на экран.
# P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
def add_tag(tag):
    def inner_funk(s):
        return f"<{tag}>{s}</{tag}>"
    return inner_funk


tag = input()
s = input()

p = add_tag(tag)
print(p(s))


#
def counter_add(tag):
    def counter_in(s):
        return f'<{tag}>{s}</{tag}>'
    return counter_in

tag = input()
s = input()

print(counter_add(tag)(s))

#
def counter_add(tag):
    def inner_func(s):
        return f'<{tag}>{s}</{tag}>'
    return inner_func


tag = input()
s = input()
cnt = counter_add(tag)
print(cnt(s))


#
def counter_add(x):
    def zam(k):
        nonlocal x
        return f"<{x}>{k}</{x}>"

    return zam


teg,st = input(),input()
print(counter_add(teg)(st))


# Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел, записанных
# через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции. Если tp = 'list',
# то используется список, иначе (при другом значении) - кортеж.
# Далее, на вход программы поступают две строки: первая - это значение для параметра tp; вторая - список целых чисел,
# записанных через пробел. С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.
# Результат вывести на экран командой (lst - ссылка на коллекцию):
# print(lst)
def array_definition(tp):
    def convert_string(s):
        if tp == "list":
            return list(s)
        return tuple(s)
    return convert_string


tp = input()
s = map(int, input().split())

print(array_definition(tp)(s))

#
def counter_add(tp):
    def inner_func(s):
        if tp == 'list':
            return list(map(int, s.split()))
        elif tp == 'tuple':
            return tuple(map(int, s.split()))
    return inner_func


t = input()
s = input()
lst = counter_add(t)
print(lst(s))


#
def counter_add(x):
    def zam(k):
        nonlocal x
        if x == 'list':
            x = list(int(i) for i in k.split())
        else:
            x = tuple(int(i) for i in k.split())
        return x

    return zam


type_, sp = input(), input()
print(counter_add(type_)(sp))



