# Словари (dict). Операции и методы словаря.
# Словарь - неупорядоченная коллекция произвольных объектов с доступом по ключу.
# Словать - это ассоциативный список (ассоциативный массив).
a = ['moskva', 'piter', 'penza']
# ассоциации:
#'mockva' - 495,
#'piter' - 812,
#'penza' - 8412

# Элемент словаря - ключ-значение:
# 1. Способ создания словаря:
d = {
    #key:value # пара ключ-значение - элемент словаря
    'mockva': 495,
    'piter': 812,
    'penza': 8412
}
print(d)

# 2. Способ создания словаря - с помощью функции dict()
# (если в качестве ключей используются строковые типы):
r = dict(moskva=495, piter=812, penza=8412)
print(r)

# 3. Способ создания словаря - через вложенные списки:
a = [['moskva', 495], ['piter', 812], ['penza', 8412]]
t = dict(a)
print(t)

# 4. Способ создания словаря - если необходимо проинециализировать список ключей каким-то одним значением
q = dict.fromkeys(['a', 'b', 'c'])
print(q)

q = dict.fromkeys(['a', 'b', 'c'], 100)
print(q)

q = dict.fromkeys(['a', 'b', 'c'], [100, 200, 300])
print(q)

# 5. Способ создания словаря - пустой словать:
# 5.1
v = {}
print(v, type(v))

# 5.2
s = dict()
print(v, type(v))

# Ключем может быть строка и число (ключем не может быть изменяемый объект, допустим список):
d = {
    'mockva': 495,
    'piter': 812,
    'penza': 8412
}
print(d)

d = {
    1: 495,
    2: 812,
    3: 8412
}
print(d)

# Значением могут быть любые типы:
d = {
    1: 45,
    2: 'two',
    3: [1, 2, 3]
}
print(d)

# Обращение к словарю не по индексу, а по ключу:

d = {
    1: 45,
    'hello': 'two',
    3: [1, 2, 3]
}
print(d['hello'])
print(d[3])
print(d[1])

#
print('Добавление значения в словарь -  с помощью присвоения значения новому ключу:')
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}

d[4] = 'four'
print(d)

#
print('Изменение значения ключа:')


d[1] = [1, 2, 3]
print(d)

#
print('Заполнение словаря:')
person = {}
s = 'IVANOV IVAN Samara SGU 5 4 5 5 4 3 5'
s = s.split()

print(s)

person['lastName'] = s[0]
person['firstName'] = s[1]
person['city'] = s[2]
person['univercity'] = s[3]
person['marks'] = []

for i in s[4:]:
    person['marks'].append(int(i))

print(person)

#
print('Удаление значений словаря по ключу:')
del d[1]
print(d)

#
print('Найти длину словарая (количество пар ключ - значение) - функция len():')
print(len(d))

#
print('Наличие ключа - функция in')
print(1 in d, 2 in d, 5 in d)

#
print('Обход ошибки отсутствия ключа:')
if 5 in d:
    print(d[5])
else:
    d[5] = 'five'
print(d)

#
print('Обход словаря в цикле for:')
for key in d:
    print(key, d[key])

#
print('Методы словарей.')
print('1. Очищение словаря - Метод .clear():')
d.clear()
print(d)

#
print('2. Получение значения словаря - Метод .get():')
d = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print(d.get(1))
print(d.get(5, 'No such key'))
print(d.get(5, [1, 2, 3]))              # возвращает значение второго параметра при отсутствии ключа
print(d)

#
print('3. Создание пустого ключа в словаре  и новой пары ключ-значение - Метод .setdefault():')
print(d.setdefault(6))
print(d)

d.setdefault(7, 'seven')
print(d)

#
print('4. Возвращает ключ и удаляет его из словаря - Метод .pop():')
print(d.pop(3))
print(d)

#
print('4. Возвращает пару и удаляет ее из словаря - Метод .popitem():')
print(d.popitem())
print(d)

#
print('5. Получит значение всех ключей словаря - Метод .keys():')
for key in d.keys():
    print(key, d[key])

#
print('6. Получит все значения словаря - Метод .values():')
for value in d.values():
    print(value)

#
print('7. Получит все пары ключ-значения - Метод .items():')
for para in d.items():
    print(para)

for para in d.items():
    print(para[0], para[1])

#
print('Принцип множественного присвоения:')
for key, value in d.items():
    print(key, value)

#
print('Tasks')
# На вход программе поступает целое число n. Вам необходимо создать словарь, который будет включать в себя ключи
# от 1 до n, а значениями соответствующего ключа будет значение ключа в квадрате.
# В качестве ответа выведите полученный словарь
n = int(input())
d = {}
for i in range(1, n + 1):
    d.update({i: i ** 2})
