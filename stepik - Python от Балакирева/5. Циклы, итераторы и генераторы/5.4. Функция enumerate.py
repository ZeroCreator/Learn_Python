# Примеры работы оператора цикла for. Функция enumerate
# Вычисление факториала от натурального числа N:
# n! = 1*2*3*...*n
n = int(input("Введите натуральное число не более 100: "))
if n < 1 or n > 100:
    print("Неверное введено натуральное число.")
else:
    p = 1
    for i in range(1, n+1):
        p *= i

    print(f"Факториал {n}! = {p}")


# Отображение елочки
for i in range(1, 7):
    print('*' * i)

# Записать слова в одну строку
words = ["Python", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
s = ''
for w in words:
    s += ' ' + w
print(s.lstrip())

# или

s = ''
fl_first = True
for w in words:
    s += ('' if fl_first else ' ') + w
    fl_first = False
print(s)

# или
print(" ".join(words))

# Заменить все двузначные числа нулями
digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i in range(len(digs)):
    if 10 <= abs(digs[i]) <= 99:
        digs[i] = 0

print(digs)

# Для того, чтобы в итерируемом объекте обращаться сразу и к индексу, и к значениею -
# функция enumerate() (возвращает пару индекс - значение)
# индекс, значение = enumerate(объект)
digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i, d in enumerate(digs):
    if 10 <= abs(d) <= 99:
        digs[i] = 0

print(digs)

# Перобразование кириллицы в латиницу
# Создаем список соответствия русских букв кирилическим названиям
t = ["a", "b", "v", "g", "d", "e", "zh",
     "z", "i", "y", "k", "l", "m", "n", "o", "p",
     "r", "s", "t", "u", "f", "h", "c", "ch", "ch",
     "shch", "", "y", "", "e", "yu", "ya"]

start_index = ord('а')
title = "Программирование на Python - лучший курс"
slug = '' #Здесь будет храниться преобразование кириллицы в латиницу
for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s) - start_index]
    elif s == 'ё':
        slug += 'yo'
    elif s in " !?;:.,":
        slug += '-'
    else:
        slug += s

while slug.count("--"):
    slug = slug.replace("--", "-")

print(slug)

# Подвиг 1. Вводится строка. Необходимо найти все индексы фрагмента "ра" во введенной строке. Вывести в строку через
# пробелы найденные индексы. Если этот фрагмент ни разу не будет найден, то вывести значение -1.


s = input().lower()
count = 0

for i in range(len(s) - 1):
	if s[i] + s[i +1] == 'ра':
		count += 1
		print(i, end=' ')
if count == 0:
	print(-1)

#
st = input()
count = 0

while 'ра' in st:
    print(st.find('ра'), end=' ')
    st = st.replace('ра', '**', 1)
    count += 1

if count == 0:
    print(-1)

#
s = input()
count = 0
for i, j in enumerate(s):
    if j.lower() == 'р' and s[i+1].lower() == 'а':
        print(i, end=" ")
        count += 1
if not count:
    print('-1')

#
s = input()
res = [i for i in range(len(s) - 1) if s[i] == 'р' and s[i + 1] == 'а']
print(*res or [-1])

# Большой подвиг 3. В виде строки записано арифметическое выражение, например:
# "10 + 25 - 12"
# или
# "10 + 25 - 12 + 20 - 1 + 3"
# и т. д. То есть, количество действий может быть разным.
# Необходимо выполнить вычисление и результат отобразить на экране. Полагается, что в качестве арифметических операций
# здесь используется только сложение (+) и вычитание (-), а в качестве операндов - целые неотрицательные числа.
# Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.
lst = input().replace(' ', '').replace('+', ' +').replace('-', ' -').split()
for i, d in enumerate(lst):
    lst[i] = int(d)

print(sum(lst))

#
text = input().replace(' ', '').replace('-', '+-').split('+')
print(sum(map(int, text)))

#
e = map(int, input().replace(' ', '').replace('+', ' +').replace('-', ' -').split())
print(sum(e))

#
print(eval(input()))

#
s=input().strip().replace(" ","")
res=0
lst=s.replace("-","+-").split("+")
for n in lst:
	res+=int(n)
print (res)

#
print(sum(map(int, input().replace(' ', '').replace('+', ' +').replace('-', ' -').split())))

# Подвиг 4. Вводится список в виде целых чисел в одну строку через пробел. Необходимо сначала сформировать список
# на основе введенной строки, а затем, каждое значение этого списка изменить, возведя в квадрат.
# Отобразить результат на экране в виде строки полученных чисел, записанных через пробел. Программу следует
# реализовать с использованием функции enumerate.
sp = list(map(int, input().split()))

for s, d in enumerate(sp):
    sp[s] = d ** 2

print(*sp)

#
n = list(map(int, input().split()))
for i, d, in enumerate(n):
    print(d**2, end=' ')

