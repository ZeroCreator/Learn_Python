# Встроенные математические функции по работе с целыми числами.

print('1. Функция abs(value) - модуль числа:')
print(abs(-7))
print(abs(7))
print(abs(-5*4))

#
print('2. Функция min(x1, x2, ..., xn)')
print(min(3, 4, 6, 73))

#
print('3. Функция max(x1, x2, ..., xn)')
print(max(3, 4, 6, 73))

#
print('4. Функция pow(x, y)  - возводит в степень')
print(pow(3, 4))

#
print('5. Функция round() округляет до целого числа по правилам математики')
print(round(3.5), round(3.4))

#
print('Округляет до сотых')
print(round(3.456, 2))

#
print(round(3.456, 1))

#
print(round(456, -1))

#
print(round(456, -2))

#
print('6. Тип объекта')
print(type(4))
print(type(4.5))

#
print('Примеры:')
print(max(4, 5, 3, 42, abs(-56)))

#
print('Извлечение корня числа')
print(9**0.5)
print(pow(9, 0.5))
print(pow(9, 1/2))
