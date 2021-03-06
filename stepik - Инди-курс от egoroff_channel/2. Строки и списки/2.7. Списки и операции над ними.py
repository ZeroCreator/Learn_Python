# СПИСКИ И ОПЕРАЦИИ НАД НИМИ.

# Списки - упорядоченные коллекции элементов.
print('1.Примеры списков')
marks = [4, 5, 3, 4, 5]
print(marks)
t_july = [20, 24, 0, 43, 12, 23]
print(t_july)

#
print('Внутри списка можно хранить значения разных типов')
a = [True, 43, 'Hello', 5.4, [4, 5, 6]]

#
print('Пустой список')
b = []

print(type(b))

#
print('Операции над списками:')
print('1. Нахождение длины списка - функция len:')
print(len(a))
print(len(b))

#
print('2. Сцепление списков (сложение):')
a = a + [4]
print(a)
print([1, 2, 3] + [4, 5, 6])

a = ['hi'] + a
print(a)

#
print('3. Дублирование списков (умножение):')
print([0]*5)

#
print('4. Проверка вхождения:')
print(5.4 in a)

#
print('5. Максимальное значение, минимальное значение, сумма списка:')
w = [43, 54, 65, 3, 4, 65, -43, 32]
print(max(w), min(w), sum(w))

print(sum([1, 2, 3, 4]))

#
print('6. Сортировка списка по возрастанию:')
print(sorted(w), w)

#
print('7. Сортировка списка по убыванию:')
print(sorted(w, reverse=True))

#
print('8. Сравнивание списков:')
print([100, 54] > [34, 543, 654, 43])

#
print('9.Найти среднее арифметическое списка:')
print(sum(marks)/len(marks))

#
print('функцию для считывания строки через запятую:')
#a = eval(input())
#print(a)
c = list(map(int, input().split()))
print(c)
c = list(map(float, input().split()))

#
print('Tasks')
# Допишите программу ниже, чтобы она вывела через пробел в одной строке значения
# самого маленького и самого большого элементов списка my_list
print(min(my_list), max(my_list))

my_list.sort()
print(my_list[0],my_list[-1])

# Программа получает на вход список из целых чисел. Ваша задача найти среднее арифметическое введенного списка чисел
list_numbers = list(map(int, input().split()))
print(sum(list_numbers)/len(list_numbers))


