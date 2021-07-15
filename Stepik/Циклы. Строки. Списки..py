# Вывести все нечетные числа в интервале:
a = min
while a <= max:
    print(a)
    a += 2

# или пробегая весь диапазон чисел, выводя только соответствующие:
a = min
while a <= max:
    if a % 2 == 1:
        print(a)
    a += 1


# Напишите программу, которая считывает со стандартного ввода целые числа, по одному
# числу в строке, и после первого введенного нуля выводит сумму полученных на вход
# чисел.
n = int(input())
a = 0
while n != 0:
    a += n
    n = int(input())
print(a)

# или
n = int(input())        #считываем целое число
s = 0                   #сумма чисел изначально равна нулю
while n != 0:           #запускаем цикл с условием
    s = s+n             #прибавляем к сумме введённое число
    n = int(input())    #просим ввести число повторно
print(s)                #выводим сумму

# break and continue
i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if (a == 0) and (b == 0):
        break           # досрочно завершаем цикл
    if (a == 0) or (b == 0):
        continue        # переходим к следующей итерации
    print(a * b)
    i += 1

# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.
# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.
n = int(input())
while n <= 100:
    if n < 10:
        n = int(input())
    else:
        print(n)
        n = int(input())


# или
while True:
    number = int(input())
    if number >100:
        break
    if number <10:
        continue
    print(number)



# или
i = int(input())
while i <= 100:
    if i >= 10:
        print(i)
    i = int(input())


# Квадрат из звездочек:
n = int(input())
for i in range(n):
    print(' * ' * n)

# или
n = int(input())
for i in range(n):
    for j in range(n):
        print(' * ', end='')
    print()



# Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в
# своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел
# отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
# Числа aa, bb, cc и dd являются натуральными и не превосходят 10, a ≤ b, c ≤ d.
# Следуйте формату вывода из примера, для разделения элементов внутри строки
# используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой
# выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.
""" Делать нужно всё построчно.
Первая строка - табуляция+цикл for для последовательности от c до d: сначала необходимо 
вызвать оператор print для вывода табуляции, не забывая о том, что последующий вызов 
oператора print должен находиться на этой же строке (т.е. необходимо определить верный 
параметр end для первого print, об этом сказано в пред. видеопримере), ну а следующий 
вызов оператора print на этой же строчке (с параметром табуляции) будет производиться 
в введённом первом цикле for для определения последовательности от с до d.
Далее необходимо третий раз (вне предыдущего цикла) вызвать оператор print для перехода 
на новую строку, опять же не забывая о том, что последующий вызов оператора print должен 
находиться на этой же строке (т.е. необходимо определить верный параметр end для первого 
print, об этом сказано в пред. видеопримере). После этого построчно выведем всё, что нам 
нужно, циклом с вложенным циклом.
Вводим второй цикл для определения последовательности от a до b, в этом цикле четвертый 
раз вызываем print с выводом первого столбца (последовательности от a до b), не забывая 
про параметр табуляции. Во втором цикле формируем вложенный в него третий цикл, аналогичный 
первому, во вложенном третьем цикле пятый раз вызываем оператор print для вывода произведения, 
не забывая про параметр табуляции. Наконец, завершаем второй цикл шестым вызовом оператора 
print для перехода на новую строку - чтобы повторять построчные итерации для произведения.
Не забывайте про "лестничную" структуру самого кода (табуляции) для правильного 
определения/завершения циклов."""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, d + 1):
    print('\t', j, end=" ")
print()
for i in range(a, b + 1):
    print(i, end=" ")
    for j in range(c, d + 1):
        print('\t', i * j, end=" ")
    print()


# или
a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d + 1):
    print('\t', i, end='')
print()
for j in range(a, b + 1):
    print(j, end='\t')
    for k in range(c, d + 1):
        print(j * k, end='\t')
    print()



# или
a, b, c, d = (int(input()) for x in range(4))
print('', *range(c,d+1), sep='\t')
for x in range(a, b+1):
    print(x, *[y*x for y in range(c, d+1)], sep='\t')



