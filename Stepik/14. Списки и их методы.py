# СПИСКИ И ИХ МЕТОДЫ.

# 1. Метод добавления в конец списка append:
s = 'hello'
s.upper()
print(s)

a = [12, 43, 54, 65, 76, 3]
a.append(46)
print(a)

a.append('hello')
a.append([1, 2, 3])
print(a)

# 2. Метод очищения списка clear:
a.clear()
print(a)

# 3. Копия списка - метод copy:
a = [12, 43, 54, 65, 76, 3]
a.copy()  # аналогично a[:]
b = a.copy()
a.append([1, 2, 3])
print(a, b)

# 4. Подсчет количества значения в списке - метод count:
print(b.count(12))
print(a.count(3))
b.append(12)
print(b.count(12))

# 5. Поиск индекс первого значения в списке - метод index:
print(b.index(54))
print(b.index(12))
print(b.index(12, 3))

print(12 in b[3:5])

# 5. Метод вставки значения по индексу insert:
b.insert(2, 100)
print(b)

# 6. Удаление значения из конца списка - метод pop:

