# Оператор return.
def send_mail(from_name, old ):
    text = f"""Hello!
Ваш навсегда{from_name}! 
И не судите строго, мне всего {old} лет!"""
    print(text)


def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    print(x)
    return res
    print(x)

a = get_sqrt(49)
print(a)

def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res, x # кортеж с данными

a = get_sqrt(49)
print(a)

# Функция максимальное из двух значений
print("Функция максимальное из двух значений")
def get_max2(a, b):
    return a if a > b else b

x, y, z = 5, 7, 10
print(get_max2(x, get_max2(y, z)))

# Функциональный подход в программировании
print("Функциональный подход в программировании")
# Нахождение максимума из трех чисел
print("Нахождение максимума из трех чисел")
def get_max3(a, b, c):
    return get_max2(a, get_max2(b, c))

x, y, z = 5, 7, 10
print(get_max3(x, y, z))


PERIMETR = True
if PERIMETR:
    get_rect = 1
else:
    get_rect = 2

print(get_rect)


PERIMETR = True
if PERIMETR:
    def get_rect(a, b):
        return 2 * (a + b)
else:
    def get_rect(a, b):
        return a * b

print(get_rect(1.5, 3.8))


def get_rect(a, b):
    return 2 * (a + b)

def get_rect(a, b):
    return a * b

print(get_rect(1.5, 3.8)) # будет ссылаться на последнюю функцию

# Функция для определения четности числа
def even(x):
    return x % 2 == 0

for i in range(1, 20):
    if even(i):
        print(i, end=" ")

print()

print("Tasks")
# Объявите функцию, которая принимает один аргумент (вещественное число), и возвращает квадрат этого числа.
# После объявления функции прочитайте (с помощью функции input) вещественное число и вызовите функцию с этим значением.
# Выведите на экран результат работы функции.
def foo(x):
    return x**2

print(foo(float(input())))

#
ff = lambda x: x**2

print(ff(float(input())))


#  Объявите функцию с именем is_triangle, которая принимает три стороны треугольника (целые числа) и проверяет,
#  можно ли из переданных аргументов составить треугольник. (Напомню, что у любого треугольника длина третьей стороны
#  всегда должна быть меньше суммы двух других). Если  проверка проходит, вернуть булево значение True, иначе - значение False.
def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False


#
def is_triangle(a, b, c):
    return a < b + c and b < a + c and c < a + b


#
def is_triangle(a, b, c):
    a, b, c = sorted((a, b, c)) # в скобках кортеж
    return c < a + b


# Объявите функцию с именем is_large, которая принимает строку (в качестве аргумента) и возвращает False, если длина
# строки меньше трех символов. Иначе возвращается значение True.
def  is_large(str):
    return len(str) >= 3



# Объявите функцию для проверки числа на четность (возвращается True, если переданное число четное и False, если число нечетное).
#
# После объявления функции в цикле необходимо считывать целое числовое значение (функцией input), пока не поступит число 1.
# Если прочитанное значение четное (проверяется с помощью заданной функции), то оно выводится на экран (в столбик, то есть,
# каждое значение с новой строки).
def  set_num(n):
    t = []
    while n != 1:
        t.append(n)
        n = int(input())
    return t


def even(t):
    for i in t:
        if i % 2 == 0:
            print(i)


even(set_num(int(input())))


#
def is_even(n):
    return not n % 2

n = int(input())

while n != 1:
    if is_even(n):
        print(n)
    n = int(input())


#
def check_parity_number(number):
    return number % 2 == 0

n = int(input())
while n != 1:
    if check_parity_number(n):
        print(n)
    n = int(input())


#
def is_even(n):
    return n % 2 == 0


n = int(input())
while n != 1:
    if is_even(n):
        print(n)
    n = int(input())


