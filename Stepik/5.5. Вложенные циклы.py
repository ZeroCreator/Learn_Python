# Вложенные циклы.
# Формат вложенных циклов:
# for <переменная> in <объект>"
#    for <переменная> in <объект>:                  # вложенный цикл.
#       <действия>
#   <действия>

for i in range(3):
    for j in range(5):
        print('*', end='')
    print()                         # Перенос на новую строчку


for i in range(3):
    for j in range(5):
        print(i, end='')
    print()

for i in range(3):
    for j in range(5):
        print(j, end='')
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end='')
    print()

for i in range(1, 4):
    for j in range(10, 13):
        print(i, j)

for i in 'ab':
    for j in 'cdef':
        print(i, j)

# Вложенные циклы используются для перебора всех возможных значений:
print('Длина пароля 3. Необходимо перебрать все возможные значения:')

from string import printable

#for b1 in printable:
#    for b2 in printable:
#        for b3 in printable:
#            print(b1, b2, b3)

print('Составить таблицу умножения:')
for j in range(1, 10):
    for i in range(1, 11):
        print(i, '*', j, '=', i*j, end=' ')
    print()

# Сколько шестибуквенных слов, начинающихся и заканчивающихся согласной буквой и содержащих ровно 2 гласные, можно
# составить из букв Т, Ы, К, В, А? Каждая из допустимых букв может входить в слово несколько раз.
k = 0
for b1 in 'tukva':
    for b2 in 'tukva':
        for b3 in 'tukva':
            for b4 in 'tukva':
                for b5 in 'tukva':
                    for b6 in 'tukva':
                        rez = b1 + b2 + b3 + b4 + b5 + b6
                        if rez[0] in 'tkv' and rez[-1] in 'tkv':
                            if rez.count('a') + rez.count('u') == 2:
                                k += 1
print(k)

#
print('Посчитать сумму всех цифр заданного диапазона:')
sum = 0
for i in range(1000, 10000):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    if s == 20:
        sum += i
print(sum)

#
for i in range(1, 100001):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    print(i, s)

#
print('Tasks')
# Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20.
s = 0
for i in range(1000, 10000):
    if sum(map(int, str(i))) == 20:
        s += i
print(s)

#
count = 0
for i_1 in range(1, 10):
    for i_2 in range(10):
        for i_3 in range(10):
            for i_4 in range(10):
                if i_1+i_2+i_3+i_4 == 20:
                    a = str(i_1)+str(i_2)+str(i_3)+str(i_4)
                    count += int(a)
print(count)

#
print(sum([num for num in range(1000, 10000) if sum([int(i) for i in str(num)]) == 20]))

#
s = []
m = []
for i in range(1000, 10000):
    s = []
    for j in str(i):
        s.append(int(j))
    if sum(s) == 20:
        m.append(i)
print(sum(m))

#
my_list = list(range(1000, 10000))
summa = 0
for i in my_list:
    if i // 1000 + i // 100 % 10 + i // 10 % 10 + i % 10 == 20:
        summa += i
print(summa)

# В этой задаче вам предстоит построить лесенку из чисел. Программа принимает на вход целое положительное число
# n (n<=15) - количество уровней, ваша задача вывести n уровней, в каждом из которых стоят числа от 1 до значения уровня.
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#
n = int(input())
for i in range(1, n+1):
    print(*range(1, i+1))

#
for i in range(int(input())):
    print(*range(1, i + 2))

#
[print(*[j+1 for j in range(i)]) for i in range(1, int(input())+1)]

#
n = int(input())
a = []
for i in range(1, n+1):
    a.append(str(i))
    print(*a)

#
