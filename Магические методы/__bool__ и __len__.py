# Проверка логического значения:
# __bool__ и __len__
class Truth:
    def __bool__(self): return True


X = Truth()
if X:
    print("yes!")


# yes!
class Truth:
    def __bool__(self): return True # первым опробуется __bool__
    def __len__(self): return 0


X = Truth()
print(bool(X))
# False
if not X:
    print("no!")