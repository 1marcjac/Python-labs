# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number = -1

# Use a while loop to repeatedly ask for a number until it's within the valid range
while number < 0 or number > 1000000000:
    # Ask the user for a number
    number = int(input('Please enter a number between 0 and 1,000,000,000: '))

    # Check if the number is within the valid range
    if 0 <= number <= 1000000000:
        print(f"The number you entered is: {number}")
        break  # Exit the loop since a valid number was found
    else:
        # If the number is not valid, print an error message and continue asking
        print("Error: The number is not within the valid range. Please try again.")
