# РАБОТА С ФАЙЛАМИ.
file = open('test.txt', encoding='utf-8')
print(file.read())

#
print('Абсолютный путь к файлу')
file = open(r'C:\Users\shkol\PycharmProjects\PycharmProjects\Stepik\test.txt', encoding='utf-8')
print(file.read())

#
print('Методы:')
print('Чтение - .read(2):')     # Прочитать первые два символа
file = open('test.txt', encoding='utf-8')
print(file.read(3))
print(file.read(3))
print(file.read(4))

#
print('Метод ')



