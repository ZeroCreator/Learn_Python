# Методы словаря. Перебор его элементов в циклe.
# Метод 1. dict.fromkeys(список[,значение по умолчанию]) -
#  - формирует словарь с заданными ключами, которые передаются в виде списка, и некоторыми значениями
print("Метод 1. dict.fromkeys(список[,значение по умолчанию])")
lst = ["+7", "+6", "+5", "+4"]
a = dict.fromkeys(lst)
print(a)
a = dict.fromkeys(lst, "код страны")
print(a)

# Метод 2. dict.clear() - служит для очистки словаря
print("Метод 2. dict.clear() - служит для очистки словаря")
a.clear()
print(a)

# Метод 3. dict.copy() - Создание копии словаря
print("Метод 3. dict.copy() - Создание копии словаря")
d = {True: 1, False: "Лож", "list": [1, 2, 3], 5: 5}
print(d)
d2 = d.copy()
print(d2)
d2["list"] = [5, 6, 7]
print(d2)
print(d)

# Создание копии словаря - способ 2:
print("Создание копии словаря - способ 2:")
d3 = dict(d)
print(d3)
print(id(d2))
print(id(d3))

# Метод 4. dict.get(key) - Получение значения словаря с помощью функции get():
print("Метод 4. dict.get(key) - Получение значения словаря с помощью функции get():")
print(d.get("list")) # вернет None при несуществующем ключе, либо заданный параметр
print(d["list"]) # вернет ошибку при несуществующем ключе
print(d.get(3, False))

# Метод 5. dict.setdefault(key[,default]) - если ключ существует - возвращает значение ключа,
# если ключ не существует - создает ключ в словаре со значением None, либо с указанным значением
print("Метод 5. dict.setdefault(key[,default])")
print(d.setdefault("list"))
print(d.setdefault(2))
print(d)
d.setdefault(3, "three")
print(d)

# Метод 6. dict.pop() - позволяет удалять из словаря тот или иной ключ и возвращяет его значение
print("Метод 6. dict.pop()")
d.pop(2)
print(d)

# Для несуществующих ключей возвращает определенное значение:
print(d.pop("abc", False))

# Метод 7. dict.popitem() - удаляет случайновыбранный ключ (последнюю созданную запись):
print(d.popitem())

# Метод 8. dict.keys() - возвращяет список ключей:
print("Метод 8. dict.keys() - возвращяет список ключей:")
print(d.keys())
# Словарь обходится по ключам. И то же самое, что и:
for x in d:
    print(x, end=' ')

print()
# Метод 9. dict.values() - возвращаето список значений:
print("Метод 9. dict.values() - возвращаето список значений:")
print(d.values())
# это то же самое, что и:
for x in d.values():
    print(x)

# Метод 10. dict.items() - возвращает пару ключ-значение в виде списка кортежей:
print("Метод 10. dict.items() - возвращает пару ключ-значение:")
print(d.items())

for x in d.items():
    print(x)

for key, value in d.items():
    print(key, value)

# Метод 11. dict.update() - обновление словаря:
print("Метод 11. dict.update() - обновление словаря:")
d = dict(one = 1, two = 2, three = "3", four = "4")
print(d)
d2 = {2: "неудовлетворительно", 3: "удовлетворительно", "four": "хорошо", 5: "отлично"}
#p = d.update(d2)
#print(p)

# Метод 12. Объединение словарей:
print("Метод 12. Объединение словарей:")
d3 = {**d, **d2}
print(d3)
d4 = {**d2, **d}
print(d4)

# Объединение словарей - способ 2:
print("Объединение словарей - способ 2:")
d | d2

