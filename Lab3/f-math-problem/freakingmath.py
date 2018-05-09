from random import *
from random import randint,choice

op = choice(["+","-","*","/"])
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
    return result


def generate_quiz(x,y,op,result):
    result =0
    if op == "+":
        result = x+y
    elif op == "-":
        result = x-y
    elif op == "*":
        result = x*y
    elif op == "/":
        result = float(x/y)
    # Hint: Return [x, y, op, dis_result]
    return [x,y,op, dis_result]

    # user_choice: True, False
    # if elif
def check_answer(x, y, op, dis_result, user_choice):
    result = calc(x, y, op)
    if result == dis_result:
        if user_choice == True:
            return True
        else:
            return False
    elif result != dis_result:
        if user_choice == True:
            return False
        else:
            return True
