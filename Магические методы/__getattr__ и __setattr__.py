# Обращения к атрибутам: __getattr__ и __setattr__
class empty:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError(attrname)

X = empty()
print(X.age)
#40
print(X.name)
#AttributeError: name

class accesscontrol:
    def __setattr__(self, attr, value):
        if attr == "age":
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + " not allowed")

X = accesscontrol()
X.age = 40 # Вызовет метод __setattr__
print(X.age)
#40
X.name = "mel"
#AttributeError: name not allowed