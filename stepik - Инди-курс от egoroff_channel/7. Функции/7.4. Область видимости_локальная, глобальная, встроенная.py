# Область видимости: локальная, глобальная и встроенная.
# Область видимости - то место, где было присвоенно значение переменной и осуществляется поиск по этому значению.
# Локальная область видимости создается внутри функции.
def s():
    a, b, c = 1, 2, 3
    print(a, b, c)

s()
# print(a) # Будет ошибка
def q():
    r, t = 1, 5
    print(r, t)
q()
# Внутри функции нельзя обращаться к переменной другой функции.
# Глобальная область видимости - любые переменные, которые создаются вне функций.
#global
w = 'hello'
y = 100

def s():
    #local
    a, b, c = 1, 2, 3
    w = 'HELLO'      # Локальная перемнная
    print(id(w))
    print(a, b, c, w)

s()
print(w, id(w)) # Глобальная переменная

def s():
    #local
    a, b, c = 1, 2, 3
    #w = 'HELLO'      # Локальная перемнная
    print(a, b, c, w)


w = 'hello'
s()
print(w) # Глобальная переменная

def l():
    a = 11
    b = 22
    c = 33
    print(a, b, c, 'local')

a = 100
b = 200
c = 300

l()
print(a, b, c, 'global')


def t():
    a = 11
    b = 22
    #c = 33
    print(a, b, c, 'local')

a = 100
b = 200
c = 300

t()
print(a, b, c, 'global')

def g(a, b, c):
    a = 30
    print(a, b, c, 'local')

a = [1, 2, 4, 5, 6]
b = 200
c = 300

g(a, b, c)
print(a, b, c, 'global')

def g(a, b, c):
    a[1] = 100
    print(a, b, c, 'local')

a = [1, 2, 4, 5, 6]
b = 200
c = 300

g(a, b, c)
print(a, b, c, 'global')

# Изменение значения глобальной переменной в функции:
print('Изменение значения глобальной переменной в функции:')
def s():
    #local
    global a
    a = 30

#global
a = [1, 2, 4, 5, 6]


s()
print(a,'global')

# Функция как глобальная переменная:
def s():
    #local
    global a
    a = 30

def q():
    s()

#global
a = [1, 2, 4, 5, 6]

s()
print(a, 'global')

# Встроенная область видимости (все встроенные функции, объекты и переменные)(builtins):
print('Встроенная область видимости:')
# Ctrl + Space

# Переопределение значения переменных встроенной области видимости:
'''
def w(x):
    return x**2

abs = w # Переопределение имени, находящегося во встроенной области видимости
print(abs(-7), abs(5))
'''

def s():
    abs = 10
    print(abs)

s()
def w(x):
    return x**2
print(abs(-7), abs(5))

# min, max = max, min :))))
# Ключевые слова переопределять не можем (False, True, in и т.д.)

# Вложенные функции:
def s():
    abs = 200
    def q():
        abs = 'hello'
        print(abs, 'q')
    q()
    print((abs, 's'))

abs = [1, 2, 3]
s()

# Правило поиска имен:
# Local - Enclosing - Global - Built in (LEGB)
def s():
    abs = 200
    c = 200
    def q():
        abs = 'hello'
        print(abs, c, 'q')
    q()
    print((abs, 's'))

#global
c = 333
abs = [1, 2, 3]
s()

# Изменение переменной во вложенной функции - nonlocal:
def s():                    # Объемлющая функция
    abs = 200
    def q():
        nonlocal abs
        abs = 'hello'
        print(abs, c, 'q')
    q()
    print((abs, 's'))

#global
c = 333
abs = [1, 2, 3]
s()

#
print('Tasks')
# Напишите функцию, которая имя и возраст водителя. Функция должна распечатать на экран заключение, может ли данный
# водитель управлять транспортом и определять она должна это по возрасту водителя: он должен быть больше или равен
# MIN_DRIVING_AGE
# Если водитель может управлять, выведите фразу "<name> может водить> " , в противном случае "<name> еще рано садиться за руль"
# MIN_DRIVING_AGE = 18
# allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
# allowed_driving('bob', 18) # выведет "bob может водить"
MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    if age >= MIN_DRIVING_AGE:
        print(name, 'может водить')
    else:
        print(name, 'еще рано садиться за руль')

#
MIN_DRIVING_AGE = 18
ANSWERS = ("еще рано садиться за руль", "может водить")
def allowed_driving(name, age):
    print(f'{name} {ANSWERS[age >= MIN_DRIVING_AGE]}')

#
MIN_DRIVING_AGE = 18


def allowed_driving(name: str, age: int) -> str:
    """It decides can you drive."""
    print(f"{name} может водить" if age >= MIN_DRIVING_AGE else f"{name} еще рано садиться за руль")

#
MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    flag = age >= MIN_DRIVING_AGE
    print(f'{name} может водить' if flag else f'{name} еще рано садиться за руль')

#
MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    print([f'{name} может водить', f'{name} еще рано садиться за руль'][age < MIN_DRIVING_AGE])

#
MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    print([f'{name} еще рано садиться за руль', f'{name} может водить'][age >= MIN_DRIVING_AGE])