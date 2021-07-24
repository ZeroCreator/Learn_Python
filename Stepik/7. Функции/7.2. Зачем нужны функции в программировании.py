# Зачем нужны функции в программировании.
# Помогают избавиться от избыточности кода.
import turtle

def draw_squere():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

turtle.speed(1)

draw_squere()
turtle.goto(150, 150)
draw_squere()
