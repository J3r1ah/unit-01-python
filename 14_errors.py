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

try: #put the try and except after def so it can process the functions output as my inputted error
       divide_numbers(10, 0)
except ZeroDivisionError:
              print("Error: You Cannot Divide By Zero")


"""
Example 2: Opening Files
"""

def read_file(filename):
    file = open(filename, 'r')
    contents = file.read()
    print("File contents:", contents)
    file.close()
try:
    read_file("nonexistent.txt") # try and except on the defined function so it can process error 
except FileNotFoundError:
       print("Error: File Not Found")



"""
Example 3: List Items
"""

def get_item(lst, index):
    item = lst[index]
    print("Item:", item)

try:
      my_list = [1, 2, 3]#  function can take from the list and the try can process error from function
      get_item(my_list, 5)
except IndexError:
      print("Error: Index 5 Doesn't Exist")


"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    value = dictionary[key]
    print("Value:", value)

# Example usage:
my_dict = {"a": 1, "b": 2}
try: # try and except over the key error so it can process it
    get_value(my_dict, "c")
except KeyError:
      print("Error: object C Doesn't Exists")


"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file: # adding else and finally so code can run without visible error regardless of error
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        print("File processed")
    finally:
        print("File finished ")

# Example usage:
process_file("example.txt") 
process_file("non-existent-file.txt")# this willl give  a file not found error


   