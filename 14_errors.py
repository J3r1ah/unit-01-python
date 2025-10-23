"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    result = num1 / num2
    print("Result:", result)

try:
       divide_numbers(10, 0)
except ZeroDivisionError:
              print("error: You cannot divide by zero")



   