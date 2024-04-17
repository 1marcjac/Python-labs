# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
import sys 
import pathlib 

file_in = open((r'C:\Users\1marc\OneDrive\Documents\CodingNomads\python-201-main/03_file-input-output/words.txt'))

contents = file_in.read()

# Assuming your file path is correct and 'words.txt' is properly located
file_path = pathlib.Path(r'C:\Users\1marc\OneDrive\Documents\CodingNomads\python-201-main/03_file-input-output/words.txt')

# Initialize variables to store the shortest and longest words and the total word count
shortest_words = []
longest_words = []
word_count = 0

min_length = float('inf')
max_length = 0 

with file_path.open('r') as file: 
    for line in file:
        words = line.split()
        for word in words:
            word_count +=1
            word_length = len(word)
            #Check for shortest wordd
            if word_length < min_length: 
                min_length == word_length
                shortest_words = [word]
            elif word_length == min_length:
                if word not in shortest_words:  # Avoid duplicates
                    shortest_words.append(word)
            # Check for longest word(s)
            if word_length > max_length:
                max_length = word_length
                longest_words = [word]
            elif word_length == max_length:
                if word not in longest_words:  # Avoid duplicates
                    longest_words.append(word)

# Print the results
print(f"Shortest word(s): {shortest_words}")
print(f"Longest word(s): {longest_words}")
print(f"Total number of words: {word_count}")