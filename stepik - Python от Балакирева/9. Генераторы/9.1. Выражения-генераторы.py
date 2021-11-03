# Выражения-генераторы.
a = (x**2 for x in range(6))

for x in a:
    print(x)

for x in a: # второй раз не перебирается
    print(x)

# Функции, которые работают с итераторами:
# list, set, sum, max, min, ...(итератор в качестве аргумента)

a = (x**2 for x in range(6))
print(list(a)) # на выходе получаем множество
print(set(a)) # второй раз не перебирается
a = (x**2 for x in range(6))
print(set(a))

print(sum((x**2 for x in range(6))))
print(max((x**2 for x in range(6))))
print(min((x**2 for x in range(6))))

lst = (x for x in range(1000000000))
for i in lst:
    print(i, end=" ")
    if i > 50:
        break

# функция len() не работает
a = (x for x in range(10, 20))
b = list(a)
print(b)
d = [(x**2 for x in range(6))]
print(d)


#
print("Tasks")
# На вход программы поступают два целых числа a и b (a < b), записанные в одну строчку через пробел. Определите генератор,
# который бы выдавал модули целых чисел из диапазона [a; b]. В цикле выведите первые пять значений этого генератора.
# Каждое значение с новой строки. (Гарантируется, что пять значений имеются).
a, b = map(int, input().split())
tp = (abs(x) for x in range(a, b+1))
c = 1
for i in tp:
    print(i)
    c += 1
    if c > 5:
        break


#
a, b = map(int, input().split())
gen = (abs(x) for x in range(a, b + 1))
for i in range(5):
    print(next(gen))


