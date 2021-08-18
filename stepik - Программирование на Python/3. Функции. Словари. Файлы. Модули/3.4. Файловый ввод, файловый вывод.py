# Файловый ввод/вывод.
# 1. Чтение из файла.
print('1. Чтение из файла.')

inf = open('file.txt', 'r') # open('file.txt')
s1 = inf.readline()
s2 = inf.readline()
inf.close()

with open('text.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()
# здесь файл уже закрыт

# Методы:
print('Методы:')
# 1. Убирание служебных символов - метод .strip():
print('1. Убирание служебных символов - метод .strip():')
s = inf.readline().strip()

# 2. Путь к файлу:
print('2. Путь к файлу:')
os.path.join('.', 'dirname', 'filename.txt')

'''
Если вы используете Windows и при попытке чтения файла у вас выдаёт ошибку такого плана, как

"SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"
То вы можете сделать две вещи для её устранения, либо добавить двойной слеш в ваш адрес, например, a=open('C:\\Users\\User\\Desktop\\dataset.txt', 'r') или букву r перед Path --
a=open(r'C:\Users\User\Desktop\dataset.txt', 'r')

Дело в том, что питон воспринимает ваш путь как обычную строку, а нам необходима неформатированная.
'''

# Построчное чтение файла:
print('Построчное чтение файла:')
with open('input_3.4.3.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)    # Вывод содержимого исходного файла

# 2. Запись в файл.
print('2. Запись в файл.')
ouf = open('file.txt', 'w')
ouf.write('Some text\n') # \n - перевод строки на новую
ouf.write(str(25))
ouf.close()

with open('text.txt', 'w') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))
# здесь файл уже закрыт

#
print('Tasks')
# На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление
# исходной строки обратно.
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j
'''
Первый символ - гарантированно буква.
Перебираем все последующие, пока они цифровые или пока не достигнут конец строки.
После внутреннего цикла j либо указывает на следующую букву, либо на конец строки. В обоих случаях между s[i] и s[j] - цифры, составляющие нужное нам число повторов символа s[i].
Печатаем символ нужное число раз, присваиваем i индекс следующей буквы для новой итерации цикла.
'''

#
s, d = input(), []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')

#
m, s, n = '', '', 0
with open('dataset_3363_2.txt', 'r+') as f:     # открываем файл в режиме чтение и запись
    for i in f.readline():                      # читаем строку и перебираем
        if '0' <= i <= '9':                     # если число
            n += i                              # соединяем числа в строку
            continue
        m += s * int(n)                         # преобразуем число в соответствующее количество символов
        s, n = i, ''
    f.seek(0)                                   # перемещаем указатель в начало файла для перезаписи
    f.write(m)                                  # записываем преобразованную строку в файл

#
with open('dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()


for i in range(len(s)):
    r = 1
    number=''
    if s[i].isalpha():
        while s[i+r].isdigit():
            number += str(s[i + r])
            r+=1
        for _ in range(int(number)):
            print(s[i],end='')

'''
Тут всё достаточно прозрачно. Работа идёт с инкрементированием (к слову, инкремент - хороший костыль во многих случаях, рекомендую!).
1. Перебираем каждый символ строки, с каждым новым перебором задаём тот самый инкремент r и пустую строку number (где r отвечает за проход от текущего элемента в итерации (элемента s[i] ) ровно на 1 элемент вперед, а number - за число, на которое нужно умножить нашу букву)
2. Работая ищейкой, r посимвольно вынюхивает, являются ли элементы за s[i] (которое у нас буква) digit-ами. Если так, то в number записывается число после s[i] до тех пор, пока элемент s[i+r] станет НЕdigit (в нашем случае - alpha).
3. Цикл while заканчивает свою работу, вступает цикл for, который записывает s[i]-ую букву ровно number раз.
4. Самый первый цикл for идёт дальше по элементам нашей строки и применяет вышеназванные пункты только к ALPHA-элементам ( if s[i].isalpha() ), в ином случае, итерация цикла переходит к следующему символу строки s
'''

# Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
# смотреть, как, например, на наиболее часто используемые.
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
# слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически
# первое (можно использовать оператор < для строк).
# В качестве ответа укажите вывод программы, а не саму программу.
# Слова, написанные в разных регистрах, считаются одинаковыми.
dictionary = {}

with open('input_3.4.3.txt') as in_f_obj:
    for line in in_f_obj:
        line = line.lower()
        for word in line.split():
            if word not in dictionary:
                dictionary[word] = 1
            elif word in dictionary:
                dictionary[word] += 1

max_quantity = 1

for key, value in dictionary.items():
    current_quantity = dictionary[key]
    if current_quantity > max_quantity:
        max_quantity = current_quantity
        word_with_max_quantity = key

with open('output_3.4.3.txt', 'w') as out_f_obj:
    most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
    out_f_obj.write(most_popular)

#
with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))

#
with open('words.txt') as f:
    text = f.read().lower().split()
popular_word = max(set(text), key=text.count)
print(popular_word, text.count(popular_word))

#
def CountWord(d, key, value):
    if key in d:
        d[key] += 1
    else:
        d[key] = value

s1 = []
with open('D:\python\\bibl.txt', 'r') as text:
    for line in text:
        L = line.lower().strip().split()
        s1.extend(L)
s1.sort()

dict_of_word = {}
for word in s1:
    CountWord(dict_of_word, word, 1)

max_q = 0
first_word = ''
for word, q in dict_of_word.items():
    if q > max_q:
        max_q = q
        first_word = word
print(first_word, max_q)