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

# На первой строке вводится один символ — строчная буква.
# На второй строке вводится предложение.
# Нужно вывести список слов (словом считается часть предложения, окружённая символами пустого пространства), в которых
# присутствует введённая буква в любом регистре, в том же порядке, в каком они встречаются в предложении.
b = input()
p = input()
for i in p.split():
    if b in i.lower():
        print(i)

letter = input()
print(*[i for i in input().split() if letter in i], sep='\n')

a = input().lower()
print(*[i for i in input().split() if a in i.lower()], sep='\n')

a = input()
c = input().split()
for i in c:
    if a in i:
        print(i)

a = input()
b = map(str, input().split())
for i in b:
    if a in i.lower():
        print(i)

# На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное значение.
# В случае, если положительных значений нет, выведите строку "Empty"
a = list(map(int, input().split()))
c = []
for i in a:
    if i > 0:
        c.append(i)
if len(c) == 0:
    print('Empty')
else:
    print(min(c))

print((sorted([i for i in map(int, input().split()) if i > 0]) + ['Empty'])[0])

numbers = map(int, input().split())
for number in sorted(numbers):
    if number > 0:
        print(number)
        break
else:
    print('Empty')

# Напишите программу, которая находит рекордное количество вхождений (не обязательно подряд) символа в строку.
# Формат ввода: Вводится одна строка.
# Формат вывода: Выводится одно целое число — максимальное количество раз, которое встречается какая-либо буква
# (без учёта регистра) или иной символ во введённой строке.
a = input().lower()
s = []
for i in a:
    s.append(a.count(i))
print(max(s))

word = input().lower()
print(max([word.count(i) for i in word]))

print(max(s.count(c) for s in (input().lower(),) for c in s))

s = input().lower()
print(max(s.count(i) for i in s))

# Делимость на 11
# Для делимости числа на 11 необходимо, чтобы разность между суммой цифр, стоящих на четных местах, и суммой цифр,
# стоящих на нечетных местах, делилась на 11.
# Требуется написать программу, которая проверит делимость заданного числа на 11.
# Входные данные: Программа получает на вход одно натуральное число N, делимость которого надо проверить
# Выходные данные: Выведите “YES”, если число делится на 11, или “NO” иначе.
x = input()
s_even = 0
s_odd = 0
for i in range(len(x)):
    if i % 2 == 0:
        s_even += int(x[i])
    else:
        s_odd += int(x[i])
diff = s_even - s_odd
if diff % 11 == 0:
    print('YES')
else:
    print('NO')

#
x = input()
s = 0
for i in range(len(x)):
    if i % 2 == 0:
        s += int(x[i])
    else:
        s -= int(x[i])

if s % 11 == 0:
    print('YES')
else:
    print('NO')

#
x = input()
s = 0
for index, value in enumerate(x):
    if index % 2 == 0:
        s += int(value)
    else:
        s -= int(value)

if s % 11 == 0:
    print('YES')
else:
    print('NO')

#
num = input()
print(('NO', 'YES')[(sum(int(i) for i in num[0::2]) - sum(int(i) for i in num[1::2])) % 11 == 0])

#
n = [int(i) for i in input()]
print('NO' if (sum(n[1::2]) - sum(n[0::2])) % 11 else 'YES')

#
a = input()
sch = 0
snch = 0
for i in range(0, len(a), 2):
    sch += int(a[i])
for i in range(1, len(a), 2):
    snch += int(a[i])
if (sch-snch)%11 == 0:
    print("YES")
else:
    print("NO")

#
[print(('NO', 'YES')[(sum(num[::2]) - sum(num[1::2])) % 11 == 0]) for num in [[int(i) for i in input()]]]


#
n = [int(i) for i in input()]
a, b = sum(n[::2]), sum(n[1::2])
k = abs(a - b)
print('NO' if k%11 else 'YES')

#
a = str(input())
if (sum([int(i) for i in a[1:len(a):2]]) - sum([int(i) for i in a[0:len(a):2]])) % 11 == 0:
    print('YES')
else:
    print('NO')

n = input()
even     = sum([int(n[i]) for i in range(0,len(n),2)])
not_even = sum([int(n[i]) for i in range(1,len(n),2)])

print('YES' if (even-not_even) % 11 == 0 else 'NO')


# На вход программе поддается строка, а ваша задача определить сколько символов в данной строке являются цифрами и
# также найти сумму всех этих цифр. Например, в строке "Комната 1408" содержится 4 цифры и их сумма равна 13.
# В качестве ответа необходимо через пробел вывести 2 числа - количество цифр в введенной строке и их сумма

a = input()                     # Ввод строки
al = len(a)                     # Длинна строки a
b = []                          # Пустой список b

for i in range(al):
    if a[i].isdigit():          # если символ цифра
        b.append(a[i])          # добавить символ в пустой список b

cb = 0                          # счетчик начальный для цифр из писка b
bl = len(b)                     # длинна списка b

for i in range(bl):
    cb += int(b[i])               # проходим по списку b и суммируем все цифры

print(bl, cb)