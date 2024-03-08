# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

import os
from pathlib import Path
import shutil

def find_img_files(directory, max_depth=2, current_depth=0):
    img_files = []
    if current_depth > max_depth:  # Stop if the max depth is exceeded
        return img_files
    
    try:
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            if os.path.isdir(path):
                img_files += find_img_files(path, max_depth, current_depth + 1)
            elif item.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_files.append(path)
    except PermissionError as e:
        print(f"Permission denied: {e}")
    
    return img_files

# Usage
directory_to_search = r'C:\Users\1marc\Desktop'
img_files = find_img_files(directory_to_search)
print(f"Found {len(img_files)} image files.")

choice = input("Do you want to move these files to a folder? Y/N ")
if choice.upper() == 'Y':
    destination_path = Path(r'C:\Users\1marc\Desktop\screenshots')
    destination_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist
    for file_path in img_files:
        src_path = Path(file_path)
        dst_file_path = destination_path / src_path.name
        shutil.move(src_path, dst_file_path)  # Move the file
        print(f"Moved {src_path} to {dst_file_path}")
