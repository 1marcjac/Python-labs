
# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

# Brooklyn is the code word 
# Initialize the game
code_word = "Brooklyn"
guessed_word = ['_'] * len(code_word)  # Create a list of blanks
attempts_left = 10  # Set the number of allowed attempts
Hint = 'If you know me, tell me the hometown of my favorite rapper?'
# Explain the game to the user
print("Welcome to Hip Hop Hangman!")
print("Try to guess the word letter by letter.")

# Function to display the current state of the word
def display_word():
    print(' '.join(guessed_word))

# Main game loop
while attempts_left > 0 and '_' in guessed_word:
    print (Hint)
    display_word()
    guess = input("Guess a letter: ").lower()
    
    # Validate the input
    if not guess.isalpha() or len(guess) != 1:
        print("aht aht, please enter a single alphabetic character.")
        continue
    
    # Check if the guess is in the code_word
    if guess in code_word.lower():
        print("Correct guess!")
        # Reveal the guessed letters in the guessed_word
        for i, letter in enumerate(code_word.lower()):
            if letter == guess:
                guessed_word[i] = code_word[i]
    else:
        print("Incorrect guess. Try again!")
        attempts_left -= 1  # Reduce the number of attempts left
    
    # Check win condition
    if '_' not in guessed_word:
        print("Congratulations! You've guessed the word:", code_word)
        break

# Check lose condition
if attempts_left == 0:
    print("You've run out of attempts! The word was:", code_word)