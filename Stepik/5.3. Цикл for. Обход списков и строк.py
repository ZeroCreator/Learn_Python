# Цикл for. Обход списков и строк.
a = [43, 65, 3, 54, 6]
count = 0                   # Счетчик обходов программы
for i in a:
    print(i)
    count += 1
    print(count, 'обход')
    input()                 # Пауза для одтверждение после каждого цикла

print('Обход по значениям:')
#
print('Увеличение каждого элемента списка на 5')
a = [43, 65, 3, 54, 6]
count = 0                   # Счетчик обходов программы
for i in a:
    i += 5                  # Операция над копией значения, не можем изменять значения списка
    print(i)
print(a)

#
print('Указать на каком месте стоит каждый элемент')
a = [43, 65, 3, 54, 6]
# count = 0                   # Счетчик обходов программы
# Обход по значениям:
# for i in a:
#    print(i, a.index(i))     # Программа будет работать только если нет повторяющихся элементов

#
print('Обход по индексам:')
# Обход по индексам:
for i in range(5):            # Значение зависит от длины списка
    print(i, a[i])

n = len(a)                    # Поменяется с изменением списка
for i in range(n):
    print(i, a[i])

# Изменение значений элемента списка:
n = len(a)                    # Поменяется с изменением списка
for i in range(n):
    print(i, a[i])            # Обращение как к индексу элемента, так и к его значению
    a[i] += 5
print(a)

# Исключить все дубли из списка:
print('Исключить все дубли из списка:')
a = [43, 65, 3, 54, 6]
b = []
for i in a:
    if not i in b:
        b.append(i)
print(b)

# Деление списка на четный и нечетный:
print('Деление списка на четный и нечетный:')
a = [43, 65, 3, 54, 6, 78, 91]
chet = []
nechet = []
n = len(a)
for i in range(n):
    if a[i] % 2 == 0:
        chet.append(i + 1)
    else:
        nechet.append(i + 1)
print(chet)
print(nechet)

# Работа со строками:
print('Работа со строками:')
s = 'hello world'
# обход по значениям:
for i in s:
    print(i)
#
s = 'helLo woRld'
for i in s:
    if i >= 'a' and i <= 'z':
        print(i, 'small')
    elif 'A' <= i <= 'Z':
        print(i, 'big')
    else:
        print(i)

# Обход строки по парам:
print('Вывести соседние пары, в которых обе буквы являются гласными:')
vowels = 'aeiou'
s = 'aertiooikjoaikl'
n = len(s)
for i in range(n):
    if s[i] in vowels and s[i + 1] in vowels:
        print(s[i], s[i + 1])

#
print('Tasks')
# Ваша задача создать список из n строк. Программа сперва будет принимать натуральное число n, а затем n строк в каждой
# отдельной строке. В качестве ответа выведите получившийся список.
a = int(input())
b = []
for i in range(a):
    s = str(input())
    b.append(s)
print(b)

n = int(input())
a = [input() for _ in range(n)]
print(a)

print([input() for _ in range(int(input()))])

k = list()
for word in range(int(input())):
    k.append(input())
print(k)

s = []
n = int(input())
for i in range(n):
    s += [input()]
print(s)