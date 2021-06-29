# СПИСКИ И ИХ МЕТОДЫ.

print('1. Метод добавления в конец списка append:')
s = 'hello'
s.upper()
print(s)

a = [12, 43, 54, 65, 76, 3]
a.append(46)
print(a)

a.append('hello')
a.append([1, 2, 3])
print(a)

#
print('2. Метод очищения списка clear:')
a.clear()
print(a)

#
print('3. Копия списка - метод copy:')
a = [12, 43, 54, 65, 76, 3]
a.copy()  # аналогично a[:]
b = a.copy()
a.append([1, 2, 3])
print(a, b)

#
print('4. Подсчет количества значения в списке - метод count:')
print(b.count(12))
print(a.count(3))
b.append(12)
print(b.count(12))

#
print('5. Поиск индекс первого значения в списке - метод index:')
print(b.index(54))
print(b.index(12))
print(b.index(12, 3))

print(12 in b[3:5])

#
print('5. Метод вставки значения по индексу insert:')
b.insert(2, 100)
print(b)

#
print(' 6. Удаление значения из конца списка - метод pop:')
b.pop()
print(b)
last = b.pop()
print(last)
print(b)

#
print('Удаление по индексу:')
b.pop(3)
print(b)

#
print('7. Удаление по значению из списка - метод remove:')
b.remove(100)
print(b)
b.append(43)
print(b)
b.remove(43) #Удаляет первое значение
print(b)

#
print('8. Переворачивание списка - метод reverse:')
b.reverse()
print(b)
b.reverse()
print(b)

#
print('9. Сортировка - метод sort:')
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




