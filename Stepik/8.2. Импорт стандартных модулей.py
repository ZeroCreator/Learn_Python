# Импорт стандартных модулей.
# 1.
import pprint
# 2.
import calendar
# 3.
#import math as m
# 4.
#from math import e, pi, factorial  # как исправить конфликт имен:
#from math import e, pi, factorial as fact
# 5.
# Для того, чтобы импортировать все имена:
from math import *

def say_hello(name):
    print(f'Hello,{name}')

def summa(*args):
    return sum(args)

#def factorial(n):          будет конфликт имен при 'from math import e, pi, factorial', так как выполняется последнее.
#    print('my func')
#    pr = 1
#    for i in range(1, n - 1):
#        pr += i
#    return pr

my_str = "YOU'RE BREATH"
my_num1 = 2
my_num2 = 3

pprint.pprint(locals())
c = calendar.TextCalendar()
print(c.formatyear(2021))

# Посмотреть пространство имен модуля - dir(модуль):
#pprint.pprint(dir(math))

# Просмотреть модуль - ctrl
# Доступ к именам модуля: модуль.имя
#print(math.e)
#print(math.pi)
#print(math.factorial(10))

#print(m.e)
#print(m.pi)
#print(m.factorial(10))

print(e)
print(pi)
print(factorial(10))
