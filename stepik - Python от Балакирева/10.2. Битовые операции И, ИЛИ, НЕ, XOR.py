# Битовые операции И, ИЛИ, НЕ, XOR.
# Операция НЕ (~)
print("Операция НЕ (~)")
a = 121
print(bin(a))
print(~a)

d = 0
print(~d)

# Операция И (&)
print("Операция И (&)")
flags = 5
mask = 4
if flags & mask == mask:
    print("Включен второй бит числа")
else:
    print("Второй бит выключен")

flags = 13
mask = 5
flags = flags & ~mask
print(flags)

# Операция ИЛИ (|)
print("Операция ИЛИ (|)")
flags = 8
mask = 5
# flags = flags | mask
flags |= mask
print(flags)


# Операция XOR (исключающее ИЛИ - ^)
print("Операция XOR (исключающее ИЛИ - ^)")
# Удобно переключать биты (для шифрования информации)
flags = 9
mask = 1
flags = flags ^ mask
print(flags)
flags = flags ^ mask
print(flags)


# Смещение бит вправо >> - целочисленное деление на 2
print("Смещение бит вправо >>")
# Смещение бит влево << - умножение на 2
print("Смещение бит влево <<")
x = 160
print(bin(x))
x = x >> 1 # делит исходное число на 2
print(x)
print(bin(x))
x = x >> 2 # делит исходное число на 4
print(x)
x = x >> 2 #
print(x)
x = x >> 1
print(x)
x = x << 1
print(x)
x = x << 3
print(x)

#
print("Tasks")
# На вход программы подается целое десятичное число. Используя битовые операции, включите третий бит введенного числа.
# Выведите на экран полученное числовое значение.
# Sample Input:
# 100
# Sample Output:
# 108
print(int(input()) | 8)