# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib

# Find the path to my Desktop

# Create a new folder

# Filter for screenshots only

# Create a new path for each file

# Move the screenshot there

from pathlib import Path
import shutil

def move_files(source_directory, destination_directory, file_extensions):
    """
    Moves files from source to destination directory based on specified extensions.
    
    Parameters:
        source_directory (Path): The source directory Path object.
        destination_directory (Path): The destination directory Path object.
        file_extensions (list): A list of file extensions to move.
    """
    # Ensure the destination directory exists
    destination_directory.mkdir(exist_ok=True)

    # Find all files in the source directory with the specified extensions
    files_to_move = []
    for extension in file_extensions:
        files_to_move.extend(source_directory.glob(f'*{extension}'))

    # Print the files found and ask the user if they want to move them
    if files_to_move:
        print(f"Found {len(files_to_move)} files to move:")
        for file_path in files_to_move:
            print(file_path)
        
        choice = input("Do you want to move these files? (Y/N) ").upper()
        if choice == 'Y':
            for file_path in files_to_move:
                destination_path = destination_directory / file_path.name
                shutil.move(str(file_path), str(destination_path))
                print(f"Moved {file_path} to {destination_path}")
        else:
            print("Files were not moved.")
    else:
        print("No files found to move.")

# Define the source and destination directories
source_directory = Path(r'C:\Users\1marc\Desktop')
destination_directory = Path(r'C:\Users\1marc\Desktop\screenshots')

# List of file extensions to move
file_extensions = ['.png', '.PNG', '.jpg', '.JPG']

# Call the move_files function
move_files(source_directory, destination_directory, file_extensions)

# Developer Note:
"""
The move_files function is designed for flexible file management within a file system,
allowing for the automated movement of files based on their extension from one directory to another.
This function can be easily adapted for different use cases by altering the source_directory,
destination_directory, and file_extensions parameters.

Usage:
- source_directory: Specify the Path object of the directory from which files will be moved.
- destination_directory: Specify the Path object of the target directory to which files will be moved.
- file_extensions: Provide a list of string extensions for the types of files you want to move.
  This list can include any file type and is not case-sensitive.

The function first checks for the existence of the destination directory, creating it if necessary.
It then searches the source directory for files matching the specified extensions, lists them,
and prompts the user for confirmation before moving the files. This approach ensures that file
movements are both intentional and verified, reducing the risk of accidental data manipulation.
"""
