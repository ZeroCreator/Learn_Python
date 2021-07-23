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