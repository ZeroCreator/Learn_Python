# Индексы и срезы строк
s = "hello python"
print(s[0])
print(s[1])

print("последний символ строки")
print(s[11])
print(s[len(s)-1])
print(s[-1])


print(s[-2])
print("panda"[3])

print("срезы строк")
# строка[start:stop]
print(s[1:3])
print(s[4:])
print(s[:5])
print(s[:])
a = s[:]
print(id(s), id(a))
print(s[2:-2])

# строка[start:stop:step]
print(s[2:10:2])
print(s[2::3])
print(s[:5:3])
print(s[::2])

print(s[::-1])
print(s[::-2])

print("изменение строки через срезы")
s2 = "H" + s[1:]
print(s2)

# Подвиг 8. Из введенной строки отобразить первые пять символов в обратном порядке.
# Полагается, что введенная строка имеет минимум пять символов.
print(input()[4::-1])

# Подвиг 10. Вводятся два слова (через пробел в одной строке). Длина второго слова меньше первого.
# Из этих слов выделить символы с нечетными индексами с обрезкой первого слова до длины второго.
# Сравнить полученные строки между собой на равенство и результат (True или False) вывести на экран.
# Задачу выполнять без использования условного оператора.
a, b = input().split()
s = a[:len(b)]
print(s[1::2] == b[1::2])

#
s1, s2 = input().split()
print(s1[:len(s2)][1::2] == s2[1::2])

#
a, b = input().split()
print(a[1:len(b):2] == b[1::2])

#
a = input().split()
print(a[0][1:len(a[1]):2] == a[1][1::2])

