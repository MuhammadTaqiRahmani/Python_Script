from datetime import datetime
import re
    
def month_No(monthOP):
    months = {
    "january":str(1),
    "february":str(2),
    "march":str(3),
    "april":str(4),
    "may":str(5),
    "june":str(6),
    "july":str(7),
    "august":str(8),
    "september":str(9),
    "october":str(10),
    "november":str(11),
    "december":str(12),
    }
    return months.get(monthOP,"Unknown Month")


def input_date():
    control = True
    while control:
        date = input("Enter the Date: ").strip().lower()
        try:
            datetime.strptime(date,"%m/%d/%Y")
            return date
        except ValueError:
            pass
        
        try:    
            datetime.strptime(date,"%B %d, %Y")
            return date
        except ValueError:
            pass
        
        print("Invalid Format: Please enter date in valid format.")
            
            
def format(date):
    pattern = r"^\d{1,2}/\d{1,2}/\d{4}$"
    patternOP = r"^[a-zA-Z]+ \d{1,2}, \d{4}$"
    control = True
    while control:
        try:
            if re.match(pattern, date):
                try:
                    storage = ""
                    components = date.split("/")
                    month = components[0]
                    day = components[1]
                    year = components[2]
                    storage = storage + year
                    storage = storage + "-" + month
                    storage = storage + "-" + day
                    return storage
                except ValueError:
                    print("Invalid Format: Please enter the valid format for date.")
                
            elif re.match(patternOP, date):
                try:
                    storageOP = ""
                    componentsOP = date.split(" ")
                    monthOP = componentsOP[0]
                    dayOP = componentsOP[1]
                    yearOP = componentsOP[2]
                    storageOP = storageOP + yearOP
                    storageOP = storageOP + "-" + month_No(monthOP)
                    
                    storageOP = storageOP + "-" + dayOP
                    return storageOP
                except ValueError:
                    print("Invalid Format: Please enter the valid format for date.")
            else:
                raise ValueError("Invalid Format: Please enter the valid format for date.")
        except ValueError as ve:
            print(ve)
            
     
    
def main():
    date_format =input_date()
    datef = format(date_format)
    print(datef)
    
    
if __name__ == "__main__":
    main()