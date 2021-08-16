# Функции.
# Разбиение на логические части
# Сокрытие деталей реализации
# Переиспользование кода
# Создание новых примитивов

def f(n): # n - аргумент функции
    return n * 10 + 5
print(f(f(f(10)))) # вызов функции

# Функции могут быть:
# Без возвращаемого значения (процедура) -  например, выводит справочное сообщение на экран
# Без параметров
# Произвольное число параметров
# Параметры со значением по умолчанию

# произвольное число параметров:
print('произвольное число параметров:')
def min(*a): # Минимальное значение в списке
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m

print(min(5))
print(min(5, 3))
print(min(5, 3, 6, 10))
print(min([5, 3, 6, 10]))

print()
# значение параметров по умолчанию:
print('значение параметров по умолчанию:')
# Модификация функции range:
def my_range(start, stop, step=1):
    res = [] # Результатом будем возвращать список, куда будем накапливать элементы
    if step > 0:
        x = start # Инициализируем стартовое значение
        while x < stop:
            res += [x] # Добавляем переменную в список
            x += step # Увеличиваем переменную на значение шага
    elif step < 0:
        x = start # Инициализируем стартовое значение
        while x > stop:
            res += [x] # Добавляем переменную в список
            x += step # Увеличиваем переменную на значение шага
    return res

print(my_range(2, 5))
print(my_range(2, 15, 3))
print(my_range(15, 2, -3))

print()
# Локальные переменные
print('Локальные переменные')
# Переменные, объявленные внутри функции называются локальными. Не работают вне функции.
# Изменение объектов, связанных с локальными переменными.
def append_zero(xs):
    xs.append(0)

a = [] # Изменяемый объект 'список'
print(a) # []
append_zero(a)
print(a) # [0]
print(append_zero(a))

print()
# Глобальные переменные:
print('Глобальные переменные:')
# Переменные, объявленные вне функций называются глобальными.


# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей
# числовой прямой:
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return (x / 2) * (-1)
    elif x > 2:
        return (x - 2) ** 2 + 1
print(f(float(input())))

#
def f(x):
    if x <= -2:
        return 1 - (x+2)**2
    if x <= 2:
        return -x/2
    return (x-2)**2 + 1

#
def f(x):
    return float(x<-2 and 1-(x+2)**2 or 2<x and (x-2)**2+1 or -2<=x<=2 and -x/2)


# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
"""
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

# Функция не должна осуществлять ввод/вывод информации.

def modify_list(l):
     le = len(l) - 1
     i = le
     while i != -1:
         if l[i] % 2:
             del l[i]
         else:
             l[i] = l[i] // 2
         i -= 1
     return


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)

"""

def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 0:
            l[i] //= 2
        else:
            l.pop(i)

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)

#
def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]

#
def modify_list(l):
    l[:] = [i//2 for i in l if i % 2 == 0]

#
def modify_list(l):
    i=0
    while i<len(l):
        if l[i]%2 !=0:
            del (l[i])
        else:
            l[i]=l[i]//2
            i+=1

#
def modify_list(l):
    b = []
    for x in l:
        if x % 2 == 0:
            b.append(x // 2)
    l[:] = b

#
def modify_list(l):
    e = []  # Создаем новый список
    for x in l:  # Пробегаем все значения нового списка
        if x % 2 > 0:  # Условие нечетности
            e.append(x)  # Добавляем в новый список неустраивающее нас значение

    for i in e:  # Избавляемся от всех неподходящих нам значений
        l.remove(i)

    for i in range(len(l)):  # Делим оставшиешя значение нацело на 2
        l[i] = l[i] // 2

# Словари.


# Если ключ key есть в словаре d, то добавьте значение value в список, который хранится
# по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
# Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь и сопоставить
# ему список из переданного элемента [value].
def update_dictionary(d, key, value):
    # put your python code here
    if key in d:
        d[key].append(value)
        # print('ключ есть')
    elif key is not d:
         # d[2*key]=[]
        if 2 * key is d:
            d[2 * key].append(value)
            # print('ключ 2*key уже есть')
        elif (2 * key is not d) and d.get(2 * key) == None:
            d[2 * key] = []
            d[2 * key].append(value)
             # print('создание ключа и + новое значение списка')
        elif (2 * key is not d) and d.get(2 * key) != None:
            d[2 * key].append(value)
            # print('создание ключа и + значение списка')
    return

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}


# или
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key not in d:
        if 2*key in d:
            d[2*key].append(value)
        elif 2*key not in d:
            d[2*key] = []
            d[2*key].append(value)
    return

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)



# или
def update_dictionary(d, key, value):
    key += key * (key not in d)
    d[key] = d.get(key, []) + [value]



# или
def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]

# Напишите программу, которая считывает строку с числом nn, которое задаёт количество чисел, которые нужно считать.
# Далее считывает n строк с числами x_i, по одному числу в каждой строке. Итого будет n+1 строк.
# При считывании числа x_i программа должна на отдельной строке вывести значение f(x).
# Функция f(x) уже реализована и доступна для вызова.
# Функция вычисляется достаточно долго и зависит только от переданного аргумента xx.
# Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
dict={}
for i in range(int(input())):
    x=int(input())
    if x in dict:
        print(dict[x])
    else:
        dict[x]=f(x)
        print(dict[x])

#
a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}
for i in a:
    print(b[i])

#
cache = {}

for _ in range(int(input())):
    x = int(input())
    if x not in cache:
        cache[x] = f(x)

    print(cache[x])


