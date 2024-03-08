# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

#Collect user input 
user_input = input('Whats your favorite vocabulary word?')

#Initialize an empty dictionary to store the character coutns 
char_count = {}

for char in user_input:
    #Check if the character is already in the dictionary
    if char in char_count:
        #if it is, add the count
        char_count[char] += 1
    else:
        #if its not, add it to the dictionary with a count of 1
        char_count[char] = 1 

print("Character count:", char_count)