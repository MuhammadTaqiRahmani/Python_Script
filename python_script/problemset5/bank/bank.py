

def Greeting(greeting):
    amount=0
    if greeting.lower().startswith("hello"):
        x = amount
        return x
    elif greeting.lower().startswith("h"):
        y = amount+20
        return y
    else:
        z = amount+100
        return z
        
def main():
    greeting = input("Greeting: ").strip()
    result = Greeting(greeting)
    print(result,"$")        
    
    
if __name__ == "__main__":
    main()

    
# def Greeting(greeting):
#     amount=0
#     if greeting.lower().startswith("hello"):
#         x = amount,"$"
#         return x
#     elif greeting.lower().startswith("h"):
#         y = amount+20, "$"
#         return y
#     else:
#         z = amount+100, "$"
#         return z
        
# def main():
#     greeting = input("Greeting: ").strip()
#     print(Greeting(greeting))
        
# if __name__ == "__main__":
#     main()

