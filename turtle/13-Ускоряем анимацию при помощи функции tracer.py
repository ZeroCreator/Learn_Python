# Ускоряем анимацию при помощи функции tracer.
import turtle, random

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

window = turtle.Screen()
window.bgcolor("yellow")
window.tracer(5)

# мячи
balls = []
count = 15 # количество мячей
forms = ['circle', 'square', 'triangle', 'turtle']

for i in range(count):
    ball = turtle.Turtle(shape=random.choice(forms))
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red, green, blue)
    ball.up()
    ball.goto(random.randint(-200, 200), random.randint(100, 300))
    ball.speedY = 0
    ball.speedX = random.randint(-3, 3)
    ball.angle = random.randint(-5, 5) # угол вращения
    ball.gravitation = random.randint(1, 30)*0.01
    balls.append(ball)

gravitation = 0.1

while True:
    window.update()
    for ball in balls:
        ball.left(ball.angle) # вращение на заданный угол
        ball.speedY = ball.speedY - ball.gravitation
        ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)

        if ball.ycor() <= -250:
            ball.sety(-250) # если мяч упал ниже, чем рамка
            ball.speedY = -ball.speedY

        if ball.xcor() >= 250 or ball.xcor() <= -250:
            ball.speedX = - ball.speedX


window.mainloop()
