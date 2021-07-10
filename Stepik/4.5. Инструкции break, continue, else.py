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
