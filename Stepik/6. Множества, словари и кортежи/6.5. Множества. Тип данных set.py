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

# 4.3. Пересечение множеств:
print('4.3. Пересечение множеств:') # Результат - элементы, которые есть в обоих множествах
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a & b)
a &= b
print(a, b)
c = {10, 11, 12}
print(a & c)
print(a, c)
a &= c
print(a, c)
# Метод .intersection() == '&':
print('Метод .intersection() == "&":')
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a.intersection(b))
print(a, b)

# Метод .intersection_update() = '&':
print('Метод .intersection_update() = "&":')
a.intersection_update(b)
print(a, b)

# 4.4. Объединение множеств:
print('4.4. Объединение множеств:') # Результат - все элементы обоих множеств (Без дублей)
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a | b)
# Это то же, что и метод .union():
print('Метод .union():')
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a.union(b))
print(a)
a = a.union(b)
print(a)
# Это то же самое что:
# a |= b
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
a |= b
print(a)

# 4.5. Вычитание множеств:
print('4.5. Вычитание множеств:') # Результат - из одного множества убираются все пересекающиеся с другим множеством элементы
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a - b)
print(b - a)
print(a, b)
# Чтобы изменить само множество:
b -= a
print(b)

# 4.6. Операция симметричной разности:
print('4.6. Операция симметричной разности:') # Результат  - Все элементы обоих множеств, за исключением их общих элементов
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a ^ b)

# 4.7. Сравнение множеств:
print('4.7. Сравнение множеств:')
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a == b)
c = {4, 3, 2, 1, 2, 3, 4}
d = {3, 4, 4, 4, 2, 1, 3, 2, 2}
print(c == d)

a = {4, 3, 2, 1}
b = {1, 2, 3} # Данное подмножество b является частью множества а
print(a > b)

# 4.8. Элементы множества можно обходить с помощью цикла for:
print('4.8. Элементы множества можно обходить с помощью цикла for:')
a = {4, 3, 2, 1}

for i in a:
    print(i) # Только по значению, так как операция индексирования в множествах не поддерживается.

print('Tasks')
# Сколько всего было уникальных слов в тексте.
# Вводятся строки, пок не введется пустая строка
text = input()
a = set()
while text != '':
    slova = text.split()
    a.update(slova)
    text = input()
print(len(a))

# Даны два списка чисел.
# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
a = set(input().split())
b = set(input().split())
a = a & b
print(*sorted(int(i) for i in a))

#
a = set(map(int, input().split()))
b = set(map(int, input().split()))
c = list(a&b)
print (*sorted(c))

#
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print (*sorted(list(a&b)))

#
a=set(input().split())
b=set(input().split())
a=sorted(a&b,key=int)

print(*a)

#
print(*sorted(set(input().split()) & set(input().split()), key=int))

#
print(*sorted(map(int, set(input().split()) & set(input().split()))))

# Даны два списка чисел. Выведите все числа в порядке возрастания, которые входят в первый список, но при этом
# отсутствуют во втором.
print(*sorted(map(int, set(input().split()) - set(input().split()))))

#
a,b = set(input().split()), set(input().split())
print(*sorted(a - b))

#
print(*sorted(list(set(int(i) for i in input().split()) - set(int(i) for i in input().split()))))

#
print(*sorted(set(input().split()) - set(input().split()), key=int))

# Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше одного раза.
# Входные данные:
# Входная строка может содержать содержит цифры, пробелы и латинские буквы.
# Выходные данные:
# Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся во входной строке больше
# одного раза. Если таких цифр нет, нужно вывести слово 'NO'.
a = input()
b = [int(i) for i in a if i.isdigit()]
c = sorted(set([i for i in b if b.count(i) > 1]))
if len(c) == 0:
    print("NO")
else:
    print(*c)

#
a = [i for i in input() if i.isdigit()]
a = sorted(set([i for i in a if a.count(i) > 1]))
print(*a + ['NO'][len(a):])

#
lst = list(input())
set123 = set()
for i in lst:
    if i.isdigit() and lst.count(i)>1:
        set123.add(int(i))
if len(set123) != 0:
    print(*sorted(set123))
else:
    print('NO')

#
count = [0] * 10
for ch in input():
    if ch.isdigit():
        count[int(ch)] += 1
res = [d for d in range(10) if count[d] > 1]
print(*res or ['NO'])

#
s = input()
print(*[*sorted(set([t for t in s if t.isdigit() and s.count(t) > 1]))] if [*sorted(set([t for t in s if t.isdigit() and s.count(t) > 1]))] else ['NO'])

#
s = [int(i) for i in input() if i.isdigit()]
d = set(s)

for i in d:
    s.remove(i)
if s:
    print(*sorted(set(s)))
else:
    print("NO")

#
str = input()
c = set()

for i in str:
  if i.isdigit() and str.count(i) > 1:
    c.add(i)

print (*sorted(c) if c else ["NO"])

#
s = input()
s = set(i for i in s if i.isdigit() and s.count(i)>1)
print(*['NO']if not s else sorted(s,key=int))

#
a = input()
s = []
for i in range(10):
    if a.count(str(i)) > 1:
        s.append(i)
print(*s or ["NO"])

#
s, a = set(), input()
[s.add(_) for _ in a if _.isdigit() and a.count(_) > 1]
print(*sorted(s) if s else ['NO'])

