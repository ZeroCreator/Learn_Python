# как при помощи turtle можно обрабатывать такие события как нажатие на клавишу и
# как мы можем это использовать в своих программах.
# Событие - любое нажатие на клавишу.
import turtle

speed = 5

def moveUp():
    x = pen.position()[0]
    y = pen.position()[1]
    pen.setposition(x, y + 5)
    # print(pen.position()) # текущее местоположение карандаша

def moveDown():
    x, y = pen.position()
    # x = pen.position()[0]
    # y = pen.position()[1]
    pen.setposition(x, y - 5)

def moveLeft():
    x, y = pen.position()
    # x = pen.position()[0]
    # y = pen.position()[1]
    pen.setposition(x-5, y)

def moveRight():
    x, y = pen.position()
    # x = pen.position()[0]
    # y = pen.position()[1]
    pen.setposition(x+5, y)

def change():
    if pen.isvisible():
        pen.up() # поднимаем карандаш
        pen.hideturtle()
    else:
        pen.down() # опускаем карандаш
        pen.showturtle()

def speedUp():
    global speed
    speed += 1

def speedDown():
    global speed
    speed = max(0, speed-1) # чтобы не уйти в 0

window = turtle.Screen()
pen = turtle.Turtle()

# привязывание клавиши к событию: window.onkey(функцияб клавиша)
window.onkey(moveUp, 'Up')
window.onkey(moveDown, 'Down')
window.onkey(moveLeft, 'Left')
window.onkey(moveRight, 'Right')
# изменение видимости черепашки
window.onkey(change, 'space')
# изменение скорости
# увеличение
window.onkey(speedUp, 'q')
# уменьшение
window.onkey(speedDown, 'w')


# поставить прослушивание с помощью функции listen()
window.listen()
# для того, чтобы программа не закрывалась - функция mainloop()
window.mainloop()
