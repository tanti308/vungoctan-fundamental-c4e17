
x = int(input("x = "))
op = str(input("Operations (+,-,*,/)"))
y = int(input("y = "))
result = 0
if op == "+":
    result = x+y
    print("******************")
elif op == "-":
    result = x-y
    print("*****************")
elif op == "*":
    result = x*y
    print("*****************")
elif op == "/":
    result = float(x/y)
    print("*****************")
print("{o} {1} {2} = {3}".format(x,op,y,result))
