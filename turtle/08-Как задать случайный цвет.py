# Как задать случайный цвет.
import turtle, random, time

# colors = ['red', 'green', 'yellow', 'purple', 'orange']
def chooseRandomColor():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue

window = turtle.Screen()
bob = turtle.Turtle()
# bob.color(chooseRandomColor())
# bob.forward(100)

while True:
    # window.bgcolor(random.choice(colors))
    # window.bgcolor(RED GREEN BLUE --> RGB)
    chooseRandomColor()
    time.sleep(1)

window.mainloop()

