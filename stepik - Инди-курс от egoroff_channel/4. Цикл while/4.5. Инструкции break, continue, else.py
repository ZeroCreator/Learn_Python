# ИНСТРУКЦИИ break, continue, else.

print('Инструкция break - принудительный выход из цикла:')
i = 1
while True:
    print('Итерация №', i)
    if i == 10:
        break
        print('hi')
    i += 1
print('Hello')

while True:
    a = input()
    if a == 'exit':
        break
    print(a, len(a))

#
print('Инструкция continue - перекидывает в начало цикла:')
while True:
    a = input()
    if a == 'exit':
        break
    if len(a) < 5:
        continue
    print(a, len(a))

#
print('Инструкция else:')
i = 1
while i <= 15:
    print(i)
    i += 1
else:
    print('good')
    print('job')
print('end')

i = 1
while i <= 15:
    print(i)
    if i == 5:
        break
    i += 1
else:
    print('good')
    print('job')
print('end')

a = [54, 32, 65, 765, 32, 543]
# Yes - все четные
# No - все нечетные
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print('No', last)
        break
else:
    print('Yes', last)


#
print('Tasks')
# Гипотеза Коллатца
# Сиракузская последовательность, или последовательность Коллатца, строится так: возьмём натуральное число n;
# если оно чётное, то заменим его числом n/2; если же оно нечётное, то заменим его числом 3n+1.
# Получившееся число — следующее в сиракузской последовательности после числа n. Затем заменяем получившееся число
# по тому же правилу, и так далее.
# Определите, сколько шагов потребуется сиракузской последовательности, стартующей с заданного числа, чтобы прийти к 1.
# Обычно, если проделать такую замену достаточно много раз, мы приходим к числу 1 (за которым следует снова 1).
# Например: 8 → 4 → 2 → 1 или 10 → 5 → 16 → 8 → 4 → 2 → 1.
# Определите, сколько шагов потребуется сиракузской последовательности, стартующей с заданного числа, чтобы прийти к 1.
# Если вы обнаружите число, сиракузская последовательность от которого не приходит к 1, то... вы, скорее всего, ошиблись.
# Но если нет, то поздравляем: вы прославитесь, ведь вопрос о том, всегда ли сиракузская последовательность приходит к 1
# (независимо от начального числа), давно будоражит умы математиков.
# Формат ввода:
# Вводится одно натуральное число n.
# Формат вывода:
# Выводится одно число — количество шагов, необходимое стартующей от n сиракузской последовательности, чтобы впервые
# дойти до 1.
i = int(input())
n = 0
while i > 1:
    if i % 2 == 0:
        i = i / 2
    else:
        i = 3*i + 1
    n += 1
print(n)

#
n, i = int(input()), 0
while n != 1:
  n = 3*n+1 if n%2 else n//2
  i += 1
print(i)

#
n, cnt = int(input()), 0
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    cnt += 1
print(cnt)

#
n = int(input()) #Вводим инпут
count = 0                   #Создаем счетчик
while True:                 #Пока выражение True
    if n%2 == 0:            #Проверяем на четное число
        count += 1          #Добавляем к счетсику +1
        n = n//2            #Делим четное число на 2
        if n == 1:          #Если наше число достигнит 1,
            break           #то выходим из цикла
    if n%2 != 0:            #Проверям на нечетное число
        count += 1          #Добавляем к счетсику +1
        n = 3*n+1           #Записываем выражение из условии
        if n == 1:          #Если наше число достигнит 1,
            break           #то выходим из цикла
print(count)                #выводим счетчик

#
n, c = int(input()), 0
while n > 1:
    if not n % 2:
        n //= 2
    else:
        n = n * 3 + 1
    c += 1
print(c)

#
n = int(input())
counter = 0
while n - 1:
    n = 3*n + 1 if n%2 else n/2
    counter += 1
print(counter)


