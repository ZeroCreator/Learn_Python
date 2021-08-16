# МЕТОДЫ СТРОК.
# Метод - это функция, связанная с определенным типом объекта.
# Методы являются специфичными для каждого отдельного типа.
# Вызов метода: объектюметод(аргументы)

print('Метод перевода всех букв в заглавные: .upper()')
print('hello'.upper())
print('hello123'.upper())

#
print('Метод перевода всех букв в строчные: .lower()')
print('HELLO'.lower())
print('HelLO123'.lower())

s = 'hello world'
print(s.upper())
print(s)    # Любой метод строки не меняет саму строку

#
print('Чтобы поменять строку:')
s = s.upper()   # Присвоение переменной значения метода .upper
print(s)

print(s.lower())
print(s)
s = s.lower()
print(s)

#
print('Подсчет количества повторений подстроки в строке - метод .count():')
print(s.count('o'))
print(s.count('o', 6))
print(s.count('o', 8))
print(s.count('l', 1, 3))
print(s.count('l', 1, 4))

#
print('Поиск индекса подстроки - метод .find():')
print(s.find('e'))
print(s.find('wor'))
print(s.find('z'))  # Вернется значение -1, а не ошибка.
print(s.find('o'))  # Вернет первое значение слева.
print(s.rfind('o')) # Вернет первое значение справа.
print(s.find('o', 6))

#
print('Поиск индекса подстроки - метод .index():')
print(s.index('e'))
print(s.index('wor'))

#
print('Замена какого-либо значения подстроки в строке - метод .replace():')
print(s.replace('o', '&&&'))
print(s.replace('l', ''))
print(s.replace(' ', ''))
print(s.replace('l', '', 2))    # Сколько раз надо сделать замену

#
print('Проверяет, состоит ли строка полностью из букв - метод .isalpha():')
print(s.isalpha())
print('fdghfvyu'.isalpha())

#
print('Проверяет, состояит ли строка полностью из цифр - метод .isdigit():')
print('6541566000  84188'.isdigit())
print('12354892'.isdigit())

#
print('Дополняет строку до указанной длины - метод .rjust(), .ljust():')
d = '111'
print(d.rjust(5))
print(d.ljust(5))
print(d.rjust(5, '0'))
print(d.ljust(5, '0'))

#
print('Разбивает строку по символам в список - метод .split():')
w = 'ivanov ivan ivanovich'
print(w.split())
print(w.split('n'))
print('43,543,765,3,765,432'.split(','))

#
print('Сколько слов в строке:')
print(len(w.split()))

#
print('Соединяет элементы списка в строку - метод .join():')
t = '43,543,765,3,765,432'.split(',')
print('='.join(t))
print('hello'.join(t))

#
print('По запятой объединить результат разбиения переменной w по пробелу:')
print(','.join(w.split()))

#
print('Удалить знаки пробелов и перенос на новые строки - метод .strip():')
q = '      hello     \n'
print(q)
print(q.strip())

print('Удалить знаки пробелов и перенос на новые строки только слева- метод .lstrip():')
print(q.lstrip())

print('Удалить знаки пробелов и перенос на новые строки только справа - метод .rstrip():')
print(q.rstrip())

#
print('Использование цепочки вызовов:')
print(input().upper())
s = input()
print(s.lower().replace('d', 'w').upper())

#
print('Tasks')
# На вход программе поступает строка, ваша задача подсчитать сколько раз в ней встречается латинская буква "e".
# При этом стоит учитывать как маленькие, так и заглавные буквы
a = input()
c = a.count('e') + a.count('E')
print(c)

s = input()
print(s.lower().count('e'))

print(input().lower().count('e'))

# На вход программе поступает строка, ваша задача удалить из нее все символы "w" и "z".
s = input()
s = s.replace('w', '')
s = s.replace('z', '')
print(s)

print(input().replace('w', '').replace('z', ''))

print(''.join(''.join(input().split('w')).split('z')))

# Программа получает на вход фразу, ваша задача посчитать из скольких слов состоит данная фраза.
# Для удобства будем считать словом любую последовательность символов.
s = input()
print(len(s.split()))

# Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.
# Ваша задача заменить все пробелы запятыми и вывести полученную строку.
s = input()
print(','.join(s.split()))

print(','.join(input().split()))

print(input().replace(' ', ','))

a = input()
a=a.split(' ')
print(','.join(a))

# Программа должна делать следующее: в заданной строке, которая состоит из прописных и строчных латинских букв, она:
# - удаляет все гласные буквы,
# - перед каждой согласной буквой ставит символ ".",
# - все прописные согласные буквы заменяет на строчные.
# Гласными буквами считаются буквы "A", "O", "Y", "E", "U", "I", а согласными — все остальные.
# На вход программе подается ровно одна строка, она должна вернуть результат в виде одной строки,
# получившейся после обработки.
# Sample Input:Codeforces - Sample Output:.c.d.f.r.c.s
s = input().lower()
s = s.replace('a', '').replace('o', '').replace('y', '').replace('e', '').replace('u', '').replace('i', '')
b = list(s)
c = '.'.join(b)
f = len(s)*2
d = c.rjust(int(f), '.')
print(d)

print((input().lower().replace("a", '').replace("o", '').replace("y", '').replace("e", '').replace("u", '').replace("i", '').replace('','.'))[:-1])

s = input()
s = s.lower()
s = s.replace('a', '')
s = s.replace('o', '')
s = s.replace('y', '')
s = s.replace('e', '')
s = s.replace('u', '')
s = s.replace('i', '')
s = s.replace('', '.')
s = s.rstrip('.')
print(s)

print(*("." + i for i in input().lower() if i not in "aoyeui"), sep="")

print('.' + '.'.join(input().lower().replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')))

s = input().lower()
s = s.replace('a', '')
s = s.replace('o', '')
s = s.replace('y', '')
s = s.replace('e', '')
s = s.replace('u', '')
s = s.replace('i', '')
s ='.'.join(s)
print('.'+s)

s=input()
s=s.lower().replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')
print('.'+'.'.join(s))