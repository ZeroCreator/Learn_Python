# Методы экземпляра. Аргумент self.
class Cat:
    def hello():
        print("Hello world from kitty")


# Cat.hello - функция - <function __main__.Cat.hello()>
# bob.hello - Метод - <bound method Cat.hello of <__main__.Cat object at 0x000001B0460F2DC8>>

# 1. Метод - это функция, объявленная внутри класса.
# 2. Метод - привязан к конкретному объекту и связан с ним.
# Функция не связана с отдельным объектом.
# 3. При вызове метода, тот объект, с которым он связан, будет автоматически подстовляться в аргумент функции.

class Cat:
    def hello(*args):
        print("Hello world from kitty", args)

jim = Cat()
print(jim.hello())  # Hello world from kitty (<__main__.Cat object at 0x00000206B9A0A248>,) где 0x206b9a0a248 - адрес памяти

#
class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

walt = Cat()
print(walt.show_breed())        # 'my breed is pers'

walt.breed = 'siam'
print(walt.show_breed())        # 'my breed is siam'

bob = Cat()
print(bob.show_breed())         # 'my breed is pers'

#
class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)

    def show_breed(instance):
        print(f'my breed is {instance.breed}')

    def show_name(instance):
        print(f'my name is {instance.name}')

mary = Cat()
mary.name = 'MARY'
print(mary.show_name())         # 'my name is MARY'

