# Словари (dict). Базовые операции над словарями.
d = {"house": "дом",
     "car": "машина",
     "tree": "дерево",
     "road": "дорога",
     "river": "река"}

print(d)

print(d["house"])

# dict(ключ1=значение1, ключ2=значение2, ...)
# ключи должны быть строками и записываются без кавычек
s = dict(one=1, two=2, three="3", foure="4")
print(s)

# Преобразование списка в словарь
print("Преобразование списка в словарь")
lst = [[2, "неудовлетворительно"], [3, "удовлетворительно"], [4, "хорошо"], [5, "отлично"]]
print(dict(lst))

# Создание пустого словаря
print("Создание пустого словаря")
d = dict()
print(d)

d[True] = "Истина"
d[False] = "Лож"
print(d)
d[True] = 1
print(d)

print(len(d))

# В качетсве ключей - только неизменяемый тип данных,
# в качестве значение - любой тип данных
d = {True: 1, False: "Ложь", 'list': [1, 2, 3], 5: 5}
print(d)

# Число элементов в словаре - len()
print("Число элементов в словаре - len()")
print(len(d))

# Удаление пары ключ-значение по ключу
print("Удаление пары ключ-значение по ключу")

del d[True]
print(d)

print(True in d)
print(True not in d)

# Проверить, есть ли ключ в словаре - in
print("Проверить, есть ли ключ в словаре - in")
print("abc" in d)
print("list" in d)


# Подвиг 3. Вводятся данные в формате ключ=значение в одну строчку через пробел. Значениями здесь являются целые
# числа (см. пример ниже). Необходимо на их основе создать словарь d с помощью функции dict() и вывести его
# на экран командой:
# print(*sorted(d.items()))
l = [i.split("=") for i in input().split()]
s = [[s[0], int(s[1])] for s in l]
d = dict(s)
print(*sorted(d.items()))

#
lst_in = input().split()
lst = [[i.split('=')[0], int(i.split('=')[1])] for i in lst_in]
d = dict(lst)
print(*sorted(d.items()))

#
d = dict(c.split('=') for c in input().split())
for c in d:
  d[c] = int(d[c])
print(*sorted(d.items()))

# В данном случае в функцию dict() передаются списки вида:
# ['one', '1'], ['two', '2'], ...
# Посмотри в документации как работает эта функция. Она делает ключом ПЕРВЫЙ элемент переданной пары ключ-значение,
# а значением - ВТОРОЙ элемент этой пары. Если бы списки, переданные в функцию, были вот такими - ['1', 'one'], то
# ключами бы стали '1', '2' и тд. , а значениями -  'one', 'two' и тд. Таким образом, функция dict() вернула словарь,
# где ключами служат именно 'one', ... :
# {'one': '1', 'two': '2', 'three': '3'}
# Ну а дальше мы просто идем циклом по словарю (словари по умолчанию итерируются по ключам), в переменную цикла
# попадает ключ, в блоке кода цикла обращаемся по ключу к значению этого ключа и преобразуем его к целому числу,
# как просят в условии задачи.


#
s = input().split()
d = {}
for x in s:
    x = x.split('=')
    d[x[0]] = int(x[1])

print(*sorted(d.items()))

#
print(*sorted({x.split('=')[0]: int(x.split('=')[1]) for x in input().split()}.items()))

#
print(*sorted({k: int(v) for pair in input().split() for k, v in [pair.split('=')]}.items()))

#
d = dict([[i.split('=')[0], int(i.split('=')[1])] for i in input().split()])
print(*sorted(d.items()))

# Подвиг 4. На вход программы поступают данные в виде набора строк в формате:
# ключ1=значение1
# ключ2=значение2
# ...
# ключN=значениеN
# Ключами здесь выступают целые числа (см. пример ниже). Необходимо их преобразовать в словарь d
# (без использования функции dict()) и вывести его на экран командой:
# print(*sorted(d.items()))
lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
d = dict((int(x.split("=")[0]), x.split("=")[1])for x in lst_in)
print(*sorted(d.items()))

#
d = {}
for i in lst_in:
    key, value = i.split('=')
    d[int(key)] = value
print(*sorted(d.items()))

#
lst = [i.split('=') for i in lst_in]
d = {int(i): v for i, v in lst}
print(*sorted(d.items()))

# Подвиг 5. Вводятся данные в формате ключ=значение в одну строчку через пробел. Необходимо на их основе создать словарь,
# затем проверить, существуют ли в нем ключи со значениями: 'house', 'True' и '5' (все ключи - строки). Если все они
# существуют, то вывести на экран ДА, иначе - НЕТ.
d = dict([i.split("=") for i in input().split()])
if 'house' in d and 'True' in d and '5' in d:
    print("ДА")
else:
    print("НЕТ")

#
d = dict([i.split('=') for i in input().split()])
print('ДА' if 'house' in d and 'True' in d and '5' in d else 'НЕТ')

#
d = dict([i.split('=') for i in input().split()])
check_values = ['house', 'True', '5']

for i in check_values:
    if i not in d:
        print('НЕТ')
        break
else:
    print('ДА')

#
d = dict((c.split('=') for c in input().split()))
print(('НЕТ', 'ДА')[all(['house' in d, 'True' in d, '5' in d])])

#
d = dict([i.split('=') for i in input().split()])
print(('НЕТ', 'ДА')['house' in d and 'True' in d and '5' in d])

# Подвиг 6. Вводятся данные в формате ключ=значение в одну строчку через пробел. Необходимо на их основе создать
# словарь d, затем удалить из этого словаря ключи 'False' и '3', если они существуют. Ключами и значениями словаря
# являются строки. Вывести полученный словарь на экран командой:
# print(*sorted(d.items()))
d = dict([i.split("=") for i in input().split()])
if "False" in d:
    del d["False"]

if "3" in d:
    del d["3"]
print(*sorted(d.items()))

#
d = dict([i.split('=') for i in input().split()])
del_values = ['False', '3']

for i in del_values:
    if i in d:
        del d[i]

print(*sorted(d.items()))

#
d = dict(pair.split('=') for pair in input().split())
for key in ('False', '3'):
    d.pop(key, 'Да не очень то и надо')
print(*sorted(d.items()))

#
print(*sorted(dict([i.split("=") for i in input().split() if i.split("=")[0] not in ('False', '3')]).items()))


