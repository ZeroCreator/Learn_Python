# Паттерн "Моносостояние".
# Делаем класс, у которого объекты имеют единое локальное пространство, единые локальные атрибуты
# - паттерн "Моносостояние".
class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()
th2.id = 3
print(th2.id)
print(th1.id)


# Добавление нового атрибута
print("Добавление нового атрибута")

th1.attr_new = 'new_attr'

print(th1.__dict__)
print(th2.__dict__)