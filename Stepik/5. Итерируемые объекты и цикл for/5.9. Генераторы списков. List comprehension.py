# Генераторы списков. List comprehension.
# шаблон для заполнения списка:
# [выражение for val in коллекция]
a = [0 for i in range(7)]
print(a)

a = [i for i in range(10)]
print(a)

a = [i**2 for i in range(10)]
print(a)

# коллекция - строки
a = [i for i in 'hello']
print(a)

a = [i*5 for i in 'hello']
print(a)

# функции
a = [ord(i) for i in 'abcd']
print(a)

import random
a = [random.randint(-10, 10) for i in range(10)]
print(a)
b = [abs(elem) for elem in a]
print(b)

# Изменить значение элементов первоначального списка:
a = [elem + 1 for elem in a]
print(a)

# Условные конструкции:
# [выражение for val in коллекция if условие]
b = [elem for elem in a if elem%2==0]
print(b)

b = [elem for elem in a if elem%2==0 and elem%3==0]
print(b)

# Ввод нескольких чисел через пробел в одну строку:
a = input('Ведите числа: ').split()
a = [int(i) for i in a]
print(a)

# Инициализация двумерного списка:
n = 5
m = 4

a = [[0]*m for i in range(n)]
# a[1][3] = 100
for i in a:
    print(i)

# Двойные циклы:
a = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(a)
# Каждое значение сочетается с каждым.

a = [i*j for i in (2, 3, 4, 5) for j in [1, 2, 3] if i*j > 10]
print(a)

#
print('Tasks')
# При помощи генератора-списка создайте список [1, 2, 3, ..., n], само натуральное число n будет поступать на вход
# вашей программе.
# В качестве ответа просто выведите получившийся список
print([i for i in range(1, int(input()) + 1)])

#
print([*range(1, int(input())+1)])

