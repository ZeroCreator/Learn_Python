# АЛГОРИТМ ЕВКЛИДА.
# Алгоритм Евклида позволяет найти наибольший общий делитель (НОД) для двух чисел.

# Даны числа a и b.
# Пока a не равно b:
#    Находим большее из них
#    И уменьшаем его на значение меньшего
#Выводим a или b

# Если НОД (a, b) = 1, то a и b - взаимнопростые числа
a = int(input())
b = int(input())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)

#
print(' Реализация через остаток от деления:')
a = int(input())
b = int(input())
while b > 0:
    c = a % b       # Или a, b = b, a % b
    a = b
    b = c
print(a)

a, b = map(int, input().split())
b = int(input())
while b > 0:
    a, b = b, a % b
print(a)

#
print('Через функцию:')
def Evklid(a, b):
    while b > 0:
        a, b = b, a % b
    return a

#
print('Нахождение НОК:')
#НОК = (A * B) / НОД

a, b = map(int, input().split())
d, c = a, b  # сохраняем исходные данные в новых переменных
while b > 0:
    a, b = b, a % b
NOK = int((c * d) / a)  # произведение исходных данных делим на НОД и приводим к целочисленному значению
print(NOK)

a, b = map(int, input().split())
d, c = a, b
while b > 0:
    a, b = b, a % b
print(int(d*c / a))

a, b = map(int, input().split())
c = a * b
while b > 0:
    a, b = b, a % b
print(int(c / a))

def NOD(a, b):
    while b: a, b = b, a % b
    return a

def NOK(a, b):
    return a * b // NOD(a, b)

print(NOK(*map(int, input().split())))

a, b = map(int, input().split())
n = b * a
while b > 0:
    a, b = b, a % b
print(n//a)