'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
if 5 > 10:
    print(True)
else:
    print(False)


'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
age = 17

student =True

age < 18
if age <18 or student: # sees if you over or under 18
    price = 10
else:
    price =20

print("Ticket price: $",price) 

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

# List of fruits
box_fruits = ["apple", "banana", "orange", "grape", "mango", "pineapple"]

# let someone enter a fruit name
human = input("Enter the name of a fruit: ").strip().lower()

# Check if the fruit is in the list
if human in box_fruits:
    print("Yes,that fruit is in the list.")
else:
    print("No, that fruit is not in the list.") # Prints a message if the fruit is not in the list



'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

weight= int(input("What is the weight: "))#create variable for weight integer and zone string
zone=str(input("Which zone are you taking: "))
A=5#create varable for zone A and zone B
B=7

if weight <= 0:#creating an error if  the weight is less than or equal to zero
    print("Error")

if zone == "A" or zone == "zone A":#then create if statements for zone a and zone B
    weight * A
    print(weight * A)
elif zone == "B" or zone == "zone B":
    weight * B
    print(weight * B)
else:#create else statement if user does not pick zone A or B
    print("pick a zone")




'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("The triangle is Equilateral.") 
        elif a == b or b == c or a == c:
            print("The triangle is Isosceles.") #dos sides are equal
        else:
            print("The triangle is Scalene.") #sides  different
    else:
        print("Not a triangle.")