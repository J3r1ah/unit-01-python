import os 
import sys 



"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""

current_dir = os.getcwd()
print("the current directory", current_dir)





"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""

os.makedirs('test folder', exist_ok=True)
list = os.listdir('.')

print("files and directory")
for list in list:
    print(list)

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""

print("---task3---")
print()
print()

if os.path.isdir("data"):
    print("The folder data exists.")
else:
    print("The folder data does not exist.")
    os.mkdir("data")

"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""

print("---task4---")
print()
print()

config_file = "config.txt"
if os.path.isfile(config_file):
    print(f"File found: {os.path.abspath(config_file)}")
else:
    print("File not found.")


"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""

print("---task5---")
print()
print()

print("Python version:")
print(sys.version)

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""

print("---task6---")
print()
print()

platform = sys.platform
if platform.startswith("linux"):
    print("Platform: Linux")
elif platform == "win32":
    print("Platform: Windows")
elif platform == "darwin":
    print("Platform: MacOS")
else:
    print(f"Platform: Unknown ({platform})")


