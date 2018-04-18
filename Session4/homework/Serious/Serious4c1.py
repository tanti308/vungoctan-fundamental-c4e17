m=1
for n in range(1,10,1):
    for i in range(1,10,1):
        i = i*m
        print(i, end=" ")
        if i<10:
            print(end=" ")
        else:
            print(end="")
    m+=1
    print()
