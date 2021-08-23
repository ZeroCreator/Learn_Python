# 10.6. Сортировка коллекций. Метод sort и функция sorted.
# sort - метод списка; sorted - встроенная функция
print('sort - метод списка; sorted - встроенная функция')
a = [4, -10, 43, -300, 54, 89, -34]
b = 'hello world'
c = ('hi', 'zero', 'abracadabra', 'pikachu')
a.sort() # без присвоения
sorted(b)
sorted(a)
sorted(c)

# sort - метод изменяет первоначальный список
print('sort - метод изменяет первоначальный список')
print(a)

# sorted  не изменяет первоначальную коллекцию
# результатом всегда будет список независимо от переданной коллекции
print('sorted  не изменяет первоначальную коллекцию')
print(sorted(b))
print(b)

b = sorted(b)
print(b)

# Порядок сортировки элементов
print('Порядок сортировки элементов')

# c = sorted(c, key=function, reverse=False/True)
# c.sort(key=function, reverse=False/True)
# c = sorted(c, reverse=False/True)
# False - по возрастанию
# True - по убыванию
c = ('hi', 'zero', 'abracadabra', 'pikachu')
c = sorted(c, reverse=False)
print(c)

d = ('hi', 'zero', 'abracadabra', 'pikachu')
d = sorted(d, reverse=True)
print(d)
