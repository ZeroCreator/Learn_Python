# Задание 1:
# Создайте функцию, которая принимает две строки и вычисляет расстояние Хэмминга между ними.
# Расстояние Хэмминга — число позиций, в которых соответствующие символы двух слов одинаковой длины различны.
# Например, в строке «ABCB» на четвертой позиции стоит буква «B», а в строке «ABCD» на той же позиции — буква «D».
# Расстояние Хэмминга между этими строками — 1.
# Примечание: Исходим из того, что передаваемые строки всегда будут одинаковой длины.
# Примеры:
# hamming_distance("abcde", "bcdef") ➞ 5
# hamming_distance("abcde", "abcde") ➞ 0
# hamming_distance("strong", "strung") ➞ 1
# hamming_distance("ABBA", "abba") ➞ 4
def hamming_distance(a, b):
    first_str = list(a)
    second_str = list(b)
    count = 0

    for i in range(len(first_str)):
        if first_str[i] != second_str[i]:
            count += 1

    return count

print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
print(hamming_distance("ABBA", "abba"))

#
def hamming_distance(string_1:str, string_2:str) -> int:
    distance = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            distance += 1
    return distance


# Задание 2:
# 22 октября — ДЕНЬ CAPS LOCK. За исключением этого дня, все предложения должны быть в нижнем регистре. Поэтому напишите
# функцию для нормализации предложения.
# Эта функция должна принимать строку. Если строка состоит только из символов верхнего регистра, переведите их в нижний
# регистр и добавьте в конце восклицательный знак.
# Примечания:
# - каждая передаваемая в функцию строка - отдельное предложение
# - предложение после нормализации должно начинаться с заглавной буквы
# - восклицательный знак добавляем к предложениям, которые переводили из верхнего регистра в нижний.
# Примеры:
# normalize("CAPS LOCK DAY IS OVER")
# ➞ "Caps lock day is over!"
# normalize("Today is not caps lock day.")
# ➞ "Today is not caps lock day."
# normalize("Let us stay calm, no need to panic.")
# ➞ "Let us stay calm, no need to panic."

def normalize(text_sentence):
    if text_sentence[1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return f"{text_sentence.capitalize()}!"
    return text_sentence


print(normalize("CAPS LOCK DAY IS OVER"))
print(normalize("Today is not caps lock day."))
print(normalize("Let us stay calm, no need to panic."))

#
def normalize(txt):
    if txt.isupper()==True:
        txt = txt.capitalize()+"!"
    return txt


# Задание 3:
# Создайте функцию, которая определяет, представляет ли ввод «stalactites» (сталактиты) или «stalagmites» (сталагмиты).
# Если ввод содержит и сталактиты, и сталагмиты, верните «both» («оба»).
# Ввод будет двухмерным списком, где 1 представляет кусок камня, а 0 — воздушное пространство.
"""
mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]) ➞ "stalactites"

mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "stalagmites"

mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]) ➞ "both"
"""


def mineralFormation(mas):
    stalactites = 0
    stalagmites = 0
    for i in mas[0]:
        if i == 1:
            stalactites = 1

    for i in mas[-1]:
        if i == 1:
            stalagmites = 1

    if stalactites and stalagmites:
        return "both"
    if stalactites:
        return "stalactites"
    if stalagmites:
        return "stalagmites"



p1 = mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
])

print(p1)

p2 = mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
])

print(p2)

p3 = mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
])
print(p3)


p4 = mineralFormation([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
])
print(p4)

#
def mineral_formation(input):
    if 1 in input[0] and 1 in input[-1]:
        return 'both'
    if 1 in input[0] :
        return 'stalactites'
    if 1 in input[-1]:
        return 'stalagmites'


# Задача 4
# Задание:
# Панцифровое число — целое число (в какой-то выбранной системе счисления), в котором каждая цифра данной системы
# счисления появляется по крайней мере один раз.
# Для целей нашей задачи мы будем считать панцифровым целое число в десятичной системе, в котором встречается хотя бы
# раз каждая цифра от 0 до 9.
# Напишите функцию, которая будет принимать целое число и возвращать True, если оно является панцифровым, и False —
# в противном случае.
# Подсказка: подумайте о свойствах панцифрового числа после удаления всех дубликатов.
# Примеры:
# is_pandigital (98140723568910) ➞ True
# is_pandigital (90864523148909) ➞ False: 7 отсутствует.
# is_pandigital (112233445566778899) ➞ False
def is_pandigital(num):
    if sorted(set(str(num))) == list('0123456789'):
        return True
    return False


