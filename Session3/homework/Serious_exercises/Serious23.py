list = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is Tan and these are my sheep sizes: ")
print(list, sep=", ")

bigsz = max(list)
print("Now my biggest sheep has size", bigsz, ", let's shear it!")
index = list.index(bigsz)
list[index]= 8
print("After shearing, here is my flock: ")
print(list, sep=", ")
