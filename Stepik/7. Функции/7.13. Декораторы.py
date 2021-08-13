# Декораторы.
# Декоратор это функция внутрь которой входит еще какая либо функция выполнение которой дополняет функция декоратор,
# в декораторе также присутствует замыкание.


def decorator(func):

    def inner():
        print('start decorator...')
        func()
        print('finish decorator...')

    return inner

def say():
    print('hello world')

def buy():
    print('buy world')
'''
d = decorator(say)
print(d)
print(d())
'''
print()
say = decorator(say)
say()

print()
buy = decorator(buy)
buy()
