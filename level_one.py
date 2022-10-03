from random import randint

number = randint(1, 10)

guesses = 0

possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while guesses < 3:
    prompt = input('Guess a number between 1 and 10! ')
    guess = int(prompt)

    if guess not in possible_numbers:
        print('Please enter a valid number.')
        continue

    guesses = guesses + 1

    if guess == number:
        break
    elif guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high')

if guess == number:
    print('You guessed it!')
elif guess != number:
    print('Try again next time!')