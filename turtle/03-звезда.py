# Как нарисовать звезду при помощи turtle.
import turtle, time
joe = turtle.Turtle()
joe.speed(10)

# Закрашиваем звузду
def starFILL(n, dlina):
    joe.begin_fill()
    star(n, dlina)
    joe.end_fill()

# Рисуем звезду
def star(n, dlina):
    if n % 2 != 0:
        for i in range(n):
            joe.forward(dlina)
            angle = n // 2 * 360 / n
            joe.left(angle)


for i in range(5, 16, 2):
    joe.speed(10)
    starFILL(9, 150)
    time.sleep(1)
    joe.reset()
