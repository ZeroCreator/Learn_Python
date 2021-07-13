# Функции как атрибут класса.
class Car:
    model = 'BMW'
    engine = 1.6

    def drive():
        print("Let's go")


print(Car.__dict__)

#
print('Вызов функции:')
print(Car.drive())

print(getattr(Car, 'drive')())

a = Car()
a.drive()