#practice
#Import the module 
import random 
import itertools
#Pick a random number between 1 and 10
number = random.randint(1,10)
#import counting functio
lucky_number = itertools.repeat(number,3)
#Initialize program - whats a your PCs favorite number? 
def program (): 
    for num in lucky_number:
        print(f'{num} is the lucky number for today')

program()