from turtle import*

speed(0)
color("green", "yellow")

begin_fill()
for i in range(50):
    for t in range(4):
        forward(100)
        left(90)
    left(7)
end_fill()

mainloop()
