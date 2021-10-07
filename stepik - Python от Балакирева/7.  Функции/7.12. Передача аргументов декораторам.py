# Передача аргументов декораторам.
# Декоратор для вычисления производных произвольных функций
import math


def df_decorator(dx=0.01):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper
    return func_decorator

# Декораторы с параметрами
#@df_decorator(dx=0.0000001)
def sin_df(x):
    return math.sin(x)


#df = df_decorator(dx=0.001)
#sin_df = f(sin_df)
# Это тоже самое, что и :
sin_df = df_decorator(dx=0.001)(sin_df)

df = sin_df(math.pi/3)
print(df)

# Потеря имени и описания
# Передача аргументов декораторам.
# Декоратор для вычисления производных произвольных функций
import math


def df_decorator(dx=0.01):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__

        return wrapper
    return func_decorator


@df_decorator(dx=0.0000001)
def sin_df(x):
    """Функция для вычисления производной синуса"""
    return math.sin(x)


print(sin_df.__name__)
print(sin_df.__doc__)

# Или
from functools import wraps
def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        #wrapper.__name__ = func.__name__
        #wrapper.__doc__ = func.__doc__

        return wrapper
    return func_decorator


@df_decorator(dx=0.0000001)
def sin_df(x):
    """Функция для вычисления производной синуса"""
    return math.sin(x)


print(sin_df.__name__)
print(sin_df.__doc__)


#
print("Tasks")
#  Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и
#  возвращает их сумму.
# Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
# Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:
# s = input()
# Результат отобразите на экране.
def decorator(start=5):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            return func()
        return wrapper
    return func_decorator


def get_sum(s):
    s = list(map(int, input().split()))
    return sum(*s)