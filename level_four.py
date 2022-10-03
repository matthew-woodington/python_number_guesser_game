from level_one import user_playing
from level_three import computer_playing

player_choice = int(input('Choose to guess the computers number or pick a number for the computer to guess! Type "1" to guess and "2" to pick. '))

if player_choice == 1:
    user_playing()
elif player_choice == 2:
    computer_playing()
else:
    print('Please enter a valid response.')