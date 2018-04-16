size_list = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Hiep and these are my sheep sizes: ")
print(size_list, sep=", ")

biggest_sz = max(size_list)
print("Now my biggest sheep has size", biggest_sz, ", let's shear it!")
size_list.remove(biggest_sz)
print("After shearing, here is my flock: ")
print(size_list, sep=", ")

for i in range(3):
    new_list= size_list
    for size in size_list:
        size = size + 50
        new_list.append(size)
    print("One month has passed, now here is my flock: ")
    print(size_list, sep=", ")

total =0
for j in size_list:
    total= total + list[j]
money = total * 2
print("My flock has size in total: ", total)
print("I would get ", total, "* 2$ = ", money)
