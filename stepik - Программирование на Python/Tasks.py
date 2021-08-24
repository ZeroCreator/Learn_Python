# [STEPIK]
# Программирование на Python https://stepik.org/67

# 01_12_01 Задачи по материалам недели

'''
В то далёкое время, когда Паша ходил в школу, ему очень не нравилась формула Герона для вычисления площади треугольника, так как казалась слишком сложной.
В один прекрасный момент Павел решил избавить всех школьников от страданий и написать и распространить по школам программу, вычисляющую площадь треугольника по трём сторонам.
Одна проблема: так как эта формула не нравилась Павлу, он её не запомнил.
Помогите ему завершить доброе дело и напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона.
На вход программе подаются целые числа, выводом программы должно являться вещественное число, соответствующее площади треугольника.
Sample Input:
3
4
5
Sample Output:
6.0
'''

a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(float(s))

# 01_12_02 Задачи по материалам недели

'''
Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал 
(−15,12]∪(14,17)∪[19,+∞)(−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).
Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и открытые интервалы.
Sample Input 1:
20
Sample Output 1:
True
Sample Input 2:
-20
Sample Output 2:
False
'''

x = int(input())

if (x > - 15 and x <= 12) or (x > 14 and x < 17) or (x >= 19):
    print('True')
else:
    print('False')


# 01_12_03 Задачи по материалам недели

'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и 
операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит 
результат на экран. Поддерживаемые операции: +, -, /, *, mod, pow, div, где 
mod — это взятие остатка от деления, 
pow — возведение в степень, 
div — целочисленное деление.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
Обратите внимание, что на вход программе приходят вещественные числа.
Sample Input 1:
5.0
0.0
mod
Sample Output 1:
Деление на 0!
Sample Input 2:
-12.0
-8.0
*
Sample Output 2:
96.0
Sample Input 3:
5.0
10.0
/
Sample Output 3:
0.5
'''

a = float(input())
b = float(input())
oper = str(input())

if (oper == '/' or oper == 'mod' or oper == 'div') and b == 0:
    print('Деление на 0!')
elif oper == '+':
    print(a + b)
elif oper == '-':
    print(a - b)
elif oper == '/':
    print(a / b)
elif oper == '*':
    print(a * b)
elif oper == 'mod' and b != 0:
    print(a % b)
elif oper == 'pow':
    print(a ** b)
elif oper == 'div' and b != 0:
    print(a // b)


# 01_12_04 Задачи по материалам недели

'''
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. 
Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и 
соответствующие параметры, которая бы выводила площадь получившейся комнаты. 
Для числа π в стране Малевии используют значение 3.14.
Формат ввода, который используют Малевийцы:
треугольник
a
b
c
где a, b и c — длины сторон треугольника
прямоугольник
a
b
где a и b — длины сторон прямоугольника
круг
r
где r — радиус окружности
Sample Input 1:
прямоугольник
4
10
Sample Output 1:
40.0
Sample Input 2:
круг
5
Sample Output 2:
78.5
Sample Input 3:
треугольник
3
4
5
Sample Output 3:
6.0
'''

figure = str(input())

if figure == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif figure == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a* b)
elif figure == 'круг':
    r = float(input())
    print(3.14 * r**2)


# 01_12_05 Задачи по материалам недели

'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки 
сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.
Sample Input 1:
8
2
14
Sample Output 1:
14
2
8
Sample Input 2:
23
23
21
Sample Output 2:
23
21
23
'''

a = int(input())
b = int(input())
c = int(input())

if a >= b and b >= c:
    print(a)
    print(c)
    print(b)
elif a >= c and c >= b:
    print(a)
    print(b)
    print(c)
elif b >= a and a >= c:
    print(b)
    print(c)
    print(a)
elif b >= c and c >= a:
    print(b)
    print(a)
    print(c)
elif c >= a and a >= b:
    print(c)
    print(b)
    print(a)
elif c >= b and b >= a:
    print(c)
    print(a)
    print(b)


# 01_12_06 Задачи по материалам недели

