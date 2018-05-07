from turtle import *

def draw_square(length, color):
    for _ in range(4):
        speed(0)
        pencolor(color)
        forward(length)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
