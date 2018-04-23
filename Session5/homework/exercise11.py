p = {"x": 1,"y": 1}
bx=2
by=2
loop= True
while loop:
    for y in range(4):
        for x in range(4):
            if x  == p["x"] and y == p["y"]:
                print("P ", end="")
            elif x == bx and y == by:
                print("B ", end="")
            elif x == 1 and y == 3:
                print("G ", end="")
            else:
                print("- ", end="")
        print()

    move = input("Your move (W/A/S/D)? ").upper()

    if bx ==1 and by==3:
        print("Congrat!")
        loop=False

    next_px = p["x"]
    next_py = p["y"]
    dx = 0
    dy = 0

    if move == "D":
        dx = 1
    elif move == "A":
        dx = -1
    elif move == "S":
        dy = 1
    elif move == "W":
        dy = -1

    next_px += dx
    next_py += dy

    if next_px == bx and next_py == by:
        bx += dx
        by += dy
    if bx ==1 and by==3:
        print("Congrat!")
        loop=False
    if 0 <= next_px < 4:
        p["x"] = next_px

    if 0 <= next_py < 4:
        p["y"] = next_py
