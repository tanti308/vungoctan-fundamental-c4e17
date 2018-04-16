list = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Tan and these are my sheep sizes: ")
print(list, sep=", ")

while True:
    m=int(input("Enter number of month: "))
    for i in range(3):
        print("MONTH", i+1, ": ")
        for j in range(7):
            list[j] = list[j] + 50
        print("One month has passed, now here is my flock: ")
        print(list, sep=", ")

        bigsz = max(list)
        print("Now my biggest sheep has size", bigsz, ", let's shear it!")
        index = list.index(bigsz)
        list[index]= 8
        print("After shearing, here is my flock: ")
        print(list, sep=", ")
        print("Please type Ctrl+C and then press Enter if you want to exit!")

    total =0
    for j in range(len(list)):
        total= total + list[j]
    money = total * 2
    print("My flock has size in total: ", total)
    print("I would get ", total, "* 2$ = ", money)
