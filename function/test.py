"""
class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f"Робот {self.name} был уничтожен")

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя, особь человеческого рода")

    @classmethod
    def how_many(cls):
        print(f"{cls.population}, вот сколько нас еще осталось")


r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"
"""
class Robot():
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Робот {self.name} был создан")
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f"Робот {self.name} удален")

    def say_hello(self):
        print(f"Робот {self.name} приветствует тебя")

    @classmethod
    def how_many(cls):
        print(f"{cls.population} - вот сколько нас")

r2 = Robot("R2-D2")
r2.say_hello()
Robot.how_many()
r2.destroy()

def insert_sort(A):
    """insert_sort"""
    N = len(A)
    for i in range(1, N):
        k = i
        while k > 0 and A[k-1] > A[k]:
            A[k-1], A[k] = A[k], A[k-1]
            k -= 1
    return A

a = [1, 2, 8, 5, 6]
print(insert_sort(a))

def choice_sort(A):
    """choice_sort"""
    N = len(A)
    for i in range(0, N-1):
        for k in range(i + 1, N):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]


def bubble_sort(A):
    """bubble_sort"""
    N = len(A)
    for i in range(1, N):
        for k in range(0, N-i):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


a = [1, 2, 8, 5, 6]
print(insert_sort(a))



def test_sort(sort_func):
    print(sort_func.__doc__)
    A = [1, 8, 5, 6, 9, 2, 4, 7]
    test_A = [1, 2, 4, 5, 6, 7, 8, 9]
    sort_func(A)
    print("Ok" if A == test_A else "Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)


class Car:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_ferrari(self):
        return False


class Ferrary(Car):
    def is_ferrari(self):
        return True

db = Car("bmw")
print(db.get_name(), db.is_ferrari())
f40 = Ferrary("f40")
print(f40.get_name(), f40.is_ferrari())


def nod(a, b):
    if a == b:
        return a
    elif a > b:
        return nod(a-b, b)
    else:
        return nod(a, b-a)


print(nod(9, 3))

def mat(n):
    if n == 1:
        print("1")
    else:
        print("спуск", n)
        mat(n-1)
        print("восхождение", n)

mat(5)

def fact(n):
    """Факториал числа"""
    assert n >= 0, "Факториал отрицательного числа не определен"
    if n == 1:
        return 1
    return fact(n-1) * n

print(fact(5))

"""
def count_sort(a):
    p = [] * 10
    for i in a:
        p[i] += 1

    for i in range(10):
        print((str(i) + ' ') * p[i], end='')

a = [1, 2, 8, 5, 6]
count_sort(a)
"""

def palindrom(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return palindrom(str[1:-1])

p = "asdfghjkjhgfdda"
print(palindrom(p))