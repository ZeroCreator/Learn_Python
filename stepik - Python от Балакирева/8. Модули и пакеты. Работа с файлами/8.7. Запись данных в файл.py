# Запись данных в файл.
# Открывая файл на запись мы удаляем все его предыдущее содержимое.
try:
    with open("out.txt", "w") as file:
        file.write("Hello1\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
except:
    print("Ошибка при работе с файлом")


# Дозаписывание информации в файл:
print("Дозаписывание информации в файл:")
try:
    with open("out.txt", "a") as file:
        file.write("Hello1\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
except:
    print("Ошибка при работе с файлом")

# Режим и чтения, и записи:
print("Режим и чтения, и записи:")
try:
    with open("out.txt", "a+") as file:
        file.seek(0)
        file.write("Hello4\n")
        s = file.readlines()
        print(s)

except:
    print("Ошибка при работе с файлом")

# Запись сразу несколько строк: file.wfitelines(["Hello5\n", "Hello6\n"])
print("Запись сразу несколько строк:")
try:
    with open("out.txt", "a+") as file:
        file.seek(0)
        file.writelines(["Hello5\n", "Hello6\n"])
        s = file.readlines()
        print(s)

except:
    print("Ошибка при работе с файлом")

# Бинарный режим доступа (один в один как представлен в памяти):
import pickle

print("Бинарный режим доступа:")
books = [
    ("Евгений Онегин", "Пушкин А. С.", 200),
    ("Муму", "Тургенев И.С.", 250),
    ("Мастер и Маргарита", "Булгаков М.А.", 500),
    ("Метрвые души", "Гоголь Н.В.", 190),
]

file = open("out.bin", "wb")
pickle.dump(books, file)
file.close()

# Прочитать бинарный файл:
print("Прочитать бинарный файл:")
file = open("out.bin", "rb")
bs = pickle.load(file)
file.close()
print(bs)

# Сохранение нескольких коллекций в один файл:
book1 = ["Евгений Онегин", "Пушкин А. С.", 200]
book2 = ["Муму", "Тургенев И.С.", 250]
book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
book4 = ["Метрвые души", "Гоголь Н.В.", 190]

try:
    with open("out.bin", "wb") as file:
        pickle.dump(book1, file)
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)
except:
    print("Ошибка при работе с файлом")

# reed:
try:
    with open("out.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except:
    print("Ошибка при работе с файлом")

print(b1, b2, b3, b4, sep="\n")
