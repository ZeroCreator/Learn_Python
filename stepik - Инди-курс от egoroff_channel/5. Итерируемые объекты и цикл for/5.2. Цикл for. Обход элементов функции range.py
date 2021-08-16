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
    if i % 2 == 0 and i % 7 == 0:               # Условие внутри цикла
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

# На вход программе подается два натуральных числа a и b (гарантируется, что a<b), после чего для каждого целого числа
# на интервале от a до b включительно необходимо вывести фразу следующего вида:
# «Число {число}; его квадрат = {квадрат}; его куб = {куб}»
# Кавычки выводить не нужно и пользуйтесь f-строкой.
# Формат входных данных:
# На вход программе подается два натуральных числа a и b, каждое на отдельной строке.
# Формат выходных данных:
# Программа должна вывести текст в соответствии с условием задачи.
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')

#
[print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')
for i in range(int(input()), int(input()) + 1)]

#
for i in range(int(input()), int(input()) + 1): print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')

#
for i in range(int(input()), int(input()) + 1):
    print(f'Число {i}; его квадрат = {i ** 2}; его куб = {i ** 3}')

# Найдите, в каких строках из введённых и в каком месте упоминается "рок", причем регистр букв не важен.
# Вместо явного цикла прохода по строке в цикле используйте подходящий метод строки.
# Формат ввода:
# На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк.
# Формат вывода:
# Для каждой строки, в которой есть сочетание символов «рок», нужно вывести (в порядке появления таких строк)
# номер этой строки (нумерация начинается с единицы) и номер символа, с которого начинается первое вхождение
# этой подстроки (нумерация символов также с единицы).
n = int(input())                        #вводим  число сколько раз выводить слово
count = 0                               #счетчик

for i in range(1, n+1):                 #переменная i будет равна от 1 до n+1
    a = input().lower().find("рок")     #выводим n переменных
    count +=1                           #тикаем
    if a != -1:
        print(count, a+1)

#
n = int(input())
for i in range(n):
    s = input().lower()
    if 'рок' in s:
        print(i+1, s.find('рок')+1)

#
s = [[i, input().lower().find("рок")] for i in range(int(input()))]
[print(i[0]+1, i[1]+1) for i in s if i[1] != -1]

#
word = "рок"
for i in range(1,int(input())+1):
    inp = input().lower()
    if word in inp:
        print(i, inp.index(word)+1)

#
for i in range(1, int(input()) + 1):
    w = input().lower()
    if 'рок' in w:
        print(i, w.find('рок') + 1)

# Напишите программу, которая найдет сумму кубов натуральных чисел от 50 до 100 включительно
# 503 + 513 + 523 + 533 + ... + 1003
s = 0
for i in range(50,101):
    s += i**3
print(s)

#
s = 0
for i in range(50,101):
    s = i**3 + s
    print(s)

#
a = 0
b = a
for i in range(50, 101):
    a = i**3
    b += a
print(b)

# Кратные 3 или 5
# Если перечислить все натуральные числа ниже 10, которые кратны 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел 23.
# Напишите программу, которая принимает натуральное число n и находит сумму всех чисел ниже переданного числа n,
# которые делятся на 3 или на 5.
n = int(input())
b = 0
for i in range(1, n):
    if i%3 == 0 or i%5 == 0:
        b += i
print(b)

#
print(sum(i for i in range(int(input())) if not i % 3 or not i % 5))

#
#summ = 0
#for i in range(1, int(input())):
#    summ += i if not i % 3 or not i % 5 else 0
#print(summ)

print(sum(i if not i % 3 or not i % 5 else 0 for i in range(1, int(input()))))

#
