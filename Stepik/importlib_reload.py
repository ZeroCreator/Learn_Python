# К уроку 8.3.
# Каждый модуль импортируется только один раз.
# Для перезаполнения модуля - использовать модуль importlib:

import st_librery

print(st_librery.my_num1)
st_librery.my_num1 = 20
print(st_librery.my_num1)

import st_librery
print(st_librery.my_num1)

import importlib
importlib.reload(st_librery)
print(st_librery.my_num1)