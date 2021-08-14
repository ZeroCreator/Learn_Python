# Декораторы.
# Декоратор это функция внутрь которой входит еще какая либо функция выполнение которой дополняет функция декоратор,
# в декораторе также присутствует замыкание.


def decorator(func):

    def inner():
        print('start decorator...')
        func()
        print('finish decorator...')

    return inner

def say():
    print('hello world')

def buy():
    print('buy world')

d = decorator(say)
print(d)
print(d())

print()

print(say.__name__) # -> say
say = decorator(say)
print(say.__name__) # -> inner
say()

print()
buy = decorator(buy)
buy()

print()
# Потеря имени функции и потеря документации:
# 1 - при использовании декораторов функция, которая декорируется, теряет свое имя и строки с описанием (документацию)
# 2 - чтобы этого избежать можно выбрать два пути:
# 2а - в функции-декораторе нужно добавить строки с пересохранением __name__ и __doc__ функции inner (сохранить значения функции-аргумента)
# 2б - импортировать модуль wraps (from functool import wraps) и навесить декоратор @wraps на inner функцию
print('Потеря имени функции и потеря документации:')
def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

def say():
    print('hello world')

def sqr(x):
    """
    Функция возводит х в квадрат
    :param x:
    :return:
    """
    print(x**2)

print(sqr.__name__) # -> sqr
print(sqr.__doc__)
print(help(sqr))

sqr = table(sqr)
print(sqr.__doc__)
print(help(sqr))

# решение
print('решение №1')
def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__

    return inner

def say():
    print('hello world')

def sqr(x):
    """
    Функция возводит х в квадрат
    :param x:
    :return:
    """
    print(x**2)

print(sqr(20))
print(sqr.__name__)
print(sqr.__doc__)

sqr = table(sqr)
print(sqr(20))
print(sqr.__name__)
print(sqr.__doc__)

print('решение №2')
from functools import wraps

def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner

def say():
    print('hello world')

def sqr(x):
    """
    Функция возводит х в квадрат
    :param x:
    :return:
    """
    print(x**2)

print(sqr(6))

sqr = table(sqr)
print(sqr(6))

#
import time
from functools import wraps

def gettime(func):

    @wraps(func)
    def wrapper(*args):
        a = time.time()
        print('начало работы')
        res = func(*args)
        b = time.time() - a
        print(f"конец работы. время {b}")
        return res
    return wrapper


def header(func):
    @wraps(func)
    def wrapper(*args):
        print("start")
        f = func(*args)
        print("end")
        return f
    return wrapper
# listgen= header(gettime(listgen))
@header
@gettime
def listgen(n):
    """
    лалала
    :param n:
    :return:
    """
    print('header')
    return [i for i in range(n)]
lst = listgen(10**7)
print(lst)
help(listgen)