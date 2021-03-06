# Логический тип Bool. Операторы сравнения
rez = 5 == 5.0
print(rez)

# Проверка на четность
x = 6
print(x%2 == 0)

# Проверка на нечетность
x = 6
print(x%2 != 0)

# and
y = 1.8
rez = y >= -2 and y <=5 #  -2 <= y <=5
print(rez)

# or
y = 1.8
rez = y <= -2 or y >=5
print(rez)

y = -10
rez = y <= -2 or y >=5
print(rez)

# инверсия общего составного условия
x = 7
r = x % 2 == 0 or x % 3 == 0
print(r)

r1 = x % 2 != 0 or x % 3 != 0
r2 = not (x % 2 == 0 or x % 3 == 0)
print(r1)
print(r2)

# функция bool()
print(bool(1))
print(bool(0))
print(bool(''))
print(bool('0'))

# Подвиг 5. Вводится вещественное число. Нужно определить, что его целая часть кратна 3. На экран вывести True,
# если кратно и False - в противном случае. Задача делается без использования условного оператора.
print(int(float(input())) % 3 == 0)

# Подвиг 6. Вводится стоимость книги X рублей (например, X = 435.78) - положительное вещественное число с точностью
# до сотых (два знака после запятой). Требуется определить, является ли дробное значение (число после запятой) больше 50.
# На экран вывести True, если больше и False - в противном случае. Задача делается без использования условного оператора.
x = float(input())
print((x-int(x))*100 > 50)

#
digit = float(input())
print(digit % 1 > .5)
#>>> 58 % 1   # любое число делится на 1 без остатка.
# >>> 58.5 % 1   # просто выдаст дробную часть.
# 0.5

#
a = float(input())
print(round(a) > a)

#
print(float(input()) * 100 % 100 > 50)

#
print(int(input().split('.')[1]) > 50)

# Подвиг 7. Вводятся два целочисленных значения в одну строчку через пробел. Можно прочитать с помощью команды:
# a, b = map(int, input().split())
# Необходимо определить, можно ли первое число нацело разделить на второе. На экран вывести True, если делится и False -
# в противном случае. Задача делается без использования условного оператора.
a, b = map(int, input().split())
print(a % b == 0)

#
a, b = map(int, input().split())
print(not (a % b))

# Подвиг 10. Вводятся три целых положительных числа. Прочитать в переменные их можно с помощью команды:
# a, b, c = map(int, input().split())
# Необходимо определить, можно ли их интерпретировать (воспринимать) как длины сторон треугольника. Напомню, что сумма
# длин двух произвольных сторон всегда должна быть больше третьей стороны. На экран вывести True, если треугольник
# формируется и False - в противном случае. Задача делается без использования условного оператора.
a, b, c = map(int, input().split())
print((a+b) > c and (b+c) > a and (c+a) > b)

#
a, b, c = sorted(map(int, input().split()))
print(c < a + b)

#
a, b, c = map(int, input().split())
max_len = max(a,b,c)
print(a + b + c - max_len > max_len)

# Подвиг 11. Вводится вещественное число. Нужно проверить, что оно попадает или в диапазон [0; 2] или в
# диапазон [10; 20] (включительно). На экран вывести True, если попадает и False - в противном случае.
# Задача делается без использования условного оператора.
x = float(input())
print((0<=x<=2) or (10<=x<=20))

#
x = float(input())
print((0 <= x <= 2) != (10 <= x <= 20))


