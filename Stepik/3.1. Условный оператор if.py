# УСЛОВНЫЙ ОПЕРАТОР if

money = 100
ticket = 90
if money >= ticket:
    print('УРААА!!!')
    print('Я иду в кино')
print('Пора идти домой')

#
print('Нахождение максимума:')
a = int(input())
b = int(input())
c = a
if b > a:
    c = b
print(c)

#
print('Перераспределение значение переменных:')
a = int(input())
b = int(input())
if b > a:
    a, b = b, a
print(a, b)

#
print('Используя значение Истины:')
if True:
    print(1)
    print(2)
else:
    print(3)
    print(4)
print(7)

#
print('Задача с нахождением большего из чисел:')
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

#
print('Проверка на четность:')
a = int(input())
if a % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

#
print('Проверка на четность и кратность:')
a = int(input())
if a % 2 == 0 and a % 3 == 0:
    print('Yes')
else:
    print('No')

#
print('Tasks')
# Как вы знаете, в нашей стране граждане платят подоходный налог 13%. Представьте, что люди с доходом меньше
# 20000 рублей освобождены от уплаты налога. Напишите программу, которая получает на вход значение дохода и
# выводит на экран сумму, оставшуюся после уплаты налога в 13%.
a = int(input())
if a <= 20000:
    print(a)
else:
    print(a - a/100*13)

n = int(input())
print(n if n < 20000 else n * 0.87)

# На вход программе поступает одно слово.
# Если это строка «Python», программа выводит «ДА»; в противном случае программа выводит «НЕТ».
word = (input())
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')

print("ДА" if input() == "Python" else "НЕТ")

print('НДЕАТ'[input() == 'Python'::2])
#Дмитрий, здесь логика такая: input() == 'Python' - это булево выражение, принимает значение True (и тогда равно 1) или
# False (и тогда равно 0) . В первом случае из строки 'НДЕАТ' берётся срез [1::2] - это элементы начиная с 1 с шагом 2
# - получаем ДА, во втором случае срез [0::2] - это элементы начиная с 0 с шагом 2 - получаем НЕТ.

print(['НЕТ', 'ДА'][input() == 'Python'])

# Требуется написать программу, определяющую, является ли четырехзначное натуральное число N палиндромом, т.е.
# числом, которое одинаково читается слева направо и справа налево.
# Программа получает на вход целое положительное четырехзначное число N  и должна вывести "YES",  если число N является
# палиндромом, и "NO" - если не палиндром.
a = str(input())
if a[0] == a[-1] and a[1] == a[-2]:
    print("YES")
else:
    print("NO")

n = input()
if n == n[::-1]:
    print("YES")
else:
    print("NO")

n = input()
print("YES" if n == n[:: -1] else 'NO')

a = int(input())
b = a//1000
c = a % 1000//100
d = a % 100//10
e = a % 10
if b == e and c == d:
    print('YES')
else:
    print('NO')

s = input()
print(['NO', 'YES'][s == s[::-1]])


[print(('NO', 'YES')[s == s[::-1]]) for s in [input()]]

# Программа получает на вход три натуральных числа A, B и C через пробел.
# Вам необходимо вывести "YES" в том случае, если A + B = C и вывести NO в противном случае.
a, b, c = map(int, input().split())
if c == a + b:
    print("YES")
else:
    print("NO")

a, b, c = map(int, input().split())
print('YES' if a + b == c else 'NO')

a, b, c = (int(i) for i in input().split())
print(('YES', 'NO')[a + b != c])

a, b, c = map(int, input().split())
print('NO' if a+b-c else 'YES')

[print(('NO', 'YES')[a + b == c]) for a, b, c in [[int(i) for i in input().split()]]]

# Программа принимает на вход два слова s и t.
# Если слово t является словом s, записанным наоборот, выведите YES, иначе выведите NO.
t = list(input())
s = list(input())
if t == s[::-1]:
    print("YES")
else:
    print("NO")

print('YES' if input() == input()[::-1] else 'NO')

print(('NO', 'YES')[input() == input()[::-1]])

''' Наоборот '''
print("YNEOS"[input() != input()[::-1]::2])