print(d)

#
print({a: a ** 2 for a in range(1, int(input()) + 1)})

#
n = int(input())
print({x: x ** 2 for x in range(1, n + 1)})

#
a = int(input())
rez = {}
for i in range(1, a + 1):
    rez.setdefault(i, i**2)
print(rez)

#
n = int(input())
slovar = {}
for i in range(1, n + 1):
    slovar[i] = i ** 2

print(slovar)

# Напишите программу, которая печатает словарь alphabet, где ключи  - строчные английские символы, а значения -
# порядковые номера букв в алфавите.
# Начало вашего словаря должны быть таким {"a": 1, "b": 2 }
# В качестве ответа распечатайте ключи и значения данного словаря по алфавиту, каждую пару на новой строчке.
# Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:
# from string import ascii_lowercase
# print(ascii_lowercase)
from string import ascii_lowercase

c = 0
alphabet = {}
for i in ascii_lowercase:
    c += 1
    alphabet.setdefault(i, c)

for key, value in alphabet.items():
    print(key, value)

#
from string import ascii_lowercase
alphabet = {ascii_lowercase[i]:i+1 for i in range(len(ascii_lowercase))}
for key, val in alphabet.items():
    print(key, val)

#
alphabet = {chr(x): x - 96 for x in range(97, 123)}
[print(k, v) for k, v in alphabet.items()]

#
from string import ascii_lowercase
alphabet = dict()
for i, c in enumerate(ascii_lowercase, 1):
    alphabet[c] = i

for k, v in alphabet.items():
    print(k, v)

#
s = 'abcdefghijklmnopqrstuvwxyz'
alphabet = {s[a]: a + 1 for a in range(26)}
for key in alphabet:
    print(key, alphabet[key])

#
a ="abcdefghijklmnopqrstuvwxyz"
alphabet = dict()
for i in range(len(a)):
    alphabet[a[i]] = i+1
    print(a[i], i+1)

#
from string import ascii_lowercase
alphabet = {}
for i in range(len(ascii_lowercase)):
    alphabet[ascii_lowercase[i]] = i+1
for k, v in alphabet.items():
    print(k, v)

# Есть два словаря, нужно их объединить в новый словарь rez и вывести его на экран.\
# d1 = {'a': 100, 'b': 200, 'c': 333}
# d2 = {'x': 300, 'y': 200, 'z': 777}
# Sample Output:
# {'a': 100, 'b': 200, 'c': 333, 'x': 300, 'y': 200, 'z': 777}
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
rez = ({**d1 , **d2})
print(rez)

#
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
print({**d1 , **d2})

#
print({'a': 100, 'b': 200, 'c': 333} | {'x': 300, 'y': 200, 'z': 777})

#
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}

rez = dict(list(d1.items()) + list(d2.items()))
print(rez)

#
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
d1.update(d2)
rez = d1
print(rez)

#
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
rez = {}
rez.update(d1)
rez.update(d2)
print(rez)

# Система регистрации
# Система должна работать по следующему принципу. Каждый раз, когда новый пользователь хочет зарегистрироваться, он
# посылает системе запрос name со своим именем. Если данное имя не содержится в базе данных системы, то оно заносится
# туда и пользователю возвращается ответ OK, подтверждающий успешную регистрацию. Если же на сайте уже присутствует
# пользователь с именем name, то система формирует новое имя и выдает его пользователю в качестве подсказки, при этом
# подсказка также добавляется в базу данных. Новое имя формируется по следующему правилу. К name последовательно
# приписываются числа, начиная с единицы (name1, name2, ...), и среди них находят такое наименьшее i, что namei не
# содержится в базе данных сайта.
# Входные данные:
# В первой строке входных данных задано число n (1≤n≤105). Следующие n строк содержат запросы к системе.
# Каждый запрос представляет собой непустую строку длиной не более 32 символов, состоящую только из строчных букв
# латинского алфавита.
# Выходные данные:
# В выходных данных должно содержаться n строк — ответы системы на запросы: OK в случае успешной регистрации, или
# подсказку с новым именем, если запрашиваемое уже занято.
logins = {}
n = int(input())
for i in range(n):
    login = input()
    if login in logins:
        print(f'{login}{logins[login]}')
        logins[login] += 1
    else:
        print('OK')
        logins[login] = 1

#
logins = {}
n = int(input())
for i in range(n):
    name = input()
    if name not in logins:
        logins[name] = 0
        print('OK')
    else:
        logins[name] += 1
        print(name + str(logins[name]))

#
