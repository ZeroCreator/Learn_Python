#  Функция map.
# class map(object)
#   map(func, *iterables) --map object
# Какие функции можем передавать в качестве аргумента:
# 1. Встроенные
print('Какие функции можем передавать в качестве аргумента:')
print('1. Встроенные')
a = [-1, 2, -3, 4, 5]
b = map(abs, a)
print(list(b))

q = [-1, 2, -3, 4, 5]
c = [abs(i) for i in q] # Аналог функции map()
print(c)

# 2. Самописные
print('2. Самописные')
def f(x): # Функция должна принимать только одно значение
    return x**2

s = [-1, 2, -3, 4, 5]
n = list(map(f, a))
print(n)

# 3. Работа со строками
print('3. Работа со строками')
a = ['hello', 'hi', 'good morning']
b = list(map(len, a))
print(b)

# Передача методов в качестве аргумента:
print('Передача методов в качестве аргумента:')
c = list(map(str.upper, a))
print(c)

# Передача анонимной функции в качестве аргумента:
print('Передача анонимной функции в качестве аргумента:')
f = list(map(lambda x: x[::-1], a))
print(f)

g = [i[::-1] for i in a] # Аналог функции map()
print(g)

f1 = list(map(lambda x: x+'!', a))
print(f1)

# Преобразование строки к списку:
print('Преобразование строки к списку:')
d = list(map(list, a))
print(d)

c = list(map(sorted, d))
print(c)

# Преобразование ввода:
print('Преобразование ввода:')
s = list(map(int, input().split())) # Преобразование к списку - функция list()

#
print('Tasks')
# Напишите программу, которая возводит в квадрат и в куб каждое число из списка numbers пользуясь при этом функциями map и lambda.
# В результате у вас должно получится два отдельных списка: в одном квадраты, в другом кубы. Их необходимо вывести на экран.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x**2, numbers)), list(map(lambda x: x**3, numbers)), sep='\n')

#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
func = lambda x: lambda y: y ** x
print(list(map(func(2), numbers)))
print(list(map(func(3), numbers)))

#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*[list(map(func, numbers)) for func in [lambda x: x**2, lambda x: x**3]], sep='\n')

