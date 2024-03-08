# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
# Request input from user

string = input('What label was bow wow on?: ')  # Ask the user a question
symbol = input('Enter a symbol: ')  # Prompt the user to enter a symbol
first_letter = string[0] # Identify the first letter to replace 

# Replace all occurrences of the first letter with the symbol
modified_string = string.replace(first_letter, symbol)

# Print the modified string
print(modified_string)
