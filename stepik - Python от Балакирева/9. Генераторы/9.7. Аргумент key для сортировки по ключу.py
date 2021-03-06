# Аргумент key для сортировки по ключу.
# list.sort() - метод для сортировки элементов списка
# sorted() - функция для сортировки итерируемых объектов
def is_odd(x):
    return x % 2
a = [4, 3, -10, 1, 7, 12]
b = sorted(a, key=is_odd)
print(b)


a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x % 2)
c = sorted(a, key=lambda x: x % 2)
print(c)

def key_sort(x):
    return x if x % 2 == 0 else 100 + x

b = [4, 3, -10, 1, 7, 12]
c = sorted(b, key=key_sort)
print(c)

# Сортировка элементов списка по длине строк:
print("Сортировка элементов списка по длине строк:")
lst = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]

b = sorted(lst, key=len)
print(b)

# Сортировка по последнему символу слова:
print("Сортировка по последнему символу слова:")
lst = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]
b = sorted(lst, key=lambda x: x[-1])
print(b)

b = sorted(lst, key=lambda x: x[0])
print(b)

# Сортировка коллекций:
print("Сортировка коллекций (по возрастанию цены):")
books = (
    ("Евгений Онегин", "Пушкин А.С.", 200),
    ("Муму", "Тургенев И.С.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500),
    ("Мертвые души", "Гоголь Н.В.", 190)
)

b = sorted(books, key=lambda x: x[-1])
print(b)

#
print("Tasks")
# На вход программы поступает список наименований рек, записанных в одну строчку через пробел. Необходимо отсортировать
# этот список в порядке убывания длин названий. Результат вывести в одну строчку через пробел.
# Sample Input:
# Лена Енисей Обь Волга Дон
# Sample Output:
# Енисей Волга Лена Обь Дон
n = input().split()
print(*sorted(n, key=len)[::-1])

# Подвиг 2. На вход программы поступает строка в формате:
# предмет_1=вес_1
# ...
# предмет_N=вес_N
# Веса предметов заданы целыми числами. Необходимо на основе этих данных сформировать словарь и, затем, на основе этого
# словаря сформировать список предметов по убыванию их веса. (В списке должны находиться только наименования предметов
# без их весов).
# Отобразить полученный результат в виде строки с названиями через пробел.
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

dct = dict((i.split("=")[0], int(i.split("=")[1])) for i in lst_in)
print(*sorted(dct, key=dct.get, reverse=True))

#
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
d = dict(s.split("=") for s in lst_in)
res = sorted(d, key=lambda x: int(d.get(x)), reverse=True)
print(*res)


# Подвиг 3. Известно, что порядок нот, следующий: до, ре, ми, фа, соль, ля, си. На вход программы поступает строка с
# набором этих нот, записанных через пробел. Необходимо сформировать список из входной строки с нотами, отсортированными
# указанным образом. Результат вывести в виде строки из нот, записанными через пробел.
order =  ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
print(*sorted(input().split(), key=lambda x: order.index(x)))

#
s = 'до, ре, ми, фа, соль, ля, си'
print(*sorted(input().split(), key=s.find))

#
d = {'до': 0, 'ре': 1, 'ми': 2, 'фа': 3, 'соль': 4, 'ля': 5, 'си': 6}

print(*sorted(input().split(), key=lambda x: d[x]))

#
notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
print(*sorted(input().split(), key=notes.index))

#
print(*sorted(input().split(), key=lambda x: ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'].index(x)))

