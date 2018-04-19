from random import *

while True:
    print('''           Guess your number game
    Now think of a number from 0 to 100, then press 'Enter'
    All you have to do is to answer to my Guess
    'c' if my guess is 'C'orrect
    's' if my guess is 'S'maller than your number
    'l' if my guess is 'L'arger than your number''')
    print()

    loop=True
    guess = 51
    max = 100
    min = 0
    while loop:
        print ("Is", guess, "is your number?", end=" ")
        answer = input().lower()
        print("Ctr+C and then press Enter to exit!")
        if answer == "l":
            max = guess
            guess = int((min+max)/2)
        elif answer == "s":
            min = guess
            guess= int((min+max)/2)
            if guess ==99 and answer == "s":
                guess=100
        elif answer == "c":
            print("I knew it, hura!")
            loop=False