'''
В институте биоинформатики по офису передвигается робот. 
Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".
Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.
Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.
Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. 
Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из случаев входных данных (число программистов 0≤n≤1000). 
Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания. 
Так как задание повышенной сложности, вручную код решений проверяться не будет. 
Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы используете только русские символы для ответа. В остальных случаях ищите ошибку в логике работы программы.
Sample Input 1:
5
Sample Output 1:
5 программистов
Sample Input 2:
0
Sample Output 2:
0 программистов
Sample Input 3:
1
Sample Output 3:
1 программист
Sample Input 4:
2
Sample Output 4:
2 программиста
'''

n = int(input())

ending = 'ов'

if (n % 100 == 11) or (n % 100 == 12) or (n % 100 == 13) or (n % 100 == 14):
    ending == 'ов'
elif n % 10 == 1:
    ending = ''
elif (n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4):
    ending = 'а'
else:
    ending == 'ов'

print(str(n) + ' программист' + ending)



# 01_12_07 Задачи по материалам недели

'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
Sample Input 1:
090234
Sample Output 1:
Счастливый
Sample Input 2:
123456
Sample Output 2:
Обычный
'''

ticketNumber = int(input())

number1 = int((ticketNumber // 10e4) % 10e0)
number2 = int((ticketNumber // 10e3) % 10e0)
number3 = int((ticketNumber // 10e2) % 10e0)
number4 = int((ticketNumber // 10e1) % 10e0)
number5 = int((ticketNumber // 10e0) % 10e0)
number6 = int((ticketNumber // 10e-1)% 10e0)

if (number1 + number2 + number3) == (number4 + number5 + number6):
	print('Счастливый')
else:
	print('Обычный')


# 02_04_07 Строки и символы

'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.
Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод.
Кодирование должно учитывать регистр символов.
Sample Input 1:
aaaabbcaa
Sample Output 1:
a4b2c1a2
Sample Input 2:
abc
Sample Output 2:
a1b1c1
'''

# Решение с костылем
'''
string = input()
newString = string + ' ' # Дописываем пробел в конец строки
counter = 1
for i in range(len(newString)):
    if newString[i] == ' ': # Если в итерации встречается дописанный пробел, завершаем цикл
        break
    elif newString[i] == newString[i+1]:
        counter += 1
    else:
        print(newString[i] + str(counter), end='')
        counter = 1
'''

# Решение без костыля

string = input()
counter = 1
i = 0

while (i + 1) < len(string): # Проверяем, не последний ли символ, чтобы избежать out of range
    if string[i] == string[i+1]:
        counter += 1
    else:
        print(string[i] + str(counter), end='')
        counter =1

    i += 1
# Т.к. последняя последовательность отсекается, чтобы не случилось out of range, выводим остаток принудительно
print(string[i] + str(counter))

# Элегантное решение с побуквенным сравнением
'''
message = str(input())
cnt = 1
x = 1
j = message[x:x+1]
for i in message:
    if i in j:
        cnt += 1
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1
    x += 1
    j = message[x:x+1]
'''

# 02_05_10 Списки

'''
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
Sample Input 1:
1 3 5 6 10
Sample Output 1:
13 6 9 15 7
Sample Input 2:
10
Sample Output 2:
10
'''

string = [int(i) for i in input().split()]
#string = [1, 3, 5, 6, 10] # Expected output is "13 6 9 15 7"
newString = [0 for i in range(len(string))]

if len(string) == 1:
    print(string[0])
else:
    for i in range(len(string)):
        if i + 1 < len(string):
            newString[i] = string[i-1] + string[i+1]
        else:
            newString[i] = string[i-1] + string[0]

    for _ in range(len(newString)):
        print(str(newString[_]) + ' ', end='')

# Элегантное решение с отрицательной длиной списка
'''
initial_list = [1, 3, 5, 6, 10]
sum_list = []
left_index = -1
right_index = -len(initial_list) + 1
middle_index = 0
while middle_index < len(initial_list):
    print(left_index, right_index)
    sum_list.append(initial_list[left_index] + initial_list[right_index])
    left_index += 1
    right_index += 1
    middle_index += 1
print(sum_list)
'''

# 02_05_11 Списки

