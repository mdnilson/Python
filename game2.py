import random


def welcome_message():
    print('---------------------------------')
    print('             GAME 2')
    print('    Rock - Paper - Scissors')
    print('---------------------------------')
    return


welcome_message()

game_choice = ['Rock', 'Paper', 'Scissors']
player_1 = 'Computer'
print('Player 1 is a computer')
player_2 = input('Player 2 - What is your name? ')
player_2 = player_2.capitalize()

print()
print('The choice is: Rock, Paper, Scissors')
choice1 = random.choice(game_choice)

choice2 = None
while choice2 not in game_choice:
    choice2 = input(f'{player_2}, what is your choice? ')
    choice2 = choice2.capitalize().strip()
    if choice2 not in game_choice:
        print(f'Dear {player_2}, {choice2} is not a valid choice')
        continue


print(f'\n{player_1.capitalize()} is playing {choice1} and {player_2} is playing {choice2}')

winner = None

if choice1 == choice2:
    print('There is a draw!')
elif choice1 == 'Rock':
    if choice2 == 'Paper':
        winner = player_2
    elif choice2 == 'Scissors':
        winner = player_1
elif choice1 == 'Paper':
    if choice2 == 'Rock':
        winner = player_1
    elif choice2 == 'Scissors':
        winner = player_2
elif choice1 == 'Scissors':
    if choice2 == 'Paper':
        winner = player_1
    elif choice2 == 'Rock':
        winner = player_2

print(f'The winner is {winner}!')
print('bye!')
