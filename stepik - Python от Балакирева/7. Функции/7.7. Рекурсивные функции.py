# Рекурсивные функции.
# Рекурсивная функция - это функция, которая вызывает саму себя.
def recursive(value):
    print(value)
    recursive(value + 1)

#recursive(1)

# У любой рекурсивной функции должно быть условие останова! (ограничение глубины рекурсии)
def recursive(value):
    print(value)
    if value < 4:
        recursive(value + 1)
    print(value)

recursive(1)

# Вычисление факториала натурального числа
print("Вычисление факториала натурального числа")
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

p = factorial(6)
print(p)

# Обход каталогов и файлов (иерархических данных)
print("Обход каталогов и файлов")
# Обход словаря
print("Обход словаря")
F = {
    'C:': {
        'Python39': ['python.exe', 'python.ini'],
        'Program Files': {
            'Java': ['README.txt', 'Welcom.html', 'java.exe'],
            'MATLAB': ['matlab.bat', 'matlab.exe', 'mcc.bat']
        },
        'Windows': {
            'System32': ['acledit.dll', 'aclui.dll', 'zipfldr.dll']
        }
    }
}


def get_files(path, depth=0):
    for f in path:
        print(" "*depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth + 1)
        else:
            print(" "*(depth + 1), " ".join(path[f]))


get_files(F)