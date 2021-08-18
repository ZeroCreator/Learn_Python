# Requests
import requests

r = requests.get('http://example.com') # Простой GET запрос
print(r.text) # вывод ответа от сервера

# Передача дополнительных параметров в запрос:
print('Передача дополнительных параметров в запрос:')
url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par) # Передача параметров в запрос
print(r.url) #Сформированный url-адрес с учетом параметров GET запроса

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies) # Отправка сформированных cookies на сервер
print(r.text)
'''
print(r.cookies['example_cookie_name']) # Использование cookies, полученных от сервера
'''

# Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и
# посчитать число строк в нём.
# Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы
# убрать пробельные символы по краям).
# После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не
# принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.
# В поле ответа введите одно число или отправьте файл, содержащий одно число.
# https://stepic.org/media/attachments/course67/3.6.2/989.txt
r = requests.get(('https://stepic.org/media/attachments/course67/3.6.2/989.txt').strip())
a = (r.text).splitlines()
print(len(a))

#
'''
import requests

with open('dataset_3378_2.txt') as inf:
    r = requests.get(inf.readline().strip())
    print(len(r.text.splitlines()))

#
from requests import get
with open('dataset.txt') as f:
    url = f.readline().strip()
text = get(url).text.splitlines()
print(len(text))


import requests
print(len(requests.get(open('dataset.txt').readline().strip()).text.splitlines()))

#
import requests
print(requests.get(open('xxx.txt').readline().strip()).text.count('\n'))

#
import requests                          # импортируем модуль реквест
def lines_count(s):                        # вводим функцию для подсчета строк
    return len(s.splitlines())               # возвращаем количество строк цифрой
with open ('C:/Users/HP/Downloads/dataset_3378_2.txt') as inf:   # открываем файл
    g = inf.readline().strip()                   # чтение по линиям, ограничиваемое переходом strip
r = requests.get(g)                         # присваиваем значению r - содержимое файла по адресу g
b = r.text                                  # присваиваем переменной b значение содержимого
a = lines_count(b)                          # присваиваем переменной a значение возвращенной функции
my_file = open("output_3.4.3.txt", "w")           # записываем ответ в файл
print (a, file=my_file)                     # переменная а в файл
my_file.close()                             # закрываем файл
'''

# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое последнего файла из набора, как ответ на это задание.
# https://stepic.org/media/attachments/course67/3.6.3/699991.txt

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
while True:
    if not r.text.startswith('We'):
        r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
        continue
    else:
        print(r.text)
        break

#
import requests
url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'
while name[:2] != 'We':
    name = requests.get(url + name).text
print(name)


#
import requests


url = "https://stepic.org/media/attachments/course67/3.6.3/"
r = requests.get(url + "699991.txt")
while not r.text.startswith("We"):
    r = requests.get(url + r.text)
    print(r.text)
print(r.text)


#
import requests

with open("dataset_3378_3.txt") as inf:
    r = requests.get(inf.readline().strip()).text
while 'We' not in r:
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r).text
print(r)

#
with open('dataset_3378_3.txt') as dataset:
    link = dataset.readline().strip()
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
c = 0
while True:
    import requests
    if 'We' not in link:
        r = requests.get(link)
        link = url + str(r.text)
        c += 1
        print(c)
    elif 'We' in link:
        with open('dataset_answer.txt', 'w') as answer:
            answer.write(r.text)
        break

#
import requests
stp="https://stepic.org/media/attachments/course67/3.6.3/"
with open('dataset_3378_3.txt','r') as file:
    st=file.readline().strip()
r=requests.get(st).text
while r[0:2]!="We":
    ht=stp+r
    r = requests.get(ht).text
    print(ht)
else:print(ht)