# Вложенные циклы.
# Формат вложенных циклов:
# for <переменная> in <объект>"
#    for <переменная> in <объект>:                  # вложенный цикл.
#       <действия>
#   <действия>

for i in range(3):                  # Аналог строк
    for j in range(5):              # Аналог столбцов
        print('*', end='')
    print()                         # Перенос на новую строчку


for i in range(3):                  # Внешний цикл
    for j in range(5):              # Внутренний цикл
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
for i in range(1, n + 1):
    print(*range(1, i + 1))

#
for i in range(int(input())):
    print(*range(1, i + 2))

#
[print(*[j+1 for j in range(i)]) for i in range(1, int(input())+1)]

#
n = int(input())
a = []
for i in range(1, n + 1):
    a.append(str(i))
    print(*a)

# Постулат Бертрана
# Постулат Бертрана (теорема Бертрана-Чебышева, теорема Чебышева) гласит, что для любого n > 1 найдется простое число p
# в интервале n < p < 2n. Такая гипотеза была выдвинута в 1845 году французским математиком Джозефем Бертраном
# (проверившим ее до n=3000000) и доказана в 1850 году Пафнутием Чебышевым. Рамануджан в 1920 году нашел более простое
# доказательство, а Эрдеш в 1932 – еще более простое.
# Ваша задача состоит в том, чтобы решить несколько более общую задачу – а именно по числу n найти количество простых
# чисел p из интервала n < p < 2n.
# Напомним, что число называется простым, если оно делится только само на себя и на единицу.
n = int(input())
count = 0  # счетчик
for p in range(n + 1, 2 * n):
    if p % 2 == 0 and p != 2 or p == 1:     # Убираем все четные без двойки и единицу
        continue
    # Цикл для перебора всех делителей
    d = 3
    is_plain = True  # Условие наличия делителя
    while d * d <= p:  # Алгоритм нахождения делителей числа
        if p % d == 0:
            is_plain = False
            break
        d += 2
    if is_plain:
        count += 1

print(count)

# Решение через функцию:
def is_plain_number(p):

    if p % 2 == 0 and p != 2 or p == 1:             # Убираем все четные без двойки и единицу
        return False
    # Цикл для перебора всех делителей
    d = 3
    is_plain = True                                 # Условие наличия делителя
    while d*d <= p:                                 # Алгоритм нахождения делителей числа
        if p % d == 0:
            return False
        d += 2
    return True


n = int(input())
count = 0  # счетчик
for p in range(n + 1, 2 * n):
    if is_plain_number(p):
        count += 1

print(count)

#
n = int(input())
a = 0
for i in range(n + 1, n * 2):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        a += 1
print(a)


# Через сито Эратосфена
n = int(input())


def p(t):
    if t == 2:
        return True
    if t % 2 == 0 or t <= 1:
        return False

    s = int(t ** 0.5) + 1

    for d in range(3, s, 2):
        if t % d == 0:
            return False
    return True


i = 0
for j in range(n + 1, 2 * n):
    if p(j):
        i += 1

print(i)

#
# import datetime
count = 0
n = int(input())
# t0 = datetime.datetime.now()
start_of_range = n + 1
if n % 2:
    start_of_range += 1
for i in range(start_of_range, 2 * n, 2):
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            break
    else:
        count += 1
print(count)
# t1 = datetime.datetime.now()
# dt = (t1 - t0).total_seconds()
# print(dt, ' sec')
# 50000
# 4459
# 0.102284  sec

#
n, c = int(input()), 0
for i in range(n + 1, n * 2):
    for j in range(2, int(i ** .5) + 1):
        if not i % j:
            break
    else:
        c += 1
print(c)

# Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки.
n = list(map(int, input().split()))
s = 0
for i in n:
    for j in range(i):
        print('*', end='')
    print()


# Cортировки пузырьком.
# вам поступает число n - количество элементов в списке, и затем сам список.
# Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки, в случае если элементы соседние
# совпадают менять их ненужно.
# В качестве ответа нужно вывести отсортированный список и какое количество раз пришлось переставлять элементы в
# процессе сортировки
n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            c += 1

print(*a)
print(c)

#
# сортировка пузырьком
a = int(input())  # ввод кол-ва элементов для сортировки # 7
b = list(map(int, input().split()))  # ввод элементов и преобразование их в список # 8 5 3 1 4 7 9
c = 0  # счетчик проходов

for run in range(a - 1):  # цикл для поиска пузырьков - макс элемента
    for i in range(a - 1):  # цикл для перебора элементов и замены их если надо
        if b[i] > b[i + 1]:  # если элемент слева меньше элемента справа
            c += 1  # увеличиваем счетчик (подсчет кол-ва замен)
            b[i], b[i + 1] = b[i + 1], b[i]  # меняем элементы местами
            # было [8, 5, 3, 1, 4, 7, 9]
            # стало [5, 8, 3, 1, 4, 7, 9]
            # 8 и 5 поменялись местами

# вывод данных
for i in b:
    print(i, end=' ')  # вывод отсортированного списка

print()  # перенос строки, чтобы не было вывода в той же строке, что и список
print(c)  # вывод кол-ва проходов

#
l = [int(i) for i in input().split()]
for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
            c += 1
print(*l)
print(c)


# Сортировка вставками
# Программа получает на вход число n - количество элементов в списке, и затем в следующей строке сам список.
# Ваша задача отсортировать список по возрастанию при помощи сортировки вставками, в случае если элементы соседние
# совпадают менять их ненужно.
# В качестве ответа нужно вывести отсортированный список.
n = int(input())
sp = list(map(int, input().split()))
for i in range(n):
    while i != 0 and sp[i] < sp[i - 1]:
        sp[i], sp[i - 1] = sp[i - 1], sp[i]
        i -= 1
print(*sp)

#
n = int(input())
lst = [int(i) for i in input().split()]

for i in range(1, n):
    k = i
    while k > 0 and lst[k] < lst[k - 1]:
        lst[k - 1], lst[k] = lst[k], lst[k - 1]
        k -= 1


print(*lst)

#
n = int(input())
a = list(map(int, input().split()))
for i in range(1, n):
    j, e = i, a[i]
    while j > 0 and a[j - 1] > e:
        a[j] = a[j - 1]
        j -= 1
    a[j] = e
print(*a)

#
_ = int(input())
l = [int(i) for i in input().split()]
n = len(l)

for i in range(1, n):
    for j in range(i, 0, -1):
        if l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
print(*l)

#
''' Сортировка вставками '''
n = int(input())
d = list(map(int, input().split()))
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if d[i] < d[j]:
            continue
        else:
            j += 1
            break
    if d[j] > d[i]:
        d.insert(j, d.pop(i))
print(*d)