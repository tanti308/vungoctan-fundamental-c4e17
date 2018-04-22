loop=True
while loop:
    ques= input("Enter the data: ").lower()

    letters_count ={}
    for letter in ques:
        letters_count[letter] = letters_count.get(letter, 0)+1
    letter_items = list(letters_count.items())
    letter_items.sort()

    for value in letter_items:
        print(*value, end="\n")

    print("\n Ctrl+C and Enter to exit!")
