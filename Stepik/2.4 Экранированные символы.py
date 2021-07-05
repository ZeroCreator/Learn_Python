# ЭКРАНИРОВАННЫЕ (СЛУЖЕБНЫЕ) СИМВОЛЫ.

s = '''hello
world
hy
bye'''
print(s)
print(len(s))

#
print('1. "\\n" - перенос строки')
f = 'hello\nword\nhi\nbye'
print(f)
print(len(f))

a = 'abc\ndef'
print(a)
print(len(a))

#
print('2. "\\t" - табуляция')
print('hello\nword\nhi\nbye')

#
print('3. "r" - перед началом строки - убрать служебные символы в строке:')
print('hello\nword\nhi\nbye/thello\nword\nhi\nbye')
print(r'hello\nword\nhi\nbye/thello\nword\nhi\nbye')

a = 'abc\nre\tgfd\ngfd'
print(a)
print(len(a))
b = r'abc\nre\tgfd\ngfd'
print(len(b))
print(b)
#
print('Tasks')
#
'''
/\_/\ 
>^,^< 
 / \  
(|_|)_/
'''
print('Cat')
print('/\\_/\\ \n>^,^< \n / \\  \n(|_|)_/')

print(r"/\_/\ ", r">^,^< ", r" / \  ", r"(|_|)_/", sep="\n")

#
print()
'''
  /~~~\
 //^ ^\\
(/(_*_)\)
_/''*''\_
(/_)^(_\)
'''
print('Dog')
print("  /~~~\\  ", " //^ ^\\\ ", "(/(_*_)\\)", "_/''*''\\_", "(/_)^(_\\)", sep = "\n")

print('  /~~~\\\n //^ ^\\\\\n(/(_*_)\)\n_/\'\'*\'\'\_\n(/_)^(_\)')