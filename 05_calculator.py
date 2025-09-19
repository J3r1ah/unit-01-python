print("Welcome to the Calculatinator-inator 9000!")
print()
print()
print()
print()
# making input variables for the calculator
num1 = float(input("give me a number:") )
print()
print()
num2 = float(input("give me another number"))
print()
print()
operator = (input("select an operator. Options(addition, subtraction, multiplication, division, modulus, exponent, floor):"))
print()
print()
# making variables for the operator input variable 
addition = num1 + num2

subtraction = num1 - num2

multiplication =  num1 * num2

division = num1 / num2

modulus = num1 % num2

exponent = num1 ** num2

floor = num1 // num2

if operator == "addition":# if statement for addition operator
    print(addition)
elif operator == "subtraction":# if statement for subtraction operator
    print(subtraction)
elif operator == "multiplication":# if statement for multiplication operator
    print(multiplication)
elif operator == "division":# if statement for division operator and nested if statement to let the user know they cant divide by 0
    if num2 == 0:
        print("cant divide by the value 0")
    else:
        print(division)
elif operator == "modulus":# if statement for modulus operator 
    print(modulus)
elif operator == "exponent":# if statement for the exponent operator 
    print(exponent)
elif operator == "floor":# if statement for the operator floor
    print(floor)
else:# else to let user know what they typed wasn't a given operator 
    print("that is not an operator " )
    print()
    print()
    print("thanks for using the Calculatinator-inator 9000!")

    
    
    

   
    
 
    
        


    
    





 