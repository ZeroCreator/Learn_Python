# Анонимные (lambda) функции.
a = [4, 5, lambda: print("lambda"), 7, 8]
print(a[2])
a[2]()

lst = [5, 3, 0, -6, 8, 10, 1]

def get_filter(a, filter=None):
    if filter is None:
        return a

    res = []
    for x in a:
        if filter(x):
            res.append(x)


    return res


r = get_filter(lst)
print(r)

r = get_filter(lst, lambda x: x % 2 == 0)
print(r)

r = get_filter(lst, lambda x: x > 0)
print(r)

r = get_filter(lst, lambda x: x < 0)
print(r)


#
print("Tasks")
# Объявите анонимную (лямбда) функцию с одним параметром для возведения числа в квадрат.
# Присвойте эту функцию переменной get_sq.
get_sq = lambda x: x**2


# Объявите анонимную (лямбда) функцию с двумя параметрами для деления одного целого числа на другое.
# Если происходит деление на ноль, то функция должна возвращать значение None, иначе - результат деления.
get_div = lambda a, b: None if b == 0 else a/b

#
get_div = lambda x, y: x / y if y else None

#
get_div = lambda x, y: x / y if y != 0 else None


# Объявите анонимную (лямбда) функцию для вычисления модуля числа (то есть, отрицательные числа нужно делать положительными).
# Вызовите эту функцию для введенного числа x:
# x = float(input())
x = float(input())
get_div = lambda x: -x if x < 0 else x
print(get_div(x))

#
x = float(input())
foo = lambda a: abs(a)
print(foo(x))

#
x = float(input())
get_abs = lambda x: x if x >= 0 else x - 2 * x
print(get_abs(x))


# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "ra". То есть,
# функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном случае.
# Вызовите эту функцию для введенной строки s:
# s = input()
s = input()
get_ra = lambda x: 'ra' in s
print(get_ra(s))

#
print((lambda x: 'ra' in x)(input()))

#
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

lst = list(map(int, input().split()))


print(*filter_lst(lst))
print(*filter_lst(lst, lambda x: x < 0))
print(*filter_lst(lst, lambda x: x > -1))
print(*filter_lst(lst, lambda x: x > 2 and x < 6))

#
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

lst = list(map(int, input().split()))
lambda_list = [None, lambda x: x < 0, lambda x: x >= 0, lambda x: 3 <= x <= 5]
for l in lambda_list:
    print(*filter_lst(lst, l))


#
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

it = [int(i) for i in input().split()]

print(*filter_lst(it))
print(*filter_lst(it, key=lambda x: x < 0))
print(*filter_lst(it, key=lambda x: x >= 0))
print(*filter_lst(it, key=lambda x: 3 <= x <= 5))