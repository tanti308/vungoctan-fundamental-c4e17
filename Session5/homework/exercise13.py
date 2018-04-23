p = {"x": 1,"y": 1}

boxes = [
    {
        "x": 2,
        "y": 2
    },
    {
        "x": 3,
        "y": 4
    }
]

 # print(boxes[0]["x"])

for box in boxes:
    print(box["y"])

while True:
    for y in range(4):
        for x in range(4):
            if x == p["x"] and y == p["y"]:
                print("P ", end="")
            elif x == b[0]["x"] and y == b[0]["y"] or x == b[1]["x"] and y == b[1]["y"]:
                print("B ", end="")
            elif x == 1 and y == 3:
                print("G ", end="")
            else:
                print("- ", end="")
        print()

    move = input("Your move (W/A/S/D)? ").upper()

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


    if 0 <= next_px < 4:
        px = next_px

    if 0 <= next_py < 4:
        py = next_py
