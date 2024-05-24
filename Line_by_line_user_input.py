import csv
def get_user_data():
    return {"name" : input("Enter Name here: "),
            "roll_no." : input("Enter Roll_No. here: "),
            "address" : input("Enter Address here: "),
            "pincode" : input("Enter Pincode here: ")
    }
filename = "annant_Line_by_line_input.csv"

fields = ["name", "roll_no.", "address", "pincode"]

while True:
    with open(filename , mode = 'a', newline="") as user_input:
        writer = csv.DictWriter(user_input, fieldnames=fields)
        # writer.writeheader()
        writer.writerow(get_user_data())

    continue_adding  = input("Add New student (yes/no): ").lower()
    if continue_adding == "no":
        break
