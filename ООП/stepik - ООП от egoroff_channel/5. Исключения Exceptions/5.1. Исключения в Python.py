# Исключения в Python.
# Exception in Python.
# У каждой переменной свой тип ошибок.
# Исключение бывают: 1. возникают в момент выполнения и 2. исключения компиляции.
print("Обработка исключений:")
print("hello")
print("hello1")
print("hello2")
try:
    int('hello')
except ValueError:
    print("неправильное преобразование")
print("hello3")
print("hello4")
print("hello5")

print()
print("hello")
print("hello1")
print("hello2")
try:
    int('789')
except ValueError:
    print("неправильное преобразование")
print("hello3")
print("hello4")
print("hello5")


print("Типы исключений")
# Все типы исключений - это классы.
# Base Exception:
# 1. Exception
# 2. SystemExit
# 3. GeneratorExit
# 4. KeyboardInterrupt

# 1. Exteption:
# 1. Attribute Error
# 2. Arithmetic Error (1. ZeroDivisionError, 2. Floating Point Error, 3. Overflow Error)
# 3. EOF Error
# 4. Name Error
# 5. Lookup Error (1. Index Error, 2. Key Error)
# 6. OS Error (1. FileNotFound Error, 2. Interrupted Error, 3. Permission Error, 4. TimeOut Error)
# 7. Type Error
# 8. Value Error

t = IndexError()
print(t)
print(isinstance(t, IndexError))

print("Вызвать исключение - raise:")
print("hello")
print("hello1")
print("hello2")
raise ValueError("Неправильное значение")
print("hello3")
print("hello4")
print("hello5")

try:
    a = int(input())
except:
    raise ValueError("Неправильное значение, передавайте число")

