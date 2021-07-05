# F-строки.

name = 'Семен'
mid_name = 'Семенович'
balance = 32.56

text = 'Дорогой {n} {m}, баланс вашего лицевого счета составляет {b} руб.'.format(b=balance, m=mid_name, n=name)

print(text)

name = 'Семен'
mid_name = 'Семенович'
balance = 32.00

print('1. f-строка')
text = f'Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {balance} руб.'
print(text)

text = f'Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {-balance*2} руб.'
print(text)

text = f'Дорогой {name.lower()} {mid_name.upper()}, баланс вашего лицевого счета составляет {56*2} руб.'
print(text)

text = f'Дорогой {name.lower()} {mid_name.upper()}, баланс вашего лицевого счета составляет {abs(-45)} руб.'
print(text)

#
print('Использование функции:')
def f(x):
    return x**2

text = f'Дорогой {name.lower()} {mid_name.upper()}, баланс вашего лицевого счета составляет {f(5)} руб.'
print(text)

#
print('Использование словарей:')
d = {
'name': 'Семен',
'mid_name': 'Семенович',
'balance': 32.56
}

text = f"Дорогой {d['name']} {d['mid_name']}, баланс вашего лицевого счета составляет {d.get('balance')} руб."

print(text)

#
print('Использование списка:')
gender = {
    'm': 'Дорогой',
    'f': 'Дорогая'
}
a = [
    ['Семен', 'Семенович', 32.56, 'm'],
    ['Тамара', 'Ивановна', 13.12, 'f'],
    ['Михаил', 'Анатольевич', 238.12, 'm'],
]

for i in a:
    print(i)

#for name, mid_name, balance in a:
#    text = f'''Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {balance} руб.'''
#   print(text)

for name, mid_name, balance, g in a:
    text = f'{gender[g]} {name} {mid_name}, баланс вашего лицевого счета составляет {balance} руб.'
    print(text)

#
print('Tasks')
# На вход программе поступает строка - имя пользователя. Вам необходимо при помощи f-строки вывести сообщение:
# "Мое имя <name>!"
name = input()
print(f'Мое имя {name}!')

print(f'Мое имя {input()}!')

# Теперь ваша программа спрашивает у пользователя не только имя, но и его возраст.
# После этого программа должна вывести сообщение:
# "Hello <name>. You are <age> years old."
name = input()
age = input()
print(f'Hello {name.upper()}. You are {age} years old.')

print(f"Hello {input().upper()}. You are {input()} years old.")

name, age =input(), input()
print(f'Hello {name.upper()}. You are {age} years old.')

print(f"Hello {input().upper()}. You are {input()} years old.")

# Программа запрашивает у пользователя курс доллара - вещественное число,  и также количество долларов(целое число),
# которое пользователь хочет приобрести. В итоге программа должна вывести следующее сообщение:
# "Current dollar rate is <курс доллара>. You want buy <количество долларов> dollars
# You must pay <стоимость>"
course = float(input())
quantity = int(input())
print(f'''Current dollar rate is {course}. You want buy {quantity} dollars
You must pay {course*quantity}''')

a, b = float(input()), int(input())
print(f"Current dollar rate is {a}. You want buy {b} dollars\nYou must pay {a * b}")

print(*[f"Current dollar rate is {a}. You want buy {b} dollars\nYou must pay {b * a}" for a, b in [(float(input()), int(input()))]])

# Напишите программу, которая запрашивает имя пользователя и его год рождения. Программа должна вывести на
# экран сообщение "<Имя пользователя>, вам исполнится 77 лет в <год>"
name = input()
age = int(input())
print(f'''{name}, вам исполнится 77 лет в {age + 77}''')

print(f'{input()}, вам исполнится 77 лет в {int(input())+77}')

# При помощи F-строк выведем информацию о трех видах деления, которые мы с вами изучили ранее: обычное деление,
# целочисленное и деление по остатку.
# Входные данные:
# На вход программе поступают два целых числа, при этом гарантируется, что второе число не равно 0.
# Выходные данные:
# Необходимо вывести результат трех видов деления первого числа на второе в определенном формате (см. примеры ниже)
# Sample Input 1:
# 11
# 5
# Sample Output 1:
# 11 / 5 = 2.2
# 11 // 5 = 2
# 11 % 5 = 1
a, b = int(input()), int(input())
print(f'''{a} / {b} = {a/b}
{a} // {b} = {a//b}
{a} % {b} = {a%b}''')

a,b=int(input()),int(input())
print(f'{a} / {b} = {a/b}',f'{a} // {b} = {a//b}',f'{a} % {b} = {a%b}',sep='\n')

n1, n2 = input(), input()
for op in ['/', '//', '%']:
  print(f"{n1} {op} {n2} = {eval(n1 + op + n2)}")

a,b=int(input()),int(input())
print(f'{a} / {b} = {a/b}\n{a} // {b} = {a//b}\n{a} % {b} = {a%b}')