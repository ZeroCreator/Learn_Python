# Введение в строки. Операции над строками
print(bool(" "))
print(bool(""))
s1 = "Панда"
s2 = 'Panda'

text = '''Я Python выучил бы только за то,
что есть популярные курсы.
Много хороших курсов'''

print(s1)
print(s2)
print(text)

# функция str()
print("функция str()")
s1 = "Я люблю"
print(s1 + str(5))

# функция len()
print("функция len()")
print(len("hello"))

# оператор in - вхождение подстроки в строку
print("оператор in")
print("ab" in "abracodabra")

# сравнение строк
print("сравнение строк")
a = "hello"
print(a == "hello")
print(a == "Hello")
print(a == "hello ")

# лексографическое сравнение (по кодовой таблице)
print("лексографическое сравнение")
print("кот" > "кит")
print("Кот" > "кит")

# узнать код в кодовой таблице - функция ord()
print("узнать код в кодовой таблице - функция ord()")
print(ord("R"))
print(ord("Д"))

