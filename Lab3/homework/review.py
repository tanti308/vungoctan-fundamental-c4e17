•	Why should we use functions at all?
    to help us organize programs into chunks that match how we think about the problem

•	How to define/declare a function?
    def NAME( PARAMETERS ):
        STATEMENTS
    1. A header line: begins with a keyword, ends with a colon.
    2. A body consisting of one or more Python statements, each indented the same amount —
    1 Tab = 4 spaces — from the header line.

•	How to call/use a function?
    # from turtle import *
    # def draw_square(sz):
    #     for i in range(4):
    #         forward(sz)
    #         left(90)
    draw_square(100)

•	What is return, why and how do we use it?
    return values that can be used to build more complex expressions, to compute a value
    def calc(x, y, op):
        if op == "+":
            return x + y

•	Do we have to use return in every function?
    Not at all
    Ex: draw_square() is not a function that returns value
    we wrote draw_square() because we wanted it to execute a sequence of steps that caused the
    turtle to draw, not to compute a value

•	What are function arguments/parameters, why and how we use it?
    arguments: provide for generalization
    parameters: inside the arguments of the function, the values that are passed get
    assigned to variables
    Ex:
    arguments: def draw_square(length,color):
    parameters: length, color

•	How to use function from a different file other than our currently working file?
    from eval import calc
