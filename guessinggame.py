import random
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

guess(10)