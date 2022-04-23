# Магические методы математических операций
# __add__, - сложение
# __mul__, - умножение
# __sub__ - вычитание
# и __truediv__. - деление
class BankAccount:
    def __init__(self, name, balance):
        print("new_obj init")
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Клиент {self.name} с балансом {self.balance}"

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    def __radd__(self, other):
        print("__radd__ call")
        return self + other

    def __mul__(self, other):
        print('__mul__ call')
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):
            return BankAccount(self.name, self.balance + other)
        raise NotImplemented

r = BankAccount("Misha", 78)
print(r + 12)

b = BankAccount("Tanya", 900)
print(r + b)
print(r + 12)
print(12 + r)

# print(r * 3)
# print(r * "ttt")
# print(r * "Misha")

t = BankAccount("Ivan", 200)
print(t + 30)
d = t + 40
print(d)

#__addf__(+), __mul__(*),__sub__(-), __truediv__(/)

class BancAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BancAccount):#проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance + other.balance# слож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):#проверяем явл ли числом
            return self.balance + other
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ call')
        return self + other

    def __mul__(self, other):
        print('__mul__ call')
        if isinstance(other, BancAccount):#проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance * other.balance# умнож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):#проверяем явл ли строкой
            return self.name + other
        #raise NotImplemented

    def __rmul__(self, other):
        print('__rmul__ call')
        return self * other

r = BancAccount('Ivan', 900)# __add__ call
print(r + 600, r.balance + 300, r.balance)# 1500 1200 900
b = BancAccount('Luka', 1900)# __add__ call
print(r + b, b + 600, b.balance + 300, b.balance)# 2800 2500 2200 1900
print(600 + r)# 1500

#__addf__(+), __mul__(*),__sub__(-), __truediv__(/)

class BancAccount:
    def __init__(self, name, balance):
        print('New object __init__')
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BancAccount):#проверяем явл ли экземпляром этого (BancAccount) класса
            return self.balance + other.balance# слож баланса другого экз этого (BancAccount) класса
        if isinstance(other, (int, float)):#проверяем явл ли числом
            #return self.balance + other
            return BancAccount(self.name, self.balance + other)#Возвращаем новый экземпляр
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__ call')
        return self + other

t = BancAccount('Vasja', 900)# New object __init__
print(id(t))# 140062794291240
print(t + 30)# Клиент Vasja с балансом 930