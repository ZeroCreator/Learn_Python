# Цикл for. Обход элементов функции range.
# Цикл for - цикл с известным количетвом повторений.
# Формат цикла for
# for <переменная> in <объект>:
#    <тело цикла>
for i in range(4):
    print(i)                # Переменная i - это переменная цикла.

for i in range(4):
    print(i)
    i = 'hello'
    print(i)


for i in range(4):
    print('inside', i)
print('outside', i)

# Области применения:
print('1. Обход заданной последовательности:')
for i in range(100, 1000):
    if i%2 == 0 and i%7 == 0:               # Условие внутри цикла
        print(i)

for i in range(1, 11):
    print(i, i**2)

#
print('Сумма всех двузначных чисел:')
s = 0
for i in range(10, 100):
    s = s + i
print(s)

#
print('Факториал числа n:')
# 3! = 1*2*3
pr = 1
for i in range(1, 4):
    pr = pr*i
print(pr)

n = int(input())
pr = 1
for i in range(1, n+1):
    pr = pr * i
print(pr)

#
print('2.Повторение заданного действия n-количество раз:')
for i in range(4):
    print('hello')

n = int(input())
for i in range(n):
    print('hello')

#
print('n-раз вывести случайное число от 1 до 100:')
from random import randint

for i in range(5):
    a = randint(1, 100)
    print(a, end=' ')

#
print('Найти сумму случайных чисел:')
from random import randint

s = 0
n = int(input())
for i in range(n):
    a = randint(1, 100)
    s += a
    print(a, end=' ')
print()
print(s)

# Елочка
print('Елочка')
for i in range(1, 11):
    print('*'*i)

# Степени двойки
print('Степени двойки')
for i in range(1, 11):
    print(2**i)

# Вывести сумму введенных цифр:
print('Вывести сумму введенных цифр:')
n = int(input())
s = 0
for i in range(n):
    a = int(input())
    s += a
    print('current s:', s)          # Сумма по итерациям
print('total', s)                   # Итоговая сумма
print('sred arif =', s/n)           # Среднее арифметическое

# Напишите программу, которая считывает два натуральных числа a и b (гарантируется, что a<b), после чего для всех
# чисел от a до b включительно выводит:
# “Fizz”, если это число делится на 3;
# “Buzz”, если это число делится на 5;
# “FizzBuzz”, если выполнены оба предыдущих условия;
# само это число в остальных случаях.
a = int(input())
b = int(input())
for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

#
for n in range(int(input()), int(input()) + 1):
    print('Fizz' * (not n % 3) + 'Buzz' * (not n % 5) or n)

#
for n in range(int(input()), int(input()) + 1):
    if not n % 3 and not n % 5:
        print('FizzBuzz')
    elif not n % 3:
        print('Fizz')
    elif not n % 5:
        print('Buzz')
    else:
        print(n)