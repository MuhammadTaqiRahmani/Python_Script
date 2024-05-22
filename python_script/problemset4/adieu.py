import sys

def main():
    if len(sys.argv) == 1:
        storage = ""
        namesf = ""
        while True:
            name = input("Name: ")
            namesfff = namesf + " , " + name
            namesf = namesf +" , "+ name
            
            
            if name == "d":
                break
            else:
                alpha = sys.argv[0].capitalize()
                storage = alpha + ", " +  sys.argv[0] + " to " + namesfff[2:]
                
        storage = storage.rsplit(",", 1)
        storage = " and".join(storage)
        print(storage)
    else:
        print("Error")
        
        
main()
        