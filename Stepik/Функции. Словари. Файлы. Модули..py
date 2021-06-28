def f(n):
    return n * 10 + 5
print(f(f(f(10))))

# range:
def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res

print(my_range(2, 5))
print(my_range(2, 15, 3))
print(my_range(15, 2, -3))

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




