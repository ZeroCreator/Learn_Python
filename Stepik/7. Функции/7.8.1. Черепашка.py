# Черепашка
from turtle import *

def main():
    init_turtle()
    forward_krivo(200, 4)

def init_turtle():
    shape('turtle')
    shapesize(2)
    color('green', 'yellow')

def forward_krivo(l, n):
    if n == 0:
        forward(l)
    else:
        forward_krivo(l / 3, n - 1)
        left(60)
        forward_krivo(l / 3, n - 1)
        right(120)
        forward_krivo(l / 3, n - 1)
        left(60)
        forward_krivo(l / 3, n - 1)

main()