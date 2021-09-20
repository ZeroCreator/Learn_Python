# Именованные аргументы. Фактические и формальные параметры.
print("Именованные аргументы")
def get_V(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")
    return a + b + c

v = get_V(b=1, a=2, c=3)
print(v)

v = get_V(1, c=2, b=3)
print(v)

v = get_V(1, 2, c=3)
print(v)


print("Параметры со значением по умолчанию - формальные")
# a, b, c - фактические параметры, verbose - формальные параметры
def get_V(a, b, c, verbose=True ):
    if verbose:
        print(f"a = {a}, b = {b}, c = {c}")
    return a + b + c

v = get_V(1, 2, 3)
print(v)

v = get_V(1, 2, 3, verbose=False)
print(v)

# Учитывать регистр Python == PYTHON
# Учитывать пробелы до и после  " Python" == "PYTHON"
def cmp_str(s1, s2, reg=False, trim = True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip()
        s2 = s2.strip()

    return  s1 == s2

print(cmp_str("Python ", "Python"))
print(cmp_str("Python ", "Python", trim=False))
print(cmp_str("Python ", "PYTHON"))
print(cmp_str("Python ", "PYTHON", True))
print(cmp_str("Python ", "PYTHON", reg=True))

def add_value(value, lst=[]):
    lst.append(value)
    return lst

l = add_value(1)
l1 = add_value(2)
print(l)
print(l1) # [1, 2]



def add_value(value, lst=None):
    if lst is None:
        lst = []

    lst.append(value)
    return lst

l3 = add_value(1)
l4 = add_value(2, l)
print(l3) # [1]
print(l4) # [2]

#
print("Tasks")
# Объявите функцию с именем get_rect_value, которая принимает два аргумента (два числа) и еще один формальный параметр
# type с начальным значением 0. Если параметр type равен нулю, то функция должна возвращать периметр прямоугольника,
# а иначе - его площадь.
def get_rect_value(a, b, type=0):
    if type == 0:
        p = (a ** 2 + b ** 2)**0.5
        return a + b + p
    else:
        p = (a + b + type) / 2
        return (p * (p - a) * (p - b) * (p - type))**0.5



# Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль) и имеет один формальный
# параметр chars с начальным значением в виде строки "$%!?@#". Функция должна проверять: есть ли в пароле хотя бы один
# символ из chars и что длина пароля не менее 8 символов. Если проверка проходит, то функция возвращает True, иначе - False.
def check_password(password, chars="$%!?@#"):
    t = 0
    for i in password:
        if i in chars:
            t += 1
    if t >= 1 and len(password) >= 8:
        return True
    return False

#
def check_password(st, chars='$%!?@#'):
    return len(st) >= 8 and any(i in chars for i in st)

# Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, используя следующий словарь
# для замены русских букв на соответствующее латинское написание:
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
# Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную строку перевести в нижний
# регистр - малые буквы). У функции также определить формальный параметр sep с начальным значением в виде строки "-".
# Он будет определять символ для замены пробелов в строке.
# После объявления функции прочитайте (с помощью функции input) строку и дважды вызовите функцию (с выводом результата
# ее работы на экран):
# - первый раз только со строкой
# - второй раз со строкой и именованным аргументом sep со значением '+'.
