# Вложенные циклы
for i in range(1, 4):
    for j in range(1, 6):
        print(f"i - {i}, j = {j}", end=" ")
    print()

# Перебор всех значений вложенного списка
print("Перебор всех значений вложенного списка")
a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

for row in a:
    #print(row, type(row))
    for x in row:
        print(x, type(x), end=' ')
    print()

# Сложение матриц
print("Сложение матриц")
a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
c = []

for i, row in enumerate(a):
    r = []
    for j, x in enumerate(row):
        r.append(x + b[i][j])

    c.append(r)

print(c)

# Обработать коллекцию строк по количеству пробелов
print("Обработать коллекцию строк по количеству пробелов ")
t = [" - Скажи-ка,  дядя, ведь не даром",
     "Я Python выучил с  каналом",
     "Балакирев что   раздавал?",
     "Ведь были  ж заданья боевые,",
     "Да, говорят,  еще какие!",
     "Недаром помнит     вся Россия",
     "Как мы рубили  их тогда!"
     ]

for i, line in enumerate(t):
    while line.count('  '):
        line = line.replace('  ', ' ')

    t[i] = line

print(t)

# Двумерный список
print("Двумерный список")
M, N = list(map(int, input("Введите М и N").split()))

zeros = []
for i in range(M):
    zeros.append([0]*N)

print(zeros)

for i in range(M):
    for j in range(N):
        zeros[i][j] = 1

print(zeros)

# Транспонирование матрицы
print("Транспонирование матрицы")
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]


for r in A:
    for x in r:
        print(x, end='\t')
    print()

# если создавать список через так:
lst = [[1] * n] * n
# То просто копируется ссылка на один и тот же список.
# Если так:
lst2  = [[1] * n for _ in range(n)]
# То создаются отдельные списки.

# Подвиг 1. Вводится натуральное число N (то есть, положительное, целое). Требуется создать двумерный (вложенный)
# список размером N x N элементов, состоящий из всех единиц, а затем, в последний столбец записать пятерки.
# Вывести этот список на экран в виде таблицы чисел, как показано в примере ниже.
# P.S. Будьте внимательны в конце строк пробелов быть не должно!
t = int(input())
c = []
for i in range(t):
    c.append(["1 "]*t)

for i in range(t):
    c[i][-1] = "5"

for i in c:
    for j in i:
        print(j, end="")
    print()

#
n = int(input())

lst = [[1] * n] * n
lst[0][n-1] = 5

for i in lst:
    print(*i)

#
n = int(input())
a = [[1] * n for __ in range(n)]
for i in a:
  i[-1] = 5
[print(*i) for i in a]

#
n = int(input())
for i in range(n):
    print('1 ' * (n - 1) + '5')

#
a = int(input())
g = []
for i in range(a):
    g.append([1]*(a))
    g[i][-1] = 5
    print(*g[i])

#
n = int(input())
a = [[1]*(n-1)+[5] for _ in range(n)]
[print(*i) for i in a]

#
n = int(input())

for i in range(n):
    print("1 "*(n-1), "5", sep="")

#
n = int(input())
mtx = [[1] * n for _ in range(n)]
for i in range(n):
    mtx[i][-1] = 5
for row in mtx:
    print(*row)

#Подвиг 2. Вводится список из URL-адресов (каждый с новой строки). Требуется в них заменить все пробелы на символ
# дефиса (-). Следует учесть, что может быть несколько подряд идущих пробелов. Результат преобразования вывести на
# экран в виде строк из URL-адресов.
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

for i, line in enumerate(lst_in):
    while line.count('  '):
        line = line.replace('  ', ' ')
    line = line.replace(' ', '-')
    lst_in[i] = line

for i in lst_in:
    print(i)

#
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

for i in lst_in:
    print('-'.join(i.split()))

#
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

for line in lst_in:
    while '  ' in line:
        line = line.replace('  ', ' ')
    line = line.replace(' ', '-')
    print(line)

#
import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

[print("-".join(i.split())) for i in lst_in]

#
import sys
print('-'.join(sys.stdin.read().replace('\n', 'o_O').split()).replace('o_O', '\n'))

# Подвиг 5. Вводится двумерный список размерностью 5 х 5 элементов, состоящий из целых чисел (пример ввода см. ниже).
# Проверьте, является ли этот двумерный список симметричным относительно главной диагонали. Главная диагональ — та,
# которая идёт из левого верхнего угла двумерного массива в правый нижний. Выведите на экран ДА, если матрица
# симметрична и НЕТ - в противном случае.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

flag = True
for i in range(len(lst_in)):
    for j in range(i, len(lst_in)):
        if lst_in[i][j] != lst_in[j][i]:
            flag = False
            break
print("ДА" if flag == True else "НЕТ")

#
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

flag = 'ДА'

for i in range(5):
    for j in range(5):
        if lst_in[i][j] != lst_in[j][i]:
            flag = 'НЕТ'

print(flag)

#
import sys
mtx = [tuple(x.split()) for x in sys.stdin.read().split('\n')]
print(('НЕТ', 'ДА')[mtx == [*zip(*mtx)]])

#
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
fl=True
for i in range(len(lst_in)):
    for j in range(len(lst_in)):
        if lst_in[i][j]!=lst_in[j][i]:
            fl=False
            break
print(["НЕТ","ДА"][fl])



# Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть,
# в диапазоне [2; n). Результат вывести на экран в строчку через пробел. (Решето Эратосфена).
n = int(input())
a = [True] * n
for i in range(2, n):
    for j in range(i * 2, n, i):
        a[j] = False

print(*[i for i in range(2, n) if a[i]])

#
for i in range(2, int(input())):
    for j in range(2, 1 + i // 2): # i // 2 значительно ускоряет процесс
        if i % j == 0:
            break
    else:
        print(i, end=' ')

#
n = int(input())
sieve = [0, 0] + [1] * (n - 2)
for i in range(2, n):
    if sieve[i]:
        for j in range(i * i, n, i):
            sieve[j] = 0
print(*(i for i, e in enumerate(sieve) if e))

#
n = int(input())
lst = []
for i in range(2,n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        lst.append(i)
print(*lst)

#
n = int(input())

for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=' ')





