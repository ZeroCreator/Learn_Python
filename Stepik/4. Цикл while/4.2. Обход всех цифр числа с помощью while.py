# ОБХОД ВСЕХ ЦИФР ЧИСЛА С ПОМОЩЬЮ while.
x = 4782
while x > 0:
    print(x % 10)
    x = x // 10


x = int(input())
while x > 0:
    print(x % 10)
    x = x // 10

#
print('Определить, сколько разрядов в числе:')
x = int(input())
kol = 0
while x > 0:
    last = x % 10
    kol = kol + 1
    x = x // 10
print('Всего цифр:', kol)

#
print('Определить, сколько четных/нечетных:')
x = int(input())
kol = 0
kol_ch = 0
s = 0
while x > 0:
    last = x % 10
    kol = kol + 1
    if last % 2 == 0:
        kol_ch += 1
    s = s + last
    x = x // 10
print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)
print('Сумма всех цифр:', s)

#
print('Определить произведение всех цифр:')
x = int(input())
kol = 0
kol_ch = 0
s = 0
pr = 1
while x > 0:
    last = x % 10
    kol = kol + 1
    if last % 2 == 0:
        kol_ch += 1
    s = s + last
    pr = pr * last
    x = x // 10
print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)
print('Сумма всех цифр:', s)
print('Произведение всех цифр:', pr)

#
print('Определить самую большую цифру:')
x = int(input())
kol = 0
kol_ch = 0
s = 0
pr = 1
maxim = 0
while x > 0:
    last = x % 10
    kol = kol + 1
    if last % 2 == 0:
        kol_ch += 1
    s = s + last
    pr = pr * last
    if last > maxim:
        maxim = last
    x = x // 10
print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)
print('Сумма всех цифр:', s)
print('Произведение всех цифр:', pr)
print('Наибольшая цифра:', maxim)

#
print('Определить минимальную цифру числа:')
x = int(input())
kol = 0
kol_ch = 0
s = 0
pr = 1
maxim = 0
minim = 9
while x > 0:
    last = x % 10
    kol = kol + 1
    if last % 2 == 0:
        kol_ch += 1
    s = s + last
    pr = pr * last
    if last > maxim:
        maxim = last
    if last < minim:
        minim = last
    x = x // 10
print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)
print('Сумма всех цифр:', s)
print('Произведение всех цифр:', pr)
print('Наибольшая цифра:', maxim)
print('Наименьшая цифра:', minim)

#
print('Перевод в двоичную запись:')
x = int(input())

while x > 0:
    last = x % 2
    print(last)
    x = x // 2

#
print('Tasks')
# Программа принимает на вход одно натуральное число и выводит на экран сумму цифр данного числа
x = int(input())
sum = 0
while x > 0:
    last = x % 10
    sum = sum + last
    x = x // 10
print(sum)

a = int(input())
sum = 0
while a > 0:
    sum = sum + a % 10
    a = a // 10
print(sum)

n = int(input())        # вводим число
k = 0                   # устанавливаем счетчик
while n > 0:            # производим вычисления в блоке ниже пока n > 0
    k += n % 10         # берем остаток от введенного числа (последнюю цифру)
    n = n // 10         # уменьшаем наше введенное число на один разряд (убираем последнюю цифру)
print(k)                # выводим на печать

n = input()
s = i = 0
while i < len(n):
    s += int(n[i])
    i += 1
print(s)

a = input()
b = 0
for i in range(len(a)):
    b += int(a[0])
    a = a[1:]
print(b)

# Программа принимает на вход одно натуральное число и выводит на экран произведение цифр данного числа
x = int(input())
p = 1
while x > 0:
    p = p * (x % 10)
    x = x // 10
print(p)

x = 1
for i in input():
    x *= int(i)
print(x)

print(eval('*'.join(input())))

n = int(input())        # вводим число
k = 1                   # устанавливаем счетчик
while n > 0:            # производим вычисления в блоке ниже пока n > 0
    k *= n % 10         # берем остаток от введенного числа (последнюю цифру) и увеличиваем "K" на него
    n = n // 10         # уменьшаем наше введенное число на один разряд (убираем последнюю цифру)
print(k)                # выводим на печать

# Программа принимает на вход одно натуральное число. Ваша задачи найти сколько раз встречается цифра 7 в этом числе
x = int(input())
c = 0
while x > 0:
    last = x  % 10
    if last == 7:
        c += 1
    x = x // 10
print(c)

print(input().count('7'))

n = int(input())        # вводим число
k = 0                   # устанавливаем счетчик
while n > 0:            # производим вычисления в блоке ниже пока n > 0
    if n % 10 == 7:     # если последняя цифра 7
        k += 1          # увеличиваем "K" на 1
        n = n // 10     # уменьшаем наше введенное число на один разряд (убираем последнюю цифру)
    elif n % 10 != 7:   # если последняя цифра не 7
        n = n // 10     # уменьшаем наше введенное число на один разряд (убираем последнюю цифру)
print(k)                # выводим на печать

a = list(input())
c = 0
while '7' in a:
    c += 1
    a.remove('7')
print(c)