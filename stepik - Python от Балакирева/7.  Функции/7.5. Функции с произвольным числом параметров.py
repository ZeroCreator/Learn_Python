# Функции с произвольным числом параметров.
# * -  оператор упаковки аргументов
print("Фактические параметры")
def os_path(*args):
    path = "\\".join(args)
    return path

p = os_path("F:\\~stepik.org", "Добрый, добрый Python (Питон)", "39\\p39. Функции.docx")
print(p)

print("Формальные параметры")
def os_path(*args, sep='\\'):
    path = sep.join(args)
    return path

p = os_path("F:\\~stepik.org", "Добрый, добрый Python (Питон)", "39\\p39. Функции.docx")
print(p)


def os_path(*args, **kwargs):
    print(kwargs)

p = os_path("F:\\~stepik.org", "Добрый, добрый Python (Питон)", "39\\p39. Функции.docx", sep='/', trim=True)
# *args - кортеж
# **kwargs - словарь
def os_path(disk, *args, sep='\\', **kwargs):
    args = (disk, ) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]
    path = sep.join(args)
    return path

p = os_path("F:", " ~stepik.org ", " Добрый, добрый Python (Питон) ", " 39\\p39. Функции.docx ", sep='/', trim=True)
print(p)


#
print("Tasks")
# Объявите функцию с именем get_even, которая принимает произвольное количество чисел в качестве аргументов и возвращает
# список, составленный только из четных переданных значений.
def get_even(*args):
    return (i for i in args if i % 2 == 0)

print(get_even(45, 4, 8, 11, 12, 0)) # 4 8 12 0

# Объявите функцию с именем get_biggest_city, которой можно передавать произвольное количество названий городов через
# аргументы. Данная функция должна возвращать название города наибольшей длины. Если таких городов несколько, то первый
# найденный (из наибольших). Программу реализовать без использования сортировки.
def get_biggest_city(*args):
    d = ""
    s = 0
    for i in args:
         if len(i) > s:
            d = i
            s = len(i)

    return d

#
def get_biggest_city(*lst):
    return max(lst, key=len)


# Объявите функцию с именем str_min, которая сравнивает две переданные строки и возвращает минимальную из них (то есть,
# выполняется лексикографическое сравнение строк). Затем, используя функциональный подход к программированию (то есть,
# более сложные функции реализуются путем вызова более простых), реализовать еще две аналогичные функции:
# - с именем str_min3 для поиска минимальной строки из трех переданных строк;
# - с именем str_min4 для поиска минимальной строки из четырех переданных строк.
def str_min(*args):
    return min(*args)

def str_min3(*args):
    return min(*args)

def str_min4(*args):
    return min(*args)

#
def str_min(s1, s2):
    return s1 if s1 < s2 else s2


def str_min3(s1, s2, s3):
    return s1 if s1 < str_min(s2, s3) else str_min(s2, s3)


def str_min4(s1, s2, s3, s4):
    return s1 if s1 < str_min3(s2, s3, s4) else str_min3(s2, s3, s4)

#
def str_min(first_string, second_string):
    return first_string if first_string < second_string else second_string


def str_min3(third_string, *args):
    return third_string if third_string < str_min(*args) else str_min(*args)


def str_min4(fourth_string, *args):
    return fourth_string if fourth_string < str_min3(*args) else str_min3(*args)



print(str_min("Питер", "Москва"))
print(str_min3("Питер", "Москва", "Самара"))
print(str_min4("Питер", "Москва", "Самара", "Воронеж"))