from random import randint,choice
import eval

while True:
    x = randint(1,10)
    y = randint(1,10)
    op = choice(["+","-","*","/"])
    result = eval.calc(x,y,op)
    error = choice([-1,0,0,0,1])
    dis_result = result + error

    print("* " * 20)
    print("{0} {1} {2} = {3}".format(x, op, y, dis_result ))
    print("* " * 20)
    answer = str(input("Y / N?  ")).lower()


    if error ==0:
        if answer == "y":
            print("Yay")
        else:
            print("Wrong")
    else:
        if answer == "y":
            print("Wrong")
        else:
            print("Yay")
