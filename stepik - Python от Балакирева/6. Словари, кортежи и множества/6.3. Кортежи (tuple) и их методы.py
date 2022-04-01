# Кортежи (tuple) и их методы
# Кортеж - это упорядоченная, но неизменяемая коллекция произвольных данных
a = 1, 2
print(a)
b = 1,
print(b)
c = (1,)
print(c, type(c))
f = (1)
print(f, type(f))

# Распаковка кортежа
print("Распаковка кортежа")
x, y = (1, 2)
print(x, y)

x, *y = (1, 2, 3)
print(x, y)

x, y = ["hello", "Python"]
print(x, y)

a, b = "ra"
print(a, b)

a = (1, 2, 3)
print(len(a))

# Доступ к значению по индексу
print("Доступ к значению по индексу")
print(a[0])
print(a[1:2])
print(a[:2])

# Использование в качестве ключей словарей
print("Использование в качестве ключей словарей")
d = {}
d[a] = "кортеж"
print(d)


lst = [1, 2, 3]
a = (1, 2, 3)
print(lst.__sizeof__())
print(a.__sizeof__())

# Создание пустого кортежа
print("Создание пустого кортежа")
a = ()
print(a)
b = tuple()
print(b)
a = a + (1, )
print(a)

a = (2, 3) + a
print(a)

# Вложенные кортежи
print("Вложенные кортежи")
a += (("a", "hello"))
print(a)
a += (("a", "hello"), ) # запятая обязательна!!!!
print(a)

print((0, ) * 10)
print(("hello", "world") * 10)

a = tuple([1, 2, 3])
print(a)

a = tuple("hello")
print(a)

a = list(a)
print(a)

# Изменение кортежа через список
print("Изменение кортежа через список")
a = (True, [1, 2, 3], 'hello', 5, {'house': "дом"})
print(a[1])
a[1].append('5') # список внутри кортежа изменять можно!!!
print(a)

# Метод tuple.count(значение) - возвращает число найденных элементов с указанным значением
print("Метод tuple.count(значение)")
a = ("abc", 2, [1, 2], True, 2, 5)
print(a.count("abc"))
print(a.count(2))
print(a.count('hello'))

# Метод tuple.index(значение[, start[, stop]]) - возвращает индекс первого найденного элемента с указанным значением
# (start и stop - необязательные параметры, индексы начала и конца поиска)
print("Метод tuple.index(значение[, start[, stop]])")
print(a.index(2))
print(a.index(2, 2))
# print(a.index(2, 2, 3)) # получим ошибку
print(a.index(2, 2, 5))
print(3 in a)
print([1, 2] in a)


# Подвиг 3. Имеется кортеж:
# t = (3.4, -56.7)
# Вводится последовательность целых чисел в одну строчку через пробел. Необходимо их добавить в кортеж t.
# Результат вывести на экран командой:  print(t)
t = (3.4, -56.7)
k = tuple(map(int, input().split()))
print(t + k)

#
t = (3.4, -56.7)
print(t + tuple(map(int, input().split())))

# Подвиг 4. Вводятся названия городов в одну строку через пробел. На их основе формируется кортеж.
# Если в этом кортеже нет города "Москва", то следует его добавить в конец кортежа. Результат вывести на экран
# в виде строки с названиями городов через пробел.
k = tuple(map(str, input().split()))
if not "Москва" in k:
    k += ("Москва",)
print(*k)

#
t = tuple(input().split())
t = t + ('Москва',) if 'Москва' not in t else t
print(*t)

#
cities = tuple(input().split())

if "Москва" not in cities:
    cities += ("Москва",)

print(*cities)







