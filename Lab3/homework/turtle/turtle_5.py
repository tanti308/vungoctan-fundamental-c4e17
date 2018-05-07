from turtle import *

def draw_star(x,y,length):
    speed(0)
    for i in range(5):
        forward(length)
        right(144)
        penup()
        towards(x,y)
        pendown()


draw_star(10,10,100)
mainloop()
