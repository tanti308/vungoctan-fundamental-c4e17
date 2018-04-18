from random import randint
loop=True
wrong_count=8
n=randint(0,100)
print(n)
while loop:
    a=int(input("Guess my number: "))
    if a==n:
        print("BINGO!")
        loop=False
    elif a<n:
        print("Too small!")
        wrong_count-=1
        print("You have", wrong_count, "time(s) left")
    else:
        print("Too large")
        wrong_count-=1
        print("You have", wrong_count, "time(s) left")
    if wrong_count==0:
        print("Gameover, you're loser!")
        loop=False
