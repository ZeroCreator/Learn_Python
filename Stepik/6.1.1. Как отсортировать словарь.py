# Как отсортировать словарь по ключам и значениям.
# Вывод по ключу:
heroes = {
    'Spider-Man': 80,
    'Batman': 65,
    'Superman': 85,
    'Wonder Woman': 70,
    'Flash': 70,
    'Iron Man': 65,
    'Thor': 90,
    'Aquaman': 65,
    'Captain America': 65,
    'Hulk': 87
}
#for i in heroes:
#    print(i)

# Как обратиться к значению (получаем пары):
for i in heroes:
    print(i, heroes[i])

# Сортировка ключей в алфавитном порядке:
for i in sorted(heroes):
    print(i, heroes[i])

# Если нужно обойти значения в упорядоченном виде - метод .values():
for i in sorted(heroes.values()):
    print(i)

# Отсортировать значение через ключ - метод .items(), key = lambda para:
for i in sorted(heroes.items(), key=lambda para: para[1]):                # Возвращает кортеж
    print(i)

# Сортировка и по ключу, и по значению:
for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):                # Возвращает кортеж
    print(i)

#
print('Tasks')
# Представьте, у нас есть список товаров и их стоимость, но мы хотим взглянуть на него в отсортированном виде.
# Вверху хотим видеть самые дорогие товары, внизу самые дешевые
# Программа будет принимать строки, в которых сперва указывается название товара, а затем через двоеточие с пробелом
# его цена - целое положительное число.
# Строка "конец" означает списка товаров и соответственно окончание ввода
# Все товары имеют уникальные названия, цены не дублируются.
# Ваша задача вывести список товаров по уменьшению цены
s = {}
while True:
    x = list(input().split(':'))
    if x[0] == 'конец':
        break
    else:
        k, v = x[0], x[1]
    s[k] = int(v)

for i in sorted(s.items(), key=lambda para: para[1], reverse=True):
        print(i[0])

#
dict={}
while True:
    a = input()
	if a == 'конец':
		break
	else:
		temp_lst = a.split(': ')
		dict[temp_lst[0]] = int(temp_lst[1])

for key, value in sorted(dict.items(), key=lambda x: x[1], reverse=True):
	print(key)

#
d = sorted([s.split(': ') for s in iter(input, 'конец')], key=lambda x: -int(x[1]))
for v in d:
    print(v[0])

#
lis={}
while True:
    all=input()
    if all=='конец':
        break
    else:
        a,b = map(str,all.split(':'))
        lis[a]=int(b)
for i,j in sorted(lis.items(),key=lambda para:para[1],reverse=True):
    print(i)

#
d = {}
while True:
    inn = input()
    if inn == 'конец':
        break
    k, price = inn.split(': ')
    d[k] = int(price)
[print(f'{k}') for k in sorted(d, key=d.get, reverse=True)]

#
product_list = {}

while True:
    p = input()
    if p == 'конец':
        break
    prod, price = p.split(': ')
    product_list[prod] = int(price)

for key, val in sorted(product_list.items(), key=lambda para: para[1], reverse=True):
    print(key)

#
enter, ls = input().replace(':', ''), []
while enter != 'конец':
    ls.append(enter.split())
    enter = input().replace(':', '')
[print(*i[:-1]) for i in sorted(ls, key=lambda x: -int(x[-1]))]

#
l = list(iter(input, 'конец'))
for i in sorted(l, key=lambda cena: -int(cena.split()[-1])):
    print(i[:(i.index(':'))])

