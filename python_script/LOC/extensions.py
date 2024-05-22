import docx
import os

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
