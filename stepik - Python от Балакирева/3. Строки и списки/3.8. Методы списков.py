# Методы списков
a = [1, -54, 3, 23, 43, -45, 0]
print("Добавление одного элементав в конец списка - метод lst.append()")
a.append(100)
print(a)

a.append(True)
print(a)

a.append([1, 2, 3])
print(a)

print("Вставление элемент в указанное место списка - метод lst.insert()")
a.insert(3, -100)
print(a)

print("Удаление элемент по значению - метод lst.remove()")
a.remove(True)
print(a) # Удаляет первое значение 1 !!!!!!!!
a.remove(True)
print(a)

print("Удаление элемент из списка по индексу- метод lst.pop()")
v = a.pop()
print(v)
print(a)

v1 = a.pop(3)
print(v1)
print(a)


print("Очистить список - метод lst.clear()")
print("Создание копии списка - метод lst.copy()")
c = a.copy()
print(c)
c.clear()
print(c)
print(a)

print("Возвращает число элементов с указанным значением - метод lst.count()")
print(a.count(1))
a.append(1)
print(a.count(1))
a.append(True)
print(a.count(1))

print("Возвращает индекс первого найденного элемента - метод lst.index()")
print(a.index(1))
print(a.index(-54))
print(a.index(1, 2))

print("Меняет порядок следования элементов на обратный - метод lst.reverse()")
a.reverse()
print(a)

print("Сортировка значений списка по возрастанию  - метод lst.sort()")
a.sort()
print(a)

# Отличие метода lst.sort() от функции sorted() - метод меняет список и ничего не возвращает (None).
# Функция не меняет список, а возвращает отсортированный список. Изначальный список остается неизменным.
c = [1, 0, -45, 43, 23, 3, -54, 1]
a = sorted(c)
print(a)
print(c)
c.sort()
print(c)

c.sort(reverse=True)
print(c)

lst = ["Москва", "Санкт-Петербург", "Тверь", "Казань"]
lst.sort()
print(lst)

# Подвиг 2. Вводится строка из целых чисел через пробел. Если первое число не равно последнему, то нужно добавить
# значение True, а иначе - значение False. Результирующий список lst вывести на экран командой:
# print(*lst)
# Реализовать задачу без использования условных операторов.
lst = list(map(int, input().split()))
lst.append(lst[0] != lst[-1])
print(*lst)

#
nums = input()
print(nums, nums[0] != nums[-1])

#
a = list(map(int, input().split()))
a.append([False, True][a[0] != a[-1]])
print(*a)

#
lst = list(map(int, input().split()))
print(*lst, lst[0] != lst[-1])

#
[print(*i, i[0] != i[-1]) for i in [input().split()]]

#
(lambda lst: print(*lst, lst[0] != lst[-1]))(input().split())

# Подвиг 4. Вводится строка с номером телефона в формате:
# +7(xxx)xxx-xx-xx
# Необходимо преобразовать ее в список lst (посимвольно, то есть, элементами списка будут являться отдельные символы
# строки). Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы. Отобразить полученный список на экране командой:
# print("".join(lst))
# Sample Input:
# +7(912)123-45-67
# Sample Output:
# 8(912)1234567
lst=list(input())
lst.remove("+")
lst[0] = "8"
lst.remove("-")
lst.remove("-")
print("".join(lst))

#
print(input().replace('+7', '8').replace('-', ''))

#
lst = list(input().replace('-', ''))
lst.remove('+')
lst[0] = '8'
print("".join(lst))

#
print(input().replace('+7', '8').replace('-', ''))

# Подвиг 5. В одну строчку через пробел вводятся: имя, отчество и фамилия. Необходимо представить эти данные в виде
# новой строки в формате: Фамилия И.О. (Например, Сергей Михайлович Балакирев -> Балакирев С.М.).
fio = list(input().split())
print(fio[2], fio[0][0]+"." + fio[1][0]+".")

#
name = input().split()
print(f"{name[-1]} {name[0][0]}.{name[1][0]}.")

# Подвиг 7. Вводятся целые числа в одну строчку через пробел (не менее четырех). Необходимо найти три наименьших числа
# в этой последовательности чисел и вывести их на экран в порядке возрастания. Реализовать программу без использования
# условного оператора.
lst = list(map(int, input().split()))
a = min(lst)
lst.remove(a)
b = min(lst)
lst.remove(b)
c = min(lst)
print(*sorted([a, b, c]))

#
lst = list(map(int, input().split()))
print(*sorted(lst)[0:3])

#
print(*sorted(map(int, input().split()))[:3])

# Подвиг 8. Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать их в список lst , затем, удалить
# последнее значение и если оно нечетное, то в список (в конец) добавить True, иначе - False. Отобразить полученный
# список на экране командой:
# print(*lst)
lst = list(map(int, input().split()))
a = lst.pop()
lst.append(a%2!=0)
print(*lst)

#
lst = list(map(int, input().split()))
lst.append(lst.pop() % 2 != 0)
print(*lst)

#
lst = list(map(int, input().split()))
lst[-1] = lst[-1] % 2 != 0
print(*lst)

# Подвиг 9. Вводятся оценки студента (числа от 2 до 5) в одну строку через пробел. Необходимо определить количество
# двоек и вывести это значение на экран.
lst = list(input().split())
print(lst.count("2"))

#
print(input().split().count('2'))

# Подвиг 10. Вводятся названия рек в одну строчку через пробел. Необходимо все их отсортировать по именам
# (по возрастанию) и в отсортированном списке удалить первый элемент. Результат отобразить на экране в одну
# строчку через пробел.
lst = list(input().split())
lst.sort()
lst.pop(0)
print(*lst)

#
print(*sorted(input().split())[1:])

#
lst = sorted(input().split())
lst.pop(0)
print(*lst)


