# Генераторы списков (List comprehension)
# Список из квадратов целых чисел
# [0^2, 1^2, 2^2, 3^2, ..., N^2]
# N - натуральное число

N = 6
a = [0]*N


for i in range(N):
    a[i] = i ** 2

print(a)

a = [x**2 for x in range(N)]
print(a)
# [<способ формирования значения> for <переменная> in <итерируемый объект>]
a = [1 for x in range(5)]
print(a)

N = 7
a = [5 for x in range(N)]
print(a)

# Вычислить целый остаток от деления на 4
print("Вычислить целый остаток от деления на 4")
a = [x%4 for x in range(N)]
print(a)

# Определить четность значений
print("Определить четность значений")
a = [x % 2 == 0 for x in range(N)]
print(a)

# Сформировать значение линейной функции
print("Сформировать значение линейной функции")
a = [0.5 * x + 1 for x in range(N)]
print(a)

# Преобразовать строку в набор чисел
print("Преобразовать строку в набор чисел")
d_inp = input("Целые числа через пробел: ")

a = [int(d) for d in d_inp.split()]

print(a)

a = [d for d in d_inp.split()]

print(a)

# Генерация списка из строки
print("Генерация списка из строки")
a = [d for d in "python"]
print(a)

# Список кодов символов строки
print("Список кодов символов строки")
a = [ord(d) for d in "python"]
print(a)

# Определение длины строки
print("Определение длины строки")
t = ["Я", "выучу", "Python"]
a = [len(d) for d in t]
print(a)

# Дополнительные условия в генераторах списков
print("Дополнительные условия в генераторах списков")
# Сформировать список только из отрицательных элементов диапазона
print("Сформировать список только из отрицательных элементов диапазона")
a = [x for x in range(-5, 5) if x < 0]
print(a)

# Сформировать список из четных значений
print("Сформировать список из четных значений")
a = [x for x in range(-5, 5) if x % 2 == 0]
print(a)

# Составные условия
print("Составные условия")
a = [x for x in range(-6, 7) if x % 2 == 0 and x % 3 == 0]
print(a)

# Список строк определенной длины
print("Список строк определенной длины")
cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]

print([city for city in cities if len(city) < 7])

# Использование тернарного оператора внутри генератора списков
print("Использование тернарного оператора внутри генератора списков")
d = [4, 3, -5, 0, 1, 11, 122, -8, 9]

a = ["четное" if x % 2 == 0 else "нечетное" for x in d]
print(a)

a = ["четное" if x % 2 == 0 else "нечетное"
     for x in d
     if x > 0
     ]
print(a)

# Подвиг 1. Вводятся вещественные числа в строку через пробел. Необходимо на их основе сформировать список lst с
# помощью list comprehension (генератора списков) из модулей введенных чисел (в списке должны храниться именно числа,
# а не строки). Результат вывести на экран в виде списка командой:
# print(lst)
lst = list(map(float, input().split()))
print([abs(d) for d in lst])

#
print([abs(float(i)) for i in input().split()])

#
print(list(map(abs, map(float, input().split()))))

# Подвиг 2. Вводится семизначное целое положительное число. С помощью list comprehension сформировать список lst,
# содержащий цифры этого числа (в списке должны быть записаны числа, а не строки). Результат вывести на экран список
# командой: print(lst)
print([int(d) for d in input()])

#
print(list(map(int, input())))

# Подвиг 3. Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N,
# состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали от
# верхнего левого угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы чисел как показано
# в примере ниже.
t = int(input())
c = [[1 if i == j else 0 for i in range(t)] for j in range(t)]

for i in c:
    print(*i)

#
n = int(input())
a = [print(*x, sep=' ') for x in[('0' * n)[:i] + '1' + ('0' * (n - (i + 1)))for i in range(n)]]

#
n = int(input())
mtx = [[int(i == j) for j in range(n)] for i in range(n)]
for row in mtx:
    print(*row)

#
n = int(input())
[print(*[1 if x == k else 0 for x in range(n)]) for k in range(n)]

