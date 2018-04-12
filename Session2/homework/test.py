x= int(input("Enter a number, pls?"))
def print_square_root(x):
    if x <=0:
        print ("Positive number only, please.")
        return

    result = x**0.5
    print ("The square root of", x, "is", result)
