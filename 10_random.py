import random


"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""


for roll in range(1, 10):
    result_of_dice = random.randint(1,6)
    print("roll", roll + 1 , result_of_dice)


"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""

for number in range(5):
    random_float = random.randint(10,20)
    print("float", number + 1.1 , random_float)


for number in range



"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
print("----task3-----")
print()
print()

bobby_colors = ["red", "blue", "green", "yellow", "purple"]
for _ in range(3):
    print(random.choice(bobby_colors))



"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""

print("----task4-----")
print()
print()

numbers = list(range(1, 11))
random.shuffle(numbers)
print("Shuffled numbers:", numbers)



    
    
   
    

