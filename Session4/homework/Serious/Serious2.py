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
