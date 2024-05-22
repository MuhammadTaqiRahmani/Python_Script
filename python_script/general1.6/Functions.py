def main():
    x = int(input("Enter Value of x: "))
    if even(x):
        print("Even")
    else:
        print("Odd")
        
def even(value):
    return value % 2 == 0

main()
    