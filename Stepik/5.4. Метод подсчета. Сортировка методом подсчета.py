# Метод подсчета. Сортировка подсчетом.
a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]

# Подсчитать, сколько каждое число было в списке:
print('Подсчитать, сколько каждое число было в списке:')
count = [0]*6
for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print(i, count[i])

# Сортировка по возрастанию:
print('Сортировка по возрастанию:')
count = [0]*6
for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print((str(i) + ' ')*count[i], end='')