'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
Sample Input 1:
4 8 0 3 4 2 0 3
Sample Output 1:
0 3 4
Sample Input 2:
10
Sample Output 2:
Sample Input 3:
1 1 2 2 3 3
Sample Output 3:
1 2 3
Sample Input 4:
1 1 1 1 1 2 2 2
Sample Output 4:
1 2
'''

string = [int(i) for i in input().split()]
#string = [4, 8, 0, 3, 4, 2, 0, 3]
#string = [1 ,1 ,1 ,1 ,1 ,2, 2, 2]
#newString = [0 for i in range(len(string))]
newString = []
i = 0

string.sort()

while i+1 < len(string):
    if string[i] == string[i+1]:
        if string[i] in newString:
            i += 1
            continue
        newString.append(string[i])
    i += 1

for _ in newString:
    print(_, end=' ')

# 02_06_07 Задачи по материалам недели

'''
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.
Sample Input:
1
-3
5
-6
-10
13
4
-8
Sample Output:
340
'''

inputSum = int(input())
numbers = []
numbers.append(inputSum)

while inputSum != 0:
    number = int(input())
    numbers.append(number)
    inputSum += number

squaresSum = 0

for i in numbers:
    squaresSum += i*i

print(squaresSum)

# 02_06_08 Задачи по материалам недели

'''
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся положительное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
Sample Input:
7
Sample Output:
1 2 2 3 3 3 4
'''

# Не самое лучшее решение, т.к. место в памяти будет отводиться под больший список, чем выведется в итоге
# Необходима оптимизация (201707211347)

n = int(input())
numbers = []

for i in range(n+1):
    for j in range(i):
        numbers.append(str(i))

for i in range(n):
    print(numbers[i], end=' ')

# 02_06_09 Задачи по материалам недели

'''
Напишите программу, которая считывает список чисел lst из первой строки и число xx из второй строки, которая выводит все позиции, на которых встречается число xx в переданном списке lst.
Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
Sample Input 1:
5 8 2 7 8 8 2 4
8
Sample Output 1:
1 4 5
Sample Input 2:
5 8 2 7 8 8 2 4
10
Sample Output 2:
Отсутствует
'''

lst = [int(i) for i in input().split()]
x = int(input())

for i in range(len(lst)):
	if x == lst[i]:
		print(i, end=' ')

if x not in lst:
    print('Отсутствует')

# 02_06_10 Задачи по материалам недели

'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). 
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1
Sample Input 2:
1
end
Sample Output 2:
4
'''

row = ''
matrix = []

while True:
    row = input()
    if row == 'end':
        break
    matrix.append([int(i) for i in row.split()])

ai = len(matrix)
aj = len(matrix[0])

newMatrix = [
    [(matrix[i - 1][j] + matrix[(i + 1) % ai][j] + matrix[i][j - 1] + matrix[i][(j + 1) % aj])
     for j in range(aj)]
    for i in range(ai)]

for i in range(ai):
    for j in range(aj):
        print(newMatrix[i][j], end=' ')
    print()

# 02_06_11 Задачи по материалам недели

'''
Дополнительная
Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''

n = int(input())

x = 0
y = 0
dx = 1
dy = 0

# Инициализация квадратной матрицы nxn с элементами типа None
matrix = [[None] * n for _ in range(n)]

for i in range(1, n**2+1):
    matrix[x][y] = i
    nx = x + dx
    ny = y + dy
    # Проверяем, не вышла ли позиция за границы и не занята ли уже ячейка
    if (0 <= nx < n) and (0 <= ny < n) and (not matrix[nx][ny]):
        x = nx
        y = ny
    else:
        #dx, dy = -dy, dx
        # Если позиция за границей и ячейка не пуста, разворачиваем матрицу на 90 градусов
        swap = -dy
        dy = dx
        dx = swap
        x = x + dx
        y = y + dy

# Выводим заполненную матрицу
for y in range(n):
    for x in range(n):
        print(matrix[x][y], end = ' ')
    print()

# 03_01_09 Функции

'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два.
Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]
lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]
Функция не должна осуществлять ввод/вывод информации.
'''