# Задача: Вывести сумму всех нечетных чисел от a до b (включая обе границы).
a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range(a, b + 1):
    if i % 2 == 1:
        s += i
print(s)

# или
a, b = input().split()
a = int(a)
b = int(b)
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)


# или
a, b = (int(i) for i in input().split())
s = 0
if a % 2 == 0:
    a += 1
for i in range(a, b + 1, 2):
    s += i
print(s)



# Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит
# на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b], которые делятся на 33.
# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке
# [-5; 12]. Всего чисел, делящихся на 33, на этом отрезке 66: -3, 0, 3, 6, 9,12.
# Их среднее арифметическое равно 4.5
# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое
# делится на 3.
a = int(input())
b = int(input())
s = 0
t = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        t += 1
print(s / t)



# или
a,b = int(input()), int(input())
a += -a % 3
b -= b % 3
print((a + b) / 2)


# или
x = [x for x in range(int(input()), int(input()) + 1) if x % 3 == 0]
print(sum(x)/len(x))


# или
a,b = (int(input()) for i in (1, 2))
print(((a + (3-a % 3) % 3) + b - (b % 3)) / 2)


# Перечисление символов строки:
genome = "ATTG"
for c in genome:
    print(c)


genome = input()
cnt = 0
for nucl in genome:
    if nucl == 'C':
        cnt += 1
print(cnt)

# или
genome = input()
print(genome.count('C'))

# пример последовательного вызова методов:
s = "agTtcAGtc"
s.upper().count('gt'.upper())


# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и
# C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых
# символов).
# Например, в строке "acggtgttat" процентное содержание символов G и C равно (4/10) * 100 = 40.0
# где 4 -- это количество символов G и C,  а 10 -- это длина строки.
genome = input()
a = genome.upper().count('g'.upper())
b = genome.upper().count('c'.upper())
print(((int(a) + int(b)) / int(len(genome))) * 100)


# или
s = input().upper()
print((s.count('G') + s.count('C'))/len(s) * 100)


# или
a=input().upper()
print(((a.count('C')+a.count('G'))/len(a))*100)



# Задача - палиндром.
s = input()
i = 0
j = len(s) - 1
is_palindrom = True
while i < j:
    if s[i] != s[j]:
        is_palindrom = False
        break
    i += 1
    j -= 1
if is_palindrom:
    print('YES')
else:
    print('NO')



# или
s = input()
r = s[::-1]
if s == r:
    print('YES')
else:
    print('NO')



# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых
# символов исходной строки заменяются на этот символ и количество его
# повторений в этой позиции строки.
# Напишите программу, которая считывает строку, кодирует её предложенным
# алгоритмом и выводит закодированную последовательность на стандартный вывод.
# Кодирование должно учитывать регистр символов.
s = str(input())
l = len(s)-1
c = 1
t = ''
if len(s)==1:
    t = t +s+str(c)
else:
    for i in range(0,l):
        if s[i]==s[i+1]:
            c +=1
        elif s[i]!=s[i+1]:
            t = t + s[i]+str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1]==s[-2]:
            t = t +s[j]+str(c)
        elif s[-1]!=s[-2]:
            t = t +s[j]+str(c)
            c = 1
print(t)


# или
s = input()
l=len(s)
cnt=1
for i in range(l):
    if i==(l-1):
        print(s[i]+str(cnt),end='')
    else:
        if s[i]==s[i+1]:
            cnt=cnt+1
        else:
            print(s[i]+str(cnt),end='')
            cnt=1



# или
dna = input()                    # считываем строку
print(dna[0],end='')             # выводим первый символ
cnt = 1                          # счетчик символов на единице
for i in range(0,len(dna)-1):    # итератор проходит по всем индексам символов кроме предпоследнего
    if dna[i] == dna[i+1]:       # сравниваем символ по текущему индексу со следующим
        cnt+=1                   # если символы одинаковые, то увеличиваем счетчик
    else :
        print(cnt,end='')        # если разные, то выводим значение счетчика
        print(dna[i+1],end='')   # выводим следующий символ
        cnt = 1                  # счетчик текущего символа на единице
