n= int(input("Enter number of stars?"))

if n%2==0:
    for i in range(0,n,2):
        print("*", end="")
        print("*", end="")
else:
    for i in range(n):
        print("*", end="")
print()
