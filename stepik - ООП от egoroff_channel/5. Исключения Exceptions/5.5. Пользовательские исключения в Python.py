# Пользовательские исключения в Python.
class MyException(Exception):
    """This is my first Exception"""
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        print("str called")
        if self.message:
            return f"MyException({self.message})"
        else:
            return "MyException is empty"

# raise MyException("hello", 1, 2)
raise MyException()
# try:
#     raise MyException("hello", 1, 2)
# # except Exception:
# except AttributeError:
#     print("done")

print("Иерархия исключений")
print("Класс исключений для игры 'змейка'")

class SnakeExceptionBase(Exception):
    """Основной класс ошибок"""

class SnakeBorderException(SnakeExceptionBase):
    """Ошибка соприкосновения змейки со стенкой"""

class SnakeTailException(SnakeBorderException):
    """Соприкосновение головы змеи и хвоста"""

