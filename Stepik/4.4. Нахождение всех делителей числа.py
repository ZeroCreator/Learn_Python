# НАХОЖДЕНИЕ ВСЕХ ДЕЛИТЕЛЕЙ ЧИСЛА.
print('Динейные вычисления:')
n = int(input())
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=' ')
    i += 1

n = int(input())
i = 1
while i <= n // 2:
    if n % i == 0:
        print(i, end=' ')
    i += 1
print(n)

#
print('нелинейные вычисления:')
n = int(input())
i = 1
while i <= n**0.5:
    if n % i == 0:
        print(i, n // i)        # Дублируется среднее значение
    i += 1

n = int(input())
i = 1
while i*i <= n:
    if n % i == 0:
        if i == n // i:
            print(i)
        else:
            print(i, n // i)
    i += 1

print('Создание списка по порядку')
n = int(input())
i = 1
a = []
while i*i <= n:
    if n % i == 0:
        if i == n // i:
            a.append(i)
        else:
            a.append(i)
            a.append(n // i)
    i += 1
a.sort()
print(a)

n = int(input())
i = 1
a = []
while i*i <= n:
    if n % i == 0:
        a.append(i)
        if i == n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)