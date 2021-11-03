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




