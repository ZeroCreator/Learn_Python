# Определение и вызов функции. Инструкция def.
# Функции - это многократно используемые фрагменты программы. При помощи функций можно объединить несколько инструкций
# в один блок, присвоить этому блоку имя и затем, обращаясь по имени этого блока, выполнить инструкции внутри него в
# любом месте программы необходимое число раз.


# определение функции:
print('Определение функции')

def sey_hello():
    print('hello')
    print('world')
    print('and everybody')

# Определение функции с аргументом:
def square(x):
    print('Квадрат числа ', x, '=', x**2)

sey_hello()

print('pause')
sey_hello()

print('Определение функции с аргументом:')
square(5)
square(10)

for i in range(1, 11):
    square(i)

# Функция умножения двух чисел:
print('Функция умножения двух чисел:')
def multiply(a, b):
    print(a*b)

multiply(3, 5)
multiply(70, 100)

# Функция проверки на четность:
print('Функция проверки на четность:')
def even(a):
    if a%2 == 0:
        print(a, 'chetnoe')
    else:
        print(a, 'nechetnoe')

for i in range(20, 31):
    even(i)

# Функция вычисления факториала:
print('Функция вычисления факториала:')
def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr = pr * i
    print(pr)

factorial(3)
factorial(4)
factorial(5)

# Функция внутри условия:
print('Функция внутри условия:')
if 5 > 1:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

primer()

# Выводится самая последняя среди одинаковых:
def primer():
    print('hello')

def primer():
    print('HELLO')


def primer():
    print('hi')
