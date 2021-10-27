# Импорт собственных модулей.
import mymodule
import mymodule

# для повторного импортирования:
print("для повторного импортирования:")
import importlib

importlib.reload(mymodule)

print("ex1")

#sys.path.append(r"C:\Users\shkol\PycharmProjects\PycharmProjects\stepik - Python от Балакирева\8. Модули и пакеты. Работа с файлами\folder")

import pprint
import sys


#from mymodule import floor

#print(mymodule.floor(-5.4))
#print(floor(-5.4))

#pprint.pprint(dir(mymodule))
#a = mymodule.math.floor(-5.6)
#print(a)
#a = mymodule.floor(-5.6)
#b = mymodule.ceil(-5.6)
#print(a, b)


#pprint.pprint(sys.path)