n= int(input("Enter a number: "))
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        x = i*j
        print(x, end=" ")
    print()
