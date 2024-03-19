# Use Python's string mini-language to display the table
# that you've built before in a slightly better formatted manner:
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

# Loop through the numbers, creating a new row every 10 numbers
for i in range(0, 50, 10):  # Start from 0, end before 50, step by 10
    # Use an f-string to format each line: 
    # Each number is formatted to be right-aligned within a 3-character width.
    row = f"{i:2} {i+1:2} {i+2:2} {i+3:2} {i+4:2} {i+5:2} {i+6:2} {i+7:2} {i+8:2} {i+9:2}"
    print(row)
