print()
print("===================================")
print()
print("problem 2")
print()

text = "Hello, world, my name is"
count = 0

for char in text:
    if char == " ":
       count += 1

print(count)

print("give me a number")
n = input()

print()
print("===================================")
print()
print("problem 2")
print()

print("give me a number")
n = int(input())

for num in range(1, n):
    if num % 2 < 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")



print()
print("===================================")
print()
print("problem 3")
print()



num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
else:
  result = 1
  for i in range(1, num+1):
    result *= i   

  print("Factorial of " , num , "is" , result)



print()
print("===================================")
print()
print("problem 3")
print()






attempts = 0
correct_password = "secret"

while True:
    password = input("Enter your password: ")
    attempts += 1

    if password == "incorrect_password":
        print("Correct password!")
    else:
        print("Incorrect password")

    if attempts == 3:
        print("Too many attempts")
        break