# students = [
#     {"Name": "Taqi","Rollno": "283","Section": "F"},
#     {"Name": "Rashid","Rollno": "298","Section": "F"},
#     {"Name": "Hamza","Rollno": "270","Section": "F"}
# ]

# for i in range(len(students)):
#     print(i+1, students[i]["Name"]["Rollno"]["Section"])
    
    
    
# students = [
#     {"Name": "Taqi","Rollno": "283","Section": "F"},
#     {"Name": "Rashid","Rollno": "298","Section": "F"},
#     {"Name": "Hamza","Rollno": "270","Section": "F"}
# ]
# print("Name\tRoll No\tSection")
# for index, i in students:
#     print(f"{i["Name"]}\t{i["Rollno"]}\t{i["Section"]}")



# students = [
#     {"Name": "Taqi","Rollno": "283","Section": "F"},
#     {"Name": "Rashid","Rollno": "298","Section": "F"},
#     {"Name": "Hamza","Rollno": "270","Section": "F"},
#     {"Name": "Arqum","Rollno": "283","Section": "F"},
#     {"Name": "Ibad","Rollno": "298","Section": "F"},
#     {"Name": "Umer","Rollno": "270","Section": "F"},
#     {"Name": "Subhan","Rollno": "283","Section": "F"},
#     {"Name": "Saad","Rollno": "298","Section": "F"},
#     {"Name": "Imran","Rollno": "270","Section": "F"},
#     {"Name": "Hanzala","Rollno": "283","Section": "F"},
#     {"Name": "Zeeshan","Rollno": "298","Section": "F"},
#     {"Name": "Furqan","Rollno": "270","Section": "F"}
# ]
# print("No\tName\tRollNo\tSection")
# for index, i in enumerate(students, start=1):
#     print(f"{index}\t{i["Name"]}\t{i["Rollno"]}\t{i["Section"]}")




# control=True
# while control:
#     students = []
#     try:
#         while True:
#             decision = int(input("Press 1 to Add Details / Press 0 to exit / Press 9 to show Data : "))
#             if decision == 1:
#                 name = input("Enter your Name: " )
#                 rollno = int(input("Enter your Roll No: " ))
#                 per_rollno = rollno
#                 section = input("Enter your Section: " )
#                 studentID = {"Name":name, "RollNo":per_rollno, "Section":section}
#                 print("\n")
#                 students.append(studentID)
            
#             elif decision == 9:   
#                 print("No\tName\tRollNo\tSection")
#                 for index, i in enumerate(students, start=1):
#                     print(f"{index}\t{i["Name"]}\t{i["RollNo"]}\t{i["Section"]}")
                    
#             elif decision == 0:
#                 print("Exit")
#                 control=False
#                 break
            
            

#     except ValueError:
#         print("Error: Incorrect Datatype\nPlease Enter Valid Data")
        
        
        
control = True
students = []

while control:
    try:
        decision = int(input("Press 1 to Add Details / Press 0 to exit / Press 9 to show Data : "))
        if decision == 1:
            name = input("Enter your Name: ")
            rollno = int(input("Enter your Roll No: "))
            section = input("Enter your Section: ")
            studentID = {"Name": name, "RollNo": rollno, "Section": section}
            students.append(studentID)

        elif decision == 9:
            print("No\tName\tRollNo\tSection")
            for index, i in enumerate(students, start=1):
                print(f"{index}\t{i['Name']}\t{i['RollNo']}\t{i['Section']}")

        elif decision == 0:
            print("Exit")
            control = False
            break

    except ValueError:
        print("Error: Incorrect Datatype\nPlease Enter Valid Data")


