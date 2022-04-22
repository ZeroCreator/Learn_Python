# Сравнение: __lt__, __gt__ и другие
class C:
    data = "spam"
    def __gt__(self, other): # версии 3.0 и 2.6
        return self.data > other
    def __lt__(self, other):
        return self.data < other
X = C()
print(X > "ham") # Выведет True (вызовет __gt__)
print(X < "ham") # Выведет False (вызовет __lt__)