# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 3, 3, 3, 4, 3, 4, 5]


#initialize an empty list to store unique elements 
unique_list = []

#iterate through the original items in the list
for item in list_:
    #if the item is not in the unique list, add it
    if item not in unique_list:
        unique_list.append(item)

print("Method 2 - Unique List:", unique_list)