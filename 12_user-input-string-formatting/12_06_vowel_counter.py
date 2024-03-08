# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.


string = input('Whats your favorite animal?: ') 

vowel = 'aeiouy'

vowel_counter = {v: 0 for v in vowel},

vowel_counter = 0

for char in string.lower():
    if char in vowel:
        vowel_counter +=1

print(vowel_counter)