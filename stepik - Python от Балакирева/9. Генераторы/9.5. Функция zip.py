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



