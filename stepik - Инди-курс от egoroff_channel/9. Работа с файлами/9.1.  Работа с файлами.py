# РАБОТА С ФАЙЛАМИ.
'''
Будем работать с файлом формата .txt -  тоесть блокнот
Для того чтобы открыть файл нужно сначала создать его.
Создайте файл с расширением .txt и назовите его как угодно –
Я назвал его test.txt, для того чтобы работать с этим файлом нужно его открыть в нашем коде. Для этого есть фунция Open
Откроем переменную file:
file = open(‘test.txt’) у вас вместо test.txt ваше название файла.
Теперь мы можем работать с этой переменной file
И первоем что мы можем сделать это прочитать содержимое блокнота – print(file.read())
Если у вас в блокноте была кириллица и файл выдал всякую белеберду то сделайте так:
file = open(‘test.txt’, encoding=’utf-8’)
print(file.read())
теперь всё должно заработать!
Следующий метод print(file.readline()) – считывает одну линию.
Файл можно обойти циклом for.
for line in file:
         print(line) – Будет считывать по одной линии
Для того чтобы считывать по словам:
for line in file:
         for letter in line:
                   print(letter) – считывает по словам.
Для того чтобы что-то записать в файл. Нужно сделать так:
file = open(‘test.txt’, ‘w’) – ‘w’ это мод write.
По умолчанию там ‘r’ – read
File = open(‘test’.txt, ‘w’)
File.write(‘hello world’) – обратите внимание что если у вас в файле до этого уже чтото было write удалит всё и напишет то что бы укажите.
Но при последующих вызовах он будет дописывать.
Для того чтобы изначально дописывать используйте мод a
File = open(‘test.txt’, ‘a’)
File.write(‘чточто’) – теперь стираться не будет.
Для того чтобы можно было одним модом и читать и записывать а раньше этого нельзя было делать используйте мод a+
Также не забывайте закрывать файл file.close()
Если у вас в работе с файлами будет ошибка то файл не закроется

Сейчас открывают файлы конструкцией вида:

with open(file_name, 'r') as inf:
и дальше например так:
    lines = inf.read().splitlines()
Прием хорош тем, что Питон сам закроет обрабатываемый файл. Да и код короче.

file.readline().strip() - метод .strip() убирает служебные символы при чтении строки(\n,пробелы, табуляции)
можно использовать , для того. что бы убрать пустые линии -
s=file.readlines().strip()
'''
file = open('test_package/test.txt', encoding='utf-8')
print(file.read())
file.close()

#
#print('Абсолютный путь к файлу')
#file = open(r'C:\Users\shkol\Learn_Python\Learn_Python\stepik - Инди-курс от egoroff_channel\test.txt', encoding='utf-8')
#print(file.read())

#
print('Методы:')
print('Чтение - считывает весь файл целиком - .read(2):')     # Прочитать первые два символа
file = open('test_package/test.txt', encoding='utf-8')
print(file.read(3))
print(file.read(3)) # Аналог функции next()
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
file.seek(0) # Переставить коретку в любое место
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
print(a) # Результатом будет список
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
print(file.write('hi\n')) # Допишется в конец
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

# Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое длинное
# слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной, нужно вернуть слово,
# которое встречается последнее в тексте. При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки
# пунктуации необходимо исключить.  И также учитывайте, что слова в тестах будут как на русском языке, так и на английском
# Все возможные знаки пунктуации можно получить из модуля string
# from string import punctuation
def longest_word_in_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    max_word = ''
    for line in file:
        words = line.split()
        for word in words:
            word_without_punc = remove_punctuation(word)
            if len(word_without_punc) >= len(max_word):
                max_word = word_without_punc
    file.close()
    return max_word


def remove_punctuation(word):
    from string import punctuation
    for punc in punctuation:
        if punc in word:
            word = word.replace(punc, '')
    return word


# В этой задаче вам необходимо скачать файл, в котором записаны натуральные числа. Ваша задача найти
# количество трехзначных чисел;
# сумму двухзначных чисел
# В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов. Сперва количество, потом сумма
with open('numbers.txt') as inf:
    s = inf.read().strip().split()
count = 0
sum = 0

for i in s:
    if len(i) == 3:
        count += 1
    if len(i) == 2:
        sum += int(i)

print(count, sum)

#
sm, sk = 0, 0

for n in map(int, open('temp.txt')):
    if 9 < n < 100:
        sm += n
    elif 99 < n < 1000:
        sk += 1

print(f'{sk},{sm}')

#
with open('C:\\Users\\kyzmi\\Downloads\\numbers.txt') as file_numbers :
    arr = [*map(lambda x: x.strip(), file_numbers.readlines())]
    count_three_rank = len([i for i in arr if len(i) == 3])
    summ_two_rank = sum([int(i) for i in arr if len(i) == 2])
print(count_three_rank, summ_two_rank)



#
with open('numbers.txt') as f:
    l = [int(i.strip()) for i in f.readlines()]
    l2 = sum(list(filter(lambda x: 10 <= x <= 99, l)))
    l3 = list(filter(lambda x: 100 <= x <= 999, l))
    print(l2, len(l3))

