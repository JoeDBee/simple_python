import random

print('-----------------------------')
print('     Guess the number!       ')
print('-----------------------------\n')

number = random.randint(0, 100)
guess = int(input('Guess a number between 0 and 100: \n'))

while guess != number:
    if guess < number:
        print('too low')
        guess = int(input('Guess again: \n'))
    elif guess > number:
        print('too high')
        guess = int(input('Guess again: \n'))

print('Correct!')
