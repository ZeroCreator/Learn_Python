# Функции. Их объявление и вызов.
"""
f = print
f("Hello")

print = "Это была функция print"
f(print)
"""
print("Функция без параметров")

def send_mail():
    text = "Hello"
    print(text)


send_mail()
print(send_mail())
send_mail()

print("Функция с одним параметром")

def send_mail(from_name): # с параметром
    text = f"""Hello!
{from_name}"""
    print(text)


send_mail(" Иван Иванович") # с аргументом

print("Функция с несколькими параметрами")

def send_mail(from_name, old ): # с параметрами
    text = f"""Hello!
Ваш навсегда{from_name}! 
И не судите строго, мне всего {old} лет!"""
    print(text)


send_mail(" Иван Иванович", 7) # с аргументом

#
print("Tasks")
# Задайте функцию, которая не принимает никаких аргументов и просто выводит на экран строку:
# It's my first function
# В конце программы вызовите эту функцию.
def foo():
    print("It's my first function")


foo()

# Запишите функцию без аргументов, которая считывает с клавиатуры имя и фамилию, записанные в одну строку через пробел,
# и выводит на экран сообщение (без кавычек):
# "Уважаемый, <имя> <фамилия>! Вы верно выполнили это задание!"
# В конце программы вызовите эту функцию.
def foo():
    name, surname = input().split()
    print(f"Уважаемый, {name} {surname}! Вы верно выполнили это задание!")


foo()

#
def ff():
    return f'Уважаемый, {input()}! Вы верно выполнили это задание!'

print(ff())


# Объявите функцию, которая имеет один параметр - вес предмета и выводит на экран сообщение (без кавычек):
#
# "Предмет имеет вес: x кг."
#
# где x - переданное значение функции. После объявления функции прочитайте (с помощью функции input) вещественное число
# и вызовите функцию с этим значением.
def foo(m):
    print(f"Предмет имеет вес: {m} кг.")

foo(float(input()))


# Объявите функцию, которая принимает список, находит максимальное, минимальное и сумму значений этого списка и выводит
# результат в виде строки (без кавычек):
# "Min = v_min, max = v_max, sum = v_sum"
# где v_min, v_max, v_sum - вычисленные значения минимального, максимального и суммы значений списка.
# После объявления функции прочитайте (с помощью функции input) список целых чисел, записанных в одну строку через пробел,
# и вызовите функцию с этим списком.
def foo(list):
    v_min = min(list)
    v_max = max(list)
    v_sum = sum(list)
    return f"Min = {v_min}, max = {v_max}, sum = {v_sum}"


print(foo(list(map(int, input().split()))))

#
def ff(*arg):
    return f'Min = {min(arg)}, max = {max(arg)}, sum = {sum(arg)}'

print(ff(*[int(i) for i in input().split()]))


# Объявите функцию с двумя параметрами width и height (ширина и высота прямоугольника), которая выводит сообщение
# (без кавычек):
# "Периметр прямоугольника, равен x"
# где x - вычисленный периметр прямоугольника. После объявления функции прочитайте (с помощью функции input) два целых
# числа, записанных в одну строку через пробел, и вызовите функцию с этими значениями.
def perimeter(width, height):
    per = (width + height)*2
    print(f"Периметр прямоугольника, равен {per}")

perimeter(*map(int, input().split()))


#
def foo(width, height):
    print(f"Периметр прямоугольника, равен {2 * (width + height)}")

width, height = map(int, input().split())
foo(width, height)


# Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки. Будем полагать, что адрес
# верен, если он обязательно содержит символы '@' и '.', а все остальные символы могут принимать значения:
# 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.
# После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.
def verification_email(mail):
    s = 0
    if "@" not in mail and "." not in mail or mail.count("@") != 1:
        print("НЕТ")
    else:
        for i in mail:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_@.":
                s += 1
        if s == len(mail):
             print("ДА")

        else:
             print("НЕТ")

verification_email(input())


#
import re


def is_email(s: str):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, s) :
        print('ДА')
    else:
        print('НЕТ')


s = input()
is_email(s)


#
from string import ascii_letters as al, digits as ds


def correct_mail(st):
    correct_letters = al + ds + '@._'
    if '@' in st and '.' in st:
        flag = all(i in correct_letters for i in st)

    print('ДА' if flag else 'НЕТ')


st = input()
correct_mail(st)


