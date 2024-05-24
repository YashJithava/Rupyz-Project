def user_input(input1,input2,operator):
        if operator == 1:
            return input1 + input2
        elif operator == 2:
            return input1 - input2
        elif operator == 3:
            return input1 * input2 
        elif operator == 4:
            if input2 == 0:
                return "cannot dib=vide by zero!"
            return input1 / input2
        else:
            return "Entered a invalid input"
#result1 = None
result = float(input("Enter initial input here: "))
while True:
    # if result1 is None:
    input2 = float(input("Enter next input here: "))

     #else:
       #input1 = result1
       #input2 = float(input("Enter another number to operaate with the previous result: "))
    print("Enter 1 for addition")
    print("Enter 2 for subtraction")
    print("Enter 3 for multiplication")
    print("Enter 4 for division")

    operator = int(input("Enter operator here: "))

    result = user_input(result,input2,operator)
    print("result", result)

    continue_choice = input("Do you to Exit? (yes/no):")

    if continue_choice.lower() == "yes":
        break
