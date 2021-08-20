# Вложенные списки (список внутри списка).
a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, [4, 5, 7, 11], 17, 19]]

x = [1, 2, 3]                           # Одномерный список
y = [[1, 2, 3], [2, 3, 4]]              # Двумерный список
z = [[[2, 3], [4, 5]], [[6, 7], [8, 9]]]# Трехмерный список

# Ctrl + Alt + L - для форматирования согласно PEP8
print(len(a))
print(a[2])                     # Одномерный список
print(len(a[2]))
print(a[2][3])                  # Двумерный список
print(a[0][3])
print(a[2][2][1])               # Трехмерный список

b = ['hello', 'hi', 'world']
print(b[2])                     # Одномерный список
print(b[2][2])                  # Двумерный список
print(b[2][-1])

# Матрицы (таблицы).
a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
# Обойти все элементы списка:
print('1. Обход элементов списка по значению:')
for i in a:
    for j in i:
        print(j, end=' ')
    print()

# сам список не меняется:
for i in a:
    for j in i:
        j += 10
        print(j, end=' ')
    print()

print(a)

print('2. Обход элементов списка по индексам:')
# При обходе используем два вложенных цикла:
a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]

for i in range(3):                  # Перебираем строки
    for j in range(4):              # Перебираем столбцы
        print(a[i][j], end=' ')
    print()

print('Меняем значение элементов:')
a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]

for i in range(3):                  # Перебираем строки
    for j in range(4):              # Перебираем столбцы
        a[i][j] += 10
        print(a[i][j], end=' ')
    print()
print(a)

#
print('Поменять строки и столбцы местами:')
a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
for j in range(4):                      # Перебираем столбцы
    for i in range(3):                  # Перебираем строки
        print(a[i][j], end=' ')
    print()

#
print('Обход матрицы справа - налево и снизу - вверх:')
for i in range(2, -1, -1):                  # Перебираем строки
    for j in range(3, -1, -1):              # Перебираем столбцы
        print(a[i][j], end=' ')
    print()

# Посчитать сумму каждой строки и каждого столбца:
print('Посчитать сумму каждой строки и каждого столбца:')
print('Сумма по строкам:')
for i in range(3):                  # Перебираем строки
    s = 0
    for j in range(4):              # Перебираем столбцы
        s += a[i][j]
    print(s)                        # Сумма будет обнуляться после обхода каждой строки

#
print('Сумма по столбцам:')
for j in range(4):              # Перебираем столбцы
    s = 0
    for i in range(3):          # Перебираем строки
        s += a[i][j]
    print(s)                    # Сумма будет обнуляться после обхода каждой строки

# Заполение вложенного списка:
print('Заполение вложенного списка:')
a = []
n = int(input())        # stroka
m = int(input())        # stolb

#
print('Заполнение таблицы однотипными элементами:')
print("'0'")
for i in range(n):
    a.append([0]*m)
for i in a:
    print(i)

#
print('Заполнение таблицы значениями, введенными с клавиатуры:')
a = []
n = int(input())        # stroka
m = int(input())        # stolb

for i in range(n):
    b = []
    for i in range(m):
        b.append(int(input()))
for i in a:
    print(i)

# Главная диагональ - i==j
# Выше главной диагонали -  i < j
# Ниже главной диагонали - i > j
print('Заполнение матрицы через главную диагональ:')
a = []
n = int(input())
for i in range(n):              # Цикл для заполнения таблицы
    a.append([0]*n)             # Заполнение матрицы нулями

for i in range(n):              # Цикл для обработки таблицы
    for j in range(n):
        if i == j:              # Проверяем, находится ли позиция на главной диагонали
            a[i][j] = 10        # переписываем 0 на 10
        elif i < j:
            a[i][j] = 5         # переписываем 0 на 5
        else:
            a[i][j] = 3         # переписываем 0 на 3

for i in a:                     # Цикл для вывода таблицы
    print(i)

#
print('Task')
# Вам нужно посчитать сумму элементов двумерного квадратного (NxN) списка, которые расположены на главной диагонали.
# Под главной диагональю матрицы подразумевается диагональ, проведённая из левого верхнего угла в правый нижний.
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, а затем в N строках
# записаны элементы списка.
n = int(input())
s = 0
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i == j:
            s += a[i][j]
print(s)

#
n = int(input())
s = 0
for i in range(n):
    s += int(input().split()[i])
