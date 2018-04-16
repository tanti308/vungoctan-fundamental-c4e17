from turtle import *
pensize(2)
colors = ["red","blue","brown","yellow","grey"]
for i in range(len(colors)):
    color(colors[i])
    begin_fill()
    forward(30)
    left(90)
    forward(60)
    left(90)
    forward(30)
    left(90)
    forward(60)
    left(90)
    forward(30)
    end_fill()

mainloop()
