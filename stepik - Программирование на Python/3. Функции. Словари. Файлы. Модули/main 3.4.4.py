'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана
следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его
среднюю оценку по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.
Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения,
разделённые пробелом, последней строкой в файл с ответом.
В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со
средними оценками по трём предметам.
Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:
85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''

averages = []   # средние
marks_math = [] # оценки по математике
marks_phys = [] # оценки по физике
marks_rus = []  # оценки по русскому
counter = 0
value01 = 0
value02 = 0
value03 = 0

with open('dataset_3363_4.txt') as in_f_obj:
    for line in in_f_obj:
        line = line.rstrip().split(';')
        student_average = ((int(line[1]) + int(line[2]) + int(line[3])) / 3)
        averages.append(student_average)
        marks_math.append(int(line[1]))
        marks_phys.append(int(line[2]))
        marks_rus.append(int(line[3]))
        counter += 1

with open('output_3.4.4.txt', 'w') as out_f_obj:
    for _ in averages:
        out_f_obj.write(str(_) + '\n')

    for _ in marks_math:
        value01 += int(_)
    for _ in marks_phys:
        value02 += int(_)
    for _ in marks_rus:
        value03 += int(_)
    average_math = value01 / counter
    average_phys = value02 / counter
    average_rus = value03 / counter

    (out_f_obj.write(str(average_math) + ' ' + str(average_phys) + ' ' + str(average_rus)))

print(average_math)
print(average_phys)
print(average_rus)
print()

'''
Ответ на тестовую задачу:

85.0

94.0

71.66666666666667

81.0 84.0 85.66666666666667

добавить доп. округление функция round(x, 9)
'''