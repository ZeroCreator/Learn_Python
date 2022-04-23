# Моносостояние для экземпляров класса.
# Паттерн моносостояния.
'''
class Cat:
    breed = 'pers'

a = Cat()
b = Cat()

a.breed = 'siam' # Свойство только одного экземпляра класса
b.color = 'black' # Свойство только одного экземпляра класса

c = Cat() # Принимает начальные значения.
'''
# Как сделать, чтобы изменения одного экземпляра касались всех остальных экземпляров класса:
class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


d = Cat()
g = Cat()

d.breed = 'siam'
d.name = 'Bob'

h = Cat()
print(h.__dict__)