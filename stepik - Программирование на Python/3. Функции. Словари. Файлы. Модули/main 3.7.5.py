'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк, например:
Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153
Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
'''

class_rawinfo = {}
#new_heights = 0
#new_students = 0
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
#class_info = []

with open('dataset_3380_5.txt') as in_f_obj:
	for line in in_f_obj:
		#print(line)
		string = line.rstrip().split('\t')
		#print(string)
#n = int(input())
#for _ in range(n):
	#string = input().split('	')
		if string[0] not in class_rawinfo:
			class_rawinfo[string[0]] = [int(string[2]), 1]
		elif string[0] in class_rawinfo:
			heights = class_rawinfo[string[0]][0] + int(string[2])
			students = class_rawinfo[string[0]][1] + 1
			class_rawinfo[string[0]] = [heights, students]

for k, v in class_rawinfo.items():
	#print(k, str(v[0] / v[1]))
	#list.pop([int(k)-1])
	class_info[int(k)-1] = v[0] / v[1]
	#print(class_rawinfo)
	#print(class_info)

with open('output_3.7.5.txt', 'w') as out_f_obj:
	for i in range(len(class_info)):
		#print(i+1, str(class_info[i]))
		output = str(i+1) + ' ' + str(class_info[i]) + '\n'
		#print(output)
		out_f_obj.write(output)



#
# Делаем словарь {1:[0,0], 2:[0,0]... 11:[0,0]}, где [0:0] = [сумма ростов : кол-во учеников]
tab = {i: [0, 0] for i in range(1, 12)}

with open('dataset_3380_5.txt') as inf:
	# Заполняем словарь:
	for i in inf:
		line = i.strip().split('\t')
		tab[int(line[0])][0] += int(line[2])  # tab[класс][0] += рост ученика
		tab[int(line[0])][1] += 1  # tab[класс][1] += 1 (счетчик учеников в классе)

	# Распечатка:
	for i in tab.keys():
		if tab[i][1] == 0:
			print(i, '-')  # распечатываем класс, в котором нет учеников
		else:
			# считаем и распечатываем средний рост для i-го класса:
			print(i, (tab[i][0] / tab[i][1]))


#
import pandas as pd

df = pd.read_table('C:\\Users\\User\\Desktop\\py_course\\dataset_3380_5.txt', header=None, sep=r'\s{1,}')
print(df.groupby(0).mean())


#
classes = {i: [] for i in range(1, 12)}
with open('dataset_3380_5.txt') as f:
    for line in f:
        cls, name, height = line.strip().split('\t')
        classes[int(cls)].append(int(height))

for cls, heights in classes.items():
    print(cls, sum(heights) / len(heights) if heights else '-')


#
c = {str(i):[0]*2 for i in range(1,12)}
for l in open('in'):
    s = l.strip().split()[::2]
    c[s[0]] = [c[s[0]][0] + int(s[1]), c[s[0]][1] + 1]
[print(k + ' ', v[0]/v[1] if v[0] else '-') for k, v in c.items()]


#
d = {i:[0, 0] for i in range(1, 12)}
with open('dataset_3380_5.txt') as a:
    for i in a:
        s = i.split('\t')
        sum_height = d[int(s[0])][0] + int(s[2])
        n = d[int(s[0])][1] + 1
        d[int(s[0])] = [sum_height, n]
for i in d:
    if d[i][1] == 0:
        print(i, '-')
    else:
        print(i, d[i][0]/d[i][1])


#
d = dict()
with open('dataset.txt') as inf:
    for line in inf:
        a, b, c = line.strip().split( )
        d.setdefault(a, []).append(int(c))

k = 1

while k <= 11:
    if str(k) in d.keys():
        print(k, sum(d.get(str(k)))/len(d.get(str(k))))
    else:
        print(k, '-')
    k += 1

#
inf = [l.split('\t') for l in open('file.txt', 'r').read().strip().splitlines()]
#подгружаем файл в виде массива вида [[класс, фамилия, рост],...]

d = {}                       					#создаём словарь вида{класс:суммарный рост}
for y in range(1,12):      						#для каждого класса
    d[y], c = 0, 0        						#создаём нулевое значение суммарного роста и счётчика учеников
    for i in inf:       						#пробегаемся по строкам файла
        if int(i[0]) == y:    					#если нашли нужный класс, то
            d[y] += int(i[2]) 					#увеличиваем суммарный рост
            c += 1       						#увеличиваем счётчик количества учеников
    print(y, '-' if c == 0 else str(d[y] / c))	#печатаем класс и средний рост

#
from collections import defaultdict
from statistics import mean
with open('dataset_xxx.txt') as file:
    dct = defaultdict(list)
    for line in file:
        cl, _, growth = line.split()
        dct[int(cl)] += [int(growth)]
    for key, value in sorted(dct.items()):
        print(key, mean(value))

