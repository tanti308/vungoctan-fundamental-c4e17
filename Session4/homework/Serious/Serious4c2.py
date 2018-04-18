n= int(input("Enter a number: "))
m=1
for x in range(1,n+1,1):
    for i in range(1,n+1,1):
        i = i*m
        print(i, end=" ")
        if i<10:
            print(end=" ")
        else:
            print(end="")
    m+=1
    print()
