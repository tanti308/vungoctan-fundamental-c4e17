n= int(input("Enter a number?"))
factorial=1

for i in range(0,n+1,1):
    factorial= factorial * (factorial +1)


print("n! =", factorial)
