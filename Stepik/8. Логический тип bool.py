# ЛОГИЧЕСКИЙ ТИП bool. ОПЕРАТОРЫ СРАВНЕНИЯ.

# КОНЪЮНКЦИЯ - and
# ДИЗЪЮНКЦИЯ - or
# ИНВЕРСИЯ - not

# Кратность проверяется % x == 0
x = 6
print(x%4 != 0)
print(not x%4 == 0)

#
print('Союз "and"')
a = 5
b = 7
print(a>0 and b>0)

a = -5
b = 7
print(a>0 and b>0)

#
print('Союз "or"')
a = 5
b = 7
print(a>0 or b>0)

a = -5
b = 7
print(a>0 or b>0)

a = -5
b = -7
print(a>0 or b>0)

#
print('Двойные сравнения - интервал')
a = 12
print(a>=12 and a<31)

a = 51
print(a>=12 and a<31)

#
print('Проверка числа на двузначность')
a=51
print(a>=10 and a<=99)

#
print('Сравнение "=="')
a = 517
print(a%10 == 7)

print(a>5 or a%2 == 0 and a%10 == 7)
print(a>5 or (a%2 == 0 and a%10 == 7))

#
print('Tasks')
# Программа должна вывести True, если введенное значение является четным числом, в противном случае - False.
a = int(input())
print(a%2 == 0)

print(int(input()) % 2 == 0)

# - кратно 6
a = int(input())
print(a%6 == 0)

print(not int(input()) % 6)

# - не делится на 9
a = int(input())
print(a%9 != 0)

print(int(input()) % 9 != 0)

print(bool(int(input()) % 9))

# - у введенного числа последняя цифра 2
a = int(input())
print(a%10 == 2)

print(int(input())%10==2)

print(input()[-1] == '2')

#На вход поступают два целых числа. Программа должна вывести True, если оба числа делятся на 7, в противном случае - False.
a, b = map(int,input().split())
print(a%7 == 0 and b%7 == 0)

print(all([not int(i) % 7 for i in input().split()]))

print(all(not int(i) % 7 for i in input().split()))

print([0,0] == ([int(a)%7  for a in (input().split())]))

# На вход поступают три целых числа - стороны треугольника. Необходимо вывести True, если данные стороны
# образуют правильный треугольник, в противном случае - False.
a, b, c = map(int,input().split())
print(a == b == c)

print(len(set(input().split())) == 1)

a, b, c = map(int, input().split())

print(a == b and b==c)

# На вход поступают три целых числа - стороны треугольника. Необходимо вывести True, если данные стороны образуют
# равнобедренный треугольник, в противном случае - False.
a, b, c = map(int,input().split())
print(a == b  or b == c or c == a)

print(len(set(input().split())) <= 2)

# На вход поступают три целых числа - стороны треугольника. Необходимо вывести True, если данные стороны образуют
# прямоугольный треугольник, в противном случае - False.
a, b, c = map(int,input().split())
print(c**2 == a**2 + b**2 or a**2 == c**2 + b**2 or b**2 == a**2 + c**2)

f = sorted(map(int,input().split()))
print(f[0]**2 + f[1]**2 == f[2]**2)

a, b, c = sorted(map(int, input().split()))
print(a**2 + b**2 == c**2)

a,b,c=map(int,input().split())
print(a**2+b**2+c**2-max(a,b,c)**2==max(a,b,c)**2)
