#pythonic
list_num = [1,2,3,4,5,6,7]
loop= True
while loop:
    x= int(input("Nhap so nguyen de kiem tra co trong danh sach hay k? "))

    # if x in list_num:
    #     print(x, " nam trong danh sach")
    # else:
    #     print(x, " khong nam trong danh sach")
    # print("An Ctrl+C Enter de thoat!")

    c= list_num.count(x)
    if c >= 1:
        print("Found in list")
    else:
        print("Not found in list")
