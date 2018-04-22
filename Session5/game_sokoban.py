# 1. Hien map
# 2. Input command
# 3. Update map
# 4. Push box
# Tang box va people len => 1 cai hop la 1 dictionary,...
# p={"x":1,"y":1} , px => p["x"]
px =1
py =1
bx =2
by =2
loop= True
while loop:
    for y in range(4):
        for x in range(4):
            if x==px and y==py:
                print("P ", end="  ")
            elif x==2 and y==2:
                print("G ", end="  ")
            elif x==bx and y==by:
                print("B ", end="  ")
            else:
                print("- ", end="  ")

        print()

    move=str(input("Your next move? (W/A/S/D)  ")).lower()
    next_px=px
    next_py=py
    dx=0
    dy=0
    if move == "w":
        dy = -1
    elif move =="a":
        dx =-1
    elif move =="s":
        dy = 1
    elif move =="d":
        dx =1
    next_px += dx
    next_py += dy
    if 0<=next_px <4:
        px=next_px
    if 0<= next_py <4:
        py=next_py
    if next_px==bx and next_py==by:
        bx += dx
        by += dy

# matrix = [["- ", "- ", "- ", "- "],
# ["- ", "- ", "- ", "- "],
# ["- ", "- ", "- ", "- "],
# ["- ", "- ", "- ", "- "]]
# matrix[(2,2)]== "P"
# matrix[(3,3)]== "B"
# matrix[(3,4)]== "G"
# for i in matrix:
#     print(*i, end="\n")
#
# print(matrix[2,2])
