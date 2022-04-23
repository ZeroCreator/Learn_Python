from lister import ListInstance

class Spam(ListInstance): # Наследует метод __str__
    def __init__(self):
        self.data1 = "food"

x = Spam()
print(x) # print() и str() вызывают __str__
#<Instance of Spam, address 40240880:
#name data1=food

print(str(x))
#‘<Instance of Spam, address 40240880:\n\tname data1=food\n>’
print(x) # По умолчанию используется __repr__
#<__main__.Spam object at 0x026606F0>