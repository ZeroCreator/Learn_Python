# Правостороннее сложение и операция
# приращения: __radd__ и __iadd__
class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter):
            other = other.val
            print("add", self.val, other)
            return self.val + other

    def __radd__(self, other):
        print("radd", self.val, other)
        return Commuter(other + self.val)
        #return other + self.val

    def __str__(self):
        return f"Commuter: {self.val}"

x = Commuter(88)
y = Commuter(99)
print(x + 1)  # __add__: экземпляр + не_экземпляр
        # add 88 1
        # 89
print(1 + y)  # __radd__: не_экземпляр + экземпляр
        # radd 99 1
        # 100
print(x + y)  # __add__: экземпляр + экземпляр
        # add 88 < __main__.Commuter instance at 0x02630910 >
        # radd 99 88
        # 187

print(x + 10) # Результат – другой экземпляр класса Commuter
#<Commuter: 98>
print(10 + y)
#<Commuter: 109>
z = x + y # Нет вложения: не происходит рекурсивный вызов __radd__
print(z)
#<Commuter: 187>
print(z + 10)
#<Commuter: 197>
print(z + z)
#<Commuter: 374>

class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other): # __iadd__ явно реализует операцию x += y
        self.val += other # Обычно возвращает self
        return self
x = Number(5)
x += 1
x += 1
print(x.val)
#7

class Number:
    def __init__(self, val):
        self.val = val
    def __add__(self, other): # __add__ - как крайнее средство: x=(x + y)
        return Number(self.val + other) # Распространяет тип класса
x = Number(5)
x += 1
print(x.val)
#7