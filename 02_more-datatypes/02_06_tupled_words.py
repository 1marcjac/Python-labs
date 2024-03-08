# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

def string_to_tuples(input_string):
    words = input_string.split()

    result_list = []

    for word in words: 
        result_list.append(tuple(word))
    
    return result_list

if __name__ == "__main__": 
    user_input = input("please enter a string: ")

    result_list = string_to_tuples("please enter a string:" )

    user_list = string_to_tuples(user_input)

    print("return list:", result_list)