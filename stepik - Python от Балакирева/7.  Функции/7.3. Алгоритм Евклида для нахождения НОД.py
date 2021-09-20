# Алгоритм Евклида для нахождения НОД
# НОД(18, 24) = 6
# пока a != b
#   находим большее среди a и b
#   уменьшаем большее на величину меньшего
# выводим полученное значение величины a (или b)

# Медленный алгоритм Евклида
print("Медленный алгоритм Евклида")


import time


def get_nod(a, b):
    """Вычисляется НОД для натуральных чисел a и b
        по медленному алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a

res = get_nod(18, 24)
print(res)
help(get_nod)


# Тестирование функции
def test_nod(func):
    #--- тест №1 -------------------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("test1 - OK")
    else:
        print("test1 - fail")

    # --- тест №2 -------------------------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("test2 - OK")
    else:
        print("test2 - fail")

    # --- тест №3 -------------------------
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("test3 - OK")
    else:
        print("test3 - fail")


test_nod(get_nod)


# Быстрый алгоритм Евклида
print("Быстрый алгоритм Евклида")
# НОД(2, 100) = 2
# пока меньшее число больше 0
#   большему числу присваиваем остаток
#   от деления на меньшее число
# вводим большее число

def get_nod(c, d):
    """Вычисляется НОД для натуральных чисел a и b
        по быстрому алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    if c < d:
        c, d = d, c

    while d != 0:
        c, d = d, c % d

    return c

res1 = get_nod(2, 100)
print(res1)

#
print("Tasks")
#
from math import gcd as get_nod
