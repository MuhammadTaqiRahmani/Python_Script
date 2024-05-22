control=True
while control:
    students = []
    try:
        while True:
            decision = int(input("Press 1 to Add Details / Press 0 to exit / Press 9 to show Data : "))
            if decision == 1:
                name = input("Enter your Name: " )
                rollno = int(input("Enter your Roll No: " ))
                per_rollno = rollno
                section = input("Enter your Section: " )
                studentID = {"Name":name, "RollNo":per_rollno, "Section":section}
                print("\n")
                students.append(studentID)
            
            elif decision == 9:   
                print("No\tName\tRollNo\tSection")
                for index, i in enumerate(students, start=1):
                    print(f"{index}\t{i["Name"]}\t{i["RollNo"]}\t{i["Section"]}")
                    
            elif decision == 0:
                print("Exit")
                control=False
                break
            
            

    except ValueError:
        print("Error: Incorrect Datatype\nPlease Enter Valid Data")