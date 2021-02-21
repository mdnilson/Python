print('---------------------------------')
print('             GAME 2')
print('    Rock - Paper - Scissors')
print('---------------------------------')

player_1 = input('Player 1 - What is your name? ')
player_1 = player_1.capitalize()
player_2 = input('Player 2 - What is your name? ')
player_2 = player_2.capitalize()

print(f'Player 1 is {player_1} and Player 2 is {player_2}')
print()
print('The choice is: Rock, Paper, Scissors')
choice1 = input(f'{player_1}, what is your choice? ')
choice1 = choice1.capitalize()
choice2 = input(f'{player_2}, what is your choice? ')
choice2 = choice2.capitalize()
print(f'\n{player_1} is playing {choice1} and {player_2} is playing {choice2}')

