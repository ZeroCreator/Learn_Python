# Обработка исключения FileNotFoundError и менеджер контекста.
# Синтаксис try/except/finally:
# try: блок рператоров критического кода
# except [исключение]: блок операторов обработки исключения
# finally: блок операторов всегда исполняемых вне зависисмости от возникновения исключения

try:
    file = open("my_file.txt", encoding="utf-8")
    try:
        s = file.readlines()
        int(s)
        print(s)
    finally:
        file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка пр работе с файлом")

# Использование файлового менеджера контекста:
print("Использование файлового менеджера контекста:")
try:
    #file = open("my_file.txt", encoding="utf-8")
    with open("my_file.txt", encoding="utf-8") as file:
        s = file.readlines()
        print(s)
    #try:
    #    s = file.readlines()
    #    int(s)
    #    print(s)
    #finally:
    #    file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")
finally:
    print(file.closed)
