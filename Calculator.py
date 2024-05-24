input1 = float(input("Enter input here: "))
input2 = float(input("Enter 2nd input here: "))

print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

select = int(input("Enter your operation no here: "))

if select == 1:
    print(input1 + input2)
elif select == 2:
    print(input1 - input2)
elif select == 3:
    print(input1 * input2)
elif select == 4:
    print(input1 / input2)


