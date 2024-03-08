# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

#initialize an empty dict for the combined set

combined_dict = {}

#iterate over thekeys of dict_1

for key in dict_1:
    #check if the key exists in dict_2
    if key in dict_2:
        combined_dict[key] = dict_1[key] + dict_2[key] 
    else: # if it doesn't, copy the key-value pair from dict 1 to combined dict
        combined_dict[key] = dict_1[key]


#iterate over dict 2
for key in dict_2:
    if key not in combined_dict:
        combined_dict[key] = dict_2[key]

print('The combined dictionary is as followed:', combined_dict)