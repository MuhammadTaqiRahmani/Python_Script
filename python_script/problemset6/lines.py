import sys
import os

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
                    elif y.isalpha():
                        print("Not a Python file")
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
        
    
        


def search_file(file_name):
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename == file_name:
                return os.path.join(root, filename)
    return False


def lines_of_code(filepath):
    record = []
    with open(filepath, "r") as file:
        
        for data in file:
            if data.strip() and not data.startswith("#"):
                record.append(data)
                
        if not record:
            print("Empty file.")
            return 0 
        for count in range(1, len(record) + 1):
            var = count 
        return var
    
            
def main():
    command = input_command()
    if command:
        file_path = search_file(command)
        if file_path:
            print("File Path: ",file_path)
            print("Lines of Code: ",lines_of_code(file_path))
            
        else:
            print("NO such file in the operating system. ")

if __name__ == "__main__":  
    main()
