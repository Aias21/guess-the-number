"""

Guess the number!

The program will generate a random number between 1 and 9. +
The player has three tries to guess the random number. +

Expected behaviour:
- program should help the player with a message after each input, letting him know if he should go lower or upper.
- program should display error messages , if the player inserts something different than what he should.


"""
import random

random_number = random.randint(1, 9)
TRIES = 3
GUESSED = False
print("You have 3 tries to guess a random number between 1 and 9")
i = 1
while GUESSED == False and i < TRIES+1 :
    guess = input("Enter your guess:")
    if guess.isnumeric():
        guess = int(guess)
        if guess >= 1 and guess <= 9:
            guess = int(guess)
            if guess > random_number:
                if i < TRIES:
                    print("Try a smaller number!")
                else:
                    GUESSED = False
            elif guess < random_number:
                if i < TRIES:
                    print("Try a bigger number!")
                else:
                    GUESSED = False
            else:
                if i == 1:
                    print(f"Congratulations! You've guessed the number with {i} guess")
                    GUESSED = True
                else:
                    print(f"Congratulations! You've guessed the number with {i} guesses")
                    GUESSED = True
            i += 1
        elif guess < 1 or guess > 9:
            print("Already told you, only numbers between 1 and 9")
            i = TRIES + 1
    else:
        positiveGuess = guess.replace("-", "")
        if not positiveGuess.isnumeric():
            print("What part of number don't you get?!")
        else:
            print("Try a number in the given range")
        i = TRIES + 1
if not GUESSED:
    print("You did not guess the number. Better luck next time!")



