# НАХОЖДЕНИЕ ВСЕХ ДЕЛИТЕЛЕЙ ЧИСЛА.
print('линейные вычисления:')
n = int(input())
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=' ')
    i += 1

# Ускорение программы в 2 раза:
n = int(input())
i = 1
while i <= n // 2:
    if n % i == 0:
        print(i, end=' ')
    i += 1
print(n)

#
print('нелинейные вычисления:')
n = int(input())
i = 1
while i <= n**0.5:
    if n % i == 0:
        print(i, n // i)        # Дублируется значение серединное
    i += 1

n = int(input())
i = 1
while i*i <= n:
    if n % i == 0:
        if i == n // i:
            print(i)
        else:
            print(i, n // i)
    i += 1

print('Создание списка по порядку')
n = int(input())
i = 1
a = []
while i*i <= n:
    if n % i == 0:
        if i == n // i:
            a.append(i)
        else:
            a.append(i)
            a.append(n // i)
    i += 1
a.sort()
print(a)

n = int(input())
i = 1
a = []
while i*i <= n:
    if n % i == 0:
        a.append(i)
        if i == n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)

# Программа получает на вход натуральное число N.
# Нужно найти сумму его делителей.
a = int(input())
c = 0
i = 0
while c != a:
    c += 1
    if a % c == 0:
        i += c
print(i)

n = int(input())

total = 0
i = 1
while i <= n:
    if n % i == 0:
        total += i
    i += 1

print(total)

import math
n = int(input())
i = 1
a = []

while i * i <= n:
    if n % i == 0:
       if i == n // i:
           a.append(i)
       else:
           a.append(i)
           a.append(n // i)
    i += 1

print(sum(a))

n = int(input())
print(sum(i for i in range(1, n + 1) if n % i == 0))

# Дано натуральное число N. Определить, является ли оно простым. Натуральное число N называется простым, если у него
# есть только два делителя: единица и само число N.
# В качестве ответа выведите "Yes", если число простое,  "No" - в противном случае.
x = int(input())
a = x
while a > 2:
    a -= 1
    if x % a == 0:
        print('No')
        break
else:
    if x == 1:
        print('No')
    else:
        print('Yes')

#
a = int(input())
i = 2
while a % i != 0 and i < a:
    i += 1
print('Yes' if i == a else 'No')

#
def dig(x):
    i = 2
    while x % i != 0 and i < x:
        i += 1
    return i == x

print(['No', 'Yes'][dig(int(input()))])

#
def dig(x):
    i = 2
    while x % i != 0 and i < x:
        i += 1
    return i == x

print(['No', 'Yes'][dig(int(input()))])

#
n = int(input())
i = 1
count = 0
while i < n ** 0.5:
    if n % i == 0:
        count += 2
    i += 1
print('Yes' if count == 2 else 'No')

#
n = int(input())
if n==1:
  print('No')
else:
  print('YNeos'[any(1 for i in range(2,n) if n%i==0)::2])

#
a = int(input())
b = 2
cnt = 0
while b*b <= a:
    if a % b == 0:
        cnt += 1
    b += 1
if cnt == 0 and a != 1:
    print("Yes")
else:
    print('No')

#
n, f = int(input()), False
for _ in range(2, int(n**.5) + 1):
    if not n % _:
        f = True
        break
print(['Yes', 'No'][n == 1 or f])

#
n = int(input())
f = True
if n == 1 or n != 2 and not n % 2:
    f = False
else:
    for i in range(3, int(n ** .5 + 1), 2):
        if not n % i:
            f = False
            break
print("YNeos"[1 - f::2])

#
n = int(input())
a = 2
while n % a != 0 and a < n:
    a += 1
if a == n:
    print("Yes")
else:
    print("No")

#
n = int(input())
print(('No', 'Yes')[n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))])

#
n = int(input())
i = 1
dividers = []  # список делителей числа n

while i ** 2 <= n:  # находим все делители числа n
    if n % i == 0:
        dividers.append(i)  # накапливаем делители n в списоке делителей
        if i != n // i:
            dividers.append(n // i)  # отсееваем повторы
    i += 1

# простые числа делятся без остатка только на себя и еденице, следовательно
# длина списка делителей простого числа равна 2
if len(dividers) == 2:
    print('Yes')  # число простое
else:
    print('No')

#
a = int(input())
s = []
for i in range(1,a + 1):
    if a % i == 0:
        s.append(i)
if len(s) == 2:
    print('Yes')
else:
    print('No')