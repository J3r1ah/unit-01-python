import random
from random import randint

def guessing_game():
    random_number = random.randint(1, 100)
    print("welcome to guess the random number game!")
    print("i have 4 numbers 1 to 100 you have 4 guesses (emphasis on THE 4!)")
    
    for i in range(1, 5): 
        try:
            # player inputs their guessss
            user_guess = int(input(f"Guess Now (Attempt {i}): ")) 
        except ValueError:
            print("YOU GOT IT WRONG IDIOT YOU NEED A WHOLE NUMBER YA BUM!")
            continue # Skip to the next if wrong

        
        if user_guess == random_number:
            print(f"Congratulations! You guessed it in {i} attempts.")
            return # Leaves   if the guess is correct
        elif user_guess < random_number:#if the users guess is smaller than  random number then no no nuh uh
            print("ITS 1 TO 100 NOT 0 TO 0 IDIOT IF YOU CANT COUNT DONT PLAY!")
        else: # if the users guess is bigger than  random number then no no nuh uh
            print("ITS 1 TO 100 NOT 1 TO 1,000,000 IDIOT IF YOU CANT COUNT DONT PLAY!")

    # If the loop finisH no more guesses
    print("YA DONE NOW SCRAM!")
    print(f"THE RIGHT NUMBER WAS {random_number}. MAN YOUR STUPID.")



    
   








