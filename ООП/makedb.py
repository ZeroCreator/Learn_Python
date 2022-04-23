# Файл makedb.py: сохраняет объекты Person в хранилище
# import person               # Загружает класс с помощью инструкции import
# bob = person.Person()       # Обращение к классу через имя модуля

# from person import Person   # Загружает класс с помощью инструкции from
# bob = Person()              # Обращение по непосредстенному имени класса

from person import Person, Manager  # Импортирует наши классы

bob = Person("Bob Smith")  # Создание объектов для сохранения
sue = Person("Sue Jones", job="dev", pay=100000)
tom = Manager("Tom Jones", 50000)
import shelve

db = shelve.open("persondb")  # Имя файла хранилища
for object in (bob, sue, tom):  # В качестве ключа использовать атрибут name
    db[object.name] = object  # Сохранить объект в хранилище
db.close()  # Закрыть после внесения изменений
