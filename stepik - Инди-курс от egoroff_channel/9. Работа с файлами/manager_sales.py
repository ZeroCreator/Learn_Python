import json
maximum = 0
max_name = ''
max_lastname = ''
with open('manager_sales.json') as file:
    data = json.load(file)
    print(data, type(data))

    for element in data:
        name = element['manager']['first_name']
        lastname = element['manager']['last_name']
        total = 0
        for car in element['cars']:
            total += car['price']

        if total > maximum:
            maximum = total
            max_name = name
            max_lastname = lastname

    print(max_name, max_lastname, maximum)



'''
#
print(*sorted(((f"{dct['manager']['first_name']} {dct['manager']['last_name']}", sum([ls['price'] for ls in dct['cars']])) for dct in (__import__('json').loads(open('manager_sales.json', 'r').read()))), key=lambda x: x[1]), sep='\n')


#
import json

b = {}
a = 0
with open("manager_sales.json", "r", encoding='utf-8') as file:
    data = json.load(file)
    for i in data:
        name = i['manager']['first_name'] + " " + i['manager']['last_name']
        b.setdefault(name)
        price = i['cars']
        for ki in price:
            a += ki['price']
        b[name] = a
        a = 0
print(*sorted(b.items(), key=lambda x: -x[1]))

#
import json

with open('manager_sales.json', 'r') as f:
    f = json.load(f)

d = {}
for c in f:
    d[f'{c["manager"]["first_name"]} {c["manager"]["last_name"]}'] = sum([i['price'] for i in c['cars']])

print(*sorted(d.items(), key = lambda x: -x[1])[0])

#

import json

with open('manager_sales.json','r') as file:

    data=json.load(file)


list_of_sum=[] # список в котором будут все сумы

sum=0

for info in data:

    for car in info['cars']:

        sum=sum+int(car['price'])

    list_of_sum.append(sum)

    sum=0

print(max(list_of_sum))# Находим максимальную суму в списке

print(data[list_of_sum.index((max(list_of_sum)))]['manager'])# находим менеджера по индексу


#
import json

def convert(info):
    return {
        **info['manager'],
        'sum': sum(x['price'] for x in info['cars'])
    }

with open('manager_sales.json') as f:
    sales = json.load(f)

print(max(map(convert, sales), key = lambda x: x['sum']))

#
import json
with open('manager_sales.json') as f:
    print(*sorted([[man['manager']['first_name'], man['manager']['last_name'], sum(car['price']
                    for car in man['cars'])] for man in json.load(f)], key=lambda x: x[2])[-1])
                    

'''