# Операция вызова: __call__
class Callee:
    def __call__(self, *pargs, **kargs): # Реализует вызов экземпляра
        print("Called:", pargs, kargs)

C = Callee()
print(C(1, 2, 3)) # C – вызываемый объект
#Called: (1, 2, 3) {}
print(C(1, 2, 3, x=4, y=5))
#Called: (1, 2, 3) {‘y’: 5, ‘x’: 4}

"""
class C:
 def __call__(self, a, b, c=5, d=6): ... # Обычные и со значениями по умолчанию
class C:
 def __call__(self, *pargs, **kargs): ... # Произвольные аргументы
class C:
 def __call__(self, *pargs, d=6, **kargs): ... # 
 
X = C()
X(1, 2) # Аргументы со значениями по умолчанию опущены
X(1, 2, 3, 4) # Позиционные
X(a=1, b=2, d=4) # Именованные
X(*[1, 2], **dict(c=3, d=4)) # Распаковывание произвольных аргументов
X(1, *(2,), c=3, **dict(d=4)) # Смешанные режимы 
"""