# РАБОТА С ФАЙЛАМИ.
file = open('test_package/test.txt', encoding='utf-8')
print(file.read())
file.close()

#
#print('Абсолютный путь к файлу')
#file = open(r'C:\Users\shkol\Learn_Python\Learn_Python\Stepik\test.txt', encoding='utf-8')
#print(file.read())

#
print('Методы:')
print('Чтение - считывает весь файл целиком - .read(2):')     # Прочитать первые два символа
file = open('test_package/test.txt', encoding='utf-8')
print(file.read(3))
print(file.read(3))
print(file.read(4))
file.close()

#
#file.readline().strip() - метод .strip() убирает служебные символы при чтении строки(\n,пробелы, табуляции)
#можно использовать , для того. что бы убрать пустые линии -
s = file.readlines().strip()
#
print('Откат чтения до нужного места - метод - .seak()')
file = open('test_package/test.txt', encoding='utf-8')
print(file.read(3))
file.seek(0)
print(file.read(3))
print(file.read(4))
file.close()

#
print('Чтение одной строчки целиком (построчно) - метод - .readline()')
file = open('test_package/test.txt', encoding='utf-8')
print(file.readline())
print(file.readline())
file.close()

#
print('Способ обойти всю строку построчно:')
file = open('test_package/test.txt', encoding='utf-8')
for row in file:
    print(row)
file.close()

#
print('Способ обойти всю строку посимвольно:')
file = open('test_package/test.txt', encoding='utf-8')
for row in file:
    for letter in row:
        print(letter)
file.close()

#
print('Создание списка, елементом которого будут строки файла - метод .readlines():')
file = open('test_package/test.txt', encoding='utf-8')
a = file.readlines()
print(a)
file.close()

#
print('записать в файл с дописыванием в конец "a" - метод .write():')
file = open('test_package/write_test.txt', 'a', encoding='utf-8')
file.write('hello\n')         # Допишет в конец
file.write('hello\n')
file.write('hello\n')
file.close()

#
print('записать в файл с перезатиранием содержимого "w" - метод .write():')
file = open('test_package/write_test.txt', 'w', encoding='utf-8')
file.write('hello\n')         # Перезатрет веесь файл
file.write('hello\n')
file.write('hi\n')
file.close()

#
print('режим "a+" - и чтение и запись')
file = open('test_package/write_test.txt', 'a+', encoding='utf-8')
print(file.write('hi\n'))
print(file.read())
file.close()

#
print('Tasks')
# Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.
# Учитывайте, что содержимое файла может быть как на русском языке, так и на английском
def file_read(file_name):
    f = open(file_name,encoding='utf-8')
    print(f.read())
    f.close()

def file_read(file_name):
    with open(file_name, "r", encoding = "utf-8") as f:
        print(f.read())
    f.close()

# Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.
# Функция должна создать файл с название "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно,
# причем каждое число записывается  в отдельной строке
# Пример: функция create_file_with_numbers(5) должна создать файл "range_5.txt" с содержимым
def create_file_with_numbers(n):
    f = open(f'range_{n}.txt', 'a+')
    for i in range(1, n + 1):
        f.write(str(i) + '\n')
    file.close()

def create_file_with_numbers(n):
    with open(f"range_{n}.txt", "w") as file:
        for i in range(1,n+1):
            file.write(str(i)+"\n")
        file.close()