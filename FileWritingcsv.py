import csv
fields = ["Name", "Roll_no", "Address","Pincode"]

rows = [["Yash", "23", "Uttam Nagar", "110011"],
        ["Varun", "24", "Om Vihar", "110012"],
        ["Annant","25", "Gurugram", "110025"],
        ["Vinay", "26", "Noida", "110026"],
        ["Narender", "27", "Janakpuri", "110017"]]

filename = "datafile.csv"
with open(filename, mode='w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
with open(filename, mode='r') as file:
    myfile = csv.reader(file)
    for lines in myfile:
        print(lines)    