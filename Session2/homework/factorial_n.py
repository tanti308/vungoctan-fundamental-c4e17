n= int(input("Enter a number?"))

if n == 0:
    print("n! =", 0)
else:
    factorial=1
    for i in range(1,n+1,1):
        factorial= factorial * i
    print("n! =", factorial)
