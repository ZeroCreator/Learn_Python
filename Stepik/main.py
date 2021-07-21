# Урок 8.4.
# 1. Импорт директория.файл:

#import test_package.file1
#import test_package.file2

#print(test_package.file1.c)
#print(test_package.file2.d)

# 2. Импорт самого модуля:
#from test_package import file1
#from test_package import file2

#print(file1.c)
#print(file2.d)

# Импорт конкретных имен из модуля:
#from test_package.file1 import b
#from test_package.file2 import h
#print(b, h)

# Для того, чтобы были доступны все имена из
# # импортируемого модуля из всех файлов -
# # используем файл __init__ (см. файл __init__):
import test_package

print(test_package.h)

#print(test_package.file1.c)