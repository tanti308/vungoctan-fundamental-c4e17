from turtle import*

speed(0)
color("green", "yellow")

begin_fill()
for i in range(100):
    for i in range(3):
        forward(100)
        left(120)
    left(7)
end_fill()

mainloop()
