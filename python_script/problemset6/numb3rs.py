import re
def validateAddress():
    while True:
        try:
            IP = input("IPv4: ").strip()
            return IP
        except TypeError:
            print("Invalid Input: Type Error found\n please input IP in Integers")
    
    
def main():
    Ip = validateAddress()
    if re.search(r"^[0-257]+\.[0-257]+\.[0-257]+\.[0-257]$",Ip):
        print("Valid")
    else:
        print("Invalid")
        
    
if __name__ == "__main__":
    main()