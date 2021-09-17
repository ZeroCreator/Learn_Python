# Выполняет операцию и считает, сколько раз была вызвана данная функция
print('Выполняет операцию и считает, сколько раз была вызвана данная функция')
def add(a, b): # функция сложения
    return a + b

def mult(a, b, c): # функция умножения
    return a*b*c

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)

    return inner

q = counter(add)
print(q(10, 20))
print(q(40, 50))

m = counter(mult)
print(m(10, 5, 7))