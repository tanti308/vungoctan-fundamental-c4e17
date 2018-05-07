from turtle import *


def draw_square(length,color):
    speed(0)
    pencolor(color)
    for i in range(4):
        forward(length)
        left(90)

    mainloop()
