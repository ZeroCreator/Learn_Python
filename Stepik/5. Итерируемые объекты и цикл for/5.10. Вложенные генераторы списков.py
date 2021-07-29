# Вложенные генераторы списков.
# Обработка кортежей:
a = [
    ('Sidorov', 1995),
    ('Lukov', 2002),
    ('Petrov', 1991),
    ('Gorbachev', 1984),
    ('Kostin', 2000),
    ('Isaev', 2005),
    ('Eliseev', 1999),
    ('Kozlov', 2004),
    ('Bukov', 1995),
    ('Gavrilov', 1980),
    ('Efremov', 2006),
]
# Отбор по первой букве фамилии:
b = [elem[0] for elem in a if elem[0].startswith('E')]
print(b)

# Отбор по году рождения:
b = [elem[0] for elem in a if elem[1] > 2000]
print(b)

#
b = [elem[0][0] for elem in a if elem[1] > 2000]
print(b)

# Обработка словарей:
a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 200, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
    'Gavrilov': {'age': 1980, 'hobby': 'music', 'car': 'Opel'},
    'Efremov': {'age': 2006, 'hobby': 'tennis', 'car': 'Audi'},
}

# Заполнение списка ключами:
b = [elem for elem in a]
print(b)

b = [{elem, a[elem]['car']} for elem in a if a [elem]['age'] < 2000 and a[elem]['hobby']=='soccer']
print(b)