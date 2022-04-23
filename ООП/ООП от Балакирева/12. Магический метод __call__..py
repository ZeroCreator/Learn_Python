# Магический метод __call__. Функторы
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter


c = Counter()
c2 = Counter()
print(c)
c()
c(2)
c()
res = c(10)
print(res)
c2()
res2 = c2(-5)
print(res2)


# замыкания
# обработка строк с удалением вначале и в конце набор указанных символов
print("Обработка строк с удалением вначале и в конце набор указанных символов")
class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")

        return args[0].strip(self.__chars)


s1 = StripChars("?:!,; ")
res = s1(" Hello World! ")
s2 = StripChars(" ")
res2 = s2(" Hello World! ")
print(res)
print(res2)

# декораторы
# Нахождение производной произвольной функции в точке х
print("Нахождение производной произвольной функции в точке х")
import math

class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate
def df_sin(x):
    return math.sin(x)

#df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))
