# Вложенные циклы и вложенные генераторы списков
# [[генератор списка] for <переменная> in <итерируемый объект>]
a = [(i, j) for i in range(3) for j in range(4)]
print(a)
print(*[(i, j) for i in range(3) for j in range(4)])
a = [(i, j)
     for i in range(3) if i % 3 == 0
     for j in range(4) if j % 2 == 0
     ]

print(a)

# Таблица умножения
print("Таблица умножения")
a = [f"{i}*{j} = {i*j}"
     for i in range(3)
     for j in range(4)
     ]

print(a)

# Преобразование двумерного списка в одномерный
print("Преобразование двумерного списка в одномерный")
matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]
          ]

a = [x
     for row in matrix
     for x in row
     ]

print(a)

M, N = 3, 4
matrix = [[a for a in range(M)] for b in range(N)]
print(matrix)

# Возвести в квадрат все значения двумерного списка
print("Возвести в квадрат все значения двумерного списка")
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

AA = [[x ** 2 for x in row] for row in A]

a = [x ** 2
     for row in A
     for x in row
     ]

print(AA)
print(a)

# Транспонирование матрицы
print("Транспонирование матрицы")
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

AA = [[row[i] for row in A] for i in range(len(A[0]))]

print(AA)

# Поведение вложенных функций
print("Поведение вложенных функций")
# [for <переменная> in [генератор списка]]
g = [u ** 2 for u in [x + 1 for x in range(5)]]
# g(u(x+1)) = (x+1)^2
print(g)


# Подвиг 1. Вводится двумерный список в виде таблицы целых чисел (см. пример ниже). С помощью list comprehension
# преобразовать двумерный список в одномерный так, чтобы значения элементов шли в обратном порядке.
# Результат отобразить в виде строки из чисел, записанных через пробел.
lst_in = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]
          ]

print(*[x for row in lst_in[::-1] for x in row[::-1]])

#
print(*[x for row in lst_in for x in row][::-1])

# Подвиг 2. Вводится список целых чисел в строку через пробел. С помощью list comprehension сформировать из них
# двумерный список lst размером N x N (квадратную таблицу чисел). Гарантируется, что из набора введенных чисел можно
# сформировать квадратную матрицу (таблицу).


# Подвиг 4. Повторите задачу с транспонированием прямоугольной матрицы с помощью list comprehension. На вход поступает
# таблица целых чисел, на выходе нужно отобразить эту же таблицу в транспонированном виде (строки заменяются на столбцы),
# используя команду:
# for row in A:
#     print(*row)
# где A - транспонированный двумерный список.
lst_in = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [5, 4, 3]
          ]

A = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]

for row in A:
    print(*row)

#
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

for i in zip(*lst_in):
    print(*i)

#
[print(*c) for c in zip(*[x.split() for x in open(0)])]

#
import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
A=[[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
[print(*a) for a in A]


# Подвиг 2. Вводится список целых чисел в строку через пробел. С помощью list comprehension сформировать из них
# двумерный список lst размером N x N (квадратную таблицу чисел). Гарантируется, что из набора введенных чисел
# можно сформировать квадратную матрицу (таблицу). Результат отобразить в виде списка командой: print(lst)
a = list(map(int, input().split()))
N = int(len(a)**0.5)
lst = list([[a[N * i + j] for j in range(N)] for i in range(N)])
print(lst)

#
lst_in = list(map(int, input().split()))
N = int(len(lst_in) ** 0.5)
lst = [lst_in[i:i+N] for i in range(0, len(lst_in), N)]
print(lst)




