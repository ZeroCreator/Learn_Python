# СПИСКИ: ИНДЕКСЫ И СРЕЗЫ.

a = [43, 54, 2, 54, 32]

print('1. Получить элемент списка:')
print(a[0], a[4])
print(a[-1])
b = [3, 4, 5, 6, 7, 8, 9, 10, 11]

print(b)
print(b[-1])
print(b[1:4])
print(b[2:-1])
print(b[2:])
print(b[:2])
print(b[:])

#
print('С шагом 2:')
print(b[::2])

#
print('Остальные:')
print(b[1::2])

#
print('С шагом 3:')
print(b[3:6:3])

#
print('Перевернуть список:')
print(b[::-1])

#
print('С конца списка каждый второй элемент:')
print(b[::-2])

#
print('Список - объект изменяемый. По индексу можно поместить новое значение:')
print(b)
b[2] = 100
print(b)

#
print('Присвоение срезам индексов новых значений:')
b[3:5] = 34, 23
print(b)

b[2:5] = 23, 34     # Уменьшение списка
print(b)

#
print('Удаление элемента')
del b[2]
print(b)

#
print('Изменение переменных, ссылающихся на один и тот же список:')
a = [1, 2, 3]
d = a
print(a)
print(d)
b[2] = a
print(b)
print(a, d)
d[1] = 100
print(d)
print(a)

#
print('Сохранение среза списка:')
a = [1, 2, 3]
d = a[:]        # Сохранение всего списка как новый объект
print(d)
d[1] = 100
print(d)
print(a)

#
print('Tasks')
# Программа получает на вход список целых чисел и ваша задача вывести последние три элемента этого списка через срез
# Гарантируется, что список будет состоять не менее чем из пяти элементов.
a = list(map(int, input().split()))
b = len(a)
print(a[(b-3):])

a = list(map(int, input().split()))
print(a[-3:])

print(list(map(int, input().split()[-3:])))

print([*map(int, input().split())][-3:])

# Перед вами список топовых сериалов по версии кинопоиска. Ваша задача заменить в нем
# сериал "Бригада" на "Сверхъестественное" и "Друзья" на "Настоящий детектив"
top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top[-1] = 'Сверхъестественное'
top[2] = 'Настоящий детектив'
print(top)

top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']

top[top.index('Бригада')] = 'Сверхъестественное'
top[top.index('Друзья')] = 'Настоящий детектив'
print(top)

top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие',
       'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top[top.index("Бригада")], top[top.index("Друзья")] = "Сверхъестественное", "Настоящий детектив"
print(top)

top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие', 'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
top = ','.join(top).replace('Друзья', 'Настоящий детектив').replace('Бригада', 'Сверхъестественное').split(',')
print(top)


