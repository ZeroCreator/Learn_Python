# Функция-генератор. Оператор yield.
def get_list():
    for x in [1, 2, 3, 4]:
        return x


a = get_list()
print(a)
print(a)
print(a)
print(a)


print("yield")
def get_list():
    for x in [1, 2, 3, 4]:
        yield x


a = get_list() # Функция - генератор
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

for x in a:
    print(x)

def get_list():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)

a = get_list()
print(list(a))


# Подсчет индексов слова в текстовом файле:
print("Подсчет индексов слова в текстовом файле:")
def find_word(f, word):
    g_indx = 0
    for line in f:
        indx = 0
        while(indx != -1):
            indx = line.find(word, indx)
            if indx > -1:
                yield g_indx + indx
                indx += 1
        g_indx += 1

try:
    with open("lesson_yield.txt", encoding="utf-8") as file:
        a = find_word(file, "генератор")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Ошибка обработки файла!")