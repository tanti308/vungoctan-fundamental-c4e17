n =int(input("Enter number of star and x in total?"))

for i in range(n):
    if i % 2 ==0:
        print("x", end="")
    else:
        print("*", end="")
