def error_16ve():
    while True:
        try:
            operation = input("Operation: ").strip().lower()
            if operation in ["add", "addition", "sub", "subtraction", "mul", "multiplication", "div", "division"]:
                return operation
            else:
                raise ValueError("---Value Error (E-16VE): Invalid Operation---\nPlease Enter a valid operation (add, subtract, multiply, divide).")
        except ValueError as ve0:
            print(ve0)
            
def error_23ve():
    while True:
        try:
            op1 = float(input("Operand 1: "))
            op2 = float(input("Operand 2: "))
            return op1,op2
        
        except ValueError :
            print("---Value Error (E-23VE): Invalid Input---\nPlease Enter numeric values for operands.")
            

def add(op1,op2):
    result = op1 + op2
    return result
def sub(op1,op2):
    result = op1-op2
    return result
def mul(op1,op2):
    result = op1*op2
    return result
def div(op1,op2):
    while True:
        try:
            result = op1/op2
            return result
        except ZeroDivisionError:
            print("--- Zero Division Error (E-54ZD) ---\nCannot divide by zero. Please enter a non-zero value for the second operand.")
            op1, op2 = error_23ve()
            

def main(x):
    op1,op2 = error_23ve()
    if x=="add" or x=="addition":
        print("Result: ",add(op1,op2))
    elif x=="sub" or x=="subtraction":
        print("Result: ",sub(op1,op2))
    elif x=="mul" or x=="multiplication":
        print("Result: ",mul(op1,op2))
    elif x=="div" or x=="division":
        print("Result: ",div(op1,op2))
        
main(error_16ve())
