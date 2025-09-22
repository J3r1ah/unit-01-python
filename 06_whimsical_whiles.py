"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

print()
print()

i = 1 # i variable is equal to 1

while i < 11: # condition if the i variable remains less than 11 it will continue the loop
    print(i)
    i += 1 # this is so the loop gradually goes up by one 

print()
print()

 
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print()
print()

# same as exercise 1 but backwards

i = 10 # instead of 1 its 10 because we want to count down not up

while i > 0:
    print(i)
    i -= 1 # this is so we count down


print()
print()

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""


number = int(input("give me a number please:"))# input variable for number 
result = 1 #result variable 

while number > 0: # while loop so result variable is relative to number input 
    result = number * result
    number -= 1

print(result) # print for the factorial calculated result



"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""




