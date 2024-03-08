# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"

tup1 = (string,)
print(tup1)

char_in_tup = tuple(string)

for char in char_in_tup:
    print(char)