# Объявите функцию для проверки числа на нечетность (возвращается True, если переданное число нечетное и False, если число четное).
# После объявления функции прочитайте (с помощью функции input) список целых значений, записанных в одну строку через пробел.
# И, используя генератор списков и созданную функцию, сформируйте список из нечетных значений на основе введенного исходного списка.
# Результат отобразите на экране командой:
# print(*lst)
# где lst - сформированный список из нечетных значений.
def even(n):
    return n % 2

print(*[i for i in map(int, input().split()) if even(i)])


#
def is_odd(n):
    return n % 2

lst = [i for i in map(int, input().split()) if is_odd(i)]

print(*lst)



# Вводится слово в переменную tp. Если это слово RECT, то следует объявить функцию с именем get_sq с двумя параметрами,
# вычисляющую площадь прямоугольника и возвращающую вычисленное значение. (На экран она ничего не должна выводить, только
# возвращать значение).
# Если же введенное слово не RECT (любое другое), то объявляется функция с тем же именем get_sq, с одним параметром для
# вычисления площади квадрата (формула: a*a). Вычисленное значение возвращается функцией. (Она также ничего не выводит на экран).
# Примечание: в программе должна быть задана только одна функция с именем get_sq в зависимости от введенного слова.
# Вызывать функцию не нужно, только объявлять.
tp = input().strip()

def get_sq(a, b=0):
    return a * b if tp == "RECT" else a * a


#
tp = input().strip()

def get_sq(*a):
    return a[0] * a[-1]


#
tp = input().strip()

if tp == 'RECT':
    def get_sq(a, b):
        return a * b
else:
    def get_sq(a):
        return a * a


#
type = input().strip()

if type == 'RECT':
    get_sq = lambda a, b: a * b
else:
    get_sq = lambda a: a * a


# Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает False, если длина строки меньше 6 символов.
# Иначе возвращается значение True.
# После объявления функции прочитайте (с помощью функции input) список названий городов, записанных в одну строку через
# пробел. Затем, используя генератор списка и созданную функцию, сформируйте список из названий городов длиной не менее
# шести символов на основе введенного исходного списка. Результат отобразите на экране командой:
# print(*lst)
# где lst - итоговый сформированный список.
def is_len(n):
    return len(n) >= 6


print(*[i for i in input().split() if is_len(i)])


#
def len_(lst):
    return [x for x in lst if len(x) >= 6]


print(*len_(input().split()))


# Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает два значения в виде кортежа: переданная
# строка и ее длина.
# После объявления функции прочитайте (с помощью функции input) список названий городов, записанных в одну строку через
# пробел. Затем, используя генератор словарей и созданную функцию, сформируйте словарь d в формате:
# d = {<город 1>: <число символов>, ..., <город N>: <число символов>}
# Выведите этот словарь в порядке возрастания длин строк с помощью команд:
# a = sorted(d, key=lambda x: d[x])
# print(*a)
def length(st):
    return st, len(st)


d = {length(x)[0]: length(x)[1] for x in input().split()}
print(*sorted(d, key=lambda x: d[x]))


#
def length(word):
    return word, len(word)


d = {length(x)[0]: length(x)[1] for x in input().split()}
print(*sorted(d, key=lambda x: d[x]))


# Вводится список целых чисел в одну строчку через пробел. Необходимо задать функцию, которая принимает два аргумента
# (максимальное и минимальное значения из списка) и возвращает их произведение. Вызовите эту функцию и отобразите на
# экране полученное числовое значение.
# Подсказка: для передачи аргументов функции используйте функции max и min для введенного списка чисел.
t = list(map(int, input().split()))
min_sp = min(*t)
max_sp = max(*t)


def length(min_sp, max_sp):
    return min_sp * max_sp


print(length(min_sp, max_sp))


#
def min_max(a, b):
    return a * b

lst = list(map(int, input().split()))

print(min_max(min(lst), max(lst)))


#
def multiply_max_min(max_x, min_x):
    return max_x * min_x

lst = list(map(int, input().split()))
print(multiply_max_min(max(lst), min(lst)))


#
def foo(lst):
    return min(lst) * max(lst)


print(foo(list(map(int, input().split()))))







