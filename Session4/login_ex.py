from getpass import *                                                           # break: tac dong vong lap gan nhat
user_name="C4E"
pass_word="codethechange"
wrong_count=0                                                                   #dat bien dem so lan nhap sai
loop=True                                                                       #dat bien loop => loop =False => dung lai.

while loop:
    u=input("User name: ").upper()
    p=getpass("Password: ")
    print("Please type Ctrl+C and then press Enter to exit!")

    if u != user_name:
        print("No such user, please try again!")
        wrong_count+=1
        print("You have", 3-wrong_count, "time(s) left")
    elif p != pass_word:
        print("Wrong password!")
        wrong_count+=1
        print("You have", 3-wrong_count, "time(s) left")
    else:
        print("Welcome!")
        loop=False
    if wrong_count==3:
        print("Go away!")
        loop=False
