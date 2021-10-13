# Словари (dict). Базовые операции над словарями.
d = {"house": "дом",
     "car": "машина",
     "tree": "дерево",
     "road": "дорога",
     "river": "река"}

print(d)

print(d["house"])

# dict(ключ1=значение1, ключ2=значение2, ...)
# ключи должны быть строками и записываются без кавычек
s = dict(one=1, two=2, three="3", foure="4")
print(s)

# Преобразование списка в словарь
print("Преобразование списка в словарь")
list = [[2, "неудовлетворительно"], [3, "удовлетворительно"], [4, "хорошо"], [5, "отлично"]]
print(dict(list))

d[True] = "Истина"
d[False] = "Лож"
print(d)
d[True] = 1
print(d)

print(len(d))

del d[True]
print(d)

print(True in d)
print(True not in d)
