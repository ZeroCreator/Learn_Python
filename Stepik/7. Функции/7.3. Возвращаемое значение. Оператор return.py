# Возвращаемое значение. Оператор return.
'''
def square(x):
    print(x**2)

a = square(6)
print(a)
'''

def square(x):
    return x**2

a = square(6)
print(a)

a = square(square(3))
print(a)

def example():
    print(1)
    print(2)
    return 'hello' # Работает как break в цикле - выход из функции
    print(3)
    print(4)

example()

print(example())

# Функция, возвращающая ответ на вопрос о четности числа.
print('Функция, возвращающая ответ на вопрос о четности числа')
'''
# Вариант 1:
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False

for i in range(1, 11):
    print(i, even(i))
'''
'''
# Вариант 2:
def even(x):
    if x % 2 == 0:
        return True

for i in range(1, 11):
    print(i, even(i))
'''
# Вариант 3:
def even(x):
    return x % 2 == 0

for i in range(1, 11):
    print(i, even(i))

# Функция факториала:
print('Функция факториала:')
def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr*i
    return pr

# Факториал чисел от 1 до 7 включительно:
for i in range(1, 8):
    print(i, factorial(i))

def sochet(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print(sochet(5, 3))

# Функция для вычисления площади и периметра:
print('Функция для вычисления площади и периметра:')
def sq_and_per(a, b):

    return a*b, 2*(a + b)

print(sq_and_per(3, 6)) # Возвращает кортеж

square, perimetr = sq_and_per(3, 6)
print(square, perimetr)

def sqAndPer(a, b):
    mas = []
    mas.append(a*b)
    mas.append(2*(a + b))
    return mas

print(sqAndPer(2, 6))

#
print('Tasks')
# Ваша задача написать функция find_duplicate, которая принимает один аргумент - список чисел. Функция должна возвращать
# список из дублей, каждый дубль нужно брать только один раз в том порядке, в котором они встречаются в исходном списке.
# Под дублем будем подразумевать число, которое присутствовало в списке несколько раз.
def find_duplicate(s):

    duplicates = []
    for i in s:
        if s.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates


print(find_duplicate([1, 2, 2, 3]))
print(find_duplicate([7, 7, 7]))
assert find_duplicate([1, 2, 2, 3]) == [2]
assert find_duplicate([7, 7, 7]) == [7]
assert find_duplicate([3, 2, 1, 1, 2, 3]) == [3, 2, 1]
assert find_duplicate([1, 2, 3]) == []


# Напишите функцию first_unique_char, которая принимает строку символов и возвращает позицию первого уникального символа
# в строке. В случае, если уникальных символов в переданной строке нет, верните -1. Регистр символов не учитывайте.
# Ваша задача написать только определение функции first_unique_char
def first_unique_char(s):
    l = []
    for i in s.lower():
        if s.count(i) == 1:
            l.append(s.find(i))
    if len(l) > 0:
        return l[0]
    else:
        return -1

#
def first_unique_char(array):
    for i, num in enumerate(array):
        if array.count(num) == 1:
            return i
    return -1

#
def first_unique_char(s):
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1

