# Вложенные генераторы списков.
# Обработка кортежей:
import random

print('Кортежи:')
a = [
    ('Sidorov', 1995),
    ('Lukov', 2002),
    ('Petrov', 1991),
    ('Gorbachev', 1984),
    ('Kostin', 2000),
    ('Isaev', 2005),
    ('Eliseev', 1999),
    ('Kozlov', 2004),
    ('Bukov', 1995),
    ('Gavrilov', 1980),
    ('Efremov', 2006),
]
# Отбор по первой букве фамилии:
b = [elem[0] for elem in a if elem[0].startswith('E')]
print(b)

# Отбор по году рождения:
b = [elem[0] for elem in a if elem[1] > 2000]
print(b)

#
b = [elem[0][0] for elem in a if elem[1] > 2000]
print(b)

# Обработка словарей:
print('Словари:')
a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 200, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
    'Gavrilov': {'age': 1980, 'hobby': 'music', 'car': 'Opel'},
    'Efremov': {'age': 2006, 'hobby': 'tennis', 'car': 'Audi'},
}

# Заполнение списка ключами:
b = [elem for elem in a]
print(b)

b = [a[elem]['car'] for elem in a]
print(b)

b = [a[elem]['hobby'] for elem in a]
print(b)

b = [{elem, a[elem]['car']} for elem in a if a[elem]['age'] < 2000 and a[elem]['hobby']=='soccer']
print(b)

# Обработка строк:
print('Строки:')
print('Достать при помощи генератора цифры:')
s = 'vgdfbu iygfbdufg9654foinsjgf452sdhbf'
b = [i for i in s if i.isdigit()]
print(b)

# Превратить каждое значение в число:
b = [int(i) for i in s if i.isdigit()]
print(b)

# Обработка двумерных списков:
print('Двумерные списки:')
n = 5
m = 3
a = [[0]*m for i in range(n)]
for i in a:
    print(i)

print('Использование вложенного генератора:')
import random
n = 4
m = 6
a = [[random.randint(1, 6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)


print('Вывести элементы главной диагонали:')
n = 7
m = 7
a = [[random.randint(1, 6) for j in range(m)] for i in range(n)]
for i in a:
    print(i)
b = [a[i][j] for i in range(n) for j in range(m) if i == j]
print('main diagon', b)

print('Вывести элементы строки:')
c = [a[2][j] for j in range(m)]
print('2 str', c)

print('Вывести элементы столбца:')
d = [a[i][3] for i in range(n)]
print('3 stolb', d)

# Таблица умножения:
print('Таблица умножения:')
n = 10
m = 10
a = [[i*j for j in range(1, m)] for i in range(1, n)]

for i in a:
    print(i)

#
print('Tasks')
# В вашем распоряжении есть двумерный список vector. Ваша задача при помощи генератора-списка сделать на основании
# vector линейный(одномерный ) список и вывести его
# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
print([j for i in vector for j in i])

#
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
print(sum(vector, []))

#
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
print([vector[i][j] for i in range(len(vector)) for j in range(len(vector[i]))])

