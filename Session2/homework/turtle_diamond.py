from turtle import *

color("red")
speed(0)
for i in range (4):
    right(30)
    forward(100)
    left(60)
    forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)
    if i in range(3):      #Chỗ này em làm y như hình của BT ra
        right(120)
    else:
        pass
mainloop()
