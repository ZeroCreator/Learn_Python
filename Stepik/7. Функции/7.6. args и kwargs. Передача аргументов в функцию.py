# *args и **kwargs. Передача аргументов в функцию.
# Множественные присваивания.
# Оператор '*' при распаковке аргумента:
print('Оператор "*" при распаковке аргумента:')

a, b, c = 4, 7, 8
print(a, b, c)

a, b, c = [True, 7, 'hello'] # Процесс распаковки
print(a, b, c)

a, *b, c = [True, 7, 'hello', 9, '54', 67, 4, 3]  # Процесс распаковки
print(a, b, c)

a, b, *c = [True, 7, 'hello', 9, '54', 67, 4, 3]  # Переменная со звездочкой будет представлять собой список
print(a, b, c)

*a, b, c = [True, 7, 'hello', 9, '54', 67, 4, 3]
print(a, b, c)

*a, b, c = (True, 7, 'hello', 9, '54', 67, 4, 3) # Распаковка кортежа
print(a, b, c)

*a, b, c = 'hello world' # Распаковка строки
print(a, b, c)

*a, b, c = [2, 3]
print(a, b, c)

s = [4, 10]
print(list(range(1, 5)))
print(list(range(*s)))

def f(a, b, c, d):
    print(a, b, c, d)

f(1, 2, 3, 4)
a = ('hello', True, 78, [3, 4, 5])

f(*a)

# Оператор '*' при опеределении функции:
print('Оператор "*" при опеределении функции:')

def f(*args):
    print(args, type(args))

f(1, 2, 3, 4, 5, 6)
f(1, 2)
f()


def f(*args): # С помощью *args можем передать неограниченное количество неименованных агументов
    s = 0
    for i in args:
        s +=  i
    return s

print(f(1, 2, 3, 4, 5, 6))

# Передача функции именованных аргументов:
print('Передача функции именованных аргументов:')
def f(**kwargs):
    print(kwargs) # При распаковке именованных аргументов получаем словарь

f(a = 1, b = 5, c = 6)

def f(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
f(a = 1, b = 5, c = 6, name = 89)

# Комбинирование двух способов:
print('Комбинирование двух способов:')
def f(*args, **kwargs):
    print(args, kwargs) # Получим список и словарь


f(5, 4, 3, 5, 7, 7, a = 5, b = 8, d = 'hello')

print(1, 2, 3, 5, 43, sep=' ', end=' ')
def outPrint(*args, sep='#', end='@'):
    print(args, sep, end)

outPrint(1, 2, 3, 4, 5, sep='90')
outPrint(1, 2, end='90')
outPrint(1, 2)

a = [3, 4, 5, 6, 7]
print(a)
print(*a)
print(3, 4, 5, 6, 7)

#
print('Tasks')
# Напишите функцию count_args, которая принимает произвольное количество аргументов. Данная функция должна возвращать
# количество переданных ей на вход аргументов
def count_args(*args):
    a = len(args)
    return a

print(count_args(5, 6, 4))

#
def count_args(*args, **kwargs):
    return sum(map(len, (args, kwargs)))

# Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.
# Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке в виде пары <Ключ> = <Значения>,
# причем ключи должны следовать в алфавитном порядке.
def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(key, '=', value)

info_kwargs(first_name="John", last_name="Doe", age=33)

#
def info_kwargs(**kwargs):
    for k,v in sorted(kwargs.items()):
        print(f'{k} = {v}')


#
def info_kwargs(**keys):
    [print(f'{key} = {value}') for key, value in sorted(keys.items())]


#
def info_kwargs(**kwargs):
    for key in sorted(kwargs):
        print(f'{key} = {kwargs[key]}')



