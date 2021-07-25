# Зачем нужны функции в программировании.
# Помогают избавиться от избыточности кода.
import turtle
'''
def move():
    turtle.forward(100)
    turtle.left(90)

def draw_squere():
    for i in range(4):
        move()

turtle.speed(1)

draw_squere()
turtle.goto(150, 150)
draw_squere()
'''
'''
# Позволяют декомпозировать решение проблемы (большую задачу разбить на маленькие функции и выстроить взаимосвязь между ними).

def move(a):
    turtle.forward(a)
    turtle.left(90)

def draw_squere(a):
    for i in range(4):
        move(a)

turtle.speed(1)

draw_squere(60)
turtle.goto(150, 150)
draw_squere(120)

'''
# Цветной квадрат
def move(a):
    turtle.forward(a)
    turtle.left(90)

def draw_squere(a):
    for i in range(4):
        move(a)

def draw_square_color(a, color):
    turtle.color(color)
    turtle.begin_fill()
    draw_squere(a)
    turtle.end_fill()

turtle.speed(1)

draw_square_color(60, 'red')
turtle.goto(150, 150)
draw_square_color(120, 'blue')