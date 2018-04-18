from random import randint
loop=True
wrong_count=8
n=randint(0,100)
print(n)
while loop:
    a=int(input("Guess my number: "))
    print("Type Ctrl+C and press Enter to exit!")
    if a==n:
        print("BINGO!")
        loop=False
    elif a<n:
        print("Too large!")
        wrong_count-=1
    else:
        print("Too small")
        wrong_count-=1
    if wrong_count==0:
        print("You're loser!")
        loop=False
