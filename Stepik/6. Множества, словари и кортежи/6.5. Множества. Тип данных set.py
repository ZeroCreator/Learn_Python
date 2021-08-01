# Множества. Тип данных set.
# Множество (set) - неупорядоченная коллекция уникальных элементов (отсутствуют повторяющиеся значения).
# Множество состоит из элементов неизменяемых объектов: чисел, строк, кортежей.
# 1. Создание множества:
print('1. Создание множества:')
a = {1, 2, 3, 1, 2, 1, 3, 4}
b = {'hi', 'ha', 'hi', 'ha', 'ho', 'he', 'ho'}
print(a, type(a))
print(b, type(b))

print('С помощью функции set():')
c = set('abc')
print(c)

print('Создание множества из строки:')
d = set('abracadabra') # Функция set() разбивает строку на символы и создает из них множество. При этом исключаются дубли.
print(d)

print('Создание множества из списка:')
d = set([1, 2, 3, 4, 3, 2, 1])
print(d)

print('Создание множества из функции range():')
e = set(range(5))
print(e)

print('Создание пустого множества:')
f = set()
print(f, type(f))

print('Исключение всех дублей из списка:')
a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
a = list(set(a))
print(a, type(a))

# 2. Добавление элемента в множество:
print('2. Добавление элемента в множество:')
print('2.1. Метод .add():')
a = {54, 32, 54, 3, 4, 2,}
print(a)
a.add(9)
a.add(4) # Ничего не поменяется в множестве.
print(a)

a = a.add(9) # Потеряем все значения.
print(a)

print('2.2. Метод .update():')
a = {54, 32, 54, 3, 4, 2,}
# Итерабельный объект - список:
print('Итерабельный объект - список:')
a.update([5, 6, 7]) # Добавляет итерабельный элемент не целиком, а поэлементно.
# Это тоже самое что:
# a.add(5)
# a.add(5)
# a.add(7)
print(a)

# Итерабельный объект - строка:
print('Итерабельный объект - строка:')
a.update('hello')
print(a)

# Итерабельный объект - функция range():
print('Итерабельный объект - функция range():')
a.update(range(5, 10))
print(a)

# Итерабельный объект - множество:
print('Итерабельный объект - множество:')
a.update({11, 12, 13})
print(a)

# 3. Удаление элемента из множества:
print('3. Удаление элемента из множества:')
# 3.1. метод .discard():
print('3.1. метод .discard():')
a.discard(4) # Удаляем 4
a.discard(4) # Ошибки не будет
print(a)

# 3.2. метод .remove():
print('3.2. метод .remove():')
a.remove(2)
# a.remove(2) # Будет ошибка

# 3.3. метод .pop():
print('3.3. метод .pop():')
# Удаляться будет случайный элемент:
print(a.pop()) # Возвратит удаляемый элемент
print(a)

# 3.4. метод .clear():
print('3.4. метод .clear():')
# Очищает все элементы множества
a.clear()
print(a)

# 4. Операции над множествами:
print('. Операции над множествами:')
# 4.1. Нахождение длины множества - функция len():
print('4.1. Нахождение длины множества - функция len():')
a = {54, 32, 54, 3,4,2}
print(len(a))
# 4.2. Принадлежит ли элемент множеству - in:
print('4.2. Принадлежит ли элемент множеству - in:')
print(4 in a, 100 in a, 50 not in a)
