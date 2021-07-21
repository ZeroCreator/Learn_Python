from math import *

def say_hello(name):
    print(f'Hello,{name}')

def summa(*args):
    return sum(args)

def factorial(n):
    print('my func')
    pr = 1
    for i in range(1, n + 1):
        pr += i
    return pr

my_str = "YOU'RE BREATHTAKING"
my_num1 = 2
my_num2 = 3


# Атрибут __name__ используется, если необходимо, чтобы программа срабатывала не автоматически после импортирования,
# а по требованию:
if __name__ == '__main__':
    print(1, 2, 3)
    print('hello')