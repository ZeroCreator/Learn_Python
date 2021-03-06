# ФОРМАТИРОВАНИЕ СТРОК.

name = 'Семен'
mid_name = 'Семенович'
balance = 32.56

text = '''Дорогой $$ , баланс вашего лицевого счета составляет $ руб.'''

print(text)

print('1. Способ - конкатенация:')

text = """Дорогой """ + name + ' ' + mid_name + """, баланс вашего лицевого счета составляет """ + str(balance) +  """ руб."""
print(text)

print('2. Способ - метод строки - формат:')
print('Позиционное форматирование:')
name = 'Семен'
mid_name = 'Семенович'
balance = 32.56
text = """Дорогой {0} {1}, баланс вашего лицевого счета составляет {2} руб.""".format(name, mid_name, balance)
print(text)

print('Именованное использование перменных:')   # Если нужно исподльзовать одну переменную несколько раз
text = """Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {balance} руб.""".format(name=name, mid_name=mid_name, balance=balance)
print(text)

text = """Дорогой {n} {m}, баланс вашего лицевого счета составляет {b} руб.""".format(n=name, m=mid_name, b=balance)
print(text)

#
print('Tasks')
# Напишите программу, которая считывает слово, затем выводит:
#  «Что Вы сказали? [это слово] ? Какое интересное слово».
text = input()
print('''Что Вы сказали? {t}? Какое интересное слово'''.format(t=text))

print('Что Вы сказали? {0}? Какое интересное слово'.format(input()))

a = input()
text = """Что Вы сказали? {a}? Какое интересное слово""".format(a=a)
print(text)

print(f'Что Вы сказали? {input()}? Какое интересное слово')

# Программа запрашивает у пользователя имя и фамилию, после чего выводит приветственное сообщение в
# следующем формате "Здравствуйте, <фамилия> <имя>!"
name = input()
surname = input()
print('''Здравствуйте, {s} {n}!'''.format(n=name, s=surname))


print("Здравствуйте, {1} {0}!".format(input(), input()))

name = input()
surname = input()
print('Здравствуйте, {1} {0}!'.format(name, surname))

a = input()
b = input()
print(f'Здравствуйте, {b} {a}!')

a,b = input(), input()
print("Здравствуйте, {0} {1}!".format(b, a))

print('Здравствуйте, {1} {0}!'.format(input(), input()))