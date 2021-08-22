# Выражения - генераторы.
"""
Выражение генератор это почти тоже самое что и генератор списков, отличия лишь в скобках
Выражение генератор это – итератор обьекты которого можно обойти только один раз.
Итератор это обьект который поддерживает функцию next()
a = (i for i in range(1, 6))
print(next(a)) – выведется 1, данное выражение мы можем написать только 5 раз после чего уже не получится так как элементы генератора можно обойти только один раз.
Можно генератор обойти циклом for:
for i in a:
         print(i) -  Второй раз обойти уже не получится.
Можно найти сумму элементов генератора: print(sum(a))
Почему нельзя обойти второй раз? Потому-что элементы генератора попросту не хранятся в памяти.
Где это может пригодиться? Например если нужно сделать итератор с очень большой цифрой например 100000000
Такое большое число запихнуть в список через range() – не получится ибо выйдет ошибка memoryError
Но решение проблемы есть! – Генератор.
a = (i for i in range(1000000000)) – и никаких ошибок.
a = (i for i in range(10)) – его можно преобразовать в список:
print(list(a)) – [0,1,2,3,4,5,6,7,8,9] – список из генератора.
a = [(i for i in range(10))] – из этого список не выйдет.
"""
# Генератор списка
a = [i**2 for i in range(1, 6)]
print(a)

# Выражения - генераторы.
b = (i**2 for i in range(1, 6))
print(b)
print(list(b))
print()

d = [1, 5, 8, 9]
for i in iter(d):
    print(i)
# Генератор - итератор, элементы которого можно итерировать только один раз.
# Итератор - объект, который поддерживает функцию next(). Помнит о том, какой элемент будет браться следующим.
# Итерируемый объект - объект, который предоставляет возможность обойти поочередно свои элементы.
# Может быть преобразован к итератору.

# Список - итерируемый объект, который не является итератором, но который можно к итератору преобразовать:
s = [1, 2, 3]
'''
print(next(s))) # будет ошибка
'''
d = iter(s)
print(next(d))
print(next(d))
print(next(d))

print()
# Генератор сразу изначально является итератором.
b = (i**2 for i in range(1, 6))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

print()
# Итерация - процесс перебора элементов коллекции внутри цикла или какой-то функции, которая делает перебор
b = (i**2 for i in range(1, 6))
print('first')
for i in b: # Генератор поддерживает только один обход:
    print(i)

print('second')
for i in b:
        print(i)

print()
b = (i ** 2 for i in range(1, 6))
print(sum(b)) # = 55
print(sum(b)) # = 0

# Элементы генератора не хранятся в памяти все вместе, а формируются налету.
