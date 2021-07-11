# ВЛОЖЕННЫЙ ОПЕРАТОР if.

a = 35
if a % 5 == 0:                  # Значение кратное 5
    if a > 9 and a < 100:       # Проверка на двузначность
        print(1)
        print(2)
    else:
        print(3)
        print(4)
else:
    if a % 2 == 0:              # Значение кратное 2
        print(5)
        print(6)

    else:
        print(7)
        print(8)
print('end')

#
print('Нахождение минимума 3-х чисел:')
a = int(input())
b = int(input())
c = int(input())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)

#
print('Какой координате четверти принадлежит данная точка:')
x = int(input())
y = int(input())
if x > 0:
    # 1 or 4
    if y > 0:
        print(1)
    else:
        print(4)
else:
    # 2 or 3
    if y > 0:
        print(2)
    else:
        print(3)

#
print('Какой будет остаток при делении на 4:')
a = int(input())
if a % 4 == 0:
    print(0)
else:
    if a % 4 == 1:
        print(1)
    else:
        if a % 4 == 2:
            print(2)
        else:
            print(3)

#
print('Tasks')
# В данной задаче необходимо сравнить два целых числа A и B. Они поступают на вход программе отдельно в каждой строке.
# Ваша задача вывести символ "<", если A меньше B, ">", если A больше B и "=", если A=B.
a = int(input())
b = int(input())
if a == b:
    print('=')
else:
    if a > b:
        print('>')
    else:
        print('<')

a, b = int(input()), int(input())
print('<' if a < b else '>' if a > b else '=')

A, B = int(input()), int(input())
print('>'*(A > B) + '<'*(A < B) + '='*(A == B))

d = int(input()) - int(input())
print('=><'[(d > 0) - (d < 0)])

A, B = int(input()), int(input())
print(['=', '>', '<'][(A > B) - (A < B)])

A, B = int(input()), int(input())
print('><='[(A < B) + (A == B)*2])

a, b = int(input()), int(input())
print('=' if a == b else '<' if a < b else '>')

# Даны три целых числа, каждое записано в отдельной строке.
# Нужно вывести значение наибольшего из данных чисел
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

a, b, c = int(input()), int(input()), int(input())
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
print(a)

a, b, c = int(input()), int(input()), int(input())
if a>b and a>c:
    print(a)
else:
    if b>c and b>a:
        print(b)
    else:
        print(c)

a, b, c = (int(input()) for _ in 'abc')
if a < b: a = b
if a < c: a = c
print(a)

a, b, c = int(input()), int(input()), int(input())
print(a if a > b and a > c else b if b > a and b > c else c if c > a and c > b else '')

a, b, c = int(input()), int(input()), int(input())
print(a if a > b and a > c else b if b > a and b > c else c)

a, b, c = int(input()), int(input()), int(input())
print(a*(c < a > b) or b*(c < b > a) or c*(a < c > b))

# На свой день рождения Петя купил красивый и вкусный торт, который имел идеально круглую форму. Петя не знал, сколько
# гостей придет на его день рождения, поэтому вынужден был разработать алгоритм, согласно которому он сможет быстро
# разрезать торт на N равных частей. Следует учесть, что разрезы торта можно производить как по радиусу, так и по
# диаметру.
# Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей.
n = int(input())
if n == 1:
    print(0)
else:
    if n % 2 == 0:
        print(int(n/2))
    else:
        print(n)

a = int(input())
print(a if a % 2 != 0 and a > 1 else int(a/2))

# В отделе работают 3 сотрудника, которые получают заработную плату в рублях. Требуется определить: на сколько
# зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.
# Входные данные: Размеры зарплат всех сотрудников вводятся в одну строку через пробел.
# Каждая заработная плата – это натуральное число, не превышающее 105. И гарантируется ,что все зарплаты различны
# Выходные данные: Необходимо вывести одно целое число — разницу между максимальной и минимальной зарплатой.
a, b, c = map(int, input().split())
if a > b and a > c:
    if b > c:
        print(a - c)
    else:
        print(a - b)
if b > a and b > c:
        if a > c:
            print(b - c)
        else:
            print(b - a)
if c > a and c > b:
    if b > a:
        print(c - a)
    else:
        print(c - b)

a, b, c = map(int,input().split())
if a > b:
    if a > c:
        if b > c:
            print(a - c)
        else:
            print(a - b)
