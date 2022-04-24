# property
class newprops(object):
    def getage(self):
        return 40
    age = property(getage, None, None, None) # get,set,del,docs

x = newprops()
print(x.age) # Вызовет метод getage
#40
#print(x.name) # Нормальная операция извлечени

class newprops(object):
    def getage(self):
        return 40

    def setage(self, value):
        print("set age:", value)
        self._age = value

    age = property(getage, setage, None, None)

x = newprops()
print(x.age) # Вызовет метод getage
#40
x.age = 42 # Вызовет метод setage
#set age: 42
print(x._age) # Нормальная операция извлечения; нет вызова getage
#42
x.job = "trainer" # Нормальная операция присваивания; нет вызова setage
print(x.job) # Нормальная операция извлечения; нет вызова getage
#"trainer"

class classic:
    def __getattr__(self, name): # При ссылке на неопределенный атрибут
        if name == "age":
            return 40
        else:
            raise AttributeError
    def __setattr__(self, name, value): # Для всех операций присваивания
        print("set:", name, value)
        if name == "age":
            self.__dict__["_age"] = value
        else:
            self.__dict__[name] = value

x = classic()
print(x.age) # Вызовет метод __getattr__
#40
x.age = 41 # Вызовет метод __setattr__
#set: age 41
print(x._age) # Определен: нет вызова __getattr__
#41
x.job = "trainer" # Запустит метод __setattr__ опять
print(x.job )