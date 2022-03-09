# Основные методы строк
# синтаксис методов
# объект.метод(аргументы)
s = "python"
t = s.upper()
print(t)
print(s)
t1 = t.lower()
print(t1)

print("Метод string.count() - нахождения подстроки в строке")
msg = "abrakadabra"
print(msg.count("ra"))
print(msg.count("ra", 4))
print(msg.count("ra", 4, 10))
print(msg.count("ra", 4, 11))

print("Метод find.count() - нахождения индекса подстроки в строке слева - направо")
print(msg.find("br"))
print(msg.find("br", 2))
print(msg.find("br", 2, 8))
print(msg.find("brr", 2))

print("Метод rfind.count() - нахождения индекса подстроки в строке справа - налево")
print(msg.rfind("br", 2))

print("Метод index.count() - нахождения индекса подстроки в строке")
print("Метод replace.count() - замена подстроки")
print(msg.replace("a", "o"))
print(msg.replace("ab", "AB"))
print(msg.replace("ab", ""))
print(msg.replace("a", "o", 2))

print("Метод isalpha()")
print(msg.isalpha())
print("hello world".isalpha())

print("Метод isdigit()")
print("5.6".isdigit())
print("56".isdigit())
print("-56".isdigit())

print("Метод string.rjust()")
d = "abc"
print(d.rjust(5))
print(d.rjust(4, "0"))
print(d.rjust(1, "0"))

print("Метод string.ljust()")
d = "12"
print(d.ljust(5, "*"))

print("Метод string.split() - возвращает коллекцию строк")
print("Иванов Иван Иванович".split(" "))

digs = "1, 2, 3,4,   5, 6"
s = digs.replace(" ", "").split(",")
print(s)

print("Метод " ".join(string) - из списка строк собирает единую строку")
print(", ".join(s))
fio = "Иванов Иван Иванович"
print(", ".join(fio.split()))
print(", ".join(fio))

print("Метод string.strip() - удаляет все символы пробелов и переносов строк в начале и в конце строки")
d = "    hello, world   \n".strip()
print(d)
d = "    hello, world   \n".rstrip()
print(d)
d = "    hello, world   \n".lstrip()
print(d)


# Подвиг 7. Вводится строка (слаг). Замените в этой строке все двойные дефисы (--) и тройные (---) на одинарные (-).
# Подумайте, в какой последовательности следует выполнять эти замены. Результат преобразования выведите на экран.
s = input().replace("---", "-")
print(s.replace("--", "-"))

#
print(input().replace('---','-').replace('--','-'))

#
s1 = input()
while '--' in s1:
    s1 = s1.replace('--','-')
print(s1)

#
print('-'.join(input().replace('-', ' ').split()))

# Подвиг 8. Вводятся три целых положительных числа (максимум трехзначные) через пробел в одну строчку.
# Для двухзначных и однозначных чисел нужно добавить слева незначащие нули так, чтобы все числа содержали по три цифры.
# Вывести на экран полученные числа в столбик.
a, b, c = input().split()
print(a.rjust(3, '0'), b.rjust(3, '0'), c.rjust(3, '0'), sep='\n')

#
[print(_.zfill(3)) for _ in input().split()]

#
[print(i.rjust(3, '0')) for i in input().split()]


# Подвиг 9. Вводится строка, состоящая из слов, разделенных пробелом. Необходимо подсчитать число слов в этой строке и
# результат (число) отобразить на экране.
print(len(input().split()))

#
s1 = input()
print(s1.count(' ') + 1)