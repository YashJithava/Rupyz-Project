def collect_student_info ():
    name = input("Enter Name")
    roll_no = input("Enter Roll_No")
    address  = input("Enter Address")
    pincode = input("Enter Pincode")

    student_dict = {
        "Name" :"name",
        "Roll_NO" : "roll_no",
        "Address" : "address",
        "Pincode" : "Pincode"
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