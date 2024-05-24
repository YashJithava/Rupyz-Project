import csv
def collect_student_info ():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll_No: ")
    address  = input("Enter Address: ")
    pincode = input("Enter Pincode: ")

    student_dict = {
        "Name" : name,
        "Roll_No" : roll_no,
        "Address" : address,
        "Pincode" : pincode
        }
    
    return student_dict

student_list = []

while True:
    student_info = collect_student_info()
    student_list.append(student_info)

    print(student_list)
    #for student in student_list:
        #print(student)
    
    continue_adding = input("Add New student (yes/no):")
    if continue_adding.lower() == "no":
        break

print("student_information")
for student in student_list:
    print(student)

filename = "User_application.csv"

fields = ["Name", "Roll_No", "Address", "Pincode"]

with open(filename, mode = 'w', newline='') as user_input:
    writer = csv.DictWriter(user_input, fieldnames= fields)
    writer.writeheader()
    for entry in student_list:
        writer.writerow(entry)

    #writer.writerows(student_list)


"""with open(filename, 'w') as user_input:
    writter = csv.writer(user_input)
    writter.writerow(fields)
    for entry in student_list:
        writter.writerow(entry)
    #writter.writerows(student_list)"""