def modify_list(l):

    list = []

    for element in l:
        if element % 2 == 0:
            list.append(element // 2)

    l.clear()
    l += list

'''
def modify_list(l):
    last_index = len(l) - 1
    i = last_index
    while i != -1:
        if l[i] % 2 != 0:
            l.remove(l[i])
        else:
            l[i] = l[i] // 2
        i -= 1
'''

# 03_02_05 Словари

'''
Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value.
Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2⋅key. Если и ключа 2⋅key нет, то нужно добавить ключ 2⋅key в словарь и сопоставить ему список из переданного элемента [value].
Требуется реализовать только эту функцию, кода вне неё не должно быть.
Функция не должна вызывать внутри себя функции input и print.
Пример работы функции:
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''

def update_dictionary(d, key, value):
    if key in d:
        list = d[key]
        list.append(value)
        d[key] = list
    elif key not in d:
        new_key = key * 2
        if new_key in d:
            list = d[new_key]
            list.append(value)
            d[new_key] = list
        elif new_key not in d:
            list = [value]
            d[new_key] = list

'''
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2*key in d:
        d[2*key].append(value)
    else:
        d[2*key]=[value]
'''

# 03_02_06 Словари

'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.
Sample Input 1:
a aa abC aa ac abc bcd a
Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2
Sample Input 2:
a A a
Sample Output 2:
a 3
'''

strng = input()
d = {}

string = strng.lower().split()

for word in string:
    if word not in d:
        d[word] = 1
    elif word in d:
        d[word] +=1

for key, value in d.items():
    print(key + ' ' + str(value))

# 03_02_07 Словари

'''
Имеется реализованная функция f(x), принимающая на вход целое число x, которая вычисляет некоторое целочисленое значение и возвращает его в качестве результата работы.
Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только от переданного аргумента x.
Напишите программу, которой на вход в первой строке подаётся число n — количество значений x, для которых требуется узнать значение функции f(x), после чего сами эти n значений, каждое на отдельной строке. Программа должна после каждого введённого значения аргумента вывести соответствующие значения функции f на отдельной строке.
Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по времени исполнения кода на тесте.
Sample Input:
5
5
12
9
20
12
Sample Output:
11
41
47
61
41
'''

# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
d = {}
n = int(input())

for i in range(n):
    x = int(input())
    if x in d:
        print(d[x])
    elif x not in d:
        function = f(x)
        d[x] = function
        print(d[x])

'''
n=int(input())
d={}
for i in range(n):
    x=int(input())
    if x not in d:
        d[x]=f(x)
    print(d[x])
'''

# 03_04_02 Файловый ввод/вывод

'''
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Sample Input:
a3b4c2e10b1
Sample Output:
aaabbbbcceeeeeeeeeeb
'''
# o10l11Y19t19C6u14p7J19S18b7T16B6s9k10N19C4X9v11t5e2o15W18
# o10l11y19t19c6u14p7j19s18b7t16b6s9k10n19c4x9v11t5e2o15w18

# test_string = 'a12b10c3d1'

digits = set('0123456789')
i = 0
multiplier = ''
decrypted = ''

with open('03_04_02_input.txt') as in_f_obj:
    string = in_f_obj.readline().strip()

char = string[i]
i += 1

while i < len(string):

    while string[i] in digits:
        multiplier += string[i]
        i += 1
        if i > (len(string) - 1):
            break

    # print(char * int(multiplier), end='')
    decrypted += (char * int(multiplier))

    multiplier = ''
    if i > (len(string) - 1):
        break
    char = string[i]

    i += 1

with open('03_04_02_ouput.txt', 'w') as out_f_obj:
    out_f_obj.write(decrypted)

'''
03_04_02_input.txt
L17Y9C17L1W14X5e1H1s8w9r16K15p15A3o17k11E11S12G11C17r19z11R10y19

03_04_02_ouput.txt
LLLLLLLLLLLLLLLLLYYYYYYYYYCCCCCCCCCCCCCCCCCLWWWWWWWWWWWWWWXXXXXeHsssssssswwwwwwwwwrrrrrrrrrrrrrrrrKKKKKKKKKKKKKKKpppppppppppppppAAAoooooooooooooooookkkkkkkkkkkEEEEEEEEEEESSSSSSSSSSSSGGGGGGGGGGGCCCCCCCCCCCCCCCCCrrrrrrrrrrrrrrrrrrrzzzzzzzzzzzRRRRRRRRRRyyyyyyyyyyyyyyyyyyy
'''

# 03_04_03 Файловый ввод/вывод

'''
Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.
Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
'''

dictionary = {}

with open('03_04_03_input.txt') as in_f_obj:
    for line in in_f_obj:
        line = line.lower()
        for word in line.split():
            if word not in dictionary:
                dictionary[word] = 1
            elif word in dictionary:
                dictionary[word] += 1

max_quantity = 1

for key, value in dictionary.items():
    current_quantity = dictionary[key]
    if current_quantity > max_quantity:
        max_quantity = current_quantity
        word_with_max_quantity = key

with open('output_3.4.3.txt', 'w') as out_f_obj:
    most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
    out_f_obj.write(most_popular)


# 03_04_04 Файловый ввод/вывод

'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''

averages = []
marks_math = []
marks_phys = []
marks_rus = []
counter = 0
value01 = 0
value02 = 0
value03 = 0

with open('03_04_04_input.txt') as in_f_obj:
    for line in in_f_obj:
        line = line.rstrip().split(';')
        student_average = ((int(line[1]) + int(line[2]) + int(line[3])) / 3)
        averages.append(student_average)
        marks_math.append(int(line[1]))
        marks_phys.append(int(line[2]))
        marks_rus.append(int(line[3]))
        counter += 1

with open('output_3.4.4.txt', 'w') as out_f_obj:
    for _ in averages:
        out_f_obj.write(str(_) + '\n')

    for _ in marks_math:
        value01 += int(_)
    for _ in marks_phys:
        value02 += int(_)
    for _ in marks_rus:
        value03 += int(_)
    average_math = value01 / counter
    average_phys = value02 / counter
    average_rus = value03 / counter

    out_f_obj.write(str(average_math) + ' ' + str(average_phys) + ' ' + str(average_rus))

print(average_math)
print(average_phys)
print(average_rus)
print()

# 03_05_03 Модули, подключение модулей

'''
Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.
Пример работы программы:
> python3 my_solution.py arg1 arg2
arg1 arg2
'''

import sys

for i in range(1, len(sys.argv)):
	print(sys.argv[i], end = ' ')

'''
import sys
print(*sys.argv[1:])
'''

# 03_06_02 Установка дополнительных модулей

'''
Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.
Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям). 
После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.
В поле ответа введите одно число или отправьте файл, содержащий одно число.
'''

import requests

with open('03_06_02_input.txt') as in_f_obj:
	url = in_f_obj.read().strip()

r = requests.get(url)
counter = 0

for line in r.text.splitlines():
	counter += 1

# Цикл выше можно заменить более простой конструкцией
# print(len(r.text.splitlines()))

with open('03_06_02_output.txt', 'w') as out_f_obj:
	out_f_obj.write(str(counter))

'''
03_06_02_input.txt
https://stepic.org/media/attachments/course67/3.6.2/895.txt

03_06_02_output.txt
237
'''

# 03_06_03 Установка дополнительных модулей

'''
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора. 
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое последнего файла из набора, как ответ на это задание.
'''

import requests

url_pattern = 'https://stepik.org/media/attachments/course67/3.6.3/'

with open('03_06_03_input.txt') as in_f_obj:
	url = in_f_obj.read().strip()

counter = 0


while True:
	r = requests.get(url)
	if 'We' in str(r.text.strip()):
		break
	url = url_pattern + str(r.text.strip())
	#print(str(counter) + ' ' + url)
	#counter += 1

text = r.text.strip()

with open('03_06_03_output.txt', 'w') as out_f_obj:
	out_f_obj.write(text)

'''
with open('test.txt') as f_obj:
	text = f_obj.read().strip()
print()
print('*' * 40)
print(text)
print()
print(text[:2])
print('*' * 40)
with open('ntest.txt') as f_obj:
	text = f_obj.read().strip()
print()
print('*' * 40)	
print(text)
print()
print(text[:2])
if 'We' in text:
	print(True)
print('*' * 40)
'''

'''
03_06_03_input.txt
https://stepic.org/media/attachments/course67/3.6.3/699991.txt

03_06_03_output.txt
We are the champions, my friends,
And we'll keep on fighting 'til the end.
We are the champions.
We are the champions.
No time for losers
'Cause we are the champions of the world.
'''

# 03_07_01 Задачи по материалам недели

'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
'''

n = int(input())

teams = {}
games = 1
wins = 0
draws = 0
loses = 0
points = 0
# team_list = [games, wins, draws, loses, points]

i = 0

for _ in range(n):

    string = input().split(';')

    # Проверка наличия команд из ввода в словаре
    # если нет, добавляем
    # если есть, увеличиваем количество игр на 1

    # Проверка наличия первой команды из ввода в словаре
    if string[i] not in teams:
        teams[string[i]] = [games, wins, draws, loses, points]
    elif string[i] in teams:
        teams[string[i]][0] += 1

    # Проверка наличия второй команды из ввода в словаре
    if string[i + 2] not in teams:
        teams[string[i + 2]] = [games, wins, draws, loses, points]
    elif string[i + 2] in teams:
        teams[string[i + 2]][0] += 1

    # Проверка результатов матча

    if string[i + 1] > string[i + 3]:
        teams[string[i]][1] += 1  # Начисление победы для К1
        teams[string[i]][4] += 3  # Начисление очков победы для К1
        teams[string[i + 2]][3] += 1  # Начисление поражения для К2
        teams[string[i + 2]][4] += 0  # Начисление очков поражения для К2
    elif string[i + 1] < string[i + 3]:
        teams[string[i + 2]][1] += 1  # Начисление победы для К2
        teams[string[i + 2]][4] += 3  # Начисление очков победы для К2
        teams[string[i]][3] += 1  # Начисление поражения для К1
        teams[string[i]][4] += 0  # Начисление очков поражения для К1
    elif string[i + 1] == string[i + 3]:
        teams[string[i]][2] += 1  # Начисление ничьей для К1
        teams[string[i]][4] += 1  # Начисление очков ничьей для К1
        teams[string[i + 2]][2] += 1  # Начисление ничьей для К2
        teams[string[i + 2]][4] += 1  # Начисление очков ничьей для К2

for key, value in teams.items():
    row = key + ':' + ' ' + str(value[0]) + ' ' + str(value[1]) + ' ' + str(value[2]) + ' ' + str(value[3]) + ' ' + str(
        value[4])
    print(row)

# 03_07_02 Задачи по материалам недели

'''
Дополнительная
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков. 
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи: 
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%
Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac
Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac
Sample Input 2:
dcba
badc
dcba
badc
Sample Output 2:
badc
dcba
'''

string = str(input())
cipher = str(input())

message_to_cipher = str(input())
cipher_to_message = str(input())
ciphered_message = ''
unciphered_message = ''

encryption = {}

# Наполняем шифровальный словарь
for i in range(len(string)):
    encryption[string[i]] = cipher[i]

# Зашифровываем сообщение по наполненному словарю
for i in range(len(message_to_cipher)):
    for key in encryption.keys():
        if message_to_cipher[i] == key:
            ciphered_message += encryption[key]

# Расшифровываем сообщение по наполненному словарю
for i in range(len(cipher_to_message)):
    for key, value in encryption.items():
        if cipher_to_message[i] == value:
            unciphered_message += key

print(ciphered_message)
print(unciphered_message)

#
a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))

#
# Считываем 4 строки в цикле
original, coding, first_string, second_string = (input() for i in range(4))

# По индексу символа из оригинала берём символ на замену из кодировки,
# для каждого символа из строки, которую нужно закодировать
print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# Аналогично, только наоборот :D
print(*[original[coding.find(symbol)] for symbol in second_string], sep='')

#
def code(source, end, data):
    ''' Data coder '''
    cryptData = ''
    for char in data:
        cryptData += end[source.index(char)]
    return cryptData

# Input data
key1 = input()
key2 = input()
decode = input()
encode = input()

print(code(key1, key2, decode))
print(code(key2, key1, encode))

#
class Encryption():
    def __init__(self, letters, replacement):
        self.encr_dic = {letters[i]: replacement[i] for i in range(len(letters))}
        self.decr_dic = {replacement[i]: letters[i] for i in range(len(letters))}

    def encrypt(self, string):
        return ''.join(self.encr_dic[i] for i in string)

    def decrypt(self, string):
        return ''.join(self.decr_dic[i] for i in string)


ans = Encryption(input(), input())
print(ans.encrypt(input()))
print(ans.decrypt(input()))

#
def decode(dictionary, mes):
    return ''.join(str(dictionary[ch]) for ch in mes)

a, b, c, d = input(), input(), input(), input()
print(decode(dict(zip(a, b)), c))
print(decode(dict(zip(b, a)), d))

#
a1=input()
a2=input()
print(''.join([a2[a1.find(s)] for s in input()]))
print(''.join([a1[a2.find(s)] for s in input()]))

# 03_07_03 Задачи по материалам недели

'''
Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.
Напишем подобную систему.
Через стандартный ввод подаётся следующая структура: первой строкой — количество dd записей в списке известных слов, после передаётся  dd строк с одним словарным словом на строку, затем — количество ll строк текста, после чего — ll строк текста.
Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa
Sample Output:
aab
aba
c
aaa
'''

d = int(input())
# words = []
words = set()
# unknow_words = []
unknow_words = set()

for _ in range(d):
    # words.append(input().lower())
    words.add(input().lower())

l = int(input())

for _ in range(l):
    string = input().lower().split()

    for i in range(len(string)):
        if string[i] not in words:
            # unknow_words.append(string[i])
            unknow_words.add(string[i])

for word in unknow_words:
    print(word)


#
dic = {input().lower() for i in range(int(input()))}

wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

print(*wrd.difference(dic), sep="\n")

#
count_dict = int(input())
dict = []
check_words = []
result = []

#заполняем словарь
for i in range(count_dict):
  dict.append(input().lower())


count_lines = int(input())

#заполняем список проверяемых слов
for i in range(count_lines):
  check_words += input().lower().strip().split(' ')


#выбираем слова которые не проходят проверку
for i in check_words:
  if i not in dict and i not in result:
    result.append(i)


#печатаем
for i in result:
  print(i)

#
words = set(input().lower() for i in range(int(input())))
text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
print('\n'.join(text - words))


# 03_07_04 Задачи по материалам недели

'''
Группа биологов в институте биоинформатики завела себе черепашку.
После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное расстояние в сантиметрах, которое должна пройти черепашка.
Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, что можно написать программу, которая определит, куда в итоге биологи приведут черепашку. Для этого программисты просят вас написать программу, которая выведет точку, в которой окажется черепашка после всех команд. Для простоты они решили считать, что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.
Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, после чего nn строк с самими командами. Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. Все координаты целочисленные.
Sample Input:
4
север 10
запад 20
юг 30
восток 40
Sample Output:
20 -20
'''

n = int(input())
movement = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}


for _ in range(n):
    direction = input().split()
    if direction[0] in movement:
        movement[direction[0]] += int(direction[1])

x = movement['восток'] - movement['запад']
y = movement['север'] - movement['юг']

print(x, y)

#
n=int(input())
d={'север':0,'запад':0,'юг':0,'восток':0}
for i in range(n):
    x=input().split()
    d[x[0]]+=int(x[1])
print(d['восток']-d['запад'], d['север']-d['юг'])

#
dict = {'север': 0, 'юг': 0, 'запад': 0, 'восток': 0}

for _ in range(int(input())):
    key, value = input().split()
    dict[key] += int(value)

print(dict['восток'] - dict['запад'], dict['север'] - dict['юг'])

#


# 03_07_05 Задачи по материалам недели

'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк, например:
Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
'''

class_rawinfo = {}
#new_heights = 0
#new_students = 0
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
#class_info = []

with open('03_07_05_input.txt') as in_f_obj:
	for line in in_f_obj:
		#print(line)
		string = line.rstrip().split('\t')
		#print(string)
#n = int(input())
#for _ in range(n):
	#string = input().split('	')
		if string[0] not in class_rawinfo:
			class_rawinfo[string[0]] = [int(string[2]), 1]
		elif string[0] in class_rawinfo:
			heights = class_rawinfo[string[0]][0] + int(string[2])
			students = class_rawinfo[string[0]][1] + 1
			class_rawinfo[string[0]] = [heights, students]

for k, v in class_rawinfo.items():
	#print(k, str(v[0] / v[1]))
	#list.pop([int(k)-1])
	class_info[int(k)-1] = v[0] / v[1]
	#print(class_rawinfo)
	#print(class_info)

with open('03_07_05_output.txt', 'w') as out_f_obj:
	for i in range(len(class_info)):
		#print(i+1, str(class_info[i]))
		output = str(i+1) + ' ' + str(class_info[i]) + '\n'
		#print(output)
		out_f_obj.write(output)


