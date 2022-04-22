# Магический метод __bool__ определения правдивости объектов
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y

p = Point(10, 10)
print(bool(p))
print(len(p))

if p:
    print("Объект р дает True")
else:
    print("Объект р дает False")