print(s)

#
print(sum(int(input().split()[i]) for i in range(int(input()))))

#
n = int(input())
mtrx = [list(map(int, input().split())) for _ in range(n)]
print(sum(mtrx[i][i] for i in range(n)))


# Обход элементов матрицы - 1
# Задана целочисленная квадратная матрица размером N x N. Необходимо обойти элементы этой матрицы сверху вниз слева
# направо и вывести элементы именно в таком порядке в виде таблицы.
# Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. В каждой из последующих
# N строк записаны N целых чисел – элементы матрицы. Все числа во входных данных не превышают 100 по абсолютной величине.
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for j in range(n):
    for i in range(n):
        print(a[i][j], end=' ')
    print()

#
n = int(input())
m = [[int(j) for j in input().split()] for i in range(n)]
for i in range(n):
    print(*[m[j][i] for j in range(n)])

#
[print(*row) for row in zip(*(input().split() for i in range(int(input()))))]

#
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(a[j][i], end=' ')
    print()

#
n=int(input())
a=[input().split() for i in range(n)]
for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[x][y], end=' ')
    print()

#
n = int(input())                                        #задали размер
a = [list(map(int, input().split())) for i in range(n)] #заполнили матрицу
for i in range(n):                                      #пробежали по циклу i
    for j in range(n):                                  #пробежали по циклу j
        print(a[j][i], end=" ")                         #меняем индексы местами, столбец через пробел
    print()                                             #перенос строки

#
n = int(input())
l = [[*map(int, input().split())] for _ in '.' * n]
[print(*(l[i][j] for i in range(n))) for j in range(n)]

# Обход элементов матрицы - 2
# Задана целочисленная квадратная матрица размером N x N. Необходимо обойти элементы этой матрицы снизу вверх справо
# налево и вывести элементы именно в таком порядке в виде таблицы.
# Программа принимает на вход натуральное число N – количество строк и столбцов матрицы. В каждой из последующих
# N строк записаны N целых чисел – элементы матрицы.
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for j in range((n-1), -1, -1):
    for i in range((n-1), -1, -1):
        print(a[i][j], end=' ')
    print()

#
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
for j in range((n-1), -1, -1):
    for i in range((n-1), -1, -1):
        print(a[i][j], end=' ')
    print()

# Обход "по срезам"
n = int(input())
a = []
for _ in range(n):
    a += input().split()
for i in range(n):
    print(*a[-1-i::-n])

#
n = int(input())
table = [input().split() for _ in range(n)]

for i in range(n - 1, -1, -1):
    print(*[table[j][i] for j in range(n)][::-1])

#
[print(*l[::-1]) for l in [*zip(*[[*map(int,input().split())] for _ in range(int(input()))])][::-1]]


# Обход элементов матрицы - 3
# Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы cправо налево
# сверху вниз и вывести элементы именно в таком порядке в виде таблицы.
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы. В каждой из последующих
# N строк записаны M целых чисел – элементы матрицы.
n, m = list(map(int, input().split()))
a = []
for i in range(n):
        a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m-1, -1, -1):
        print(a[i][j], end=' ')
    print()

#
n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m-1, -1, -1):
        print(a[i][j], end=' ')
    print()

#
n, _ = map(int, input().split())
for _ in range(n):
    print(*input().split()[::-1])

#
for _ in range(int(input().split()[0])):
    print(*input().split()[:: -1])

#
[print(*input().split()[::-1]) for i in range(int(input().split()[0]))]

#
n, m = map(int, input().split())
[print(*input().split()[::-1]) for _ in n * '-']

# Обход "по срезам".
n = int(input().split()[0])
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
for i in a:
    print(*i[::-1])


# Обход элементов матрицы - 4
# Задана целочисленная матрица, состоящая из N строк и M столбцов. Необходимо обойти элементы этой матрицы слева направо
# снизу вверх и вывести элементы именно в таком порядке в виде таблицы.
# Программа принимает на вход два натуральных числа N и M – количество строк и столбцов матрицы. В каждой из последующих
# N строк записаны M целых чисел – элементы матрицы.
n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(m):
        print(a[i][j], end=' ')
    print()

#
n, _ = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())
print(*s[::-1], sep='\n')

''' Обход элементов матрицы - 4, вариант 2 '''
print(*[input() for _ in range(int(input().split()[0]))][::-1], sep="\n")

