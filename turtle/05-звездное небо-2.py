# Расставляем мышкой звезды на небе turtle.
import turtle, random, time

def starFILL(n, dlina):
    joe.left(random.randint(10, 350)) # Случайный угол поворота звезд.
    joe.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            joe.forward(dlina)
            angle = n // 2 * 360 / n
            joe.left(angle)
    joe.end_fill()

# Устанавливаем фон и размеры неба
window = turtle.Screen()
window.bgcolor("black")
window.setup(700, 500)

joe = turtle.Turtle()
joe.speed(0)
joe.color('yellow')
joe.hideturtle()

for i in range(5):
    x = random.randint(-320, 320)
    y = random.randint(-220, 220)
    joe.up()
    joe.setposition(x, y)
    joe.down
    size = random.randint(10, 20)
    vershina = random.choice([5, 7, 9, 11, 13, 15])
    starFILL(vershina, size)

def move(x, y):
    joe.up()
    joe.setposition(x, y)
    joe.down
    size = random.randint(10, 20)
    vershina = random.choice([5, 7, 9])
    starFILL(vershina, size)

window.onclick(move)
window.listen()
window.mainloop()
