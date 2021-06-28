# Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введённым
# числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление
# на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.
x, y = float(input()), float(input())
z = input()
if z == '+':
    print(x + y)
elif z == '-':
    print(x - y)
elif z == '/':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x / y)
elif z == '*':
    print(x * y)
elif z == 'mod':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x % y)
elif z == 'pow':
    print(x ** y)
elif z == 'div':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x // y)


# или
a = float(input())
b = float(input())
act = input()

if (act=="/" or act=="mod" or act=="div") and b==0:
    c = "Деление на 0!"
elif act=="+":    c = a + b
elif act=="-":    c = a - b
elif act=="/":    c = a / b
elif act=="*":    c = a * b
elif act=="mod":  c = a % b
elif act=="pow":  c = a ** b
elif act=="div":  c = a // b

print (c)

# или
first_integer = float(input())
second_integer = float(input())
operation = str(input())
if second_integer == 0 and operation == "/":
  print("Деление на 0!")
elif second_integer == 0 and operation == "div":
  print("Деление на 0!")
elif second_integer == 0 and operation == "mod":
  print("Деление на 0!")
elif operation == "+":
  print (first_integer + second_integer)
elif operation == "-":
  print(first_integer - second_integer)
elif operation == "/":
  print (first_integer / second_integer)
elif operation == "*":
  print(first_integer * second_integer)
elif operation == "mod":
  print(first_integer % second_integer)
elif operation == "pow":
  print(first_integer ** second_integer)
elif operation == "div":
  print(first_integer // second_integer)


# Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают
# треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется
# написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие
# параметры, которая бы выводила площадь получившейся комнаты.
# Для числа π в стране Малевии используют значение 3.14.
# Формат ввода, который используют Малевийцы:
# треугольник:
# a
# b
# c
# где a, b и c — длины сторон треугольника
# прямоугольник:
# a
# b
# где a и b — длины сторон прямоугольника
# круг:
# r
# где r — радиус окружности
x = input()
if x == "треугольник":
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2  # полупериметр
    s = (p * (p - a) * (p - b) * (p - c)) ** .5  # формула Герона
elif x == "прямоугольник":
    a, b = float(input()), float(input())
    s = a * b
elif x == "круг":
    a = float(input())
    s = 3.14 * a ** 2
print(s)


# или
PI = 3.14

type = input()
if (type == 'круг'):
    print(PI*int(input())**2)
elif (type == 'прямоугольник'):
    print(int(input())*int(input()))
elif (type == 'треугольник'):
    a,b,c = int(input()),int(input()),int(input())
    p = (a + b + c)/2
    print((p * (p - a) * (p - b) * (p - c))**0.5)



# Напишите программу, которая получает на вход три целых числа, по одному числу в
# строке, и выводит на консоль в три строки сначала максимальное, потом минимальное,
# после чего оставшееся число.

# На ввод могут подаваться и повторяющиеся числа.
a, b, c = int(input()), int(input()), int(input())
if a >= b and a >= c:
    x = a
    if b >= c:
        y, z = b, c
    else:
        z, y = b, c
elif b >= a and b >= c:
    x = b
    if a >= c:
        y, z = a, c
    else:
        y, z = c, a
elif c >= a and c >= b:
    x = c
    if a >= b:
        y, z = a, b
    else:
        y, z  = b, a
print(x)
print(z)
print(y)


# или
a,b,c = int(input()), int(input()), int(input())
if a < b:
    a, b = b, a
if a < c:
	a, c = c, a
if b > c:
	b, c = c, b
print(a)
print(b)
print(c)


# или
a, b, c = int(input()), int(input()), int(input())
max_int = max(a, b, c)
min_int = min(a, b, c)
print(max_int)
print(min_int)
print((a + b + c) - max_int - min_int)


# или
x = sorted([int(input()), int(input()), int(input())])
print(x[2], x[0], x[1], sep="\n")



# Напишите программу, принимающую на вход целое число, которая выводит True, если
# переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞)
# и False в противном случае (регистр символов имеет значение).
x = int(input())
if -15 < x <= 12 or 14 < x < 17 or 19 <= x:
    print('True')
else:
    print('False')


# или
n = int(input())
print(-15 < n <= 12 or 14 < n < 17 or 19 <= n)
