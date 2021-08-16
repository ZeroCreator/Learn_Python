# Генераторы словарей.
# key:value
a = {i: i ** 2 for i in range(1, 11)}  # Обход любой коллекции, которая поддерживает итерацию.
print(a)

# Это то же самое, что:
b = {}
for i in range(1, 11):
    b[i] = i ** 2

print(b)

a = {word: len(word) for word in ['hello', 'hi', 'www']}  # Список, состоящий из строк.
print(a)

data = {
    'Джефф Безос': '177',
    'ИлоН МаСк': '126',
    'бернар АрнО': '150',
    'БиЛл ГейтС': '124',
}
# 1. Сделать все буквы в словах маленькими, кроме первых.
# 2. Каждое значение преобразовать в целое число.
new_data = {key.title(): int(value) for key, value in data.items()}
print(data)
print(new_data)

# Это то же самое, что:
new_data = {}
for key, value in data.items():
    new_data[key.title()] = int(value)
print(data)
print(new_data)

#
print('Преобразование типа данных')
users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [3, 'username', '1234d'],
    [51, 'qwerty', '1234'],
]
print(users[4])
# Задача - обращаться к данным списка по ID пользователя, а не по индексам.
new_users = {user[0]: user for user in users} # Создаем словарь из списка
print(new_users)
print(new_users[51])

#
print('Tasks')
# В вашем распоряжении имеется вложенный список people, в котором хранятся имена и телефоны.
# Ваша задача создать словарь при помощи генератора словарей, в котором в качестве ключей будут хранится номера телефонов,
# а значениями будут имена владельцев. Обязательно сохраните этот словарь в переменной phone_book.
# Выводить ничего не нужно, только правильно заполните словарь в переменной phone_book
people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601'],
    ['Ann Hoffman', '434.104.4302'],
    ['John Leonard', '(956)182-8435'],
    ['Daniel Ross', '870-365-8303x416'],
    ['Jacqueline Moon', '+1-757-865-4488x652'],
    ['Gregory Baker', '705-576-1122'],
    ['Michael Spencer', '(922)816-0599x7007'],
    ['Austin Vazquez', '399-813-8599'],
    ['Chad Delgado', '979.908.8506x886'],
    ['Jonathan Gilbert', '9577853541']
]

phone_book = {user[1]: user[0] for user in people}
print(phone_book)

#
phone_book = {value:key for key, value in people}


