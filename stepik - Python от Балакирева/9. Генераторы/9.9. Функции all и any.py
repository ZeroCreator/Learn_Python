# Функции all и any.
print("all")
a = [True, True, True, True]
b = all(a)
print(b)


a = [True, True, True, False]
b = all(a)
print(b)


a = [True, True, True, True, [], [1, 2, 3], {}]
b = all(a)
print(b)

a = [True, True, True, True, [1, 2, 3], {1}]
b = all(a)
print(b)


a = [True, True, True, True, [1, 2, 3], {1}]
all_res = True
for x in a:
    all_res = all_res and bool(x)

print(all_res)

print("any")
a = [True, True, True, True, [], [1, 2, 3], {}]
b = any(a)
print(b)

a = [False, False, False, False]
b = any(a)
print(b)

a = [True, True, True, True, [1, 2, 3], {1}]
all_res = False
for x in a:
    all_res = all_res or bool(x)

print(all_res)

# Игра крестики-нолики:
print("Игра крестики-нолики:")
p = ['x', 'x', '0', '0', 'x', '0', 'x', 'x', 'x']

# row_1 = all(map(lambda x: x == "x", p[:3]))
# row_2 = all(map(lambda x: x == "x", p[3:6]))
# row_3 = all(map(lambda x: x == "x", p[6:]))



def true_x(a):
    return a == 'x'

# Проверка по строчкам:
row_1 = all(map(true_x, p[:3]))
row_2 = all(map(true_x, p[3:6]))
row_3 = all(map(true_x, p[6:]))

print(row_1, row_2, row_3)

# Проверка по стобцам
col_1 = all(map(true_x, p[::3]))
col_2 = all(map(true_x, p[1::3]))
col_3 = all(map(true_x, p[2::3]))

print(col_1, col_2, col_3)

# Игра сапер
print("Игра сапер")
N = 10
P = [0]*(N*N)

P[4] = "*"

loss = any(map(lambda x: x == "*", P))
print(loss)