#
print(*[int(i) ** 2 for i in input().split()])

# Подвиг 5. Вводится список в виде целых чисел в одну строку через пробел. Сначала нужно сформировать список из
# введенной строки. Затем, каждый элемент этого списка продублировать один раз. Результат отобразить на экране
# в виде строки полученных чисел, записанных через пробел.
lst = list(map(int, input().split()))
for i in lst:
    print(i, i, end=' ')

#
for i in input().split():
    print((i+" ")*2,sep=" ", end="")

# Подвиг 6. Вводится список в виде вещественных чисел в одну строку через пробел. С помощью цикла for необходимо
# найти наименьшее значение в этом списке. Полученный результат вывести на экран.  Реализовать программу без
# использования функции min, max и сортировки.
lst = list(map(float, input().split()))

for i in lst:
    if i < lst[0]:
        lst[0] = i
print(lst[0])

#
lst = list(map(float, input().split()))
a = lst[0]
for i in lst:
  if i < a:
    a = i
print(a)

#
s = list(map(float, input().split()))
print(min(s))

# Подвиг 7. Вводится список в виде вещественных чисел в одну строку через пробел. Сначала нужно сформировать список из
# введенной строки. Затем, все отрицательные значения в этом списке заменить на -1.0. Результат вывести на экран в виде
# строки чисел через пробел. Программу следует реализовать с использованием функции enumerate.
sp = list(map(float, input().split()))

for s, value in enumerate(sp):
    if value < 0:
        sp[s] = -1.0

print(*sp)

#
print(*[-1.0 if float(num) < 0 else num for i, num in enumerate(input().split())])

#
print(*['-1.0' if '-' in c else c for c in input().split()])

#
a = map(float, input().split())
print(*[i if i > 0 else float(-1) for i in a])

#
for i in map(float, input().split()):
    print(i if i > 0 else -1.0, end = ' ')

#
print(*(e - (e + 1.0) * (e < 0) for i, e in enumerate(map(float, input().split()))))

# Подвиг 2. Вводится строка с номером телефона. Ожидается формат ввода:
# +7(xxx)xxx-xx-xx
# где x - это цифра. Размер введенных символов считается верным (то есть, не может быть, чтобы отсутствовала
# какая-либо цифра или была лишняя). Необходимо проверить, что введенная строка соответствует этому формату.
# Вывести ДА, если соответствует и НЕТ - в противном случае.
tel = input()
if len(tel) == 16:
    if tel[0]=='+' and tel[1]=='7' \
        and tel[2] == '(' and tel[6] == ')' \
        and tel[10]=='-' and tel[13]=='-' \
        and tel[3:6].isdigit() and tel[7:10].isdigit() \
        and tel[11:13].isdigit() and tel[14:-1].isdigit():
        print ('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')

#
num = input()
костыль = num[:3] == '+7('
на = num[3:6].isdigit()
костыле = num[6] == ')'
и = len(num[7:].split('-')) == 3
костылём = [len(i) for i in num[7:].split('-')] == [3, 2, 2]
погоняет = ''.join(num[7:].split('-')).isdigit()
print('ДА' if all([костыль, на, костыле, и, костылём, погоняет]) else 'НЕТ')

# Создаём шаблон из пришедшей на вход строки. Буквенные символы в шаблоне лучше не использовать,
# так как при совпадении символа в нашем шаблоне и входящей строке, шаблон будет верным а решение
# нет. А цифра (любая) -- она и так должна там быть. Всё, осталось проверить на соответствие s шаблону,
# написанному ручками, и наличие <7> по индексу [1].
n = input()
s = ''.join('0' if i.isdigit() else i for i in n)
print(('НЕТ', 'ДА')[s == '+0(000)000-00-00' and n[1] == '7'])

#
str = input()
n = '1234567890'
lst = ['+', '7', '(', n, n, n, ')', n, n, n, '-', n, n, '-', n, n]
for i, m in enumerate(str):
    if m not in lst[i]:
        print('НЕТ')
        break
else:
    print('ДА')


#
a = input()
try:
  assert a[0] == '+'
  assert a[1] == '7'
  assert a[2] == '('
  assert a[6] == ')'
  assert a[3: 6].isdigit()
  assert a[7: 10].isdigit()
  assert a[11: 13].isdigit()
  assert a[-2:].isdigit()
  assert len(a.split('-')) == 3
  print('ДА')
except:
  print('НЕТ')

#
s = input()
t = ''.join([c for c in s if c.isdigit()])
print('ДА' if f'+7({t[1:4]}){t[4:7]}-{t[7:9]}-{t[9:]}' == s else 'НЕТ')

#
s=list(input())
for i in range(2,len(s)):
  if s[i].isdigit():
    s[i] = '1'
if ''.join(s)=='+7(111)111-11-11': print('ДА')
else: print('НЕТ')







