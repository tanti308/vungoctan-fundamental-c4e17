from getpass import getpass
while True:                                 #Vong lap chay mai mai, user phai nhap Ctrl+C ; dung break de dung khi nhap dung
    print("Welcome to the superuser gateway!")

    user_name= input(("User name: "))
    pass_word= getpass("Password: ")

    if user_name != "C4E":                  #thay = != k hop le trc
        print("No such user!")
    else:
        if pass_word != "codethechange":
            print("Login failed")
        else:
            print("Welcome!")
            break
