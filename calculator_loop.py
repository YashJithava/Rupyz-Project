def user_input(input1,input2,operator):
        if operator == 1:
            return input1 + input2
        elif operator == 2:
            return input1 - input2
        elif operator == 3:
            return input1 * input2 
        elif operator == 4:
            if input2 == 0:
                 return "cannot divide by zero"
            return input1 / input2
        else:
            return "Entered a invalid input"

while True:
     input1 = float(input("Enter input here: "))
     input2 = float(input("Enter 2nd input here: "))
     print("Enter 1 for addition")
     print("Enter 2 for subtraction")
     print("Enter 3 for multiplication")
     print("Enter 4 for division")

     operator = int(input("Enter operator here: "))

     result = user_input(input1,input2,operator)
     print("result=", result)

     continue_choice = int(input("Do you to Exit? (0/1):"))

     if continue_choice == "0":
        break

