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