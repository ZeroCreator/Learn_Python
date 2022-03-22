# Операторы break, continue и else
# break - досрочное завершение цикла
# continue - пропуск одной итерации тела цикла

print("break")
print("запуск цикла")
i = 0
while True: # условие бесконечного цикла
    i += 1
    break

print("Завершение цикла")

print("Определяем первое четное значение")
d = [1, 5, 3, 6, 0, -4]

flFind = False
i = 0
while i < len(d):
    print(i)
    flFind = d[i] % 2 == 0
    if flFind:
        break
    i += 1

print(flFind, i)


d = [1, 5, 3, 7, 5, 9]
flFind = False
i = 0
while i < len(d) and d[i] % 2 != 0:
    i += 1

flFind = i != len(d)

print(flFind)

print("continue")
print("Будем суммировать четные значения, при введении 0 подстчет суммы прекращатся")

s = 0
d = 1

while d !=0:
    d = int(input("Ведите целое число"))
    if d % 2 == 0:
        continue

    s += d
    print("s = " + str(s))

# else - блок, выполняемый после штвтного завершения цикла
print("Блок else")
# s = 1/2 + 1/3 + 1/4 + 1/10 + ... + 1/0
s = 0
i = -10

while i < 0:
    if i == 0:
        break
    s += 1/i
    i += 1
else:
    print("Сумма выведена корректно")

print(s)


# Подвиг 2. Имеется одномерный список длиной 10 элементов, состоящий из нулей:
# p = [0] * 10
# На каждой итерации цикла пользователь вводит целое число - индекс элемента списка p, по которому записывается
# значение 1, если ее там еще нет. Если же 1 уже проставлена, то список не менять и снова запросить у пользователя
# очередное число. Необходимо расставить так пять единиц в список. (После этого цикл прерывается).
# Программу реализовать с помощью цикла while и с использованием оператора continue, когда 1 не может быть добавлена
# в список. Результат вывести на экран в виде последовательности чисел, записанных через пробел.
p = [0] * 10
s = 0

while s < 5:
    n = int(input())
    if p[n] == 1:
        continue
    p[n] = 1
    s += 1

print(*p)

#
p = [0] * 10
while sum(p) != 5:
    n = int(input())
    if p[n] == 1:
        continue
    p[n] = 1
print(*p)

#
p = [0] * 10
while p.count(1) != 5:
    d = int(input())
    if p[d] == 1:
        continue
    p[d] = 1
print(*p)

# Подвиг 3. На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных
# чисел, до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue,
# а также использовать цикл while. Результат произведения вывести на экран.
pr = 1
while True:
    n = int(input())
    if n == 0:
        break
    elif n < 0:
        continue
    pr *= n

print(pr)

#
res, x = 1, 1
while x:
    x = int(input())
    if x <= 0:
        continue
    res *= x
print(res)

#
n = int(input())
prod = 1

while n != 0:
    if n > 0:
        prod *= n
    n = int(input())

print(prod)

#
summa = 1
x = 1
while x != 0:
    x = int(input())
    if x < 0:
        continue
    summa*= x if x > 0 else 1
print(summa)


# Подвиг 4. Вводится список названий городов в одну строчку через пробел. Определить, что в этом списке все города
# имеют длину более 5 символов. Реализовать программу с использованием цикла while и оператора break.
# Вывести ДА, если условие выполняется и НЕТ - в противном случае.
s = input().split()
i = 0
fl = 0
while i < len(s):
    if len(s[i]) < 5:
        break

    fl += 1
    i += 1
print(["НЕТ", "ДА"][len(s) == fl])

#
city = input().split()
i = 0
while i < len(city):
    if len(city[i]) < 5:
        print('НЕТ')
        break
    i += 1
else:
    print('ДА')

#
print(('НЕТ', 'ДА')[len(min(input().split(), key=len)) > 5])

#
print(('НЕТ', 'ДА')[all(len(c) > 5 for c in input().split())])

#lst = input().split()
lst = input().split()
count = 0
flag = 'ДА'
while count < len(lst):
    if len(lst[count]) > 5:
        count += 1
    else:
        flag = 'НЕТ'
        break

print(flag)

#
cities = input().split()
for city in cities: answer = "НЕТ" if len(city) < 5 else "ДА"
print(answer)


