# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"

flag = '.pdf'

filename = "operators.pdf"
flag = ".pdf"

# Assuming flag is always lowercase
flag_idx = 0

for char in filename.lower():
    if char == flag[flag_idx]:
        flag_idx += 1
        if flag_idx == len(flag):  # All characters in flag matched
            print('Yes, the filename is a pdf')
            break
    else:
        flag_idx = 0  # Reset index if any character does not match

if flag_idx != len(flag):
    print('No, the filename is not a pdf')
