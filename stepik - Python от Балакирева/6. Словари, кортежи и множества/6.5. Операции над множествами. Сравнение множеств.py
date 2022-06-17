# Операции над множествами. Сравнение множеств
# пересечения &
# объединения |
# вычетания -
# симметричная разность ^


# пересечения & - общие элементы для двух множеств
print("пересечения & - общие элементы для двух множеств")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
print(setA & setB) # новое множество
print(setA)
print(setB)
rez = setA & setB
print(rez)
setA &= setB
print(setA)
setA = {1, 2, 3, 4}
setC = {9, 10, 11}
print(setA & setC)

# Метод setA.intersection(setB)
print("Метод setA.intersection(setB)")
print(setA.intersection(setB))

# Метод setA.intersection_update(setB)
print("Метод setA.intersection_update(setB)")
setA.intersection_update(setB)
print(setA)


# объединение множеств |
print("объединение множеств |")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
print(setA | setB) # новое множество
print(setA)
print(setB)

setA |= setB
print(setA)

# Метод setA.union(setB)
print("Метод setA.union(setB)")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
print(setA.union(setB))

# вычетание одного множества из другого -
print("вычетание одного множества из другого -")
# setA - setB и setB - setA
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
print(setA - setB)
print(setB - setA)
print(setA)
print(setB)

setA -= setB
print(setA)

# симметричная разность ^ - исключаются общие элементы
print("симметричная разность ^ - исключаются общие элементы")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
print(setA ^ setB)

# Сравнение множеств между собой
print("Сравнение множеств между собой")
setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5, 6, 7}
print(setA == setB)
print(setA != setB)

setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5}

print(setB < setA)
print(setB > setA)

setB.add(22)
print(setB < setA)
print(setB > setA)

setA = {7, 6, 5, 4, 3}
setB = {3, 4, 5, 6, 7}
print(setB < setA)
print(setB > setA)

print(setB <= setA)

# Подвиг 1. Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел).
# Необходимо выбрать и отобразить на экране уникальные числа, присутствующие и в первом и во втором списках одновременно.
# Результат выведите на экран в виде строки чисел, записанных по возрастанию через пробел, используя команду
# (здесь s - это множество): print(*sorted(s))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
rez = setA & setB
print(*sorted(rez))

#
print(*sorted(set(input().split()) & set(input().split()), key=int))

#
print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))

#
print(*sorted(map(int, set(input().split()) & set(input().split()))))

#
print(*sorted(set(map(int, input().split())).intersection(set(map(int, input().split())))))

# Подвиг 2. Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел).
# Необходимо выбрать и отобразить на экране уникальные числа, присутствующие в первом списке, но отсутствующие во втором.
# Результат выведите на экран в виде строки чисел, записанных по возрастанию через пробел.
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
rez = setA - setB
print(*sorted(rez))

#
a, b = [set(map(int, input().split())) for i in range(2)]
print(*sorted(a-b))

#
print(*sorted(set(map(int, input().split())) - set(map(int, input().split()))))

#
print(*sorted(set(map(int, input().split())).difference(set(map(int, input().split())))))


# Подвиг 3. Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел).
# Необходимо выбрать и отобразить на экране уникальные числа, присутствующие в первом или втором списках, но
# отсутствующие одновременно в обоих. Результат выведите на экран в виде строки чисел, записанных по возрастанию
# через пробел.
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
rez = setA ^ setB
print(*sorted(rez))

#
print(*sorted(map(int, set(input().split()) ^ set(input().split()))))

#
a, b = [set(map(int, input().split())) for i in range(2)]
print(*sorted(a^b))

# Подвиг 4. Вводятся два списка городов каждый с новой строки (в строке названия через пробел). Необходимо сравнить их
# между собой на равенство по уникальным (не повторяющимся) городам. Если списки содержат одни и те же уникальные города,
# то вывести на экран ДА, иначе - НЕТ.
a = set(map(str, input().split()))
b = set(map(str, input().split()))
print(["НЕТ", "ДА"][a == b])

#
print(('НЕТ', 'ДА')[set(input().split()) == set(input().split())])

#
print('ДА' if set(input().split()) == set(input().split()) else 'НЕТ')

#
a=set(input().split())
b=set(input().split())
s=a.intersection(b)
print('ДА' if a==b else 'НЕТ')

# Подвиг 5. Вводится список оценок студента - его ответов у доски по предмету "Информатика" в виде чисел от 2 до 5 в
# одну строку через пробел. Если студент имеет хотя бы одну двойку, то он не допускается до экзамена.
# Определить на основе введенного списка, допущен ли студент. Если допущен, то вывести слово ДОПУЩЕН, иначе - НЕ ДОПУЩЕН.
# При реализации задачи используйте множество для определения наличия двойки.
s = list(map(int, input().split()))
print(["НЕ ДОПУЩЕН", "ДОПУЩЕН"][2 not in set(s)])

#
print(['ДОПУЩЕН', 'НЕ ДОПУЩЕН'][2 in set(map(int, input().split()))])

# Подвиг 6. Вводятся два списка городов каждый с новой строки (в строке названия через пробел), которые объехал
# Сергей в 1-й и 2-й годы своего путешествия по России. Требуется определить, включал ли его маршрут во 2-й год все
# города 1-го года путешествия? Если это так, то вывести ДА, иначе - НЕТ.
a = set(map(str, input().split()))
b = set(map(str, input().split()))
print(["НЕТ", "ДА"][b >= a])

#
sp1 = set(input().split())
sp2 = set(input().split())
print(['НЕТ', 'ДА'][sp1.issubset(sp2)])

#
s1 = set(input().split())
s2 = set(input().split())

print('ДА' if s1 <= s2 else 'НЕТ')

# Подвиг 7. Вводится натуральное число, которое может быть определено простыми множителями 1, 2, 3, 5 и 7.
# Необходимо разложить введенное число на указанные простые множители и проверить, содержит ли оно множители
# 2, 3 и 5 (все указанные множители)? Если это так, то вывести ДА, иначе - НЕТ.
x = int(input())
t = {1, 2, 3, 5, 7}
t1 = {1, 2, 3, 5}
s = {1}

for i in t:
    if x % i == 0:
        s.add(i)

print(("НЕТ", "ДА")[s >= t1])

#
print('НЕТ' if int(input()) % 30 else 'ДА')

#
print(('НЕТ', 'ДА')[int(input()) % 30 == 0])

#
print(("НЕТ", "ДА")[not int(input()) % 30])








