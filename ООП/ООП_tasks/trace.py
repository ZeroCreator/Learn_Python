class wrapper:
    def __init__(self, object):
        self.wrapped = object # Сохранить объект
    def __getattr__(self, attrname):
        print("Trace:", attrname) # Отметить факт извлечения
        return getattr(self.wrapped, attrname) # Делегировать извлечение



x = wrapper([1,2,3])
x.append(4)
print(x.wrapped)

x = wrapper({"a": 1, "b": 2})
print(x.keys())

