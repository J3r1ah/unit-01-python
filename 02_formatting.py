# I made a mango password so it can right password 
password = "mangos123"


u_input = input("put your password: ")#made a input password 


if u_input.upper() == password.upper():
    print("its your password!.")
else:
    print("This ain't yo account!.")
    

#Task 2 
b_input = input("Enter now!: ")

if b_input == "":
    print("nope")
else:
    print("yup")


    #Task 3:

name= input("What you like to eat? Cat or Dog?:")
#i ask the input question
new_name = name.lower().replace("cat", "dog")
#whatever is put is replaced 
print(new_name)





    #task 4:

name = input("Enter yo name: ")#add inputs
age = input("Enter yo age gang: ")

print("YO Name:", name)#print inputs
print("Yo Age:", age)


#Task 5:
num1 = float(input("Enter yo float: "))
num2 = float(input("Enter another float: "))

if num2 != 0:
    quotient = round(num1 / num2, 1)  # Round to 1 decimal place
    print("Quotient (rounded to 1 decimal):", quotient)
else:
    print(" YO you cant divide by zero idiot.")









