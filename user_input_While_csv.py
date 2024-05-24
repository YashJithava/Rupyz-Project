import csv
def collect_student_info ():
    name = input("Enter Name")
    roll_no = input("Enter Roll_No")
    address  = input("Enter Address")
    pincode = input("Enter Pincode")

    student_dict = {
        "Name" :name,
        "Roll_NO" : roll_no,
        "Address" : address,
        "Pincode" : pincode
    }
    return student_dict

student_list = []

while True:
    student_info = collect_student_info()
    student_list.append(student_info)

    continue_adding = input("Add New student (yes/no):")
    if continue_adding.lower() != "yes":
        break

print("student_information")
for student in student_list:
    print(student)

filename = "User_application1.csv"

fields = {"Name", "Roll_No", "Address", "Pincode"}

with open(filename, mode = 'w') as user_input:
    writer = csv.DictWriter(user_input, fieldnames = fields)
    writer.writeheader()
    writer.writerows(student_list)