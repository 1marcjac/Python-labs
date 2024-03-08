# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input('whats your name: ')

first_name = name.split()[0]  #Split the name by spaces and take the first part, this returns only the 1st name 

# Print a welcome message using only the first name
print(f'Welcome to the script, {first_name}!')


