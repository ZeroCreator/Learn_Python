# Функция zip.
# zip(iter1 [, iter2 [, iter3] ...]) - создает кортежи со значениями соответсвующих переменных из переданных коллекций.

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]

z = zip(a, b)
print(*z)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"
z = tuple(zip(a, b, c))
# print(z)
for v1, v2, v3 in z:
    print(v1, v2, v3)

z1, z2, z3, z4 = zip(a, b, c)
print(z1, z2)

z = zip(a, b, c)
lz = list(z)
print(*zip(*lz))

t1, t2, t3 = zip(*lz)
print(t1, t2, t3, sep='\n')

# Tasks
print("Tasks")
# Подвиг 1. Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой.
# При реализации программы используйте функции zip и map. Выведите на экран первые три значения, используя функцию next.
# Значения выводятся в строчку через пробел. (Полагается, что три выходных значения всегда будут присутствовать).
a = list(map(int, input().split()))
b = list(map(int, input().split()))
rez = [x[0]*x[1] for x in zip(a, b)]
print(*[rez[i] for i in range(3)])

#
lst1 = map(int, input().split())
lst2 = map(int, input().split())

lst = map(lambda x, y: x * y, lst1, lst2)

print(*(next(lst) for _ in range(3)))

#
n=map(int, input().split())
m=map(int, input().split())
res=(x*y for x,y in zip(n, m))
for _ in range(3):
    print(next(res), end= " ")


# Подвиг 4. Вводится строка из слов, записанных через пробел. Необходимо на их основе составить прямоугольную
# таблицу из трех столбцов и N строк (число строк столько, сколько получится). Лишнее (выходящее) слово - отбросить.
# Реализовать эту программу с использованием функции zip. Результат отобразить на экране в виде прямоугольной таблицы
# из слов, записанных через пробел (в каждой строчке).
t = list(map(str, input().split()))
x = iter([i for i in t])
rez = list(zip(x, x, x))
for i in rez:
    print(*i)

#
s = input().split()

lst = [s[i::3] for i in range(len(s) // 3)]

for i in zip(*lst):
    print(*i)

#
for row in zip(*[iter(input().split())]*3):
    print(*row)

#
s = iter(input().split())
for x in zip(s, s, s):
    print(' '.join(x))

#
s = input().split()
a = zip(*[iter(s)] * 3)
for i in a:
    print(*i)

# Подвиг 3. Вводится таблица целых чисел. Необходимо сначала эту таблицу представить двумерным списком чисел, а затем,
# с помощью функции zip выполнить транспонирование этой таблицы (то есть, строки заменить на соответствующие столбцы).
# Результат вывести на экран в виде таблицы чисел (числа в строках следуют через пробел).
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']
lst = list([i.split() for i in lst_in])
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = int(lst[i][j])

lst1 = zip(*[i for i in lst])
for i in lst1:
    print(*i)

#
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst = [list(map(int, i.split())) for i in lst_in]

for i in zip(*lst):
    print(*i)


# Подвиг 2. Вводится неравномерная таблица целых чисел. С помощью функции zip выровнить эту таблицу, приведя ее к
# прямоугольному виду, отбросив выходящие элементы. Вывести результат на экран в виде такой же таблицы чисел.
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
lst = [list(map(int, i.split())) for i in lst_in]
t = zip(*lst)
s = zip(*t)
for i in s:
    print(*i)

#
list(map(print, *zip(*map(str.split, lst_in))))

#
for i in zip(*zip(*lst_in)):
    print(*i, sep='')

#
z = zip(*zip(*lst_in))
for i in z:
    print(''.join(list(i)))

#
[print(*c, sep='') for c in zip(*zip(*lst_in))]

#
mport sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)

lst_in = [list(map(int, x.split())) for x in lst_in]
# скармливаем zip нашу распакованную матрицу
res = [list(row) for row in zip(*lst_in)]
# из-за того, что в процессе матрицу повернуло, траснпонируем ее еще раз
for row in zip(*res):
    print(*row)

