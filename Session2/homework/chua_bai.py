n = int(input("Enter number of stars and x's in total: "))
x = "x"
s = "*"
if n % 2 == 0:
    for i in range (int(n/2)):
        print(x, s, end="")
    print()
else:
    for i in range (int(n/2)):
        print(x, s, end="")
    print(x)
