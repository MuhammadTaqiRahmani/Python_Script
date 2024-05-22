def main():
    name = input("Enter your name: ")
    match name:
        case "Taqi" | "Taqi Rahmani":
            print("son of Tariq Raza")
        case "Naqi" | "Naqi Rahmani":
            print("son of Tariq Raza")
        case "Tariq":
            print("Head of family")
        case _:
            print("Sorry,")
            
            
main()