print(cnt)                       # в конце распечатываем значение счетчика последнего символа


# или
a=input()
s=1
a=a+'0'
for j in range (0,len(a)-1):
    if a[j]==a[j+1]:
     s+=1
    else:
     print((a[j]+str(s)),end='')
     s=1


# или
# put your python code here
dnk = input()
dnk = dnk + '.'                 # увеличиваем строку на один символ
i = 0                           # задаем счетчик символов
s = 1                           # задаем счетчик суммы элементов.
                                # Начинаем с 1, так это минимальное количество, которое нужно указать
b = ''                          # задаем переменную, в которую будем сохранять вывод всех данных
for i in range(len(dnk)-1):
    a = dnk[i]
    if a == dnk [i+1]:          # сравниваем соседние символы
        s += 1                  # увеличиваем сумму символов
    else:
        b+= str(a) + str(s)     # запоминаем последний элемент
        s = 1                   # обнуляем счетчик до минимального значения
print (b)


##
s = int(input())
n1 =" программистов"
n2 =" программист"
n3 =" программиста"
if  s >= 0:
  if s == 0:
    print(str(s) + n1)
  elif s % 100 >= 10 and s % 100 <= 20:
    print(str(s) + n1)
  elif s % 10 == 1:
    print(str(s) + n2)
  elif s % 10 >= 2 and s % 10 <= 4:
    print(str(s) + n3)
  else:
    print(str(s) + n1)


##
s = str(input())
sum1 = int(s[0]) + int(s[1]) + int(s[2])
sum2 = int(s[3]) + int(s[4]) + int(s[5])
if sum1 == sum2:
  print('Счастливый')
else:
  print('Обычный')


##
a = int(input())
b = int(input())
s = 1
k = 2
while s < k:
  if s % a == 0 and s % b == 0:
    k = s
  else:
    s = s + 1
    k = k + 1
print(s)


# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна
# вывести сумму этих чисел. Используйте метод split строки.
n = [int(i) for i in input().split()]
a = 0
for i in range(len(n)):
    a += n[i]
print(a)

# или
a = [int(i) for i in input().split()]
s = 0
for i in a:
    s += i
print(s)

# или С использованием generator expression.
print(sum(int(i) for i in input().split()))


# или
print(sum(map(int, input().split())))


# Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для
# каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся
# крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7"
# (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
x = input().split() #строка с числами разделенными пробелами на вход
if len(x) == 1:
    print(x[0])
elif len(x) > 1: # создаю новый список
    y = [int(x[i-1])+int(x[i+1]) for i in range(-1, len(x)-1)]
    for i in range(1, len(y)):
        print(y[i], end=' ') #вывожу значения со второго до последнего
    print(y[0]) #вывожу первое значение


# или
a = [int(i) for i in input().split()]
if len(a) > 1:
    for i in range(len(a)):
        print(a[i - 1] + a[i + 1-len(a)])
else:
    print(a[0])


# или
src = [int(i) for i in input().split()]
if len(src) == 1:
    print(src[0])
else:
    [print(src[i-1] + src[(i+1) % len(src)], end=' ') for i in range(len(src))]
    # выражение src[(i+1) % len(src)] на выходе для src = [1, 3, 5, 6, 10] даст [3, 5, 6, 10, 1]
    # потому, что (i+1) % len(src) даёт 1 2 3 4 0
    # т.е. таким образом 0й элемент оказывается в конце списка (как будто повернули циферблат)
    # таким образом если при обращении к i+1 случится выход за границу диапазона для последнего элемента
    # то при обращении к (i+1) % len(src) элементу выхода не произойдет
    # поэтому складывая -1й элемент с [(i+1) % len(src)]-тым элементом
    # мы выполним условие найти сумму предыдущего и следующего элементов
    # [print( src[(i+1) % len(src)]) for i in range(len(src))]



# или
lst= [int(i) for i in input().split()]
if len(lst) == 1:
        print(lst[0])
