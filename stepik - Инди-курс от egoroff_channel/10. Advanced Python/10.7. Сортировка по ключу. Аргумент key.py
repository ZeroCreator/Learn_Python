# 10.7. Сортировка по ключу. Аргумент key.
a = [4, -10, 43, -300, 54, 289, -34, -8, 749]
print(sorted(a))

# 1. встроенная функция
print('1. встроенная функция')
print(sorted(a, key=abs))

# 2. собственный функции
print('2. собственный функции')
def f(x):
    return x%10 # по возрастанию

def f1(x):
    return -(x%10) # по убыванию
# сортировка по последнему числу
a = [4, 10, 43, 300, 54, 289, 34, 8, 749]
print(sorted(a, key=f))
print(sorted(a, key=f1))

# 3. Сортировка по двум критериям
print('3. Сортировка по двум критериям')
def f2(x):
    return x%10, x//10%10

print(sorted(a, key=f2))

# 4. Встроенные методы объектов
print('4. Встроенные методы объектов')
a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(a))
print(sorted(a, key=str.lower))

# 5. Анонимные функции
print('5. Анонимные функции')

a = ['ZZZ 79', 'aaa 45 ', 'eee 43 ', 'ddd 800 ', 'BBB 5', 'www 14']
print(sorted(a, key=lambda x: int(x.split()[1])))

# Двойная сортировка при помощи lambda-функции
print('Двойная сортировка при помощи lambda-функции')
a = ['ZZZ 800', 'aaa 45 ', 'eee 43 ', 'DDD 800 ', 'BBB 43', 'www 14']
print(sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0].lower())))
print(sorted(a, key=lambda x: (-int(x.split()[1]), x.split()[0].lower()))) # по убыванию

print(sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0].lower()), reverse=True))

a = ['ZZZ 800', 'aaa 45 ', 'eee 43 ', 'DDD 800 ', 'AaA 43', 'aaa 14']
a = (sorted(a, key=lambda x: int(x.split()[1])))
print(sorted(a, key=lambda x: x.split()[0].lower(), reverse=True))

#
print('Tasks')
# Напишите программу, которая отсортирует список subject_marks по возрастаю оценок.
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
a = sorted(subject_marks, key=lambda x: x[1])
for i in a:
    print(*i)


# Напишите программу, которая отсортирует список subject_marks по убыванию оценок.
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]

a = sorted(subject_marks, key=lambda x: -(x[1]))
for i in a:
    print(*i)

# Напишите программу, которая отсортирует список subject_marks по убыванию оценок. Предметы, имеющих одинаковые оценки,
# должны быть отсортированы в алфавитном порядке
# Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел
subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

a = sorted(subject_marks, key=lambda x: (-(x[1]), x[0]))
for i in a:
    print(*i)

#
subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

[print(*i) for i in sorted(subject_marks, key=lambda x: (-x[1], x[0]))]

#
[print(*_) for _ in sorted(subject_marks, key = lambda x: (-x[1], x[0]))]

# Напишите программу, которая отсортирует список models по цвету в лексикографическом порядке (по алфавиту)
# Затем распечатайте элементы этого списка, каждый элемент на новой строке в формате:
# Производитель: <make>, модель: <model>, цвет: <color>
models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]

[print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}") for i in sorted(models, key = lambda x: x['color'])]

#
for i in sorted(models, key=lambda x: x['color']):
    print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")

