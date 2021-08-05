# Передача аргументов. Сопоставление аргументов по имени и позиции.
# Не использовать изменяемые объекты в качестве значений по умолчанию.
def f(a, b):
    print(id(a), id(b), 'local')
    a = 100
    b = 200
    print(id(a), id(b), 'local after')
    #print(a, b, 'local')

c = 20
d = 50
print(id(c), id(d), 'global')
f(c, d)
#print(c, d, 'global')

# В момент передачи происходит автоматическое присвоение.
# a = c, b = d

def s(a, b):
    print(id(a), id(b), 'local')
    a = 100
    b = 200
    print(id(a), id(b), 'local after')
    #print(a, b, 'local')

c = 'hello'
d = [1, 2, 4, 6, 76]
print(id(c), id(d), 'global')
s(c, d)
print(c, d, 'global')

# Изменение глобальных переменных:
print('Изменение глобальных переменных:')
def k(a, b):
    print(id(a), id(b), 'local')
    a = 100
    b.append(100)
    b[1] = 'hi'
    print(id(a), id(b), 'local after')
    #print(a, b, 'local')

c = 'hello'
d = [1, 2, 4, 6, 76]
print(id(c), id(d), 'global')
k(c, d)
print(c, d, 'global')

# Чтобы избежать изменение списка в глобальной переменной, используем при передаче аргумента копию списка

k(c, d[:])

# Варианты вызова функции:
print('Варианты вызова функции:')
print('1. Позиционный')

def f(a, b, c):
    print(a, b, c)

f(1, 5, 7)

print('2. По имени')
f(b = 10, c = 20, a = 5)

print('3. Комбинированный вариант')
f(2, c = 10, b = 20)

# Присваивание аргументам значений по умолчанию:
def d(a, b, c = 'Неизвестно'):
    print(a, b, c)

d(2, 3)     # Аргумент с присвоенным значением не передается
# Если передать значение - оно перезапишется:
d(2, 3, 4)

# Изменяемые объекты в аргументов по умолчанию (mutable default):
print('Изменяемые объекты в аргументов по умолчанию (mutable default):')
# Функция добавления значения в список:
print('Функция добавления значения в список:')

def append_to_list(value, my_list):
    my_list.append(value)
    print(my_list, id(my_list))

a = [1, 2, 3]
append_to_list(10, a)
append_to_list(15, a)
append_to_list(18, a)
# Все значения накапливаются в один и тот же список.

append_to_list(18, [1, 2, 3])
append_to_list(18, [])

# Решение при дефолтном значении со списком:
print('Решение при дефолтном значении со списком:')

def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))


append_to_list(77)
append_to_list(99)
append_to_list(111)

# Решение при дефолтном значении со словарем:
print('Решение при дефолтном значении со словарем:')
def append_to_dict(key, value, my_dict=None):
    if my_dict is None:
        my_dict = {}
    my_dict[key] = value
    print(my_dict)


append_to_dict(77, 100)
append_to_dict(99, 200)
append_to_dict(111, 300)