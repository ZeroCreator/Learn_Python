# Импорт собственных модулей.
import st_librery

from pprint import pprint

# Через "." можно увидеть все пространство имен импортируемого модуля:
st_librery.summa()
print(st_librery.factorial(10))
print(st_librery.summa(43, 6, 46))

from Stepik.st_librery import my_str, my_num1
print(my_str, my_num1)

print(st_librery.e)
print(st_librery.pi)

import sys
pprint(sys.path)

# Если модули находятся в разных местах:
print(sys.path.append('ПУТЬ ФАЙЛА'))

# Каждый модуль импортируется только один раз.
# Для перезаполнения модуля - использовать модуль importlib:
import importlib
importlib.reload(st_librery)

# У каждого модуля есть атрибут __name__
print(__name__)                             # __main__
#if __name__ == '__main__':
