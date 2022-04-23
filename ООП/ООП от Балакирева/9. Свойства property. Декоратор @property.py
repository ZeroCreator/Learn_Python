# Свойства property. Декоратор @property.
class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    #old = property(get_old, set_old)
#    old = property()
#    old = old.setter(set_old)
#    old = old.getter(get_old)

    @old.deleter
    def old(self):
        del self.__old


p = Person('Сергей', 20)
p.old = 45
print(p.old)
#p.set_old(35)
#print(p.old, p.__dict__)
#p.old = 45
print(p.old, p.__dict__)
#print(p.get_old, p.__dict__)
del p.old
print(p.__dict__)
p.old = 5
print(p.__dict__)