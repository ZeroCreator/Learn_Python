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




