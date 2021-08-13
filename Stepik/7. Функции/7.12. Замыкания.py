# Замыкания.
# замыкания - когда функция пользуется переменными, не обявленными в ее теле.
def main_func(name):

    def inner_func():
        print('helllo my friend', name)

    inner_func()

main_func('Ivan')

r = main_func('Misha')
v = main_func('Vasya')

def adder(value):

    def inner(a):
        return value + a

    return inner

a2 = adder(2)

print(a2(5))
print(a2(10))

a5 = adder(5)
print(a5(10))

# Изменение значений переменных:
print('Изменение значений переменных:')
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count

    return inner

q = counter()
print(q())
print(q())
print(q())
print(q())

r = counter()
print(r())
print(r())
print(r())

# Замыкания. Часть 2
# Нахождение среднего арифметического:
print('Нахождение среднего арифметического:')
def average_numbers():
    numbers = []
    def inner(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers) / len(numbers)
    return inner

r1 = average_numbers()
print(r1(5))
print(r1(10))

d2 = average_numbers()
print(d2(100))

def average_numbers1():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa
        nonlocal count
        summa = summa + number
        count += 1

        return summa / count
    return inner

k = average_numbers1()
print(k(10))
print(k(20))
print(k(30))

# Функция - таймер:
print('Функция - таймер:')
from datetime import datetime
from time import perf_counter

def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner

r = timer()
print(r())
print(r())

#
def add(a, b):
    return a + b

def mult(a, b, c):
    return a*b*c

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)

    return inner

q = counter(add)
print(q(10, 20))
print(q(40, 50))

m = counter(mult)
print(m(10, 5, 7))