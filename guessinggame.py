import random
from re import L
#imported random to get functions

#We define a function that we have created.
def guess(x):
    random_number = random.randint(1, x) 
    """We use this to get a random integer by calling the function random.randint()."""
    
    guess = 0
    
    """guess variable has been created to equal zero as we are looking for numbers above 1."""

    """Inserted a while loop that will go on as long as the user does not get the correct number."""
    
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too Low!')
        elif guess > random_number:
            print('Sorry, guess again. Too High!')
        
        """We do not use the else variable as the while loop will stop once the condition is met, making an else
        statement unnecessary."""

    print(f'Yay, congrats. You have guessed the number {random_number}!')

"""The 10 that has been inputed corresposds with the x variable that we are using to 
define the range between the numbers that we want the user to guess. If the 10 was swtiched to 100,
the user will have to guess between 1 and 100. For now we have set the range to 10."""
#guess(10)

#Here is a program that will have the Computer guess the number between the ranges of 1 and x.
def computer_guess(x):
    low = 1
    high = x
#low and high are the varitables we will be using.
    feedback = ''
#feedback is what the computer will get back from the user. We set it to an empty string for now.
    while feedback != 'c': 
    #We use a while loop that goes on until the user types in "c" that will indicate the guess is correct.
        if low != high: #If low and high aren't equal, the computer will generate a number between the two.
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower() #Added .lower() make the input lowercase,
        #feedback is the string of three choices (h,l,c) that will dictate the next condition set.
        if feedback == 'h': #If feedback is too high, the computer will guess 1 less with a new number.
            high = guess - 1
        elif feedback == 'l': #If feedback is too low, the computer will guess one higher with a new number.
            low = guess + 1
    
    print(f'Yay! The computer has guessed your number, {guess}, correctly!')

computer_guess(10)

