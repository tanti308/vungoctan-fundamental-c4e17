n= int(input("Enter a number of sx?"))

for i in range(n*2):
    if i % 2 ==0:
        print("*", end="")
    else:
        print("x", end="")
