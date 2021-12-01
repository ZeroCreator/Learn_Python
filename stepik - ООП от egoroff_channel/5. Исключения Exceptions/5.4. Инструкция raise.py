# Инструкция raise.
# Возбуждение исключения в любой строчке кода.

# raise Exception("Big error, 1, 2")
# er =  Exception("Big error, 1, 2")
# raise er
try:
    [1, 2, 2][15]
    {}["k"]
    1/0
except (KeyError, IndexError) as error:
    print("LookupError")
    print(f" Logging error: {error} {repr(error)}")
except ZeroDivisionError as err:
    print("ZeroDivisionError")
    print(f" Logging error: {err} {repr(err)}")





try:
    def something():
         if not isinstance(some, type):
             raise TypeError
         elif statement(some_args):
             raise ValueError
except TypeError:
    print("Log TypeError")
except ValueError:
    print("Log ValueError")


a = TypeError("Ошибка типа")
print(a)
print(a.args)
b = TypeError(1, 2, 3, 4, 5)
print(b.args)
print(b)


try:
    [1, 2, 2][15]
except (KeyError, IndexError) as error:
    print(f" Logging error: {error} {repr(error)}")
    raise TypeError("Ошибка типа") from None # выведение только одной ошибки
except ZeroDivisionError as err:
    print("ZeroDivisionError")
    print(f" Logging error: {err} {repr(err)}")


try:
    raise ValueError("Ошибка значения")
except ValueError as first:
    try:
        raise TypeError("Ошибка типа")
    except TypeError as second:
        raise Exception("Большое исключение") from first