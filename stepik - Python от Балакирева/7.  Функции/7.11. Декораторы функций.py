# Декораторы функций.


def func_decorator(func):
    def wrapper():
        print("------ что-то делаем перед вызовом функции")
        func()
        print("------ что-то делаем после вызова функции")

    return wrapper


def some_func():
    print("Вызов функции some_func")

"""
f = func_decorator(some_func) # Глобальная переменная
f()
"""

some_funс = func_decorator(some_func) # Декорирование
some_funс()

# Универсальный декоратор для любых функций
print("Универсальный декоратор для любых функций")


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("------ что-то делаем перед вызовом функции")
        res = func(*args, **kwargs)
        print("------ что-то делаем после вызова функции")
        return res

    return wrapper


def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"

some_funс = func_decorator(some_func) # Декорирование
res = some_funс("Python навсегда!", "h1")
print(res)

# Тестирование функций на скорость работы
print("Тестирование функций на скорость работы")
import time
def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы: {dt} сек")
        return res

    return wrapper


@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -=b
        else:
            b -= a
        return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a


#get_nod = test_time(get_nod)
#get_fast_nod = test_time(get_fast_nod)

res = get_nod(2, 1000000)
print(res)

res2 = get_fast_nod(2, 1000000)
print(res2)


#
print("Tasks")
# Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам: width и height -
# ширина и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит). То есть, функция имеет сигнатуру:
# def get_sq(width, height): ...
# Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):
# "Площадь прямоугольника: <значение>"
def  func_show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {res}")
        return res


    return wrapper


@ func_show
def  get_sq(width, height):
    return width * height


#
def get_sq(width, height):
    return width * height

def func_show(fn):
    def wropper(*args):
        print(f'Площадь прямоугольника: {fn(*args)}')
    return wropper


#
def func_show(func):
    def print_sq(*args, **kwargs):
        print(f'Площадь прямоугольника: {func(*args, **kwargs)}')

    return print_sq


def get_sq(width, height):
    return width * height



#  На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел. Необходимо
#  задать функцию с именем get_menu, которая преобразует эту строку в список из слов и возвращает этот список.
#  Сигнатура функции, следующая:
# def get_menu(s): ...
# Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
# 1. Пункт_1
# 2. Пункт_1
# ...
# N. Пункт_N
# Примените декоратор show_menu к функции get_menu, используя оператор @. Более ничего в программе делать не нужно.
# Сами функции не вызывать.
def show_menu(func):
    def


def get_menu(s):
    def wropper(*args, **kwargs):





#  На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию get_list, которая
#  преобразовывает эту строку в список из целых чисел и возвращает его. Определите декоратор для этой функции,
#  который сортирует список чисел по возрастанию. Результат сортировки должен возвращаться при вызове декоратора.
# Вызовите декорированную функцию get_list и отобразите полученный отсортированный список lst командой:
# print(*lst)
def sort_res(func):
    def inner_func(*args, **kwargs):
        return sorted(func(*args, **kwargs))

    return inner_func

@sort_res
def get_list(st):
    return list(map(int, st.split()))

lst = get_list(input())
print(*lst)


#
