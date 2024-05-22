import sys

def input_command():
    try:
        if len(sys.argv) == 2:
            try:
                c_input = sys.argv[1]
                command = c_input
                format = "xxx.yy"
                dot = "."
                if dot in c_input:
                    x, y = c_input.split(".")
                    if y.isalpha() and y.lower() == "py":
                        return command.strip()  
                    
                    elif y.isalpha() and y.lower() == "txt":
                        return command.strip()
                    
                    elif y.isalpha() and y.lower() == "csv":
                        return command.strip()
                    
                    elif y.isalpha() and y.lower() == "html":
                        return command.strip()
                    
                    elif y.isalpha() and y.lower() == "docx":
                        return command.strip()
                    
                    elif y.isalpha():
                        print("Did not recognize the file.")
                        sys.exit()
                    else:
                        print(f"--Invalid Command--\nInput the string in {format} format.")
                        sys.exit()
                elif c_input.isalpha():
                    print("Not a Python file")
                    sys.exit()
                else:
                    raise ValueError(f"--Invalid Command--\nInput the string in {format} format.")
            except ValueError as ve:
                print(ve)
                sys.exit()
        elif len(sys.argv) == 1:
            print("Too few command-line arguments ")
            sys.exit()
        elif len(sys.argv) > 2:
            print("Too many command-line arguments ")
            sys.exit()
        else:
            raise ValueError(f"--Invalid Command--\nInput the string in {format} format.")
    except ValueError as ve:
        print(ve)
        sys.exit()