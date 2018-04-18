# menu = ['pho','com rang', 'my xao']
# print(menu)
# #Create
# menu.append('hu tieu')
# print("After append()")
# print(*menu, sep=", ")
#
# print(menu[0])

# #for i
# for i in range(len(menu)):
#     print(menu[i])

# #for each
# for item in menu:
#     print(item)

#string format
name="Tan"
age =22
status="Single"
address="TX"
message='''{0},
{1} tuoi,
tinh trang quan he: {2},
song o: {3}'''.format(name, age, status, address)
print(message)
#for enum (pho bien nhat)
# for i,item in enumerate(menu):
#     message="{0}. {1}".format(i+1,item)
#     print(message)
