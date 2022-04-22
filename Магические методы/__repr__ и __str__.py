# Строковое представление объектов:
# __repr__ и __str__
# Эти методы позволяют определить более удобочитаемый формат
# вывода ваших объектов.
class adder:
    def __init__(self, value=0):
        self.data = value # Инициализировать атрибут data
    def __add__(self, other):
        self.data += other # Прибавить другое значение

x = adder() # Формат отображения по умолчанию
print(x)

class addrepr(adder): # Наследует __init__, __add__
    def __repr__(self): # Добавляет строковое представление
        return f"addrepr({self.data})"  # Преобразует в строку программного кода
x = addrepr(2) # Вызовет __init__
print(x + 1) # Вызовет __add__
print(x) # Вызовет __repr__
#addrepr(3)
print(x) # Вызовет __repr__
#addrepr(3)
print(str(x), repr(x)) # Вызовет __repr__
#(‘addrepr(3)’, ‘addrepr(3)’
