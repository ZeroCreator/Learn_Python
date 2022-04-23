# Файл testmixin.py
from lister import * # Импортировать инструментальные классы


class Super:
    def __init__(self): # Метод __init__ суперкласса
        self.data1 = "spam" # Создать атрибуты экземпляра

    def ham(self):
        pass


# class Sub(Super, ListInstance): # Подмешать методы ham и __str__
class Sub(Super, ListTree):
    def __init__(self): # Инструментальные классы имеют доступ к self
        Super.__init__(self)
        self.data2 = "eggs" # Добавить атрибуты экземпляра
        self.data3 = 42

    def spam(self): # Определить еще один метод
        pass


class C(ListInstance):
    pass


if __name__ == "__main__":
    X = Sub()
    print(X) # Вызовет подмешанный метод __str__
    x = C()
    x.a = 1
    x.b = 2
    x.c = 3
    print(x)
