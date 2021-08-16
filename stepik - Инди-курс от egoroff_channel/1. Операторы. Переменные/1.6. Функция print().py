# Ввод и вывод данных. Функция print().

print('Параметр sep')
print(1, 2, 3, sep=',')
print(4, 5, sep="&")

#
print('Параметр end=\\n')
print(1, 2, 3, sep=',', end=' ')
print(4, 5, sep="&")

#
print('Форматирование')
rubles = 10
kop = 90
print('У меня eсть %s рублей %s копеек'%(rubles, kop))

#
print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')
