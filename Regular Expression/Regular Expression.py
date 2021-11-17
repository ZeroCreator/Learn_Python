# Regular Expression.
# Регулярные выражения в Python.
# Регулярные выражения, иногда называемые re, regex или regexp, представляют собой последовательности символов,
# составляющие шаблоны, соответствия которым ищутся в строке или тексте.
# Для работы с regexp в Python есть встроенный модуль re.
# Обычное использование регулярного выражения:
# -Поиск подстроки в строке (search and find)
# -Поиск всех подходящих строк (findall)
# -Разделение строки на подстроки (split)
# -Замена части строки (sub)
print("1. - re.search()")
# Этот метод возвращает совпадающую часть строки и останавливается сразу же, как находит первое совпадение.
# Синтаксис: re.search(шаблон, строка)
# Возвращаемое значение может быть либо подстрокой, соответствующей шаблону,
# либо None, если такой подстроки не окажется.
import re
regexp = r"([a-zA-Z]+) (\d+)"
match = re.search(regexp, "My son birthday is on July 20")
if match != None:
    print("Match at index %s, %s" % (match.start(), match.end()))   #This provides index of matched string
    print("Full match: %s" % (match.group(0)))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))
else:
    print("The given regex pattern does not match")


print("2. - re.match()")
# Этот метод ищет и возвращает первое совпадение. Но надо учесть, что он проверяет соответствие только в начале строки.
# Синтаксис: re.match(шаблон, строка)

regexp = r"([a-zA-Z]+) (\d+)"
match = re.match(regexp, "July 20")
if match == None:
    print("Not a valid date")
else:
    print("Given string: %s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))


regexp = r"([a-zA-Z]+) (\d+)"
match = re.match(regexp, "My son birthday is on July 20")
if match == None:
    print("Not a valid date")
else:
    print("Given string: %s" % (match.group()))
    print("Month: %s" % (match.group(1)))
    print("Day: %s" % (match.group(2)))


print("3. - re.findall()")
# Этот метод возвращает все совпадения с шаблоном, которые встречаются в строке. При этом строка проверяется
# от начала до конца. Совпадения возвращаются в том порядке, в котором они идут в исходной строке.
# Синтаксис: re.findall(шаблон, строка)
# Возвращаемое значение может быть либо списком строк, совпавших с шаблоном,
# либо пустым списком, если совпадений не нашлось.
string  = "Bangalore pincode is 560066 and gulbarga pincode is 585101"
regexp = '\d+'
match = re.findall(regexp, string)
print(match)

print("Task. Найти в заданном тексте номер мобильного телефона")

string = "Bangalore office number 1234567891, My number is 8884278690, emergency contact 3456789123 invalid number 898883456"
regexp = '\d{10}'  # Регулярное выражение, соответствующее числу из ровно 10 цифр
match = re.findall(regexp, string)
print(match)

print("4. - re.compile()")
# С помощью этого метода регулярные выражения компилируются в объекты шаблона и могут использоваться в других методах.
e = re.compile('[a-e]')
print(e.findall("I born at 11 A.M. on 20th July 1989"))
e = re.compile('\d')  # \d - эквивалент [0-9].
print(e.findall("I born at 11 A.M. on 20th July 1989"))
p = re.compile('\d+')  # группа из одной или более цифр
print(p.findall("I born at 11 A.M. on 20th July 1989"))
# Результат:
# ['b', 'a']
# ['1', '1', '2', '0', '1', '9', '8', '9']
# ['11', '20', '1989']

print("5. - re.split()")
# Данный метод разделяет строку по заданному шаблону. Если шаблон найден, оставшиеся символы из строки возвращаются
# в виде результирующего списка. Более того, мы можем указать максимальное количество разделений для нашей строки.
# Синтаксис: re.split(шаблон, строка, maxsplit = 0)
# '\W+' совпадает с символами или группой символов, не являющихся буквами или цифрами
# разделение по запятой ',' или пробелу ' '
print(re.split('\W+', 'Good, better , Best'))
print(re.split('\W+', "Book's books Books"))
# Здесь ':', ' ' ,',' - не буквенно-цифровые символы, по которым происходит разделение
print(re.split('\W+', 'Born On 20th July 1989, at 11:00 AM'))
# '\d+' означает цифры или группы цифр
# Разделение происходит по '20', '1989', '11', '00'
print(re.split('\d+', 'Born On 20th July 1989, at 11:00 AM'))
# Указано максимальное количество разделений - 1
print(re.split('\d+', 'Born On 20th July 1989, at 11:00 AM', maxsplit=1))
# Результат:
# ['Good', 'better', 'Best']
# ['Book', 's', 'books', 'Books']
# ['Born', 'On', '20th', 'July', '1989', 'at', '11', '00', 'AM']
# ['Born On ', 'th July ', ', at ', ':', ' AM']
# ['Born On ', 'th July 1989, at 11:00 AM']

print("6. - re.sub()")
# В данном методе исходный шаблон сопоставляется с заданной строкой и,
# если подстрока найдена, она заменяется параметром repl.
# Кроме того, у метода есть дополнительные аргументы. Это count, счетчик, в нем указывается, сколько раз заменяется
# регулярное выражение. А также flag, в котором мы можем указать флаг регулярного выражения (например, re.IGNORECASE)
# Синтаксис: re.sub(шаблон, repl, строка, count = 0, flags = 0)
# Шаблон 'lly' встречается в строке в "successfully" и "DELLY"
print(re.sub('lly', '#$', 'doctor appointment booked successfully in DELLY'))
# Благодаря использованию флага регистр игнорируется, и 'lly' находит два совпадения
# Когда совпадения найдены, 'lly' заменяется на '~*' в "successfully" и "DELLY".
print(re.sub('lly', '#$', 'doctor appointment booked successfully in DELLY', flags=re.IGNORECASE))
# Чувствительность к регистру: 'lLY' не находит совпадений, и ничего в строке не будет заменено
print(re.sub('lLY', '#$', 'doctor appointment booked successfully in DELLY'))
# С count = 1 заменяется только одно совпадение с шаблоном
print(re.sub('lly', '#$', 'doctor appointment booked successfully in DELLY', count=1, flags=re.IGNORECASE))

print("7. - re.subn()")
# Функциональность subn() во всех отношениях такая же, как и sub(). Единственная разница – это формат вывода.
# subn() возвращает кортеж, содержащий общее количество замен и новую строку.
# Синтаксис: re.subn(шаблон, repl, строка, count = 0, flags = 0)
print(re.subn('lly', '#$', 'doctor appointment booked successfully in DELLY'))
t = re.subn('lly', '#$', 'doctor appointment booked successfully in DELLY', flags=re.IGNORECASE)
print(t)
print(len(t))
# Это даст такой же вывод, как и sub()
print(t[0])

print("8. - re.escape()")
# Этот метод возвращает строку с обратной косой чертой \ перед каждым не буквенно-числовым символом. Это полезно,
# если мы хотим сопоставить произвольную буквенную строку, которая может содержать метасимволы регулярного выражения.
# Синтаксис: re.escape(строка)
# Здесь из не буквенно-цифровых символов есть только пробелы.
print(re.escape("doctor appointment booked successfully at 1PM"))
# Здесь есть , ' ', '^', '-', '[]', '\' - все эти символы не относятся к буквенно-цифровым
print(re.escape("He asked what is this [0-9], I said \t ^Numberic class"))
