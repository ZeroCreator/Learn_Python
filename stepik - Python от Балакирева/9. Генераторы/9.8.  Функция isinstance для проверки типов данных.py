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

