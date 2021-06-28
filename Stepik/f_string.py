name = 'Семен'
mid_name = 'Семенович'
balance = 32.56

text = 'Дорогой {n} {m}, баланс вашего лицевого счета составляет {b} руб.'.format(b=balance, m=mid_name, n=name)

print(text)

name = 'Семен'
mid_name = 'Семенович'
balance = 32.56

def f(x):
    return x**2

text = f'Дорогой {name.lower()} {mid_name.upper()}, баланс вашего лицевого счета составляет {f(5)} руб.'

print(text)


d = {
'name': 'Семен',
'mid_name': 'Семенович',
'balance': 32.56
}

text = f"Дорогой {d['name']} {d['mid_name']}, баланс вашего лицевого счета составляет {d.get('balance')} руб."

print(text)

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
    #print(name, mid_name, balance)


for name, mid_name, balance, g in a:
    text = f'{gender[g]} {name} {mid_name}, баланс вашего лицевого счета составляет {balance} руб.'
    print(text)