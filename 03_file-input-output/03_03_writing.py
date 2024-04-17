# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

import pathlib 

input_file_path = pathlib.Path(r'C:\Users\1marc\OneDrive\Documents\CodingNomads\python-201-main/03_file-input-output/words.txt')
output_file_path = pathlib.Path('words_reversed.txt')

with input_file_path.open('r') as file: 
    lines = file.readlines()

#Reverse the order of lines 
lines_reversed = lines [::-1]

#Additionally reverse the content of each line 
lines_reversed = [line[::-1] for line in lines_reversed]

with output_file_path.open ('w') as file:
    file.writelines(lines_reversed)

    