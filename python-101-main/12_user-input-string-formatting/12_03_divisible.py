# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

user_value = input('Give me a number, i will tell you if it can be sliced 3 ways evenly: ')

number = int (user_value) # random number betwen 1 and 1M


if 1 <= number <= 1000000000:
    if number % 3 == 0:
        print (f'{number} is divisible by 3')
    else: 
        print (f'{number} is not divisible by 3')
else: print(f'this number is not allowed in the range 1 to 1 million ')