print(is_pandigital(98140723568910))
print(is_pandigital (90864523148909))
print(is_pandigital (112233445566778899))


#
def is_pandigital(number):
    return len(set(str(number))) == 10


# Задача 5
# Напишите функцию, которая возвращает True, если в переданном числе за каждой последовательностью единиц следует
# последовательность нулей той же длины.
# Примеры:
# same_length (110011100010) ➞ True
# same_length (101010110) ➞ False
# same_length (111100001100) ➞ True
# same_length (111) ➞ False
def same_length(incoming_number: int) -> bool:
    """Функция определяет следует ли в переданном числе за каждой последовательностью единиц последовательность нулей той же длины.
    :param incoming_number: вводимое число из единиц и нулей
    :return: True or False
    """
    list_units = list(filter(None, str(incoming_number).split("0")))
    list_zeros = list(filter(None, str(incoming_number).split("1")))
    return [len(i) for i in list_units] == [len(i) for i in list_zeros]



t = same_length(110011100010)
t1 = same_length(101010110)
t2 = same_length(111100001100)
t3 = same_length(111)
t4 = same_length(000)

print(t)
print(t1)
print(t2)
print(t3)
print(t4)

def same_length(incoming_number, first_digit="1", second_digit="0"):
    list_units = list(filter(None, str(incoming_number).split(second_digit)))
    list_zeros = list(filter(None, str(incoming_number).split(first_digit)))
    return [len(i) for i in list_units] == [len(i) for i in list_zeros]



t = same_length(110011100010)
t1 = same_length(101010110)
t2 = same_length(111100001100)
t3 = same_length(111)
t4 = same_length(000)

print(t)
print(t1)
print(t2)
print(t3)
print(t4)



if __name__ == "__main__":
    assert same_length(110011100010)
    assert not same_length(101010110)
    assert same_length(111100001100)
    assert not same_length(111)
    assert not same_length(000)
    assert not same_length(1)
    assert not same_length(110100)



# Задача №6.
# Гарри — почтальон. У него есть почтовый участок размером n * m (матричный / 2D-список).
# Каждый слот в 2D-списке представляет количество писем в этом месте.
# Гарри может идти только вправо и вниз. Он начинает обход в (0, 0) и заканчивает в (n-1, m-1). n представляет высоту,
# а m — длину матрицы.
# Письма Гарри может брать только там, где находится.
# Напишите функцию, возвращающую максимальное количество писем, которое Гарри может подобрать.
# Примеры:
# harry([[5, 2], [5, 2]]) ➞ 12
# # (5+5+2)
# harry([
#   [1, 2, 3, 4, 5],
#   [6, 7, 8, 9, 10],
#   [11, 12, 13, 14, 15]
# ]) ➞ 72
# # (1+6+11+12+13+14+15)
# harry([[]]) ➞ -1
# Примечание. Как вы видели в примере 3, если матрица пуста, верните -1.

def harry(two_dimensional_list: list) -> int:
    """ Функция в двумерном списке рассчитывает сумму первых значений каждого вложенного
    списка и всех остальных значений последнего вложенного списка
    :param two_dimensional_list: матричный двухмерный список
    :return: сумма значений, если список не пустой, иначе: -1
    """
    if len(two_dimensional_list) > 1:
        sum_first_values: int = 0
        sum_last_list = sum(two_dimensional_list[-1])
        for i in two_dimensional_list[:-1]:
            sum_first_values += i[0]
        return sum_first_values + sum_last_list
    return -1


print(harry([[5, 2], [5, 2]]))
print(harry([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15]
]))
print(harry([[]]))


if __name__ == "__main__":
    assert harry([[5, 2], [5, 2]]) == 12
    assert harry([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 72
    assert harry([[]]) == -1