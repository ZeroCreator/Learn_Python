# Функция range и итерируемые объекты.
# С помощью функции rande() можно сформировать конечную арифметическую прогрессию.
# ITERABLE (ИТЕРИРУЕМЫЙ) - объект, предоставляющий возможность поочередного прохода по своим элементам.
print(range(5))
print(type(range(5)))
print(list(range(5)))

print(list(range(0)))

print(list(range(-6)))

#
print('Последовательность диапазона:')
print(list(range(10, 21)))

#
print('Изменение шага:')
print(list(range(10, 100, 10)))
print(list(range(1, 100, 10)))

#
print('Убывающая последовательность:')
print(list(range(10, 0, -1)))

#
print('От 0 до 100 только четные:')
print(list(range(0, 100, 2)))

#
print('Нахождение суммы арифметической прогрессии:')
print(sum(range(1, 101)))

#
print('Нахождение количества элементов последовательности:')
print(len(range(5, 15, 5)))

#
print('Функция множественного присвоения:')
a, b, c = range(5, 8)
print(a, b, c)

#
print('Сохранение результата функции в переменную:')
r = range(1, 7)
print(len(r))
print(r[1])

#
print('Создание итератора - функция iter():')
v = iter(range(5))
print(v)
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))

# OR
v = iter(range(5))
print(v.__next__())
print(v.__next__())
print(v.__next__())
print(v.__next__())
print(v.__next__())

#
print('Создание итератора от списка:')
n = iter([43, True, 'Hello'])
print(next(n))
print(next(n))
print(next(n))

m = iter('hi')
print(next(m))
print(next(m))

#
print('Tasks')
# Допишите программу так, чтобы она печатала на экран список, содержащий
# последовательность чисел 0,1,2,3,4,5,6,7,8,9
print(list(range(10)))

# Теперь необходимо передать в функцию range параметры, чтобы получилась
# последовательность чисел от 12 до 34 включительно
print(list(range(12, 35))

# Теперь давайте добавим шаг. Необходимо сформировать последовательность
# 25, 33, 41, 49, 57 .... , 169
print(list(range(25, 170, 8)))

# Сформируйте последовательность -11, -12, -13, -14 .... , -35
print(list(range(-11, -36, -1)))

# Сформируйте последовательность 10, 9, 8, 7, ... , 0
print(list(range(10, -1, -1)))

# И последняя последовательность 1000, 950, 900, 850, ... , 50
print(list(range(1000, 450, -50)))
