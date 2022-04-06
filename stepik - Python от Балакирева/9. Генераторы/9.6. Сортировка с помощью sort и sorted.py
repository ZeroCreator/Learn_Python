# Сортировка с помощью sort и sorted.
# list.sort() - метод для сортировки элементов списка. Меняет сам список и ничего не возвращает.
# sorted() - функция для сортировки итерируемых объектов
a = [4, 3, -10, 1, 7, 12.5]
a.sort()
print(a)

# Сортировка по убыванию:
print("Сортировка по убыванию:")
a.sort(reverse=True)
print(a)

# Создание нового отсортированного списка:
print("Создание нового отсортированного списка:")
a = [4, 3, -10, 1, 7, 12.5]
b = sorted(a)
print(b)

# Сортировка по убыванию:
print("Сортировка по убыванию:")
c = sorted(a, reverse=True)
print(c)

# Сортировка кортежей и строк:
print("Сортировка кортежей и строк:")

r = ("Волга", "Лена", "Дон", "Енисей")
g = sorted(r)
print(g)

print(sorted("python"))

# Сортировка словарей:
print("Сортировка словарей:")
d = {"river":"река", "house":"дом", "tree":"дерево", "road":"дорога"}

print(sorted(d))
print(sorted(d.values()))
print(sorted(d.items()))

print(dict(sorted(d.items())))

#
print("Tasks")
# На вход функции с именем get_sort поступает словарь, например, такой:
# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# Необходимо отсортировать словарь d по убыванию ключей (лексикографическая сортировка строк) и возвратить список из
# соответствующих значений ключей словаря. Например, для указанного словаря d, результатом должен быть список:
# ['дерево', 'лошадь', 'собака', 'кот', 'книга']
# Сигнатура функции get_sort должна быть следующей:
# def get_sort(d): ...
# В программе только определить функцию, вызывать ее не нужно и что-либо выводить на экран тоже не нужно.
# P. S. Подсказка: список в функции get_sort лучше всего формировать с помощью генератора списков.
d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}

def get_sort(d):
    return list(dict(sorted(d.items(), reverse=True)).values())

print(get_sort(d))

#
def get_sort(d):
    return [d[i] for i in sorted(d, reverse=True)]

#
def get_sort(d):
    return [i[1] for i in sorted(d.items(), reverse=True)]

#
def get_sort(d):
    return [v for k, v in sorted(d.items(), reverse=True)]


# На вход программы поступает список целых чисел, записанных в одну строчку через пробел. Необходимо выбрать из них
# четыре наибольших уникальных значения. Результат вывести на экран в порядке их убывания в одну строчку через пробел.
# Sample Input:
# 10 5 4 -3 2 0 5 10 3
# Sample Output:
# 10 5 4 3
lst = sorted(set(map(int, input().split())), reverse=True)
print(*[lst[i] for i in range(4)])

#
print(*sorted(set(map(int, input().split())), reverse=True)[:4])


# Подвиг 2. На вход поступает список целых чисел, записанных в одну строчку через пробел. Преобразуйте сначала эту
# строку в список из целых чисел, а затем список в кортеж из целых чисел. То есть, в программе будет две разные
# коллекции: список и кортеж. Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно,
# а иначе - примените функцию sorted.
# На экран ничего выводить не нужно, только сформировать две отсортированные коллекции: lst (список) - результат
# сортировки списка; tp_lst (кортеж) - результат сортировки кортежа.
# P. S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
s = input()
lst = list(map(int, s.split()))
lst.sort()
c = tuple(lst)
tp_lst = tuple(sorted(c))

#
s = input()


def get_sort(x):
    try:
        x.sort()
        return x
    except AttributeError:
        return type(x)(sorted(x))


lst = list(map(int, s.split()))
tp_lst = tuple(map(int, s.split()))


srt = get_sort(lst)
tp_lst = get_sort(tp_lst)

#
s = input()
lst = sorted(list(map(int, s.split())))
tp_lst = tuple(lst)

#
s = input()

# здесь продолжайте писать программу
lst=list(map(int, s.split()))
tp=tuple(map(int, s.split()))

lst.sort()
tp_lst=tuple(sorted(tp))

# Подвиг 5. На вход программы поступают два списка целых чисел (каждый в отдельной строке), записанных в одну строчку
# через пробел. Длины списков могут быть разными. Необходимо первый список отсортировать по возрастанию, а второй -
# по убыванию. Полученные пары из обоих списков сложить друг с другом и получить новый список чисел. Результат вывести
# на экран в виде строки чисел через пробел.
# P. S. Подсказка: не забываем про функцию zip.
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst1.sort()
lst2.sort(reverse=True)
print(*[a + b for a, b in (zip(lst1, lst2))])

#
lst1 = sorted(map(int, input().split()))
lst2 = sorted(map(int, input().split()), reverse=True)

lst = map(lambda x, y: x + y, lst1, lst2)
print(*lst)

#
lst_1 = sorted(map(int, input().split()))
lst_2 = sorted(map(int, input().split()))[::-1]

print(*map(sum, zip(lst_1, lst_2)))

#
lst1 = sorted(map(int, input().split()))
lst2 = sorted(map(int, input().split()), reverse = True)
print(*[sum(i) for i in zip(lst1, lst2)])






