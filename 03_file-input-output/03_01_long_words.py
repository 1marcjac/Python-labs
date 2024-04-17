# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
# Define a function to read words and print those with more than 20 characters
def print_long_words(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip leading and trailing whitespace from the line
            line = line.strip()
            # If the word has more than 20 characters, print it
            if len(line) > 20:
                print(line)

# Call the function with the filename 'words.txt'
print_long_words(r'C:\Users\1marc\OneDrive\Documents\CodingNomads\python-201-main/03_file-input-output/words.txt')
