# Функция isinstance для проверки типов данных с учетом иерархии наследования объектов.
# isinstance(объектб тип данных)
# True - если объект соответствует указанному типу
# False -  если не соответствует
a = 5
print(isinstance(a, int))
print(isinstance(a, float))

b = True
# тип bool наследуется от типа int
print(isinstance(b, bool))
print(isinstance(b, int))

# type - делает строгую проверку:
print("type - делает строгую проверку:")
print(type(b) == bool)
print(type(b) == int)

print(type(b) is bool)

# Множественная проверка соответствия через кортеж:
print("Множественная проверка соответствия через кортеж:")
print(type(b) in (bool, float, str))

data = (4.5, 8.7, True, "книга", 8, 10, -11, [True, False])
# s = 0
# for x in data:
#     if isinstance(x, float):
#         s += x
# print(s)

s = sum(filter(lambda x: isinstance(x, float), data))
print(s)

t = sum(filter(lambda x: type(x) is int, data))
print(t)

#
print("Tasks")
# Определите функцию с именем get_add, которая складывает или два числа или две строки (но не число со строкой) и
# возвращает полученный результат. Если сложение не может быть выполнено, то функция возвращает значение None.
# Сигнатура функции должна быть, следующей:
# def get_add(a, b): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
def get_add(a, b):
    if type(a) in (int, float) and type(b) in (int, float) or type(a) is str and type(b) is str:
        return a + b


#  Определите функцию с именем get_sum, которая принимает на входе итерируемый объект (список, строку, кортеж, словарь,
#  множество) и вычисляет сумму только целых чисел, взятых из элементов итерируемого объекта. Вычисленная сумма
#  возвращается функцией. Если целых чисел нет, то возвращается 0.
# Сигнатура функции должна быть, следующей:
# def get_sum(it): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
def get_sum(it):
    return sum(filter(lambda x: type(x) is int, it)) if any(type(i) == int for i in it) else 0

print(get_sum(4.5, 8.7, True, "книга", 8, 10, -11, [True, False]))

#
def get_sum(it):
    return sum(filter(lambda x: type(x) == int, it))

#
def get_sum(lst):
    return sum(x for x in lst if isinstance(x, int) and not isinstance(x, bool))


# Определите функцию с именем get_even_sum, которая принимает на входе итерируемый объект (список, строку, кортеж,
# словарь, множество) и вычисляет сумму только целых четных чисел, взятых из элементов итерируемого объекта.
# Результат возвращается функцией. Если целых чисел нет, то возвращается 0.
# Сигнатура функции должна быть, следующей:
# def get_even_sum(it): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
def get_even_sum(it):
    s = []
    for i in it:
        if type(i)==int:
            s.append(i)
    return sum(filter(lambda x: x % 2 == 0, s))

#
def get_even_sum(it):
    return sum(filter(lambda x: type(x) == int and x % 2 == 0, it))

#
def get_even_sum(it):
    return sum(x for x in it if isinstance(x, int) and not isinstance(x, bool) and x % 2 == 0)


#
get_even_sum = lambda a: sum(i for i in a if type(i) is int and i % 2 == 0)


# Определите функцию с именем get_list_dig, которая возвращает список только из числовых значений переданной ей
# коллекции (список или кортеж).
# Сигнатура функции должна быть, следующей:
# def get_list_dig(lst): ...
# Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
# P. S. Не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
def get_list_dig(lst):
    return list(filter(lambda x: type(x) in (int, float), lst))

print(get_list_dig([4.5, 8.7, True, "книга", 8, 10, -11, [True, False]]))

#
def get_list_dig(it):
    return list(filter(lambda x: type(x) in (int, float), it))

#
def get_list_dig(it):
    return list(filter(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), it))

#
def get_list_dig(lst):
    return [x for x in lst if type(x) in (int, float, complex)]

