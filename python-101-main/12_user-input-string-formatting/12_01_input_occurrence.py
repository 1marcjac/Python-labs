# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
string = input('Hello, world ')
# Letter input: o
letter = input('o')

found = False  # set a variable, set it to not true until we found the letter
for i, char in enumerate(string): # use enumerate to get both the character and index through the string
    if char == letter:
        print(f'The first occurrence of the letter "{letter}" is at index: {i}')
        found = True
        break  # Exit the loop since we found the letter
if not found:
    print(f'The letter "{letter}" is not in the string.')


