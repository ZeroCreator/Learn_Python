# Инициализация объекта. Метод init.
# Магические методы: __xxx__
class Cat:
    breed = 'pers'

    def set_value(self, value, age=0):
        self.name = value
        self.age = age