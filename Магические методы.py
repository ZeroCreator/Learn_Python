# Магические методы
# Доступ к элементам по индексу и извлечение
# срезов: __getitem__ и __setitem__
print("__getitem__ и __setitem__")
class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print(X[2])     # Выражение X[i] вызывает X.__getitem__(i)

for i in range(5):
    print(X[i], end=" ") # Вызывает __getitem__(X, i) в каждой итерации

print()
# Извлечение срезов
print("Извлечение срезов")
L = [5, 6, 7, 8, 9]
# с использованием синтаксиса срезов
print("с использованием синтаксиса срезов")
print(L[2:4]) # Извлечение среза с использованием синтаксиса срезов
print(L[1:])
print(L[:-1])
print(L[::2])

# с помощью объекта среза
print("с помощью объекта среза")
print(L[slice(2, 4)]) # Извлечение среза с помощью объекта среза
print(L[slice(1, None)])
print(L[slice(None, -1)])
print(L[slice(None, None, 2)])


# _getitem__
print("_getitem__")
class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index): # Вызывается при индексировании или
        print("getitem:", index) # извлечении среза
        return self.data[index] # Выполняет индексирование
                                # или извлекает срез

    def __setitem__(self, index, value):  # Реализует присваивание по индексу или по срезу
        self.data[index] = value  # Приcваивание по индексу или по срезу

X = Indexer()
print(X[0]) # При индексировании __getitem__
#getitem: 0 # получает целое число
#5
print(X[1])
#getitem: 1
#6
print(X[-1])
#getitem: -1


print(X[2:4]) # При извлечении среза __getitem__ получает объект среза
#getitem: slice(2, 4, None)
#[7, 8]
print(X[1:])
#getitem: slice(1, None, None)
#[6, 7, 8, 9]
print(X[:-1])
#getitem: slice(None, -1, None)
#[5, 6, 7, 8]
print(X[::2])
#getitem: slice(None, None, 2)
#[5, 7, 9]

# __setitem__
print("__setitem__")

# Итерации по индексам: __getitem__
print("Итерации по индексам: __getitem__")
class stepper:
    def __getitem__(self, i):
        return self.data[i]

X = stepper() # X - это экземпляр класса stepper
X.data = "Spam"
print(X[1]) # Индексирование, вызывается __getitem__
for item in X: # Циклы for вызывают __getitem__
    print(item, end=" ") # Инструкция for индексирует элементы 0..N


print("p" in X) # Во всех этих случаях вызывается __getitem__
True
print([c for c in X]) # Генератор списков
#["S", "p", "a", "m"]
print(list(map(str.upper, X))) # Функция map (в версии 3.0
#["S", "P", "A", "M"] # требуется использовать функцию list)
(a, b, c, d) = X # Присваивание последовательностей
print(a, c, d)
#("S", "a", "m")
print(list(X), tuple(X), " ".join(X))
#(["S", "p", "a", "m"], ("S", "p", "a", "m"), "Spam")
print(X)

# Итераторы: __iter__ и __next__
print("Итераторы: __iter__ и __next__")
print(" класс итератора, который возвращает квадраты чисел:")
class Squares:
    def __init__(self, start, stop): # Сохранить состояние при создании
        self.value = start - 1
        self.stop = stop
    def __iter__(self): # Возвращает итератор в iter()
        return self
    def __next__(self): # Возвращает квадрат в каждой итерации
        if self.value == self.stop: # Также вызывается функцией next
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5):
    print(i, end=" ")


X = Squares(1, 5) # Выполнение итераций вручную: эти действия выполняет
# инструкция цикла
I = iter(X) # iter вызовет __iter__
print(next(I)) # next вызовет __next__
#1
print(next(I))
#4
print(next(I))
print(next(I))
print(next(I))
# next(I) # Исключение можно перехватить с помощью инструкции try
# StopIteration

X = Squares(1, 5)
print([n for n in X]) # Получить все элементы
#[1, 4, 9, 16, 25]
print([n for n in X]) # Теперь объект пуст
#[]
print([n for n in Squares(1, 5)]) # Создать новый объект итератора
#[1, 4, 9, 16, 25]
print(list(Squares(1, 3)))
#[1, 4, 9]

def gsquares(start, stop):
    for i in range(start, stop+1):
        yield i ** 2

for i in gsquares(1, 5): # или: (x ** 2 for x in range(1, 5))
    print(i, end=" ")