# Даны три натуральных числа a, b, c записанные в отдельных строках. Ваша задача определить, существует ли треугольник
# с такими сторонами. Для этого вспоминаем теорему о существовании треугольника. Она утверждает, что треугольник
# существует, если сумма любых двух сторон больше оставшейся третьей.
# Выведите строку YES, если условие теоремы выполняется, иначе выведите строку NO.
a, b, c = int(input()), int(input()), int(input())
if a + b > c and b + c > a and a + c > b:
    print("YES")
else:
    print("NO")

a, b, c = int(input()), int(input()), int(input())
d = [a, b, c]
d.sort()
if d[2] < (d[0] + d[1]):
    print('YES')
else:
    print('NO')

a, b, c = int(input()), int(input()), int(input())
if max(a, b, c) < (a + b + c) / 2:
    print('YES')
else:
    print('NO')

a, b, c = [int(input()) for i in "123"]
print("YES" if a < b + c and b < a + c and c < a + b else "NO")

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером (иногда и с незначащими нулями), где сумма первых
# трех цифр равна сумме последних трех. Т.е. билеты с номерами 385916 и 2011 – счастливые, т.к.
# 3+8+5=9+1+6 и 0+0+2=0+1+1. Вам требуется написать программу, которая проверяет счастливость билета.
# Программа получает на вход одно целое число N (0 ≤ N < 106) и должна вывести «YES», если билет с номером N
# счастливый и «NO» в противном случае.
t = input().rjust(6, '0')
f = int(t[0])+int(t[1])+int(t[2])
l = int(t[3])+int(t[4])+int(t[5])
if f == l:
    print('YES')
else:
    print('NO')

s = input()
s = s.rjust(6, '0')
print('YES' if sum(map(int, s[:3])) == sum(map(int, s[3:])) else 'NO')

a = int(input())

if (a//100000) + (a//10000 % 10) + (a//1000 % 10) == (a//100 % 10) + (a//10 % 10) + (a % 10):
    print("YES")
else:
    print("NO")

n = [int(i) for i in input()]
print(('NO', 'YES')[sum(n[:-3]) == sum(n[-3:])])

a = input()
print('YES' if sum(map(int, a[:(len(a)-3)]))==sum(map(int, a[-3:])) else 'NO')

n = input().rjust(6, '0')
print('YES' if sum(map(int, n[:3])) == sum(map(int, n[3:])) else 'NO')

n = input().rjust(6, '0')
print('YES' if int(n[0])+int(n[1])+int(n[2])==int(n[3])+int(n[4])+int(n[5]) else 'NO')

a = input()
a = ((6 - len(a)) * '0') + a
print('YES' if int(a[0]) + int(a[1]) + int(a[2]) == int(a[-3]) + int(a[-2]) + int(a[-1]) else 'NO')

n = input()
n = n.rjust(6,'0')
x = int(n[0])+int(n[1])+int(n[2])
y = nt(n[3])+int(n[4])+int(n[5])
if x == y:
    print('YES')
else:
    print('NO')

a = list(map(int, input()))
if sum(a[-3:]) == sum(a[:-3]):
    print("YES")
else:
    print("NO")

z = [int(i) for i in input().zfill(6)]
print('YES' if sum(z[:3]) == sum(z[3:]) else 'NO')

# Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
# являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.
s = ' abcdefgh'
coord_1 = input()
coord_2 = input()
letter = coord_1[0]
letter_2 = coord_2[0]
column1 = s.find(letter)
column2 = s.find(letter_2)
row1 = int(coord_1[1])
row2 = int(coord_2[1])
if (row1 + column1) % 2 == 0 and (row2 + column2) % 2 == 0 or (row1 + column1) % 2 != 0 and (row2 + column2) % 2 != 0:
    print('YES')
else:
    print('NO')


coord_1, coord_2 = input(), input()
letter = coord_1[0]
letter_2 = coord_2[0]
column1 = s.find(letter)
column2 = s.find(letter_2)
row1 = int(coord_1[1])
row2 = int(coord_2[1])
if (row1 + column1) % 2 == (row2 + column2) % 2:
    print('YES')
else:
    print('NO')