if b > a:
    if b > c:
        if a > c:
            print(b - c)
        else:
            print(b - a)
if c > a:
    if c > b:
        if b > a:
            print(c - a)
        else:
            print(c - b)


a, b, c = map(int, input().split())
if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a
print(a - c)

# Вводятся две строки равной длины, состоящие из больших и маленьких букв латинского алфавита.
# Необходимо сравнить эти строки лексикографически. При этом регистр букв значения не имеет, то есть большая буква
# считается эквивалентной соответствующей маленькой букве.
a, b = input().lower(), input().lower()
if a == b:
    print('0')
elif a < b:
    print('-1')
elif b < a:
    print('1')

a, b = input().lower(), input().lower()
print(int(a > b) - int(b > a))

a, b = [input().lower() for _ in '..']
print(0 if a == b else (-1, 1)[b < a])

a, b=input().lower(), input().lower()
if a == b:
    print(0)
else:
    if a < b:
        print(-1)
    else:
        print(1)

# Двое решили посоревноваться в набирании текстов на сайте «Кнопочные гонки». Во время соревнования необходимо ввести
# текст из s символов. Первый участник набирает один символ за v1 миллисекунд и имеет пинг t1 миллисекунд.
# Второй участник набирает один символ за v2 миллисекунд и имеет пинг t2 миллисекунд.
# При соединении с пингом (задержкой) в t миллисекунд соревнование проходит для участника следующим образом:
# Ровно через t миллисекунд после начала соревнования участник получает текст, который необходимо ввести.
# Сразу после этого он начинает вводить этот текст.
# Ровно через t миллисекунд после того, как он перепечатал весь текст, сайт получает информацию об этом.
# Победителем в соревновании является тот участник, информация об успехе которого пришла раньше. Если информация пришла
# от обоих участников одновременно, считается, что произошла ничья.П
# о данной длине текста и информации об участниках, определите исход игры.
# Входные данные:
# Первая строка содержит пять целых чисел s, v1, v2, t1, t2 (1 <= s, v1, v2, t1, t2 <= 1000) —
# количество символов в тексте, скорость набора текста первым участником, скорость набора текста вторым участником,
# пинг первого участника и пинг второго участника.
# Выходные данные:
# Если выиграет первый участник, выведите «First». Если выиграет второй участник, выведите «Second».
# В случае ничьей выведите «Friendship».
s, v1, v2, t1, t2 = map(int, input().split())
time1 = s*v1 + 2*t1
time2 = s*v2 + 2*t2
if time1 > time2:
    print('Second')
elif time1 < time2:
    print('First')
else:
    print('Friendship')

s, v1, v2, t1, t2 =map(int,input().split())
time1= t1*2+v1*s
time2= t2*2+v2*s
print('First' if time1<time2 else 'Second' if time1>time2  else 'Friendship')

s, v1, v2, t1, t2 = map(int, input().split())
a, b = s * v1 + 2 * t1, s * v2 + 2 * t2
print('First' * (a < b) + 'Second' * (a > b) + 'Friendship' * (a == b))

a = list(map(int, input().split()))
if a[0]*a[1]+2*a[3] < a[0]*a[2]+2*a[4]:
    print('First')
elif a[0]*a[1]+2*a[3] > a[0]*a[2]+2*a[4]:
    print('Second')
elif a[0]*a[1]+2*a[3] == a[0]*a[2]+2*a[4]:
    print('Friendship')


# При игре в "Города" игроки по очереди называют названия городов так, чтобы первая буква каждого нового слова совпадала
# с последней буквой предыдущего. При этом считают, что если последняя буква предыдущего слова — мягкий знак, то с первой
# буквой следующего слова надо сравнивать букву, предшествующую мягкому знаку.
# Напишите программу, которая считывает подряд две строки, после чего выводит «Good», если последний символ первой строки
# совпадает с первым символом второй (с учётом правила про мягкий знак), и «Bad» в противном случае.
a, b = input().lower(), input().lower()
if a[-1] == b[0]:
    print('Good')
elif a[-1] =='ь':
    if a[-2] == b[0]:
        print('Good')
else:
    print('Bad')

a,b=input().lower().replace('ь',''),input().lower()
print('Good' if a[-1]==b[0] else 'Bad')