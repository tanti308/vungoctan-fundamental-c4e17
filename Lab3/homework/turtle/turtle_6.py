from turtle import *

def draw_star(x,y,length):
    speed(0)
    for i in range(5):
        forward(length)
        right(144)
        penup()
        towards(x,y)
        pendown()

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(50,100)
    draw_star(x, y, length)

mainloop()
