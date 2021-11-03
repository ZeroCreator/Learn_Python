# Функция zip.
# zip(iter1 [, iter2 [, iter3] ...]) - создает кортежи со значениями соответсвующих переменных из переданных коллекций.

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]

z = zip(a, b)
print(*z)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"
z =tuple(zip(a, b, c))
# print(z)
for v1, v2, v3 in z:
    print(v1, v2, v3)

z1, z2, z3, z4 = zip(a, b, c)
print(z1, z2)

z = zip(a, b, c)
lz = list(z)
print(*zip(*lz))

t1, t2, t3 = zip(*lz)
print(t1, t2, t3, sep='\n')

