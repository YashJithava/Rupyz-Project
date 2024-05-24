import csv
mydict = [{'name':'yash', 'roll_no':'23', 'address':'uttam nagar'},
          {'name':'varun', 'roll_no':'24', 'address':'vikaspuri'},
          {'name':'annant', 'roll_no':'25', 'address':'gurugram'},
          {'name':'vinay', 'roll_no':'26', 'address':'vikaspuri'},
          {'name':'narender', 'roll_no':'27', 'address':'jankpuri'}
]

fields = ["name", "roll_no", "address"]

filename = "dictdata.csv"

with open(filename, mode = 'w') as file:
    csvwriter = csv.DictWriter(file,fieldnames = fields)
    csvwriter.writeheader()
    csvwriter.writerows(mydict)

with open("dictdata.csv", mode='r') as myfile:
    myreader = csv.reader(myfile)
    for lines in myreader:
        print(lines)      