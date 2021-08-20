# ЦИКЛ while.

# while - инструкция для организации циклов с неизвестным количеством повторений.
print('В порядке возрастания:')
i = 1
while i < 6:
    print(i)
    i = i + 1

i = 1
while i < 20:
    print(i)
    i = i + 2

i = 1
while i < 600:
    print(i)
    i = i*2

i = 1
while i < 6:
    print('Hello')
    i = i + 1

n = int(input())
i = 1
while i < n + 1:        # while i <= n:
    print('Hello')
    i = i + 1

n = int(input())
i = 1
i = 20
while i > 0:
    print(i)
    i = i - 1
while i <= n:
    print('Hello')
    i = i + 1

#
print('В порядке убывания:')

a = int(input("Введите число: "))
while a != 0:
    print('Повторите ввод')
    a = int(input("Введите число: "))
print('Вы ввели 0')


#
print('Вод пароля:')
a = input("Введите пароль:")
password = 'qwerty'
while a != password:
    print('Пароль неверный')
    a = input("Введите пароль:")
print('Верный пароль')

#
guess = input("Введите пароль:")
password = 'qwerty'
count = 0
while guess != password:
    count += 1                                              # Добавление счетчика
    print('Пароль неверный')
    print(f'Вы ввели неправельный пароль {count} раз.')
    guess = input("Введите пароль:")

print('Верный пароль')

#
print('Удаление всех одинаковых элементов из списка')
a = [1, 2, 3]*5
print(a)
a.remove(3)
print(a)
while 3 in a:
    a.remove(3)
    print(a)

#
print('Обход всех символов строки по порядку:')
s = 'privet'
while len(s) > 0:
    print(s[0], s[1:])
    s = s[1:]

#
print('Проверка внутри списка:')
s = 'pRi/Vet4@5682,Fdj'
while len(s) > 0:
    bukva = s[0]
    if bukva >= 'a' and bukva <= 'z':
        print(bukva, 'small')
    elif bukva >= 'A' and bukva <= 'Z':
        print(bukva, 'big')
    elif bukva.isdigit():
        print(bukva, 'digit')
    else:
        print(bukva, 'znak')
    s = s[1:]

#
print('Tasks')
# Пользователь вводит числа, и пока введённые числа не равны нулю, программа работает, как только происходит
# иное –завершает работу.
x = int(input())
while x != 0:
    x = int(input())

#
while int(input()) != "0":
    pass

#
while True:
    a = int(input())
    if a == 0:
        break

#
while int(input())!=0:
    pass

#
iter(input, '0')

# Мишка Лимак хочет стать самым большим медведем, ну, или хотя бы стать больше своего старшего брата Боба.
# Сейчас вес Лимака равен a, а вес Боба равен b. Гарантируется, что вес Лимака меньше или равен весу Боба.
# Лимак ест много, и его вес утраивается каждый год, а вес Боба удваивается каждый год.
# Через сколько целых лет Лимак станет строго больше (т. е. будет весить строго больше) Боба?
# В единственной строке находятся два целых числа a и b (1<=a<=b<=10) — веса Лимака и Боба соответственно.
# Выведите одно целое число — через сколько целых лет Лимак станет строго больше Боба.
a, b = map(int, input().split())
c = 0
while a <= b:
    a = a*3
    b = b*2
    c += 1
print(c)

#
a, b = map(int, input().split())
y = 0
while a <= b:
    a, b, y = a * 3, b * 2, y + 1
print(y)

#
(a, b), cnt = map(int, input().split()), 0
while a <= b:
    a *= 1.5
    cnt += 1
print(cnt)

# На вход программе поступает слово. Вам необходимо воспроизвести процесс, в котором каждый раз у этого слово будет
# пропадать первая и последняя буква. Этот процесс необходимо закончить, когда слове останется только одна буква или
# слово  станет пустой строкой. При этом результат каждого этапа нужно выводить
n = input()
print(n)
while len(n) >= 1:
    n = n[1:-1]
    print(n)

#
s = input()
while len(s) > 0:
    print(s)
    s = s[1:-1]

