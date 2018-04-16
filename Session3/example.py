# name1= "Canh"                         CRUD create read update delete
# name2= "Hieu"
# name3= "Duc Anh"
# name4= "Nguyen"
# name5= "Don"
# Dung bien list de them sua xoa danh sach vo han +

#READ:
# 1. Bien the 1 cua list
# names = []
# print(names)
# print(type(names))

# 2. Bien the 2
# names = ["Canh"]
# print(names)

# 3. Bien the 3 (hay gap)
names= ["Canh", "Hieu", "Duc Anh", "Don"]
# print(names)
# # Create
# names.append("Nguyen")
# print(names)

#UPDATE
# new_name= "Don"
# names.append(new_name)
# print(names)
# names= ['teaching', 'netflix', 'deathnote']
# print("Hi there, here you favourite things so far", *names, sep=", ") #sep: separator: dau cach ; *names: in tung phan tu
# new_name= str(input("Name one thing you want to add?"))
#
# names.append(new_name)
#
# print(*names, sep=", ")
# x=4                         #names[]: nhu 1 bien
# print(x)
# print(names[1])             #in ra chi phan tu cua list => so am: dao lai thu tu 1 lan
# print(len(names))           # len=length
# for i in range(len(names)): #vong lap for i
#     print(names[i])         # in ra tat ca phan tu xuong dong
#
# for i in range(len(names)):
#     print(i+1, ".", names[i])                          # Vong lap FOR EACH

no=1
for n in names:
    # print(no,'. ', n, sep='')
    message ="{0}. {1}".format(no, n)       #message: gon. hon => string format:dinh dang in bien
    print(message)
    no= no+1    # == n0+=1
