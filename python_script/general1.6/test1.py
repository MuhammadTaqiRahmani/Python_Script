def main():
    number = get_number()
    repeat(number)

def get_number():
    while True:
        n = int(input("Enter a number:: " ))
        if n > 0:
            break
    return n
    
    
def repeat(n):
    message = input("")
    for i in range(n-1):
        print(message)
        
        
main()