# СТРОКИ И ОПЕРАЦИИ НАД НИМИ.

print('hello')
print("hello")
print('''hello
world
!!!
''')
print('hello\nworld\n!!!')

s = 'hello'
r = 'world'
d = ' '
e = ''

#
print('1. Операция конкатенация (сцепление строк):')
print('abc' + 'dec')

print(s + r)
print(s + ' ' + r)

#
print('2.Умножение:')
print('a'*5)
print(s*3)

print('abc' + str(3))

#
print('3. Нахождение длины строки:')
print(len('hello world'))
print(len(''))
print(len(s))

s = input()
print('Вы ввели', len(s), 'символов')

#
print('4. Проверка наличия подствроки в строке:')
s = '123456'
print('4' in s)
print('45' in s)
print('54' in s)

#
print('5. Сравнение строк:')
print('aaa' == 'aaa')
print('AAA' == 'aaa')

print('abc' > 'r')
print(ord('a')) #ascii code table
print(ord('b'))
print(ord('A'))
print(ord('r'))
print('a' > 'A')

print('FGHVYU' < 'dgvjsh')

print('abc' < 'abcd')
print('input' == 'input ')

print('Tasks')
# Напишите программу, которая выводит фразу «Я стану крутым программистом!» три раза на отдельных строках.
print('Я стану крутым программистом!\n'*3)

a = 'Я стану крутым программистом!'
print(a, a, a, sep='\n')

n = 'Я стану крутым программистом!'
print((n+'\n')*3)

d = 'Я стану крутым программистом!\n'
print(d*3)


# Напишите программу, которая сначала считывает две фразы по очереди, а потом воспроизводит их в той же
# последовательности, каждую на отдельной строчке.
print(input(), input(), sep='\n')

print(input())
print(input())

a = input()
b = input()
print(a, b, sep='\n')

print(input()+"\n" + input())
