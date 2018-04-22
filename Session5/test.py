px =1
py =1
for y in range(4):
    for x in range(4):
        if x==px and y==py:
            print("P ", end="  ")
        elif x==2 and y==2:
            print("G ", end="  ")
        elif x==1 and y==3:
            print("B ", end="  ")
        else:
            print("- ", end="  ")

    print()
