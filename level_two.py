from random import randint
import time

prompt = input("Pick a number between 1 and 10 for the computer to guess. ")
number = int(prompt)

guesses = 0

while guesses < 3:
    computer_guess = randint(1, 10)
    print('Computer guesses', computer_guess)

    guesses = guesses + 1

    if computer_guess == number:
        break
    elif computer_guess < number:
        print('Too low!')
    elif computer_guess > number:
        print('Too high!')

    time.sleep(1)

if computer_guess == number:
    print('The computer guessed your number!')
elif computer_guess != number:
    print('You stumped the computer!')