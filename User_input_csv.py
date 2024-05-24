import csv
def get_student_data():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No.: ")
    address = input("Enter Address: ")
    pincode = input("Enter pincode: ")

    return{"Name" : name,
           "Roll_No" : roll_no,
           "Address" : address,
           "Pincode" : pincode
    } 

student_list = []

for index in range(10):
    student_list.append(get_student_data())

    if input("if you want to exit (yes/no):") == "yes":
        break

    if input("if you want to check list (yes/no): ") == "yes":
        print(student_list)

filename = "User_input"

fields = {"Name", "Roll_No", "Address", "Pincode"}

with open(filename, mode = 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(student_list)