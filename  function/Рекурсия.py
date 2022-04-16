# Алгоритмы на Python 3. Лекция №7. Тимофей Хирьянов
# Рекурентный случай
# # Крайний случай
def matroshka(n):
    if n == 1:
        print("Матрешечка")
    else:
        print("Верх матрешки n=", n)
        matroshka(n-1)
        print("Низ матрешки n=", n)


matroshka(5)


# Глубина рекурсии - количество вызовов функции
# Факториал
print("# Факториал")
def f(n:int):
    assert n >= 0, "Факториал отрицательного на определен"
    if n == 0:
        return 1
    return f(n-1)*n


print(f(5))

# Алгоритм Евклида
print("Алгоритм Евклида")
# Нахождение наибольшего общего делителя - НОД(a, b)
def gsd(a, b):
    if a == b:
        return a
    elif a > b:
        return gsd(a-b, b)
    else:
        return gsd(a, b-a)

print(gsd(9, 3))


print(gsd(9, 3))
# вариант 2
def gsd(a, b):
    if b == 0:
        return a
    else:
        return gsd(b, a % b)

print(gsd(9, 3))

# вариант 3
def gsd(a, b):
    return a if b == 0 else gsd(b, a % b)

print(gsd(9, 3))


# Быстрое возведение в степень
print("Быстрое возведение в степень")
def pow(a:float, n:int):
    if n == 0:
        return 1
    else:
        return pow(a, n-1) * a


print(pow(5, 10))

# вариант 2
def pow(a:float, n:int):
    if n == 0:
        return 1
    elif n%2 == 1: # для нечетных
        return pow(a, n-1) * a
    else: # для четных
        return pow(a**2, n//2)

print(pow(5, 10))
print(pow(5, 1000))

# Ханойские башни
print("Ханойские башни")
def h(n, x, y):
    if n == 1:
        print(1, x, y)
    else:
        h(n - 1, x, 6 - x - y)
        print(n, x, y)
        h(n - 1, 6 - x - y, y)


n = 2
h(n, 1, 3)

# вариант 2
def move(n, start, finish):
    if n == 1:
        print("Перенести диск 1 со стержня", start, "на стержень", finish)
    else:
        temp = (6 - start) - finish
        move(n - 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        res = (n - 1, temp, finish)
        print(res)

        return res


if __name__ == '__main__':
    assert move(10, 1, 3)

# вариант 3
def h(n, x, y):
    if n >0:
        tmp = 6 - x-y
        h(n-1, x, tmp)
        print(n, x, y)
        h(n-1, tmp, y)
n = int(input())

h(n, 1, 3)