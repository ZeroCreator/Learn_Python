# Геттеры и сеттеры, property атрибуты.
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self): # Вернет значение
        return self.__balance

    def set_balance(self, value): # Проставит значение
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value
'''
a = BankAccount('Ivan', 100)
print(a.balance)
print(a.name)
a.balance = 'hello'
print(a.balance)
'''
# Ограничение доступа к переменной

b = BankAccount('Vasya', 200)
print(b.get_balance())
b.set_balance(400)
print(b.get_balance())
print(b.__dict__)

c = BankAccount('Tanya', 300)
#c.set_balance('he')
print(c.get_balance())
c.set_balance(500)
print(c.get_balance())
print(c.__dict__)

# property - свойство
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self): # Вернет значение
        print('get balance')
        return self.__balance

    def set_balance(self, value): # Проставит значение
        print('set balance', value)
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

d = BankAccount('Misha', 400)
d.balance # не атрибут, а свойство
print(d.balance)
d.balance = 777
print(d.balance)

# del d.balance
# print(d.balance) # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'

d.balance = 789
print(d.balance)

#
print('Tasks')
# Создайте класс UserMail, у которого есть:
# конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес. Их необходимо сохранить в экземпляр как атрибуты
# login и __email (обратите внимание, защищенный атрибут)
# метод геттер get_email, которое возвращает защищенный атрибут __email ;
# метод сеттер set_email, которое принимает в виде строки новую почту. Метод должен проверять, что в новой почте есть
# только один символ @ и после нее есть точка. Если данные условия выполняются, новая почта сохраняется в атрибут __email,
# в противном случае выведите сообщение "Ошибочная почта";
# создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email
# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # Ошибочная почта
# k.email = 'prince@still@.wait'  # Ошибочная почта
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait
class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set__email(self, new_email):
        if isinstance(new_email, str) and new_email.count('@') == 1 and '.' in new_email[new_email.find('@'):]:
            self.__email = new_email
        else:
            print("Ошибочная почта")


    email = property(fget=get_email, fset=set__email)



#
class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if isinstance(email, str) \
         and email.count('@') == 1 \
         and email.count('.', email.index('@') + 1) == 1:
            self.__email = email
        else:
            print('Ошибочная почта')

    email = property(get_email, set_email)


#
class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def __checkValue(value):  # проверка переменной явл-ся ли она
        if type(value) == str and value.count('@') == 1 and '.' in value[value.find('@') + 1:]:
            return True
        return False

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if not UserMail.__checkValue(value):
            # raise ValueError('Ошибочная почта')
            print('Ошибочная почта')
        self.__email = value

    def delete_email(self):
         del self.__email

    email = property(fget=get_email, fset=set_email, fdel=delete_email)


