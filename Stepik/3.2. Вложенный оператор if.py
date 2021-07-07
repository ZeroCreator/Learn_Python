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

