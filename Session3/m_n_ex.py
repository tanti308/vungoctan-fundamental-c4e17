m = int(input("Enter number of columns? "))
n= int(input("Enter number of rows?"))

a=str("*")                              #print(end="\n"): xuong dong`
b=str(" ")

for i in range(n):                      # Tim quy luat cua ma tran, dung 2 toa do x,y de kiem tra quy luat
    for j in range(m):
        if (i+j) % 2 ==0:               #sum=i+j => if sum %2 !=0
            print(a, end=" ")
        else:
            print(b, end=" ")
    print()
