# # # # person =["Quan",40, "single","Hanoi",2,11]
# # # # Dictionary: giai quyet bai toan lam viec nhom khi list chi bieu dien cac phan tu = 1 truong duy nhat
# # # person = {}
# # # print(person)
# #
# # person={
# # "name": "Quan"
# # }
# # print(person)
#
person = {                      #{ Key (luon o dang str): Value (all type)}
"name": "Quan",
"age": 40,
"home": "Ha Noi"
}
print(*person.keys())        #in ra tat ca cac key
print(*person.values())      #in ra tat ca cac value
for key, value in person.items():       #in ra cac cap key: value
    print(key, ": ", value, sep="")
#Update:
person["age"]=22            #key ton tai r, thay gia tri

#Create:
person["home"]="Ha Noi"     #them key + value

#Delete:
del person["age"]
# print(person["age"])
# person["age"]=22
# print(person["age"])
# # Cach check phan tu co/khong o trong dictionary
# if "home" in person:    # dung voi ca list, str
#     print(person["home"])
# else:
#     print("'home' is not in person!")
