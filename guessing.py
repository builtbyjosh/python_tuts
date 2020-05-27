from random import randint 

# find a way to check if user_guess is a number
# create a function for user_guess
# add a guess countdown


# keeps the game going until user decides to stop
next_round = True
while next_round:
    # generate numbers
    computer_guess = randint(1,10)
    user_guess = int(input("Guess a number between 1 and 10: "))
    while user_guess != computer_guess:
        if user_guess > computer_guess:
            print("too high")
            user_guess = int(input("Guess a number: "))
        elif user_guess < computer_guess:
            print("Too Low")
            user_guess = int(input("Guess a number: "))

    print("Congrats! You guessed it!")
    # check to see if user wants to play again
    play_again = input("Would you like to play again? (Y/N)")
    if play_again.lower() == "n":
        next_round = False
    elif play_again.lower() == "y":
        next_round = True
    else:
        # error checking
        print("Invalid Input")
        play_again = input("Would you like to play again? (Y/N)")

