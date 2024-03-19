# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random 

num = random.randint(1,15)
guess_attempts = 10 
guess = None

while guess != num & guess_attempts <=10 :
    guess = input('guess a number between 1 and 20 \n ')
    if guess == num: 
        print('Congratulations! ')
        break 
    else:
        guess_attempts = guess_attempts -1
        print (f'you have {guess_attempts} guesses remaining, try again buddy-o-pal\n')