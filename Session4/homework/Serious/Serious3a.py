from random import choice
from random import randrange
loop=True
word = "champion"
characters = list(word)
correct = word
print(*characters, sep=" ")

quest=""
while characters:
    index=randrange(len(characters))
    quest += characters[index]
    characters=characters[:index] + characters[(index+1):]
print(*list(quest), sep="  ")
guess=input("Your answer: ").lower()
while guess != correct:
    print(":(")
    guess=input("Your answer: ").lower()
    print("Please type Ctrl+C and press Enter to exit!")
if guess == correct:
    print("Hura!")
