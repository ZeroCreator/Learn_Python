# Генераторы списков. List comprehension.
# шаблон для заполнения списка:
# [выражение for val in коллекция]
a = [0 for i in range(7)]
print(a)

a = [i for i in range(10)]
print(a)

a = [i**2 for i in range(10)]
print(a)

a = [i % 4 for i in range(1, 15)]
print(a)

# итерабельный объект - строки
a = [i for i in 'hello']
print(a)

a = [i*5 for i in 'hello']
print(a)

# функции
a = [ord(i) for i in 'abcd']
print(a)

import random
a = [random.randint(-10, 10) for i in range(10)] # Возвращает указанное число в случайном диапазоне:
print(a)
b = [abs(elem) for elem in a]
print(b)

# Изменить значение элементов первоначального списка:
a = [elem + 1 for elem in a]
print(a)

# Условные конструкции:
# [выражение for val in коллекция if условие]
b = [elem for elem in a if elem % 2 == 0] # В списке только четные элементы
print(b)

b = [elem for elem in a if elem % 2 == 0 and elem % 3 == 0]
print(b)

# Ввод нескольких чисел через пробел в одну строку:
a = input('Ведите числа: ').split() # Строка, разделенная по пробелам
a = [int(i) for i in a] # Преобразование элементов списка к целому числу
print(a)

# Инициализация двумерного списка каким-либо значением:
n = 5
m = 4

a = [[0]*m for i in range(n)]
# a[1][3] = 100
for i in a:
    print(i)

# Двойные циклы:
a = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(a)
# Каждое значение сочетается с каждым.

a = [i*j for i in (2, 3, 4, 5) for j in [1, 2, 3] if i*j > 10]
print(a)

#
print('Tasks')
# При помощи генератора-списка создайте список [1, 2, 3, ..., n], само натуральное число n будет поступать на вход
# вашей программе.
# В качестве ответа просто выведите получившийся список
print([i for i in range(1, int(input()) + 1)])

#
print([*range(1, int(input())+1)])

# При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита
# ['A', 'B', 'C', 'D', ...]. Получить все заглавные буквы английского алфавита можно следующим образом:
# from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Входные данные:
# На вход программе подается натуральное число n, n≤26.
# Формат выходных данных:
# Программа должна вывести список из первых n заглавных букв английского алфавита
from string import ascii_uppercase

a = [ascii_uppercase[i] for i in range(int(input()))]
print(a)

#
from string import ascii_uppercase
print([i for i in ascii_uppercase[:int(input())]])

#
print([__import__('string').ascii_uppercase[i] for i in range(int(input()))])

# Создайте список первых букв каждого слова из строки st и выведите его на экран
st = 'Create a list of the first letters of every word in this string'
a = [i for i in st.split()]
s = []
for i in a:
    s.append(i[0])
print(s)

#
st = 'Create a list of the first letters of every word in this string'
print([elem[0][0] for elem in st.split()])
#
st = 'Create a list of the first letters of every word in this string'
print([i[0] for i in st.split()])

# Давайте усовершенствуем предыдущую задачу так, чтобы получался следующий список букв:
# ['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', ...]
# Входные данные:
# На вход программе подается натуральное число n, n ≤ 26.
# Формат выходных данных:
# Программа должна вывести список из первых n заглавных букв английского алфавита, причем каждая буква должна быть
# продублирована в зависимости от своего порядкового номера
from string import ascii_uppercase
s = [i*(ascii_uppercase.index(i) + 1) for i in ascii_uppercase[0:int(input())]]
print(s)

#
from string import ascii_uppercase
print([ascii_uppercase[x]*(x+1) for x in range(int(input()))])

#
def f(n):
    from string import ascii_uppercase as au
    return [i * (au.index(i) + 1) for i in au[:n]]

n = int(input())
print(f(n))

# Программа принимает на вход два целых числа a и b.
# Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b включительно и вывести его
# на экран.
# Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b включительно, двигаясь в порядке
# убывания, и затем вывести его.
# Не забывайте пользоваться генератором списков
a, b = map(int, input().split())
if a <= b:
    print([i**2 for i in range(a, b+1)])
else:
    print([i**3 for i in range(b, a+1)][::-1])

#
#  условие заключено в логике ''or'', запустится один из генераторов в зависимости от того,  какому условию range
#  удовлетворят входные данные. Например, итерация по range(a, b + 1) не запустится если a > b.
a, b = map(int, input().split())
print([i**2 for i in range(a, b + 1)] or [i**3 for i in range(a, b - 1, -1)])
# Получается, что пустой список вообще не печатается и обрабатывается как False
# a=[]
# if a: print(a)
# А вот непустой -True:
# a=[1]
# if a: print(a)

#
a, b = map(int, input().split())
if a <= b:
    print([x ** 2 for x in range(a, b + 1)])
else:
    print([x ** 3 for x in range(a, b - 1, -1)])

#
a, b = map(int, input().split())
print([i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a,b - 1,-1)])

#
a, b = map(int, input().split())
print([i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(b, a + 1).__reversed__()])

# На вход программе подается натуральное число n (n<=1000). При помощи list comprehension создайте список, с
# остоящий из делителей введенного числа.
n = int(input())
print([i for i in range(1, n + 1) if n % i == 0])

#
[print([i for i in range(1, n + 1) if not n % i]) for n in [int(input())]]


# При помощи генератора-списков создайте список, состоящий из слов,  начинающихся с буквы 't' или 'T'.
# Слова возьмите из переменной phrase, также не забывайте про метод split()
# В качестве ответа выведите полученный список, слова в нем должны стоять в том же порядке, в котором они стояли в
# изначальной фразе
phrase = 'Take only the words that start with t in this sentence'
print([i for i in phrase.split() if i[0] == 't' or i[0] == 'T'])

#
print([i for i in phrase.split() if i[0] in 'tT'])

#
print([i for i in phrase.split() if i[0].lower() == 't'])



