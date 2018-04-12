from turtle import *
color("red")
speed(0)
shape("turtle")

for i in range (16):
    if i % 2==0:
        pendown()
        forward(10)
    else:
        penup()
        forward(10)

mainloop()
