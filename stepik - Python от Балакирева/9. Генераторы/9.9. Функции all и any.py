# Функции all и any.
print("all")
a = [True, True, True, True]
b = all(a)
print(b)


a = [True, True, True, False]
b = all(a)
print(b)


a = [True, True, True, True, [], [1, 2, 3], {}]
b = all(a)
print(b)

a = [True, True, True, True, [1, 2, 3], {1}]
b = all(a)
print(b)


a = [True, True, True, True, [1, 2, 3], {1}]
all_res = True
for x in a:
    all_res = all_res and bool(x)

print(all_res)

print("any")
a = [True, True, True, True, [], [1, 2, 3], {}]
b = any(a)
print(b)

a = [False, False, False, False]
b = any(a)
print(b)

a = [True, True, True, True, [1, 2, 3], {1}]
all_res = False
for x in a:
    all_res = all_res or bool(x)

print(all_res)

# Игра крестики-нолики:
print("Игра крестики-нолики:")
p = ['x', 'x', '0', '0', 'x', '0', 'x', 'x', 'x']

# row_1 = all(map(lambda x: x == "x", p[:3]))
# row_2 = all(map(lambda x: x == "x", p[3:6]))
# row_3 = all(map(lambda x: x == "x", p[6:]))



def true_x(a):
    return a == 'x'

# Проверка по строчкам:
row_1 = all(map(true_x, p[:3]))
row_2 = all(map(true_x, p[3:6]))
row_3 = all(map(true_x, p[6:]))

print(row_1, row_2, row_3)

# Проверка по стобцам
col_1 = all(map(true_x, p[::3]))
col_2 = all(map(true_x, p[1::3]))
col_3 = all(map(true_x, p[2::3]))

print(col_1, col_2, col_3)

# Игра сапер
print("Игра сапер")
N = 10
P = [0]*(N*N)

P[4] = "*"

loss = any(map(lambda x: x == "*", P))
print(loss)

#
print("Tasks")
# Вводится строка целых чисел через пробел. Необходимо определить, являются ли все эти числа четными.
# Вывести True, если это так и False - в противном случае.
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 2 4 6 8 22 56
# Sample Output:
# True
st = list(map(int, input().split()))
print(all(map(lambda x: x % 2 == 0, st)))

#
print(not any(int(i) % 2 for i in input().split()))

#
print(all(map(lambda x: x % 2 == 0, map(int, input().split()))))

#
print(all(not int(c) % 2 for c in input().split()))

#
print(all(map(lambda x: x % 2 == 0, map(int, input().split()))))

# Вводится строка вещественных чисел через пробел. Необходимо определить, есть ли среди них хотя бы одно отрицательное.
# Вывести True, если это так и False - в противном случае.
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 8.2 -11.0 20 3.4 -1.2
# Sample Output:
# True
print(any(map(lambda x: x < 0, map(float, input().split()))))

#
print(any(float(c) < 0 for c in input().split()))

#
print(any(i < 0 for i in map(float, input().split())))

# Объявить функцию с именем is_string, на вход которой поступает коллекция (список, кортеж, множество).
# Она должна возвращать True, если все элементы коллекции строки и False - в противном случае.
# Сигнатура функции должна быть, следующей:
# def is_string(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# Sample Output:
# True
def is_string(lst):
    return all(map(lambda x: type(x) is str, lst))

#
is_string = lambda x: all(map(lambda x: type(x) is str, x))

#
def is_string(lst):
    return all(isinstance(x, str) for x in lst)

#
def is_string(lst):
  return all(type(c) is str for c in lst)


# Вводятся оценки студента в одну строчку через пробел. Необходимо определить, имеется ли в этом списке хотя бы одна
# оценка ниже тройки. Если это так, то вывести на экран строку "отчислен", иначе - "учится".
# Задачу реализовать с использованием одной из функций: any или all.
# Sample Input:
# 3 3 3 2 3 3
# Sample Output:
# отчислен
print(("учится", "отчислен") [any(map(lambda x: int(x) < 3, input().split()))])

#
print("учится" if all(map(lambda x: x > 2, map(int, input().split()))) else "отчислен")

#
print(['учится', 'отчислен'][any(int(c) < 3 for c in input().split())])


# Вводится текущее игровое поле для игры "Крестики-нолики" в виде следующей таблицы:
# # x o
# x # x
# o o #
# Здесь # - свободная клетка. Нужно объявить функцию с именем is_free, на вход которой поступает игровое поле в виде
# двумерного (вложенного) списка. Данная функция должна возвращать True, если есть хотя бы одна свободная клетка и
# False - в противном случае.
# Sample Input:
# # x o
# x # x
# o o #
# Sample Output:
# True
def is_free(lst):
    for i in lst:
        return any(map(lambda x: x == "#", i))

print(is_free([["#", "x", "o"],["x", "#", "x"],["o", "o", "#"]]))

#
def is_free(lst):
    return any('#' in i for i in lst)

#
import sys

lst = list(map(lambda x: x.strip().split(), sys.stdin.readlines()))


def is_free(lst):
    return any(j == '#' for i in lst for j in i)

