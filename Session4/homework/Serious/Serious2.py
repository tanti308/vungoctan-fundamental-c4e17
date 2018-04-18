from random import randint

n= input('''Guess your number game
Now think of a number from 0 to 100, then press 'Enter'
All you have to do is to answer to my Guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number''')
loop=True
while loop:
    g=randint(0,100)

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
