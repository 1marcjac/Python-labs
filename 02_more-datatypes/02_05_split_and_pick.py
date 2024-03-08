# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

user_input = input('Enter a message, whats on your mind?: ' )
words = user_input.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else: 
        word_count[word] = 1

most_ocurring_word = max(word_count, key=word_count.get)

word_count[most_ocurring_word]

print(f'The word that occurs the most in your text is {most_ocurring_word} and it occurs {word_count[word]}')