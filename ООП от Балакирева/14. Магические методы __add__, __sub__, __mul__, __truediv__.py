# Магические методы __add__, __sub__, __mul__, __truediv__
# Магические методы арифметических операций
# __add__() - для операции сложения
# __sub__() - для операции вычитания
# __mul__() - для операции умножения
# __truediv__() - для операции деления
class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    @classmethod
    def __get_formated(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть int или Clock")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

            return Clock(self.seconds + sc)



c1 = Clock(1000)
c2 = Clock(2000)
#c1.seconds = c1.seconds + 100
#c1 = c1 + 100
#print(c1.get_time())
c3 = c1 + c2
print(c3.get_time())
