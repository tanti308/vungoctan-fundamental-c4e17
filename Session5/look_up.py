trans ={
"ns": "noi",
"r": "roi",
"pt": "phat trien",
"stt": "so thu tu",
"lm": "lam",
"ngta": "nguoi ta",
"ys": "dang^''",
}
while True:
    for i in trans:             #in key or value: print(trans.values()) 
        print(i, end=" ")
    print("\n********************************")
    ques = str(input("Your code: ")).lower()

    if ques in trans:
        print(trans[ques])
    else:
        print(ques, "is not in this dictionary!")
    print("\nType Ctrl+C and Enter to exit!\n")
    #update
    update = str(input("Do you want to add any word into this dictionary? (Y/N)")).lower()
    if update == "y":
        ques = str(input("Your code: ")).lower()
        trans_value = str(input("Meaning: ")).lower()
        trans[ques]=trans_value