# Подвиг 5. Вводится список имен студентов в одну строчку через пробел. Определить, что хотя бы одно имя в этом
# списке начинается и заканчивается на ту же самую букву (без учета регистра). Реализовать программу с
# использованием цикла while и оператора break. Вывести ДА, если условие выполняется и НЕТ - в противном случае.
lst = input().lower().split()
i = 0
flag = 'НЕТ'
while i < len(lst):
    if lst[i][0] == lst[i][-1]:
        flag = 'ДА'
        break
    else:
        i += 1
print(flag)

#
names = input().split()
i = 0
while i < len(names):
    if names[i].lower()[0] == names[i].lower()[-1]:
        print('ДА')
        break
    i += 1
else:
    print('НЕТ')

#
lst = input().lower().split()
i = 0
while i < len(lst):
    if lst[i][0] == lst[i][-1]:
        print('ДА')
        break
    i += 1
else: print('НЕТ')


# Подвиг 6. Вводится натуральное число n (то есть, целое положительное). В цикле перебрать все целые числа в
# интервале [1; n] и сформировать список из чисел, кратных 3 и 5 одновременно. Вывести полученную последовательность
# чисел в виде строки через пробел, если значение n меньше 100. Иначе вывести на экран сообщение "слишком большое
# значение n" (без кавычек). Использовать в программе оператор else после цикла while.
n = int(input())
s = []

while n < 100:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            s.append(i)
    print(*s)
    break
else:
    print("слишком большое значение n")

#
n = int(input())
i = 1
while 100 > n:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
    i += 1
    if i == n:
        break
else:
    print('слишком большое значение n')

#
n = int(input())
print(*n < 100 and range(15, n, 15) or ['слишком большое значение n'])

#
s = int(input())
if s >= 100:
    print("слишком большое значение n")
else:
    print(*[i for i in range(1, s + 1) if i % 3 == 0 and i % 5 == 0])

# Подвиг 7. Вводится натуральное число n. Вывести первое найденное натуральное число (то есть, перебирать числа,
# начиная с 1), квадрат которого больше значения n. Реализовать программу с использованием цикла while.
n = int(input())
start = 1

while start**2 <= n:
    start += 1

print(start)

#
print(int(int(input()) ** .5) + 1)

#
n = int(input())
count = 1

while True:
    if count ** 2 > n:
        print(count)
        break
    count += 1


# Подвиг 8. (На использование цикла while). Начав тренировки, лыжник в первый день пробежал 10 км. Каждый следующий
# день он увеличивал пробег на 10 % от пробега предыдущего дня. Определить в какой день он пробежит больше x км
# (натуральное число x вводится с клавиатуры). Результат (искомый день) вывести на экран.
x = int(input())
n = 10
t = 1
while n <= x:
    n *= 1.10
    t += 1

print(t)

#
x = int(input())
y = 10
count = 1
while y < x:
  y += y / 100 * 10
  count += 1
print(count)

# Подвиг 9. (На использование цикла while). Вводятся названия книг (каждое с новой строки). Удалить из введенного
# списка все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом).
# Результат вывести на экран в виде строки из оставшихся названий через пробел.
# P. S. Для считывания списка целиком в программе уже записаны начальные строчки
lst_in = ["Муму","Евгений Онегин","Сияние","Мастер и Маргарита","Пиковая дама","Колобок"]

i = 0
rez = []
while i < len(lst_in):
    if lst_in[i].count(" "):
        i += 1
    else:
        rez.append(lst_in[i])
        i += 1

print(*rez)

#
i = 0

while i < len(lst_in):

    if " " in lst_in[i]:
        lst_in.pop(i)
    else:
        i += 1
print(*lst_in)

#
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
n = len(lst_in)
while n:
    n -= 1
    if lst_in[n].count(' '):
        del lst_in[n]

print(*lst_in)

#
print(*[book for book in lst_in if len(book.split()) < 2])

#
lst_in = list(map(str.strip, sys.stdin.readlines()))
count = 0
lst = []

while count < len(lst_in):
    if len(lst_in[count].split()) == 1:
        lst.append(lst_in[count])
    count += 1
print(*lst)

#
m = 0
while m < len(lst_in):
    if ' ' not in lst_in[m]:
        print(lst_in[m], end=' ')
    m += 1