# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

Favorite_things = [input("What are 3 things you cant live without?: \n" ), input(' \n'), input('\n')]

longest_string = max(Favorite_things, key=len)



print(f'The longest string is {longest_string}, its length is {len(longest_string)}')