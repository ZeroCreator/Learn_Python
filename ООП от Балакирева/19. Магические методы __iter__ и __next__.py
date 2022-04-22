# Магические методы __iter__ и __next__
# __iter__(self) – получение итератора для перебора объекта;
# __next__(self) – переход к следующему значению и его считывание.
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration



class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.fr = FRange(start, stop, step)
        self.rows = rows

    def __iter__(self):
        self.value_row = 0
        return self

    def __next__(self):
        if self.value_row < self.rows:
            self.value_row += 1
            return iter(self.fr)
        else:
            raise StopIteration

fr = FRange(0, 2, 0.5)
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())
print(fr.__next__())

fr = FRange(0, 2, 0.5)
print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))

fr = FRange(0, 2, 0.5)
for x in fr:
    print(x)

fr = FRange2D(0, 2, 0.5, 4)
for row in fr:
    for x in row:
        print(x, end=" ")
    print()