#
N, M = map(int, input().split())
for row in reversed([list(map(int, input().split())) for row in range(N)]):
	print(*row)

#
n = int(input().split()[0])
a = [input().split() for _ in range(n)][::-1]
[print(*i) for i in a]


# A. Красивая матрица
# Перед Вами матрица размера 5×5, состоящая из 24-x нулей и единственной единицы. Строки матрицы пронумеруем числами
# от 1 до 5 сверху вниз, столбцы матрицы пронумеруем числами от 1 до 5 слева направо. За один ход разрешается применить
# к матрице одно из двух следующих преобразований:
# Поменять местами две соседние строки матрицы, то есть строки с номерами i и i+1 для некоторого целого i (1≤i<5).
# Поменять местами два соседних столбца матрицы, то есть столбцы с номерами j и j+1 для некоторого целого j (1≤j<5).
# Вы считаете, что матрица будет выглядеть красиво, если единственная единица этой матрицы будет находиться в ее центре
# (в клетке, которая находится на пересечении третьей строки и третьего столбца). Посчитайте, какое минимальное количество
# ходов потребуется, чтобы сделать матрицу красивой.
# Входные данные:
# Входные данные состоят из пяти строк, в каждой из которых записаны пять целых чисел: j-ое число в i-ой строке входных
# данных обозначает элемент матрицы, стоящий на пересечении i-ой строки и j-ого столбца. Гарантируется, что матрица
# состоит из 24-x нулей и единственной единицы.
# Выходные данные:
# Выведите единственное целое число — минимальное количество действий, которое требуется, чтобы сделать матрицу красивой.
mas = []
for i in range(5):
    mas.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if mas[i][j] == 1:
            row = i
            column = j

print(abs(2 - row) + abs(2 - column))

#
a = []
for i in range(5):
    a.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            print((abs(2-i))+(abs(2-j)))

#
x = y = -1
for x in range(5):
    y = input().replace(' ', '').find('1')
    if y > -1:
        break

print(abs(2 - x) + abs(2 - y))

#
a = [[int(x) for x in input().split()] for y in range(5)]
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            print(abs(i-2) + abs(j-2))

#


# Сумма строк и столбцов двумерного массива
# Задан целочисленный двумерный массив, состоящий из N строк и M столбцов. Требуется вычислить сумму элементов в каждой
# строке и в каждом столбце.
# Программа получает на вход два натуральных числа N и M – количество строк и столбцов двумерного массива. В каждой из
# последующих N строк записаны M целых чисел – элементы массива. Все числа во входных данных не превышают 1000 по
# абсолютной величине.
# В первой строке вам необходимо вывести N чисел – суммы элементов массива для каждой строки в отдельности.
# Во второй строке в аналогичном формате выведите M чисел – суммы элементов для каждого столбца.
n, m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
for s in range(n):
    print(sum(a[s]), end=' ')
print()
for e in range(m):
    p = 0
    for j in range(n):
        p +=a [j][e]
    print(p, end=' ')

#

row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for row in range(row)]
for row in matrix:
	print(sum(row), end=' ')
print()
for x in range(col):
	print(sum([row[x] for row in matrix]), end=' ')


# Симметричная ли матрица?
# Проверьте, является ли двумерный массив симметричным относительно главной диагонали. Главная диагональ — та, которая
# идёт из левого верхнего угла двумерного массива в правый нижний.
# Входные данные:
# Программа получает на вход число n<100, являющееся числом строк и столбцов в массиве. Далее во входном потоке идет n
# строк по n чисел, являющихся элементами массива.
# Выходные данные:
# Программа должна выводить слово Yes для симметричного массива и слово No для несимметричного.
n = int(input())            # количество элементов в массиве
mas = []                    # создаем пустой массив
for i in range(n):          # заполняем массив
    mas.append(list(map(int, input().split())))

# Пройдем по всем индексам:
count = 0 # счетчик
for i in range(n):
    for j in range(n):
        if mas[i][j] != mas[j][i]:
            count += 1
if count > 0:
    print('no')
else:
    print('yes')

#
lst = []
for i in range(int(input())):
    lst.append(list(map(int, input().split())))
flag = 'Yes'
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] != lst[j][i]:
            flag = 'No'
print(flag)

#
n = int(input())
s = [input().split() for i in range(n)]
s1 = [[s[j][i] for j in range(n)] for i in range(n)]
print('Yes' if s == s1 else 'No')

