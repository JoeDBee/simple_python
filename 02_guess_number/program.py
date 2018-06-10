import random

print('-----------------------------')
print('     Guess the number!       ')
print('-----------------------------\n')

number = random.randint(0, 100)
guess = -1

while guess != number:
    guess = int(input('Guess a number between 0 and 100: \n'))
    if guess < number:
        print('Your guess of {} is too low, try again\n'.format(guess))

    elif guess > number:
        print('Your guess of {} is too high, try again\n'.format(guess))

print('Correct!')
