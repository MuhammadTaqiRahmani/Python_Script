from inputCommand import input_command
from extensions import search_file, lines_of_code_in_python, lines_of_code_in_csv,lines_of_code_in_docx,lines_of_code_in_html,lines_of_code_in_txt

def execute():
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
            print("No such file exist in the operating system. ")
