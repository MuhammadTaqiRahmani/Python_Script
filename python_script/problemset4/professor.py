import random

def level(n):
    if n == 1:
        x = random.randint(1,10-1)
        y = random.randint(1,10-1)
        return x , y
    elif n == 2:
        x = random.randint(10,100-1)
        y = random.randint(10,100-1)
        return x , y
    elif n == 3:
        x = random.randint(100,1000-1)
        y = random.randint(100,1000-1)
        return x , y
    
def operation(x,y):
    sum = x + y
    return sum
    
    
def input_level():
    control = True
    while control:
        try:
            n_level = int(input("Level: "))
            return n_level
        except ValueError:
            print("Invalid Input: Please Enter the level in Integers.")
            
            
def answer(equation_solved):
    control = True
    while control:
        try:
            n_answer = int(input(equation_solved))
            return n_answer
        except ValueError:
            print("Invalid Input: Please Enter the answer in Integers.")
    
    
def equation(diff):

    x , y = level(diff)
    op = operation(x,y)
    equation_solved = f"{x} + {y} = "
    return equation_solved, op
    
    
def main():
    total = 10
    obtained = 0
    diff = input_level()
    for i in range(0,10):
        sol_e, actual_result_op = equation(diff)
        your_ans = answer(sol_e)
        if your_ans == actual_result_op:
            obtained = obtained + 1
            print("(+1) ",obtained)
        elif your_ans != actual_result_op:
            obtained = obtained
            print("(0) ",obtained)
        else:
            print("---Error---")
    print("Obtained Marks: ",obtained," out of ",total)
              
    
main()