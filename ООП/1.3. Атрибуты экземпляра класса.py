# Атрибуты экземпляра класса.
# Результатом вызова класса является экземпляр класса, который можно положить в какую-либо переменную.
class Car:
    model = 'BMW'
    engine = 1.6

# У экземпляра класса можно посмотреть переменную через __dict__.
print('Посмотреть атрибуты экземпляра класса:')
a1 = Car()
a2 = Car()
print(a1.__dict__)
print(a2.__dict__)

#
print('Создание новых атрибутув экземпляру класса:')
a1.seat = 4
print(a1.__dict__)
print(a2.__dict__)
print(Car.__dict__)

a1.model = 'Lada'
print(a1.__dict__)
print(Car.__dict__)
print(a1.model)
print(a2.model)

a2.size = 80
print(a2.size)

Car.r = 100
print(a2.r)
print(a1.r)
print(a1.__dict__)

del a1.model
print(a1.model)


