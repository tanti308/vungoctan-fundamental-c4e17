#1
# text ="Overnight"
# print(text)
# characters = list(text)         #chia tu re tung phan tu nho nhat => chu cai
# print(characters)               #chuyen text => list

#2
from random import choice       #chon ngau nhien phan tu trong 1 list
list=[1,5,8,9]
for i in range(len(list)):
    print(choice(list), sep=" ")             #go xong phai xoa ki tu do di khoi pool
    list.pop(i)