else:
    for i in range(len(lst)):
        print(lst[i-1] + lst[i+1-len(lst)], end=' ')



# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в
# одну строку значения, которые повторяются в нём более одного раза. Для решения задачи может
# пригодиться метод sort списка. Выводимые числа не должны повторяться, порядок их вывода может
# быть произвольным.
a = [int(i) for i in input().split()]   # вводим числа в одной строке
a.sort()                                # сортируем полученный список по неубыванию
i = 0                                   # создаем счетчик = 0
while i < len(a):                       # пока показания счетчика < количества элементов в списке
    c = a.count(a[i])                   # считаем количество вхождений a[i]  в список
    if c > 1:                           # если вхождений больше 1
        print(a[i], end=' ')            # печатаем a[i]
        i += c                          # увеличиваем счетчик на количество вхождений
    else:                               # иначе
        i += 1                          # увеличиваем счетчик на 1



# поиск минимума в списке.
a = [int(i) for i in input().split()]
m = a[0]
for x in a:
    if m > x:
        m = x
print(m)

# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока
# сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех
# считанных чисел.
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого
# считывание продолжать не нужно.
# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих
 # чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то, что остались ещё
 # не прочитанные значения.
a = [int(input())]
x = 0
for i in a:
    if sum(a) != 0:
        a.append(int(input()))
    else:
        print(sum((i ** 2) for i in a))



# или
a = [int(input())]
while sum(a) != 0:
    a.append(int(input()))
print(sum([i ** 2 for i in a]))



# Дополнительная
# Выведите таблицу размером n × n, заполненную числами от 1 до n**2 по спирали, выходящей из левого верхнего угла и
# закрученной по часовой стрелке, как показано в примере (здесь n = 5):

n = int(input())
a = [[0 for i in range(n)] for j in range(n)]   #создаю матрицу n*n и заполняю нулями
k = 1                                           # заполняю матрицу числом к увеличивая его на 1 после заполнения каждого элемента
m = 0                                           # счётчик итераций спирали, увеличиваю на 1 на каждом витке спирали
while k <= n*n:                                 # внешний цикл с 4 вложенными циклами пока k не заполнит всю матрицу n*n
    for i in range(m, n-m):                     # цикл заполняет верхнюю сторону спирали - на каждой итерации сужаем границы цикла на m с каждой стороны
        a[m][i] = k
        k += 1
    for i in range(m+1, n-m):                   # цикл заполняет правую сторону спирали, границы зависят от m
        a[i][n-m-1] = k
        k += 1
    for i in range(n-m-2, m-1, -1):             # заполняею нижнюю сторону спирали - зависит от m
        a[n-m-1][i] = k
        k += 1
    for i in range(n-2-m, m, -1):               # цикл заполняет леаую сторону спирали - зависит от m
        a[i][m] = k
        k += 1
    m += 1
for i in range(n):                              # вывод на печать каждого элемента матрицы
    for j in range(n):
        print(a[i][j], end=' ')
    print()

# or
n = int(input())
i, j = 0, -1
max_j, max_i = n - 1, n - 1
min_j, min_i = 0, 1
count = 1
mtrx = [[0 for j in range(n)] for i in range(n)]    #создаю матрицу n*n и заполняю нулями
while True:

    while j < max_j:
        j += 1
        mtrx[i][j] = count
        count += 1
    max_j -= 1
    while i < max_i:
        i += 1
        mtrx[i][j] = count
        count += 1
    max_i -= 1
    while j > min_j:
        j -= 1
        mtrx[i][j] = count
        count += 1
    min_j += 1
    while i > min_i:
        i -= 1
        mtrx[i][j] = count
        count += 1
    min_i += 1

    if j == (n - 1) // 2 and i == n // 2:
        break
print()
print()
for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end=' ')
    print()


# or

def spiral(n):
    dx, dy = 1, 0
    x, y = 0, 0
    myarray = [[None] * n for j in range(n)]
    for i in range(1, n ** 2 + 1):
        myarray[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return myarray


def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print(myarray[x][y], end=' ')
        print()


n = int(input())
printspiral(spiral(n))