# 7 видов вызываемых (callable) объектов.
'''
Вызываем обьект это обьект который поодерживает оператор вызова, оператор вызова обозначается круглыми скобочками.
Всего есть 7 видов Вызываемых обьектов в python:

1)Встроенные функции.
Например len() внутрь которого поступает аргумент которому нужно найти длину
Проверить является ли обьект вызываемым можно функцией callable:
print(callable(len)) = True

2)Встроенные методы.
Например lower() – который делает все буквы в переданном обьекте строчными.
a = 'AbCd', print(a.lower()) – abcd
print(callable(a.lower)) – True

3)Самописные функции.
То есть функции которые вы написали сами:
def sqr(x):
         return x ** 2
Простая функция принимающая аргументом число и возвращает его квадрат.
print(callable(sqr)) – True

(Анонимные lambda функции также вызываемые)

4)Классы.
Создадим пустой класс
class dog():
         pass
print(callable(dog)) – True

5) Экземпляры классов.
Наш класс dog можно присвоить в переменную которая и станет экземпляром класса:
class dog():
         pass
a = dog()

Но в таком с нашим классом это не сработает ибо он абсолютно пуст: print(callable(a)) – False

Чтобы он наш экземпляр стал вызываевым используем магический метод __call__
class dog():
         def __call__(self, *args, **kwargs):
                   print('gav')
a = dog()
print(callable(a)) = True

Вот вызовем нашу переменную а:
a() – ‘gav’

6)Методы класса.
class dog():
         def sayhello(self):
                   print('hello')

Вот наш  метод sayhello который принимает self(Экземпляр) и выводит hello
a = dog()
print(callable(a.sayhello)) = True
print(a.sayhello()) = ‘hello’

7)Функции генераторы.
Вспомним функции генераторы которые внутри себя имеют ключевое слово yield
def gen():
         a = [1,2,3,4,5,6]
         for i in a:
                   yield i
print(callable(gen)) = True

Это и есть все вызываемые обьекты, к остальным обратиться через скобочки нельзя:
print(callable(1)) = False – обьект int
print(callable('2')) = False – обьект str
print(callable(3.0)) = False  - обьект float
print(callable([])) = False – обьект list
print(callable({})) = False – обьект dict
print(callable(())) = False – обьект tuple
'''
# 1. Встроенные функции.
print('1. Встроенные функции.')
print(callable(len))
print(callable(int))

# 2. Встроенные методы.
print('2. Встроенные методы.')
a = [1, 2, 3]
print(callable(a.sort))
print(callable('hello'.lower))

# 3. Самописные функции.
print('3. Самописные функции.')
def f():
    print('hello world')

f()
print(callable(f))

d = lambda: 'hi'
d()
print(d())
print(callable(d))

# 4. Классы.
print('4. Классы.')
# 5. Экземпляры классов.
print('5. Экземпляры классов.')
class Cat:
    def __call__(self, *args, **kwargs):
        print('may')

    def say_hello(self):
        print('hello')

bob = Cat()
print(bob)
print(callable(Cat))
print(callable(bob))

bob()

# 6. Методы класса.
print('6. Методы класса.')
print(callable(bob.say_hello))

# 7. Функции генераторы.
print('7. Функции генераторы.')
def f():
    n = 0
    while True:
        yield n
        n += 1

print(callable(f))