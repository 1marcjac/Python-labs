# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

#sort the numbers
sorted_randlist = sorted(randlist)

#store the tuples of two numbers into a new list 
tuples_list = []
for i in range(0, len(sorted_randlist), 2):
    if i + 1 < len (sorted_randlist):
    #create tuple with two consecutive numbers 
     pair_tuple = (sorted_randlist[i], sorted_randlist[i+1])
    tuples_list.append(pair_tuple)
else:
   pair_tuple = (sorted_randlist[i],0)
   tuples_list.append(pair_tuple)

#print each tuple 
for pair in tuples_list:
    print(pair)