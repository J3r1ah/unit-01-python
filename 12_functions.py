"""
Task 1: Greeting
Write a function that takes a name as a 
argument and prints a greeting message like "Hello, [name]!".
"""
def greeting(name, haio="Yo!"):
    """ this function  registers name as the variable haio i made 
     which then is printed plus the input for the name 
     """
    print( haio + " " + name )

("Chef", "Y0 Y0!")#i use the function and give an argument to overwrite the main haio or greeting

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def square(a, b):
    """defining sqaure as a and b so i can use that function to return a n
    umber when function is used then make a variable 
    so i can use square to return its root"""
    return a ** b

x = square(7,8)
print(x)







"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
def is_even_odd(number):
    """"""
    return number % 2==0
print(is_even_odd(4))

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

def adding(a,b,):
    """"""
    return a *b
x = adding(4,10)
print("length = 4")
print("width = 10")
print("area =",x)
"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def resistank(celius):
    """"""
    return celius * 4 + 50
print(resistank(10))

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""

def ave(numbers):
    """"""
    return sum(numbers) / len(numbers)

print(ave([1, 2, 3]))


"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""