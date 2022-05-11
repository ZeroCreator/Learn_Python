# Метаклассы. Объект type.
# type(name, bases, dct)
print(type(int))

# A = type('Point', (), {'MAX_COORD': 100, 'MIN_COORD': 0})
# print(A)
#
# pt = A()
# print(pt)
# print(pt.MAX_COORD)

class B1: pass

class B2: pass

A = type('Point', (B1, B2), {'MAX_COORD': 100, 'MIN_COORD': 0})


print(A)

pt = A()
print(pt)
print(pt.MAX_COORD)

print(A.__mro__)

def method1(self):
    print(self.__dict__)

C = type('Point', (B1, B2), {'MAX_COORD': 100, 'method1': lambda self: self.MAX_COORD})
pt1 = C()

print(pt1.method1)