# МНОЖЕСТВЕННЫЙ ВЫБОР elif.

#
print('Tasks')
# Ваша программа должна считать одно натуральное число, после чего вывести:
# “Fizz”, если это число делится на 3;
# “Buzz”, если это число делится на 5;
# “FizzBuzz”, если выполнены оба предыдущих условия;
# само это число в остальных случаях.
t = int(input())
if t % 5 == 0 and t % 3 == 0:
    print('FizzBuzz')
elif t % 3  == 0:
    print('Fizz')
elif t % 5 == 0:
    print('Buzz')
else:
    print(t)

n = int(input())
if n % 15 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)

n = int(input())
print('Fizz'*(n%3==0) + 'Buzz'*(n%5==0) or str(n))

n = int(input())
print((n, 'Fizz', 'Buzz', 'FizzBuzz')[(not n % 3) + 2 * (not n % 5)])

# Даны три целых числа, записанных в отдельных строках. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадают) или 0 (если все числа различны).
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

abc = {input(), input(), input()}
print(0 if len(abc) == 3 else 4 - len(abc))

print([3, 2, 0][len(set([int(input()) for _ in '123'])) - 1])

# Программа определяет наименование месяца по его номеру n. Название месяца пишется с заглавной буквы
# Программа получает на вход номер месяца - натуральное число N (N<=12) и в зависимости от его значения вывод название
# месяца
n = int(input())
if n == 1:
    print('Январь')
elif n == 2:
    print('Февраль')
elif n == 3:
    print('Март')
elif n == 4:
    print('Апрель')
elif n == 5:
    print('Май')
elif n == 6:
    print('Июнь')
elif n == 7:
    print('Июль')
elif n == 8:
    print('Август')
elif n == 9:
    print('Сентябрь')
elif n == 10:
    print('Октябрь')
elif n == 11:
    print('Ноябрь')
elif n == 12:
    print('Декабрь')

n = int(input())
month = ['Январь', 'Февраль', 'Март', 'Апрель',
         'Май', 'Июнь', 'Июль', 'Август',
         'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
print(month[n-1])

print([0, 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
       'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'][int(input())])

a = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
print(a[int(input())-1])

a = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5:' Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь',
    10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
x = int(input())
print(a[x])

# Напишите программу, которая считывает с клавиатуры два вещественных числа, а затем строку. Если эта строка является
# обозначением одной из четырёх основных математических операций (+, -, * или /), то выведите результат применения этой
# операции к введенным ранее числам, в противном случае выведите «Неизвестно». Также «Неизвестно» следует вывести, если
# пользователь захочет поделить на ноль.
a, b = float(input()), float(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('Неизвестно')
    else:
        print(a / b)
else:
    print('Неизвестно')

a = float(input())
b = float(input())
c = str(input())
print(int(a+b) if c == '+'
    else int(a-b) if c == '-'
    else a*b if c == '*'
    else a/b if c == '/' and b != 0
    else 'Неизвестно')

# Напишите программу, которая имитирует проверку пароля, придуманного пользователем. Пользователь сперва вводит пароль,
# потом вводит подтверждение пароля. Вам нужно обработать следующие ситуации:
# если пароль, который ввёл пользователь (в первый раз) короче 7 символов, программа выводит "Short"
# если пароль достаточно длинный, но введённый во второй раз пароль не совпадает с первым, программа выводит "Difference"
# если же и эта проверка пройдена успешно, программа выводит "OK" (латинскими буквами).
x = input()
y = input()
if len(x) < 7:
    print('Short')
elif x == y:
    print('OK')
elif x != y:
    print('Difference')

a=input()
b=input()
if a==b and len(a)>7:
    print("OK")
elif len(a)<7:
    print("Short")
else:
    print("Difference")