# Сначала создал список  из нулей:
# 0 for x in range(n)
# затем сделал матрицу из нулей, повторяя этот код 0 for x in range(n) n раз -
# [[0 for x in range(n)] for k in range(n)]
# Теперь у нас есть матрица, заполненная нулями. x - строки, k  - столбцы.
# Нужно добавить единички, есть закономерность, что единичка стоит в позиции внутри ряда такой же,
# как и внутри столбца. За столбцы отвечает k, а за  строку  x, поэтому k должен быть равен x.
# Добавляем тернарный условный оператор в левую часть, потому что именно там решается, что добавляется в матрицу.
# [[1 if x == k else 0 for x in range(n)] for k in range(n)]
# чтобы не мучаться с распаковкой, сразу принтуем сгенерированный список в виде набора цифр, добавляя принт с распаковкой
# [print(*[1 if x == k else 0 for x in range(n)]) for k in range(n)]
n = int(input())
[print(*[1 if x == k else 0 for x in range(n)]) for k in range(n)]

# Подвиг 4. Вводятся названия городов в строку через пробел. Необходимо сформировать список с помощью list comprehension,
# содержащий названия длиной более пяти символов. Результат вывести в строчку через пробел.
lst = input().split()
print(*[d for d in lst if len(d) > 5])

#
print(*[i for i in input().split() if len(i) > 5])

# Подвиг 5. Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension, состоящий из
# делителей числа n (включая и само число n). Результат вывести на экран в одну строку через пробел.
t = int(input())
print(*[i for i in range(1, t+1) if t % i == 0])


# Подвиг 6. Вводится натуральное число N. Необходимо сгенерировать вложенный список с помощью list comprehension,
# размером N x N, где первая строка содержала бы все нули, вторая - все единицы, третья - все двойки и так до N-й строки.
# Результат вывести в виде таблицы чисел как показано в примере ниже.
t = int(input())
[print(*[j for i in range(t)]) for j in range(t)]

#
n = int(input())

lst = [[i] * n for i in range(n)]

for i in lst:
    print(*i)

#
n = int(input())
[print(*[i]*n) for i in range(n)]

#
N = int(input())
for i in range(N):
    lst = [i for x in range(N)]
    print(*lst)

#
n = int(input())
for i in range(n):
    print(*([i] * n))

# Подвиг 7. Вводится список вещественных чисел. С помощью list comprehension сформировать список,
# состоящий из элементов введенного списка, имеющих четные индексы (то есть, выбрать все элементы с четными индексами).
# Результат вывести на экран в одну строку через пробел.
print(*[i for i in list(map(float, input().split()))][::2])

#
print(*[float(i) for i in input().split()][::2])

#
lst = [float(x) for i, x in enumerate(input().split()) if i % 2 == 0]
print(*lst)

#
s = list(map(float, input().split()))
print(*[s[i] for i in range(len(s)) if i % 2 == 0])

# Подвиг 8. Вводятся два списка целых чисел одинаковой длины каждый с новой строки. С помощью
# list comprehension сформировать третий список, состоящий из суммы соответствующих пар чисел
# введенных списков. Результат вывести на экран в одну строку через пробел.
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*[a[i] + b[i] for i in range(len(a))])

#
print(*[int(i)+int(j) for i,j in zip(input().split(),input().split())])

#
a=input().split()
b=input().split()
print(*[int(a[i])+int(b[i])for i in range(len(a))])



# Подвиг 9. Вводится список в формате:
# <город 1> <численность населения 1> <город 2> <численность населения 2> ... <город N> <численность населения N>
# Необходимо с помощью list comprehension сформировать список lst, содержащий вложенные списки из пар:
# <город> <численность населения>
# Численность населения - целое число в тыс. человек. Вывести результат на экран в виде списка командой:
# print(lst)
lst = list(map(str, input().split()))
print([[lst[i-1], int(lst[i])] for i in range(1, len(lst), 2)])

#
s = input().split()
print([[s[i], int(s[i + 1])] for i in range(0, len(s), 2)])

#
c=input().split()
a=c[::2]
b=[int(i) for i in c[1::2]]
print([[a[i],b[i]] for i in range(len(a))])

#
n=input().split()
print([[n[i] , int(n[i+1])]
        for i in range(len(n)-1)
        if i % 2 == 0])

