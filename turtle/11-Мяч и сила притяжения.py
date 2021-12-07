# Мяч и сила притяжения.
import turtle

# выбор границы
border = turtle.Turtle()
border.hideturtle()
border.speed = 0
border.pensize(5)
border.up()
border.goto(-250, 250)
border.down()
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250, 250)


# мяч
ball = turtle.Turtle(shape='circle')
ball.up()
ball.goto(0, 200)
window = turtle.Screen()
window.bgcolor("yellow")
# speedY = -1 # перемещение по координате y и x
ball.speedY = 0
ball.speedX = 2

# создаем гравитацию
gravitation = 0.1

while True:
    # x, y = ball.position()
    ball.speedY = ball.speedY - gravitation
    ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)

    if ball.ycor() <= -250:
        ball.speedY = -ball.speedY
    if ball.xcor() >= 250 or ball.xcor() <= -250:
        ball.speedX = - ball.speedX

# выбор границы


window.mainloop()
