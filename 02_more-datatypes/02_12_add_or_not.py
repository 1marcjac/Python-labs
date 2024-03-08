# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

#Initialize the game
points = 0 
unique_numbers = set()

while points >= -5:
    user_input = input('Lets play a game, enter a number: ')

    #Check if the number can be converted to an interger
    try: 
        number = int(user_input)
    except ValueError:
        print('Aht Aht, invalid input. Please enter a number.')
        continue

    #Add the number to the set and check for duplicates 
    if number in unique_numbers:
        points -= 1
        print("This is a duplicate number! for that, i'm taking a point.")
    else: 
        unique_numbers.add(number)
        points +=1
        print('Number added to set.')
    
    #Check if the user has won or lost
    if len(unique_numbers) >= 10:
        print('You a sweet, smart mutherfucer, you won!')
    elif points <= -5:
        print('you lost shorty! you ran out of points.')
        break
    else: 
        print(f'pints:{points}')

    print ('Final Set:',unique_numbers)