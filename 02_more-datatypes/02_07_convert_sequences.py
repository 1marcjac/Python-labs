# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

#Convert the string to a tuple 

tuple_from_string = tuple(string)
print("tuple from string: ", tuple_from_string)

#Convert the tuple to a list 
list_from_tuple = list(tuple_from_string)

#change the 'c' character in thel ist to 'k' 
list_from_tuple[list_from_tuple.index('c')] = 'k'
print("List with 'c' changed to 'k': ", list_from_tuple)