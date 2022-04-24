# Использование статических методов и методов класса
"""
class Methods:
    def imeth(self, x): # Обычный метод экземпляра
        print(self, x)

    def smeth(x): # Статический метод: экземпляр не передается
        print(x)

    def cmeth(cls, x): # Метод класса: получает класс, но не экземпляр
        print(cls, x)

    smeth = staticmethod(smeth) # Сделать smeth статическим методом
    cmeth = classmethod(cmeth) # Сделать cmeth методом класса.

# Подсчет количества экземпляров с помощью
# статических методов
class Spam: # Для доступа к данным класса используется
    numInstances = 0 # статический метод
    def __init__(self):
        Spam.numInstances += 1

    def printNumInstances():
        print("Number of instances:", Spam.numInstances)
        printNumInstances = staticmethod(printNumInstances)


a = Spam()
b = Spam()
c = Spam()
print(Spam.printNumInstances()) # Вызывается, как простая функция
#Number of instances: 3
print(a.printNumInstances()) # Аргумент с экземпляром не передается
#Number of instances: 3
"""
"""
# Подсчет экземпляров с помощью методов класса
class Spam2:
    numInstances = 0 # Вместо статического метода используется метод класса
    def __init__(self):
        Spam2.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances:", cls.numInstances)
        printNumInstances = classmethod(printNumInstances)

a, b = Spam2(), Spam2()
a.printNumInstances() # В первом аргументе передается класс
#Number of instances: 2
Spam2.printNumInstances() # Также в первом аргументе передается класс
#Number of instances: 2
"""
class Spam3:
    numInstances = 0
    def __init__(self):
        Spam3.numInstances = Spam3.numInstances + 1
    @staticmethod
    def printNumInstances():
        print("Number of instances created: ", Spam3.numInstances)


a = Spam3()
b = Spam3()
c = Spam3()
Spam3.printNumInstances() # Теперь вызовы могут производиться как через класс,
 # так и через экземпляр!
print(a.printNumInstances()) # В обоих случаях будет выведено
 # “Number of instances created: 3”