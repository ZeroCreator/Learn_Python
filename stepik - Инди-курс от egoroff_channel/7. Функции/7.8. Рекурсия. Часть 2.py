# Рекурсия. Часть 2.
# 1. Дана строка, содержащая только английские буквы (большие и маленькие).
# Добавить открывающиеся и закрывающиеся скобки по следующему образцу:
# '(e(x(a(m)p)l)e)' (До середины добавлены открывающиеся скобки, после
# середины - закрывающиеся. В случае, когда длина строки четная в скобках,
# в середине, должно быть два символа ('card -> (c(ar)d).
def rec(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return "(" + s[0] + "(" + rec(s[1:-1]) + ")" + s[-1] + ")"

s = input()
print(rec(s))

# Функция, которая возводит число х в степень n.
print('Функция, которая возводит число х в степень n.')
def power(x, n):
    if n == 0:  # Проверяем на выход из рекурсии
        return 1
    if n < 0:
        return 1/power(x, -n)
    if n % 2 == 0:
        return power(x, n // 2) * power(x, n // 2)
    else:
        return power(x, n - 1) * x


x = int(input())
n = int(input())
print(power(x, n))

# Имеем список с произвольной вложенностью.
# Обойти все элементы списка и указать, на каком уровне вложенности они находятся.
a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [3, 4, [2, 3], 5]]

def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if type(i) == list:
            rec(i, level + 1)


rec(a)

# Посчиать сумму чисел, введенных с клавиатуры:
print('Посчиать сумму чисел, введенных с клавиатуры:')
def s(n):
    if n == 1:      # Обработка крайнего случая
        return int(input())
    return s(n-1) + int(input())    # Обработка рекурентного случая

# Фактоириал числа:
print('Факториал числа:')
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

print(factorial(5))

# Динамическое программирование - разворот рекурсии в другую сторону


# Матрешка
print('Матрешка')
def matroska(n):
    if n == 1:
        print('Крайняя матрешечка')
    else:
        print('Верх матрешки n=', n) # Прямой ход рекурсии
        matroska(n-1)
        print('Низ матрешки n =', n) # Обратный ход рекурсии

matroska(5)

# Ханойские башни
def hanoi(n, start, finish):
    if n == 1:
        print('Переложить блин 1 с', start, 'на', finish)
    else:
        tmp = 6 - start - finish
        hanoi(n - 1, start, tmp)
        print('Переложить блин', n, 'c', start, 'на', finish)
        hanoi(n - 1, tmp, finish)

hanoi(3, 1, 2)
hanoi(4, 1, 2)



