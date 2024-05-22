import sys
import os
import docx
import paragraphs

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
        

def search_file(file_name):
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename == file_name:
                return os.path.join(root, filename)
    return False


def lines_of_code_in_python(filepath):
    record = []
    with open(filepath, "r") as file:
        
        for data in file:
            if data.strip() and not data.startswith("#") and not data.startswith("'''") :
                record.append(data)
                
        if not record:
            print("Empty file.")
            return 0 
        for count in range(1, len(record) + 1):
            var = count 
        return var
    
    # -----------------------------------------
    
def lines_of_code_in_txt(filepath):
    record = []
    with open(filepath, "r") as file:
        for data in file:
            if data.strip():
                record.append(data)
                
        if not record:
            print("Empty file.")
            return 0
        for count in range(1, len(record) + 1):
            var = count
        return var
    
    # -----------------------------------------
    
    
def lines_of_code_in_csv(filepath):
    record = []
    with open(filepath, "r") as file:
        for data in file:
            if data.strip():
                record.append(data)
        
        if not record:
            print("Empty file.")
            
        for count in range(1, len(record) + 1):
            var = count
        return var
    
        
def lines_of_code_in_html(filepath):
    record = []
    with open(filepath, "r") as file:
        for data in file:
            if data.strip() and not data.strip().startswith("<!--") and not data.strip().startswith("-->"):
                record.append(data)
        
        if not record:
            print("Empty file.")
            
        for count in range(1, len(record) + 1):
            var = count
        return var
        


def lines_of_code_in_docx(filepath):
    doc = docx.Document(filepath)
    record = []
    for data in doc.paragraphs:
        if data.text.strip():
            record.append(data.text)
        
    if not record:
        print("Emtpy file.")
    for count in range(1,len(record)+1):
        var = count
        
    return var


def main():
    command = input_command()
    if command:
        file_path = search_file(command)
        if file_path:
            print("File Path: ",file_path)
            update_string = file_path[1:]
            sp = update_string.split(".")
            if sp[-1] == "py":
                print("Lines of Code: ",lines_of_code_in_python(file_path))
            elif sp[-1] == "txt":
                print("Total number of Lines: ", lines_of_code_in_txt(file_path))
            elif sp[-1] == "csv":
                print("Total number of Lines: ", lines_of_code_in_csv(file_path))
            elif sp[-1] == "html":
                print("Total number of Lines: ", lines_of_code_in_html(file_path))
            elif sp[-1] == "docx":
                a = lines_of_code_in_docx(file_path)
                print("Total number of Paragraphs: ", a)
                
        else:
            print("NO such file in the operating system. ")

if __name__ == "__main__":  
    main()
