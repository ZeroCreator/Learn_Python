# Декоратор Property.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get_balance')
        return self.__balance

    #my_property_balance = my_balance
    @my_balance.setter
    def set_balance(self, value):
        print('set_balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value


    #my_balance = my_property_balance.setter(set_balance)
    #def del_balance(self):
        ##del self.__balance

    #my_balance = property()
   # my_balance = property(my_balance)
    #my_balance = my_balance.setter(set_balance)
    #my_balance = my_balance.deleter(del_balance)
    #balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)

a = BankAccount('lol',200)
a.set_balance =300
print(a.my_balance)

a.set_balance = 500
print(a.name)

'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    @property
    def my_balance(self):
        print('get balance')
        return self.__balance
        
    @my_balance.setter
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value,(int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value
    
    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance
'''