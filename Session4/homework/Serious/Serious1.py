numbers = [1,6,8,1,2,1,5,6]
loop=True

while loop:
    # With count() function:
    n = int(input("Enter a number: "))
    print("Type Ctrl+C Enter to exit!")
    if n not in numbers:
        print("No such number, try again!")
    else:
        count= numbers.count(n)
        print(n,"appears", count,"times in my list")

        # Without count() function:
        without_count=0
        for i in range(len(numbers)):
            if numbers[i] == n:
                without_count+=1
        print(n, "appears", without_count, "times in my list")
        
