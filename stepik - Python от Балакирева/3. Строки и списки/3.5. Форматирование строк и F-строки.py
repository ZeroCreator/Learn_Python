# Форматирование строк и F-строки
age = 18
name = "Сергей"
print("Меня зовут " + name + ", мне " + str(age) + " и я люблю язык Python")

print("Форматирование строки")
print("Меня зовут {0}, мне {1} и я люблю язык Python".format(name, age))
print("Меня зовут {fio}, мне {old} и я люблю язык Python".format(fio=name, old=age))

print("f - строка")
print(f"Меня зовут {name}, мне {age} и я люблю язык Python")
print(f"Меня зовут {name.upper()}, мне {age*2} и я люблю язык Python")
print(f"Меня зовут {len(name)}, мне {age*2} и я люблю язык Python")

# Подвиг 1. Вводятся: имя, фамилия и возраст (целое положительное число) каждое значение с новой строки. Используя
# метод строки format, через индексы переменных необходимо сформировать строку по шаблону:
# "Уважаемый <имя> <фамилия>! Поздравляем Вас с <возраст>-летием!"
# Результат вывести на экран (без кавычек).
name = input()
surname = input()
age = input()
print("Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!".format(name, surname, age))

#
s1, s2, s3 = input(), input(), input()
print('Уважаемый {} {}! Поздравляем Вас с {}-летием!'.format(s1, s2, s3))

#
a = input()
b = input()
c = input()
print("Уважаемый {name} {families}! Поздравляем Вас с {age}-летием!".format(name=a, families=b, age=c))

# Подвиг 2. Вводятся: габариты изделия (целые числа): ширина, глубина, высота - в одну строчку через пробел.
# С помощью метода format, используя ключи в качестве имен переменных, сформировать строку:
# "Габариты: <ширина> x <глубина> x <высота>". Результат вывести на экран.
a, b, c = map(int, input().split())
print("Габариты: {} x {} x {}".format(a, b, c))

#
print('Габариты: ' + input().replace(' ', ' x '))

#
s1, s2, s3 = input().split()
print('Габариты: {width} x {length} x {height}'.format(width=s1, length=s2, height=s3))

#
print('Габариты: {} x {} x {}'.format(*list(map(int,input().split()))))

# Подвиг 3. Вводятся: два целых числа в одну строку через пробел. С помощью F-строки отобразить их по возрастанию
# в одну строку через пробел. Результат вывести на экран.
# P. S. Реализовать программу без использования условных операторов. Подумайте, как это можно сделать.
a, b = map(int, input().split())
print(f"{min(a, b)} {max(a, b)}")

#
string = input().split()
print(f"{min(string)} {max(string)}")

# Подвиг 5. Вводятся (каждое с новой строки): курс доллара (вещественное значение) и число рублей (целое число)
# для обмена рублей на доллары. Вычислить целое количество получаемых долларов (с отбрасыванием дробной части)
# и сформировать строку, используя F-строку:
# "Вы можете получить <долларов>$ за <число рублей> рублей по курсу <курс доллара>".
# Вывести результат на экран (без кавычек).
cours = float(input())
rub = int(input())
print(f"Вы можете получить {int(rub/cours)}$ за {rub} рублей по курсу {cours}")

#
[print(f'Вы можете получить {int(b / a)}$ за {int(b)} рублей по курсу {a}')for a, b in [(float(input()) for _ in '__')]]



