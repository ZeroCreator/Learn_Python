# Функция filter.
# class filter(object)
#   filter(function or None, iterable) --> filter object
# Возвращает все элементы списка со значением True
# Собственные функции:
print('Собственные функции:')

def f(x):
    return x > 10

a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
b = filter(f, a)
print(list(b))

def f1(x): # Четные
    return x % 2 == 0

b = filter(f1, a)
print(list(b))

def f2(x): # Двузнаяные
    return x > 9 and x < 100

b = filter(f2, a)
print(list(b))

b = [i for i in a if i > 9 and i < 100] # Аналог функции filter()
print(b)

b = [i for i in a if i % 10 == 2]
print(b)

# Встроенные функции:
print('Встроенные функции:')
a = [14, 0, 5, '', 'hello', [5], '', 0, [], 471]
b = list(filter(bool, a))
print(b)

b = list(filter(None, a))
print(b)

# Строковый список
print('Строковый список')
a = ['world', 'hello', '3243', 'potato', 'carrot', 'hi']
# Анонимная функция в качестве аргумента:
print('Анонимная функция в качестве аргумента:')
b = list(filter(lambda x: len(x) > 4, a))
print(b)

# Методы объектов в качестве аргумента:
print('Методы объектов в качестве аргумента:')
a = '432vjb'
b = list(filter(, a))
print(b)