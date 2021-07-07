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