import random

num_guess = 0
x = random.randrange(0,101)
guess=-1
while(guess!=x):
    guess=input("Guess a number!!!")
    guess = int(guess)

    if(guess<x):
        print("Higher")
        num_guess += 1
    if(guess>x):
        print("Lower")
        
        num_guess += 1

    if(guess==x):
        print("You're right!")
        print( "It took you" , num_guess , "guesses.")




