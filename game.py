import random

print('------------------------------')
print('        Guess Game')
print('------------------------------')

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

print('Guess how many M&Ms are in the jar')
print('The max number is 100.')
print('You have 5 chances')
print()
while attempts < attempt_limit:
    guess = int(input('What is your guess? '))
    if guess == mm_count:
        print('Great! You won!')
        break
    elif guess < mm_count:
        print('Too low')
    elif guess > mm_count:
        print('Too high')
    else:
        print('It is not a value between 1 and 100')
print('Bye!')

