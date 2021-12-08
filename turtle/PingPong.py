# Пинг-Понг (Ping Pong) на Python. Часть 1.
# рисуем стол
import turtle

window = turtle.Screen()
window.title("PingPong")
window.setup(width=1.0, height=1.0)
window.bgcolor("black")

# рисуем прямоугольник игрового поля
border = turtle.Turtle()
border.speed(0)
border.color("green")
border.begin_fill()
border.up()
border.goto(-500, 300)
border.down()
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

# создание пунктирной линии
border.goto(0, 300)
border.color("white")
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()

border.hideturtle()

# создаем ракетки
rocket_a = turtle.Turtle()
rocket_a.color("white")
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=1, stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-450, 0)

rocket_b = turtle.Turtle()
rocket_b.color("white")
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=1, stretch_wid=5)
rocket_b.penup()
rocket_b.goto(450, 0)
# движение ракетки
def move_up():
    y = rocket_a.ycor() + 10
    if y > 250:
        y = 250
    rocket_a.sety(y)

def move_down():
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)

def move_up_b():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)

def move_down_b():
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_up_b, "o")
window.onkeypress(move_down_b, "k")


window.mainloop()

