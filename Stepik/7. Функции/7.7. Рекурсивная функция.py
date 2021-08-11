# Рекурсивная функция.
# Рекурсия - функция, которая вызывает саму себя.
# В Python есть онраничения на глубину вызова рекурсии.
# Рекурсия - это сведение решения задачи к аналогичной подзадаче/подзадачам.

'''
def rec(x):
    print(x)
    rec(x + 1)

rec(1)
'''
# Правила вызова рекурсивной функции:
print('Правила вызова рекурсивной функции:')
# 1. У рекурсии должен быть выход (остановка рекурсивной функции).
print('1. У рекурсии должен быть выход (остановка рекурсивной функции)')
# 2. Подзадача равна исходной задаче.
print('2. Подзадача равна исходной задаче.')
# 3. При выполнении вложенных функций масштаб задачи уменьшается.
print('3. При выполнении вложенных функций масштаб задачи уменьшается.')
def rec(x):
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)

rec(1)

# стек вызова: r1 - r2 - r3 - r4

# Нахождение факториала:
print('Нахождение факториала:')
def fact(x):
    if x == 1: # Проверяем функцию на выход
        return 1
    return fact(x-1)*x

print(fact(4))
print(fact(10))

# Нахождение чисел Фибоначчи:
print('Нахождение чисел Фибоначчи:')
# Выходом из функции будут первые два числа ряда Фибоначчи - 0 и 1
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n - 2)
# Эта программа очень долго работает
print(fib(3))
print(fib(10))

# Является ли строка палиндромом.
print('Является ли строка палиндромом.')
# Палиндромы:
# шалаш
# asdffdsa
# '' и 'a'
def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

print(palindrom('шалаш'))

#
print('Tasks')
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи.
# Входные данные:
# Программе поступает на вход целое число N (0 ≤ N ≤ 30) - порядковый номер числа Фибоначчи.
# Выходные данные:
# Вам необходимо вывести на экран N-е число Фибоначчи.
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))

#
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(int(input())))

# Быстрые вычисления
def fib(n):
    l = [*range(0, n + 1)]
    for i in range(2, n + 1):
        l[i] = l[i - 1] + l[i - 2]
    return l[n]


print(fib(int(input())))

#
def fibo(n):
    return n if n < 2 else fibo(n-2) + fibo(n-1)

print(fibo(int(input())))

# Напишите функцию list_sum_recursive, которая принимает на вход список из целых чисел и возвращает сумму элементов
# переданного списка. Не забывайте, что реализовать это нужно при помощи рекурсии.
def list_sum_recursive(n):
    if len(n) == 1:
        return n[0]
    return list_sum_recursive(n[1:]) + n[0]

n = list(map(int, input().split()))
print(list_sum_recursive(n))

#
def list_sum_recursive(s):
    return s.pop() + list_sum_recursive(s) if s else 0

#
def list_sum_recursive(l):
    return l[0] if len(l) == 1 else l[0] + list_sum_recursive(l[1:])

# Представьте, что у нас есть список целых чисел неограниченной вложенности. То есть наш список может состоять из
# списков, внутри которых также могут быть списки. Ваша задача превратить все это в линейный список при помощи функции
# flatten
# flatten([1, [2, 3, [4]], 5]) # вернет [1,2,3,4,5]
# flatten([1, [2,3], [[2], 5], 6]) # вернет [1,2,3,2,5,6]
# flatten([[[[9]]], [1,2], [[8]]]) # вернет [9,1,2,8]
def flatten(s):
    if not s: # условие на выход: if s == []
        return []

    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])

print(flatten([1, [2, 3, [4]], 5]))

#
def flatten(s):
    out = []
    for v in s:
        if isinstance(v, list):
            out.extend(flatten(v))
        else:
            out.append(v)
    return out

#
def flatten(x):
  k=[]
  if type(x)==type(k):
    for i in x:
      k.extend(flatten(i))
    return k
  return [x]

#


