student_list = []
while True:
    student_dict = {
                    "Name" : input("name"),
                    "Roll_No" : input("roll_no"),
                    "Address" : input("address"),
                    "Pincode" : input("pincode")
    }
    student_list.append(student_dict)
 
    
    continue_adding = input("if you want to exit (yes/no):")
    if continue_adding == "yes":
        break

    check_list = input("if you want to check list (yes/no):")
    if check_list == "yes":
        print(student_list)
 