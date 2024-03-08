# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]


list_ = [2, 2, 8, 8, 9, 'hey', 'wassup','hello', 19, 100]

unique_list = [item for item in list_ if list_.count(item) == 1] 
print(unique_list)