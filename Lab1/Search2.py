nums = [1,2,3,4,5,6,7,8,9,10]

x = int(input("Enter an integer: "))
# must not use count() or in or index()
found= False

for num in nums:
    if num ==x:
        print("Found")
        break
else:                               #gap not found lien tuc thi tab else ra ngoai
    print("Not found")
# if found:
#     print("Found")
# else:
#     print("Not found")
