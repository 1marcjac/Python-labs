# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import os

def print_python_files(directory, prefix=""):
    """Recursively walks through a directory, printing out the names of any
    Python files it contains. Adds indentation to subdirectories for better readability.
    
    Args:
        directory: The directory to walk through.
        prefix: A string of spaces for indentation, indicating the depth of recursion.
    """
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            print(f"{prefix}{item}/")  # Print and format directory names
            print_python_files(path, prefix + "    ")  # Recurse into subdirectories with added indentation
        elif item.endswith('.py'):
            print(f"{prefix}{item}")  # Print and format Python file names

# Replace 'your_labs_folder_path_here' with the path to the folder you want to analyze
coding_nomads_folder_path = (r'C:\Users\1marc\Documents\CodingNomads\python-101-main\python-101-main')

print_python_files(coding_nomads_folder_path, '.py')



