from turtle import *
pensize(2)
r=3                         #so canh va so goc ban dau
for i in range(4):
    for j in range(i+r):
        if (i+r) % 2 !=0:
            color("blue")
        else:
            color("red")
        forward(100)
        left(360/(i+r))

mainloop()
