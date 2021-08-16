# Lambda функции.
# Синтаксис (шаблон для определения функции):
# lambda арг1, арг2, ... : выражение
def f(x):
    return x**2

print(f(4))

r = lambda x: x**2
print(r(7))

# Используется, когда нужно выполнить одно действие.
print('Используется, когда нужно выполнить одно действие')
def perimetr(a, b, c):
    return a + b + c

per = lambda a, b, c: a + b + c
print(per(5, 8, 4))

# Функция lambda без аргументов:
print('Функция lambda без аргументов:')
h = lambda : 'hello'
print(h())

# Заменяют те функции, в которых есть return
# Условный оператор if:
print('Условный оператор if:')
def f(x):
    if x > 0:
        return 'posittive'
    else:
        return 'negative'


t = lambda x: 'positive' if x > 0 else 'negative'
print(t(-5))

# Сортировка по последней цифре:
print('Сортировка по последней цифре:')
def f(x):
    return x%10

a = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
a.sort(key=f)
print(a)

a = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
a.sort(key=lambda x: x%10)
print(a)

# Сортировка по предпоследней цифре:
print('Сортировка по предпоследней цифре:')
a = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
a.sort(key=lambda x: x//10%10)
print(a)

# Линейная функция
print('Линейная функция')
def linear(k, b):
    return lambda x: x*k + b

graf1 = linear(2, 5)
print(graf1(3))

graf2 = linear(-4, 1)
print(graf2(5))

#
print('Tasks')
# Напишите lambda функцию, которая принимает одно число и увеличивает его на 10.
adding_10 = lambda x: x + 10

# Напишите lambda функцию, которая принимает строку и отвечает на вопрос начинается ли переданная строка с буквы W
starts_with = lambda x: x[0] == 'W'

# В python есть стандартный модуль datetime.
# Внутри него имеется функция datetime.datetime.now() при помощи которой, можно найти текущую дату в формате
# (год, месяц, день, час, минуты, секунды, млсекунды)
# Ваша задача написать три lambda функция, которые принимают текущую дату и возвращают год, месяц и день соответственно.
# Эти три lambda функции нужно будет сохранить в переменные get_year, get_month и get_day соответственно.
import datetime

now = datetime.datetime.now()

get_day = lambda now: now.day

get_month = lambda now: now.month
get_year = lambda now: now.year

print(get_day(now),get_month(now),get_year(now))