# JSON - текстовый формат обмена данными.
# Структура данных - как в словаре Python.
# JavaScript Object Notation

# Преобразование json --> python
print('# Преобразование json --> python')

import json
from random import randint
from datetime import datetime
str_json = """
{
"response": {
    "count": 5942572,
    "items": [{
        "first_name": "Дмитрий",
        "id": 575849341,
        "last_name": "Ткачёв",
        "can_access_closed": false   
    }, {
        "first_name": "Ардак",
        "id": 393624838,
        "last_name": "Максим",
        "can_access_closed": true
}]
}
}
"""
print(type(str_json))
data = json.loads(str_json)
print(data)
print(type(data))
print(data['response'])
print(data['response']['count'])
print(data['response']['items'], type(data['response']['items']))

for item in data['response']['items']:
    print(item, type(item))
    print(item['first_name'], item['last_name'])

# удаление ключей:
print('удаление ключей:')
for item in data['response']['items']:
    del item['id'] # Удаляем ключ
    item['likes'] = randint(100, 200) # Добавляем ключ
    item['a'] = None
    item['now'] = datetime.now().strftime('%d/%m/%y')
print(data['response']['items'])

new_json = json.dumps(data, indent=2)
print(new_json)
print(json.loads(new_json))


# Преобразование python --> json
with open('my_json', 'w') as file:
    json.dump(data, file, indent=3)


with open('my_json', 'r') as file: # чтение из файла
    data = json.load(file)
print(data)
print(type(data))

#
print('Tasks')
# ctrl + alt + l - форматирование
