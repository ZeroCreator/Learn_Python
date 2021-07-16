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
print('Сортировка по возрастанию:')             # Каждую цифру выводить столько раз, сколько она встретилась.
count = [0]*6
for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print((str(i) + ' ')*count[i], end='')


# Посчитать количество символов в строке:
print('Посчитать количество символов в строке:')
s = "jhdf HG jgkfYGg jhgkdf 543 *(@$%#"
letters = [0]*26
for i in s.lower():
    if i >= 'a' and i <= 'z':
        nomer = ord(i) - 97             # Получаем код символа и отнимаем от него 97
        letters[nomer] += 1

for i in range(26):
    if letters[i] > 0:
        print(chr(i+97), letters[i])    # Преобразовываем символ обратно в букву

# Сортировка подсчетом:
s = "jhdf HG jgkfYGg jhgkdf 543 *(@$%#"
letters = [0]*26
for i in s.lower():
    if i >= 'a' and i <= 'z':
        nomer = ord(i) - 97             # Получаем код символа и отнимаем от него 97 (смещаем код символа на 97)
        letters[nomer] += 1

for i in range(26):
    if letters[i] > 0:
        print(chr(i+97)*letters[i], end='')    # Преобразовываем символ обратно в букву (нейтрализуем первоначальное смещение)

# задача с использованием отрицательных значений:
a = []
import random
for i in range(10):
    a.append(random.randint(-10, 10))  # смещение +10

count = [0]*21
for i in a:
    count[i + 10] += 1
print(a)
for i in range(21):
    if count[i] > 0:
        print(i - 10, count[i])

# На вход вашей программе поступает положительное целое число n, а ваша задача вывести в порядке возрастания все цифры,
# которые встречались в этом числе, и напротив каждого также необходимо вывести сколько раз данная цифра встречалась
# в числе n
a = input()
count = [0] * 10
for i in a:
    count[int(i)] += 1
for i in range(10):
    if count[i] > 0:
        print(i, count[i])

#
n = input()
for i in range(10):
    if str(i) in n:
        print(i, n.count(str(i)))

#
digits = [0] * 10
for d in input():
    digits[int(d)] += 1
for i, d in enumerate(digits):
    print(i, d) if d > 0 else None

#
n = input()
a = [0]*10
for i in str(n):
    digit = int(i)
    a[digit] += 1
for i in range(10):
    if a[i] > 0:
        print(i, a[i])


# Вам необходимо отсортировать список, состоящий только из чисел в пределах от -100 до 100 включительно, сортировкой подсчетом.
# Программа получает на вход число n - количество элементов в списке, затем сами элементы списка
# Вам необходимо вывести отсортированный список
n = int(input())
a = list(input().split())
count = [0]*201
for i in a:
    count[int(i) + 100] += 1
for i in range(201):
    if count[int(i)] > 0:
        print((str(int(i) - 100) + ' ')*count[i], end='')

#
n = int(input())        # число элементов списка
a = map(int,input().split())
cnt = [0]*201
for i in a:
    cnt[i] += 1
for i in range(-100,101):
    if cnt[i] != 0:
        print((str(i)+' ') * cnt[i], end='')

#
n = int(input())
ls = input().split()
for i in range(0, len(ls)):
    for j in range(i+1, len(ls)):
        if int(ls[i]) > int(ls[j]):
            ls[i], ls[j] = ls[j], ls[i]
print(*ls)

#
