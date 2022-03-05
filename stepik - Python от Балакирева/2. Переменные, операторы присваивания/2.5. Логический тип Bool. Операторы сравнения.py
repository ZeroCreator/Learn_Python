# Логический тип Bool. Операторы сравнения
rez = 5 == 5.0
print(rez)

# Проверка на четность
x = 6
print(x%2 == 0)

# Проверка на нечетность
x = 6
print(x%2 != 0)

# and
y = 1.8
rez = y >= -2 and y <=5 #  -2 <= y <=5
print(rez)

# or
y = 1.8
rez = y <= -2 or y >=5
print(rez)

y = -10
rez = y <= -2 or y >=5
print(rez)

# инверсия общего составного условия
x = 7
r = x % 2 == 0 or x % 3 == 0
print(r)

r1 = x % 2 != 0 or x % 3 != 0
r2 = not (x % 2 == 0 or x % 3 == 0)
print(r1)
print(r2)

# функция bool()
print(bool(1))
print(bool(0))
print(bool(''))
print(bool('0'))