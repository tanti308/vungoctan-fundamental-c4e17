from random import randint,choice

# Define function
def calc(x,y,op):
    result =0
    if op == "+":
        result = x+y
    elif op == "-":
        result = x-y
    elif op == "*":
        result = x*y
    elif op == "/":
        result = float(x/y)
    return result #day result ra khoi scope cua function
print(__name__) # __name__ ten file

# chi khi file chay truc tiep name == main => in ra eval.py...
# file chay gian tiep (import) => k chay cac function trong file
if __name__ == "__main__":
    print('eval.py imported')

# Call function
