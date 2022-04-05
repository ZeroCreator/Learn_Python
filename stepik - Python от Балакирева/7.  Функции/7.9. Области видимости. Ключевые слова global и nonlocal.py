# Области видимости. Ключевые слова global и nonlocal.
N = 100
WIDTH, HEIGHT = 1000, 500


def my_func(lst):
    #print(N, WIDTH)
    #N = 20
    for x in lst:
        n = x + 1 + N
        print(n)

my_func([1, 2, 3])
print(N)

# Изменение глобальной переменной.
def my_func(lst):
    global N
    N = 20
    for x in lst:
        n = x + 1 + N
        print(n)

my_func([1, 2, 3])
print(N)

###
x = 0

def outer():
    global x
    x = 1
    def inner():
        #nonlocal x
        x = 2
        print("inner: ", x)

    inner()
    print("outer: ", x)

outer()
print("global: ", x)


# nonlocal
# Tasks
print("Tasks")
# Подвиг 3. Имеется программа (см. листинг ниже), где читается глобальная переменная WIDTH (из входного потока) и
# функция с именем func1. Допишите в теле функции команду, которая бы позволяла изменять глобальную переменную WIDTH.
WIDTH = int(input())


def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH


print(func1())

# Подвиг 4. Имеется программа (см. листинг ниже). Необходимо в теле функции func2 дописать команду, которая бы меняла
# значение уже существующей переменной msg, объявленной в функции func1.
def func1():
    msg = input()


    def func2():
        nonlocal msg
        msg = input()
        print(msg)


    func2()
    print(msg)


func1()

# Подвиг 5. Объявите функцию с именем create_global, которая имеет, следующую сигнатуру:
# def create_global(x): ...
# Эта функция должна создавать глобальную переменную с именем TOTAL и присваивать ей значение x.
# (Ничего выводить на экран она не должна, только создавать переменную).
# Вызывать функцию не нужно, только определить.
def create_global(x):
    global TOTAL
    TOTAL = x