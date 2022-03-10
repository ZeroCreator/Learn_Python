# Вложенные условия и множественный выбор
x = int(input())

if x%2 == 0:
    if 0<=x<=9:
        print(f"{x} - цифра")
    else:
        print(f"{x} - число")
else:
    print(f"{x} - нечетное число")


print("Большее из трех чисел")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a > b:
    if a > c:
        print("a -> max")
    else:
        print("c -> max")
else:
    if b > c:
        print("b -> max")
    else:
        print("c -> max")

