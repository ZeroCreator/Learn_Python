# Использование словарейю
# 1. Подсчет количества обектов. При таком использовании в словаре ключи будут являться обектами,
# а значение ключа - количество появления этих обектов.
# Подается строка на вход. Надо подсчитать, колько в этой строке появилась та или иная буква.
'''
s = input()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
'''
s = input()
d = {}
for i in s:
    if i.isalpha():
        d[i] = d.get(i, 0) + 1

for i in sorted(d):
    print(i, d[i])

# 2. Замена разряженного списка. Вместо списка массива) из большого количества элементов, в котором предполагается,
# что не все элементы будут использоваться.
# Метод подсчета - сколько раз встречается каждая буква в слове.
s = input()
letters = [0]*26
for i in s.lower():
    if i.isalpha():
        nomer = ord(i) - 97
        letters[nomer] += 1

print(letters) # Разряженный список - много пустых элементов.

#for i in range(26):
#    if letters[i] > 0:
#        print(chr(i + 97), letters[i])

# 3. Установить соответствие между обектами.
print('Словарь')
# Соответствие между русским словом и английским.
'''
words = {}
while True:
    s = input()
    if s in words:
        print('Слово', s, 'переводится как', words[s])
    else:
        print('Введите перевод слова ', s)
        words[s] = input()
'''
# 4. Хранение данных об обекте.
contacts = {
    "John Kennedy": {
        'birthday': "29 may 1917", 'city': 'Brookline',
        'phone': None, 'children': 3
    },
    "Arnold Schwarzenegger": {
        'birthday': "30 july 1947", 'city': 'Gradec',
        'phone': '555-555-555', 'children': 5
    },
    "Donald John Trump": {
        'birthday': "14 july 1946", 'city': 'New York',
        'phone': '777-777-777', 'children': 4

    }
}

persons = ["Donald John Trump", "Arnold Schwarzenegger", "John Kennedy"]
for person in persons:
    print(person, contacts[person]['birthday'])

for person in persons:
    birthday = contacts[person]['birthday']
    city = contacts[person]['city']
    phone = contacts[person]['phone']
    children = contacts[person]['children']
    print(person, contacts[person])
    print(person, children, phone)
