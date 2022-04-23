# Инициализатор __init__ и финализатор __del__
# __Имя магического метода__
# __init__(self) - инициализатор объекта класса
# __del__(self) - финализатор класса

# __init__(self) - инициализатор объекта класса
print("__init__(self) - инициализатор объекта класса")
class Point:
    color = "red"
    circle = 2

    def __init__(self, x=0, y=0):
        #print("вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    def set_coords(self, x, y):
        print("вызов метода set_coords")
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
##pt = Point(1, 2)
#pt.set_coords(1, 2)
print(pt.__dict__)


# __del__(self) - финализатор класса
print("__del__(self) - финализатор класса")
