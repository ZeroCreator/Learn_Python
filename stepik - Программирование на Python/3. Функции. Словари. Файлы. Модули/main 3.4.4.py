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

math_values = []
physics_values = []
russian_values = []
with open('dataset_3363_4.txt', 'r') as in_file:
    for line in in_file:
        current_line = line.strip().split(';')
        math_values.append(int(current_line[1]))
        physics_values.append(int(current_line[2]))
        russian_values.append(int(current_line[3]))
out_file = open('output_3.4.4.txt', 'w')
for i in range(len(math_values)):
    out_file.write(str((math_values[i] + physics_values[i] + russian_values[i]) / 3) + '\n')
if len(math_values) > 0:
    out_file.write(str(sum(math_values) / len(math_values)) + ' ' +
                   str(sum(physics_values) / len(physics_values)) + ' ' +
                   str(sum(russian_values) / len(russian_values)))
out_file.close()

#print(round(average_math, 9))
#print(round(average_phys, 9))
#print(round(average_rus, 9))
#out_f_obj('{},{},{}, {}'.format(average_math, average_phys, average_rus,  ))
'''
Ответ на тестовую задачу:

85.0

94.0

71.66666666666667

81.0 84.0 85.66666666666667

добавить доп. округление функция round(x, 9)
'''