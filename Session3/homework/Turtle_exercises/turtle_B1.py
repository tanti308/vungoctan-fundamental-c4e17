from turtle import *
pensize(2)
colors=["red", "blue", "brown", "yellow", "grey"]
r= 3                        #so canh va so goc ban dau`

for i in range(5):
    for j in range(r):
        color(colors[i])
        forward(100)
        left(360/(i+3))
    r=r+1

amainloop()
