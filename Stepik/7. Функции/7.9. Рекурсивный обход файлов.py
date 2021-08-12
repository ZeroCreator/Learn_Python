# Рекурсивный обход файлов.
import os
path = 'D:\\3_Чикуров'

print((os.listdir(path)))
for i in os.listdir(path):
    print(i, type(i), path + '\\' + i)

print()
# Является ли найденный элемент папкой:
print('Является ли найденный элемент папкой:')
for i in os.listdir(path):
    print(i, type(i), path + '\\' + i, os.path.isdir(path + '\\' + i))

print()
# Является ли найденный элемент файлом:
print('Является ли найденный элемент файлом:')
for i in os.listdir(path):
    print(i, type(i), path + '\\' + i, os.path.isfile(path + '\\' + i))

print()
# Функция обхода всех фалов в указанных папках:
# Рекурсия входа в папку.
print('Функция обхода всех фалов в указанных папках:')
def obxodFile(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            obxodFile(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)

obxodFile(path)