#
s = input()
print(s, *[s[i:-i] for i in range(1, len(s) // 2 + 1)], sep="\n")

#
n = input()
print(n)
i = 1
while i < len(n):
    print(n[i:-i])
    i += 1

# Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.
# Задано единственное целое число N
# Необходимо вывести  все точные квадраты натуральных чисел, не превосходящие данного числа N.
n = int(input())
a = 1
while a**2 <= n:
    print(a**2)
    a += 1

#
n = int(input())
i = 1
while i*i <= n:
    print(i*i)
    i += 1

# В первый день спортсмен пробежал X километров. В каждый последующий день он увеличивал пробег на 15% от предыдущего
# дня. Вам необходимо определить номер дня, в который пробег спортсмена составил не менее Y километров. Само число Y
# будем поступать на вход программе.
# Входные данные:
# Программа получает на вход два положительных вещественных числа X и Y (X,Y ≤ 1000).
# Выходные данные:
# Выведите целое число – номер дня, в который спортсмен пробежал не менее Y километров.
x, y = map(int, input().split())
c = 1
while x < y:
    x = x + x*15/100
    c += 1
print(c)

#
x, y = map(int, input().split())
a = 1
while x <= y:
    x *= 1.15
    a += 1
print(a)

# У Васи есть n пар носков. Утром каждого дня, собираясь в школу, Вася должен надеть пару носков. Вечером, прийдя со
# школы, Вася снимает надетые носки и выбрасывает их. Каждый m-й день (в дни с номерами m,2m,3m,...)
# мама покупает Васе одну пару носков. Она делает это поздно вечером, поэтому Вася может надеть новые носки не раньше
# следующего дня. На сколько подряд идущих дней Васе хватит носков?
# В единственной строке записано два целых числа n и m (1≤n≤100; 2≤m≤100), разделенные пробелом.
# Выведите единственное целое число — ответ на задачу.
n, m = map(int, input().split())
c = 0
while n:
    n -= 1
    c += 1
    if c % m == 0:
        n += 1
print(c)

#
n, m = map(int, input().split())
d = 0
while n - d * 1 + d//m > 0:
    d += 1
print(d)

# Начиная с числа n, умножайте имеющееся число на его первую цифру, пока у получившегося числа первая цифра не станет
# равной 1, либо пока оно не превысит миллиарда. В качестве ответа выведите результат
n = int(input())
while int(str(n)[0]) != 1 and n <= 10**9:
    n = int(n) * int(str(n)[0])
print(n)

#
a = input()
while int(a[0]) != 1 and len(a) < 10:
    a = str(int(a[0])*int(a))
print(a)

#
n = int(input())
first = int(str(n)[0])
while first != 1 and n <= 10**9:
    n = n*first
    first = int(str(n)[0])
print(n)

#
number = int(input())
while str(number)[0] != '1' and number < 1000000000:
    number *= int(str(number)[0])
print(number)


# В архитектуре компьютера важную роль играют числа, являющиеся степенями двойки: 1, 2, 4, 8 и так далее.
# Напишите программу, которая проверяет, является ли введённое натуральное число степенью двойки. Если да,
# то выводится сама эта степень; если нет, выводится «НЕТ»
n = int(input())
i = 0
while 2**i < n:
    print(f'Число = {2**i}, степень = {i}')
    i += 1
print(f'Число = {2**i}, степень = {i}')
if 2**i == n:
    print(i)
else:
    print('НЕТ')

#
a = int(input())
count = 0
while a >= 1 and a % 2 == 0:
    a //= 2
    count += 1
print(count if a == 1 else 'НЕТ')

#
a = int(input())
power = 0
while a % 2 == 0:
    a /= 2
    power += 1
if a == 1:
    print(power)
else:
    print('НЕТ')

#
n = int(input())
st = 0                      # счётчик степени
if n > 0:                   # если введёное значение больше нуля
    while 2 ** st < n:      # если 2 в степени будет больше n, то n точно не степень двойки и нужно завершать цикл
        st += 1             # увеличение степени
    if 2 ** st == n:        # если n является 2 в степени
        print(st)
    else:
        print('НЕТ')
else:
    print('НЕТ')

#
n = int(input())
m = 0
answer = 'НЕТ'
while 2 ** m <= n:
    if 2 ** m == n:
        answer = m
    m += 1
print(answer)

#
n = int(input('Введите произвольное число: '))
counter = 0
while n > 1:         # до тех пор пока n > 1
    n = n / 2        # делим на 2
    counter += 1     # увеличиваем счетчик на 1
if n == 1:           # если таки дошли до 1 - значит все числа делились без остатка на 2
    print(counter)   # печатаем счетчик степеней
else:
    print('НЕТ')     # в противном случае печатаем нет


# Ваня и кубики
# Ване на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду. Ваня хочет построить пирамиду
# следующим образом: на верхушке пирамиды должен находиться 1 кубик, на втором уровне — 1+2=3 кубика,
# на третьем — 1+2+3=6 кубиков, и так далее. Таким образом, на i-м уровне пирамиды должно располагаться
# 1+2+..+(i-1)+i кубиков.
# Ваня хочет узнать, пирамиду какой максимальной высоты он может создать с использованием имеющихся кубиков.
# Входные данные:
# В первой строке записано целое число n (1≤n≤104) — количество кубиков, подаренных Ване.
# Выходные данные:
# Выведите единственной строкой максимально возможную высоту пирамиды.
n = int(input())
level = 0
cub_level = 0
s = 0
while s < n:            # Цикл закончится когда s==n or s>n
    level += 1
    cub_level += level
    s += cub_level
if s == n:
    print(level)
else:
    print(level-1)

#
n = int(input())
x = i = 1
while n > 0:
    i += 1
    x += i
    n -= x
print(i - 1)

#
n = int(input())
i = 0                       # уровень пирамиды или её высота
s = 0                       # число кубиков в слое
v = []                      # список чисел кубиков по слоям
while sum(v) <= n:
    i = i + 1
    s = s + i
    v.append(s)
print(i - 1)

# Система уравнений
# Фурик очень любит уроки математики, поэтому, в отличие от Рубика, он их не посещает. Но теперь Фурик хочет получить
# хорошую оценку по математике. Для этого Лариса Ивановна, учительница математики, дала ему новое задание.
# Задана система уравнений:
#  a**2 + b == n and a + b**2 == m
# Нужно посчитать количество пар целых чисел (a,b) (0≤a,b), которые удовлетворяют системе.
# Входные данные:
# В единственной строке заданы два целых числа n,m (1≤n,m≤1000) — параметры системы. Числа в строке разделены пробелом.
# Выходные данные:
# В единственную строку выведите ответ на задачу.
n, m = map(int, input().split())
count = 0
a = 0
while a**2 <= n:
    b = n - a**2
    if b >= 0 and a + b**2 == m:
        count += 1
    a += 1
print(count)

#
n, m = map(int,input().split())            # Вписываем исходные данные
a,i = 0,0                                  # a - переменная, i - счетчик, b не требуется
while a < max(n,m):                        # Пока a < максимального из исходных значений:
    # Так как у нас 2 уравнения:
    # a**2 + b = n и b**2 + a = m : найдем, чему будет равно a и b:
    # a = (n - b)**0.5 и b = (m - a)**0,5. Подставляем в первое уравнение значение "b" из второго:
    # a = (n - (m - a)**0.5)**0.5
    if a == (n - (m - a)**0.5)**0.5:       # Если равенство истинно, то прибавляем счетчик на один
        i +=1
    a += 1                                 # В любом случае увеличиваем "a" на 1 и все по новой
print(i)

#
n, m = [int(i) for i in input().split()]
print(len([i for i in range(n) for j in range(m) if i ** 2 + j == n and i + j ** 2 == m]))

#
n, m = map(int, input().split())
count = 0
a = 0
b = 0
while a ** 2 + b + a + b ** 2 <= m + n:
    if a ** 2 + b + a + b ** 2 == m + n:
        count += 1
        b += 1
    a += 1
print(count)

#
n, m = map(int, input().split())
cnt = 0
for a in range(0, 1000 + 1):
    for b in range(0, 1000 + 1):
        if a ** 2 + b == n and a + b ** 2 == m:
            cnt += 1
print(cnt)


# Дело о нулях и единицах
# Андроид Андреид — известный на всю галактику детектив. В свободное от работы время он размышляет о строках из нулей и
# единиц.
# Как-то раз ему в голову пришла строка длины n, состоящая из нулей и единиц. Рассмотрим следующую операцию — мы
# выбираем любые две соседние позиции в строке, и если в одной из них ноль, а в другой — единица, то разрешается удалить
# обе эти цифры, в результате чего строка строка становится длины n-2.
# Андреид задумался — какой минимальной длины строка может остаться, если применить описанную операции некоторое
# (возможно, нулевое) количество раз?
# Входные данные:
# В первой строке входных данных задано целое число n (1≤n≤2·105) — длина строки, которая пришла в голову Андреиду.
# Во второй строке записана строка длины n, состоящая из нулей и единиц.
# Выходные данные:
# Выведите единственное целое число — минимальное возможное значение длины строки, которая останется после применения
# операций, описанных в условии задачи.
n = int(input())
s = input()
while '01' in s or '10' in s:
    s = s.replace('10', '')
    s = s.replace('01', '')
print(len(s))

#
n = int(input())
s = input()
ones = s.count('1')
zeroes = s.count('0')
union = min(ones, zeroes)
print(max(ones - union, zeroes - union))

#
n, a = input(), input()
print(abs(a.count('1')-a.count('0')))

# Бал в БерлГУ
# По случаю 100500-летия Берляндского государственного университета совсем скоро состоится бал! Уже n юношей и m девушек
# во всю репетируют вальс, менуэт, полонез и кадриль.
# Известно, что на бал будут приглашены несколько пар юноша-девушка, причем уровень умений танцевать партнеров в каждой
# паре должен отличаться не более чем на единицу.
# Для каждого юноши известен уровень его умения танцевать. Аналогично, для каждой девушки известен уровень ее умения
# танцевать. Напишите программу, которая определит наибольшее количество пар, которое можно образовать из n юношей и m
# девушек.
# Входные данные:
# В первой строке записано целое число n (1≤n≤100) — количество юношей. Вторая строка содержит последовательность
# a1,a2,...,an (1≤ai≤100), где ai — умение танцевать i-го юноши.
# Аналогично, третья строка содержит целое m (1≤m≤100) – количество девушек. В четвертой строке содержится
# последовательность b1,b2,...,bm (1≤bj≤100), где bj — умение танцевать j-й девушки.
# Выходные данные:
# Выведите единственное число — искомое максимальное возможное количество пар.
n = int(input())
boys = list(map(int, input().split()))

m = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()
i = 0
j = 0
count = 0
while i < n and j < m:
    if abs(boys[i] - girls[j]) <= 1:
        count += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1
print(count)

#
n = int(input())    # количество юношей
sn = sorted(list(map(int, input().split())))    # умение танцевать каждого юноши по возрастанию
m = int(input())    # количество девушек
sm = sorted(list(map(int, input().split())))    # умение танцевать каждой девушки по возрастанию
couple = 0    # количество пар

while len(sn) > 0 and len(sm) > 0:    # пока есть хотя бы 1 юноша и девушка
    if 0 <= abs(sn[0] - sm[0]) <= 1:    # если разница умения между юношей и девушкой не больше 1
        couple += 1    # счётчик количества пар
        sn.pop(0)    # удаление первого юноши в списке
        sm.pop(0)    # удаление первой девушки в списке
    elif sn[0] < sm[0]:    # если юноша танцует хуже девушки
        sn.pop(0)    # удаление первого юноши в списке
    else:    # если девушка танцует хуже юноши
        sm.pop(0)    # удаление первой девушки в списке
print(couple)

#
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))
i, j, p = 0, 0, 0
while i < n and j < m:
    if abs(a[i] - b[j]) < 2:
        i += 1
        j += 1
        p += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(p)

#
n = int(input())
bb = sorted(map(int, input().split()))
m = int(input())
bg = sorted(map(int, input().split()))
cnt = 0

while bb and bg:
    diff = bb[0] - bg[0]
    if diff < -1: bb.pop(0)
    elif diff > 1: bg.pop(0)
    else:
        bb.pop(0); bg.pop(0); cnt += 1
print(cnt)

# В последний день уходящего 2016 года Лимак собирается принять участие в соревновании по спортивному программированию.
# Соревнование начнётся в 20:00 и будет продолжаться четыре часа, то есть ровно до полуночи. Участникам будет предложено
# n задач, упорядоченных по возрастанию сложности, то есть задача 1 будет самой лёгкой, а задача номер n — самой сложной.
# Лимак знает, что ему потребуется 5·i минут на решение i-й задачи.
# Друзья Лимака планирую устроить роскошную новогоднюю вечеринку и Лимак хочет прибыть в полночь или ранее.
# Он знает, что ему требуется ровно k минут чтобы добрать до места проведения вечеринки от своего дома, где он
# собирается участвовать в соревновании.
# Сколько максимум задач может успеть решить Лимак, так чтобы не опоздать на новогоднюю вечеринку?
# Входные данные:
#
# В первой строке входных данных записаны два целых числа n и k (1≤n≤10, 1≤k≤240) — количество задач в соревновании и
# количество минут, за которое Лимак доберётся от дома до места проведения вечеринки.
# Выходные данные:
# Выведите одно целое число, равное максимальному количеству задач, которое может решить Лимак, так чтобы прибыть на
# новогоднюю вечеринку ровно в полночь или раньше.
n, k = map(int, input().split())
a, b = n, k
i = 0
t = 0
tav = 240 - k
while 1:
    t += (i + 1) * 5
    if t > tav or i == n:
        break
    i += 1
print(i)

#
n, k = map(int, input().split())
i, t = 0, 0
while i < n and t + k + 5*(i + 1) <= 240:
    i += 1
    t += 5 * i
print(i)

#
a, b = map(int, input().split())
s, x = 0, 5
while x < 240 - b and s < a:
    s = s + 1
    x = x + (5 * s)
print(s)

#
n, k = map(int, input().split())
print(min(n, int((1 + 2 * (240 - k) / 5)**0.5 - 0.5)))

#
n, k = map(int, input().split())
h = (240 - k) # время на решение задач
kol = 0       # количество решенных задач
i = 0         # номер задачи
t = 0         # время на решенные задачи

while i < n:
    i += 1
    vremya = 5 * i # время на i задачу
    t += vremya
    if t <= h:
        kol += 1
    else:
        break
    # print(i,vremya,t,h,kol)
print(kol)

#
n,m = map(int,input().split())
c = 0
b = 1
a = 240-m
while c < n and a > b:
    a-=b*5
    b+=1
    c+=1
print(c)

#
n, k = map(int, input().split())
count = 0
time = k
while ((time + count * 5 ) < 240) and (count < n):
    count += 1
    time += 5 * count
print(count)


# Слияние списков
# В вашем распоряжении имеется два отсортированных списка по неубыванию элементов, состоящих из n и m элементов
# Ваша задача слить их в один отсортированный список размером  n + m
# Входные данные:
# Программа получает на вход два числа n и m - количество элементов первого списка и второго списков
# Затем с новой строки поступают элементы первого отсортированного списка, а со следующей строки - второго списка
# Выходные данные:
# Слить два списка в один в порядке неубывания и вывести элементы полученного списка
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=0
while m>0:
    if b[0]<=a[i]:
        a.insert(i,b[0])
        del b[0]
        m=m-1
        i=0
    elif i==len(a)-1:
        a.append(b[0])
        m=m-1
        i=0
    else:
        i=i+1
a=list(map(str,a))
a=' '.join(a)
print(a)

#
n, m = input().split()
f = list(map(int, input().split()))
s = list(map(int, input().split()))

total = f + s
solution = []
while len(total) > 0:
    solution.append(min(total))
    total.remove(min(total))

print(*solution)

#
from heapq import merge
n, m = input().split()
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(*list(merge(list1, list2)))

#
n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = list1+list2
list_sort =[]
while len(list3) > 0:
    min1 = min(list3)
    list_sort.append(min1)
    list3.remove(min1)
print(*list_sort)

#
n,m=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=a+b
new=[]
x=0
while x<len(c):
    new.append(min(c))
    c.remove(min(c))
print(*new)

#
a, b = map(int, input().split())            # количствео символов в стрках
spis_a = list(map(int, input().split()))    # Строки
spis_b = list(map(int, input().split()))    # Строки 2
act_a = spis_a[:a + 1]                      # Список для обработки
act_b = spis_b[:b + 1]                      # Список для обработки 2
spisok = []                                 # Пополняемый список
while sum(act_a) != 0 or sum(act_b) != 0:   # Если цифр в строках не осталось
    if sum(act_a) != 0:                     # Если в списке А что то есть
        if sum(act_b) == 0:                 # Если в списке Б пусто
            spisok.append(act_a[0])         # Добовляем первый знак из перовго списка
            act_a.remove(act_a[0])          # Удаляем первый знак из перовго списка
        elif act_a[0] < act_b[0]:           # Сравниваем первые числа списков
            spisok.append(act_a[0])         # Добовляем первый знак из перовго списка
            act_a.remove(act_a[0])          # Удаляем первый знак из перовго списка
        else:                               # Если первый символ в списке А больше чем в списке Б
            spisok.append(act_b[0])         # Добовляем первый знак из второго списка
            act_b.remove(act_b[0])          # Удаляем первый знак из перовго списка
    else:                                   # Если в списке а Ничего нет
        spisok.append(act_b[0])             # Добовляем первый знак из второго списка
        act_b.remove(act_b[0])              # Удаляем первый знак из перовго списка

print(str(spisok).replace(',', '').replace('[', '').replace(']', ''))
                # Переделаваем список в строку и заменяем ',' на ''.



