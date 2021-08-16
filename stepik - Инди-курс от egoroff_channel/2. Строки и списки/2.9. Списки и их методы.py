# СПИСКИ И ИХ МЕТОДЫ.

print('1. Метод добавления в конец списка .append():')
s = 'hello'
s.upper()
print(s)

a = [12, 43, 54, 65, 76, 3]     # Добавляет по одному элементу
a.append(46)
print(a)

a.append('hello')
a.append([1, 2, 3])
print(a)

#
print('2. Метод очищения списка .clear():')    # Делает список пустым
a.clear()
print(a)

#
print('3. Копия списка - метод .copy():')
a = [12, 43, 54, 65, 76, 3]
a.copy()  # аналогично a[:]
b = a.copy()
a.append([1, 2, 3])
print(a, b)

#
print('4. Подсчет количества значения в списке - метод .count():')
print(b.count(12))
print(a.count(3))
b.append(12)
print(b.count(12))

#
print('5. Поиск индекс первого значения в списке - метод .index():')
print(b.index(54))
print(b.index(12))
print(b.index(12, 3))   # С какого индекса начинается поиск

print(12 in b[3:5])

#
print('5. Метод вставки значения по индексу .insert():')
print(len(b))
b.insert(2, 100)    # Длина списка Увеличивается, список сдвигается вправо. Добавляется только один объект
print(b)
print(len(b))

#
print(' 6. Удаление значения из конца списка и показывает его - метод .pop():')
print(b.pop())
print(b)
last = b.pop()      # Сохранение значения, который попнут из списка
print(last)
print(b)

#
print('Удаление по индексу:')
print(b.pop(3))
print(b)

#
print('7. Удаление по значению из списка - метод .remove():')
b.remove(100)
print(b)
b.append(43)
print(b)
b.remove(43)    # Удаляет первое найденное значение
print(b)

#
print('8. Переворачивание списка - метод .reverse():')
b.reverse()
print(b)
b.reverse()
print(b)

#
print('9. Сортировка - метод .sort():')
print('по возрастанию:')
b.sort()
print(b)

#
print('по убыванию:')
b.reverse()  # Отсортирует по убыванию
print(b)
a = [12, 43, 54, 65, 76, 3]
a.sort(reverse=True)
print(a)

#
print('Tasks')
# На вход программе поступает список значений. Ваша задача преобразовать его таким образом,
# чтобы элементы расположились в обратном порядке.
mas = input().split()
mas.reverse()
print(*mas)

# Программа получает на вход список из целых чисел. Подсчитайте сколько раз в нем присутствует число 999
a = list(map(int, input().split()))
print(a.count(999))

print(input().split().count('999'))

print(list(map(int, input().split())).count(999))

# Вводится два слова через пробел. Ваша задача преобразовать данную фразу таким образом, чтобы все буквы стали
# заглавными и между буквами в каждом слове появились дефисы
a = list(input().upper())
c = '-'.join(a)
print(c.replace('- -', ' '))

re = input().upper()
print('-'.join(re).replace('- -',' '))

print(*['-'.join(i) for i in input().upper().split()])

print(*map('-'.join, input().upper().split()))

a, b = input().upper().split()
print('-'.join(a), '-'.join(b))

# Напишите программу, которая выводит слова введённой строки (части, разделённые символами пустого пространства)
# в столбик. Нужно обойтись только методом split у списков и методом join у строк, в программе должен быть всего
# один вызов print.
a = list(input().split())
print('\n'.join(a))

print('\n'.join(input().split()))

print(input().replace(' ', '\n'))

print(*input().split(), sep='\n')

# Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека
# Вам необходимо вывести фамилию и инициалы, как в примерах ниже:
# Sample Input 1:
# Марина Денисовна Климова
# Sample Output 1:
# Климова М.Д.
a = list(input().split())
n, m, d = a[0], a[1], a[2]
print(f'{d} {n[0]}.{m[0]}.')

n = input().split()
print(f'{n[-1]} {n[0][0]}.{n[1][0]}.')

text = input().split()
print(f'{text[2]} {text[0][0]}.{text[1][0]}.')

