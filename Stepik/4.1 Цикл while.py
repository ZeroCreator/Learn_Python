# ЦИКЛ while.

# while - инструкция для организации циклов с неизвестным количеством повторений.
print('В порядке возрастания:')
i = 1
while i < 6:
    print(i)
    i = i + 1

i = 1
while i < 20:
    print(i)
    i = i + 2

i = 1
while i < 600:
    print(i)
    i = i*2

i = 1
while i < 6:
    print('Hello')
    i = i + 1

n = int(input())
i = 1
while i < n + 1:        # while i <= n:
    print('Hello')
    i = i + 1

n = int(input())
i = 1
i = 20
while i > 0:
    print(i)
    i = i - 1
while i <= n:
    print('Hello')
    i = i + 1

#
print('В порядке убывания:')

a = int(input("Введите число: "))
while a != 0:
    print('Повторите ввод')
    a = int(input("Введите число: "))
print('Вы ввели 0')


#
print('Вод пароля:')
a = input("Введите пароль:")
password = 'qwerty'
while a != password:
    print('Пароль неверный')
    a = input("Введите пароль:")
print('Верный пароль')

#
guess = input("Введите пароль:")
password = 'qwerty'
count = 0
while guess != password:
    count += 1                                              # Добавление счетчика
    print('Пароль неверный')
    print(f'Вы ввели неправельный пароль {count} раз.')
    guess = input("Введите пароль:")

print('Верный пароль')

#
print('Удаление всех одинаковых элементов из списка')
a = [1, 2, 3]*5
print(a)
a.remove(3)
print(a)
while 3 in a:
    a.remove(3)
    print(a)

#
print('Обход всех символов строки по порядку:')
s = 'privet'
while len(s) > 0:
    print(s[0], s[1:])
    s = s[1:]

#
print('Проверка внутри списка:')
s = 'pRi/Vet4@5682,Fdj'
while len(s) > 0:
    bukva = s[0]
    if bukva >= 'a' and bukva <= 'z':
        print(bukva, 'small')
    elif bukva >= 'A' and bukva <= 'Z':
        print(bukva, 'big')
    elif bukva.isdigit():
        print(bukva, 'digit')
    else:
        print(bukva, 'znak')
    s = s[1:]