import pathlib
from collections import Counter
from pprint import pprint

# Find the path to my Desktop - Corrected for OneDrive redirection
desktop = pathlib.Path(r"C:\Users\1marc\OneDrive\Desktop")

file_in = open('Desktop_cleaner.py', "r")
contents = file_in.read()

file_type_counts = Counter()

# Iterate over all files on the Desktop and update the counter based on file suffix.
for file_path in desktop.iterdir():
    if file_path.is_file():  # Ensure counting only files, not directories
        file_type_counts[file_path.suffix] += 1

# Print all file types counts on the Desktop
print("File type counts on your Desktop:")
pprint(dict(file_type_counts))

# Attempt to create a new folder for screenshots within the Desktop directory
new_path = desktop / "screenshots"
try:
    new_path.mkdir(exist_ok=True)
    print(f"'screenshots' directory created or already exists at: {new_path}")
except Exception as e:
    print(f"Error creating 'screenshots' directory: {e}")

# Filter for screenshots (both .jpg and .png) and move them
for filepath in desktop.iterdir():
    if filepath.suffix in ('.JPG', '.jpeg', '.png'):  # Adjusted to include JPEG
        print(f"Moving {filepath.name} to 'screenshots' directory...")
        new_filepath = new_path.joinpath(filepath.name)  # Define new path for each file
        try:
            filepath.replace(new_filepath)  # Move the screenshots into the new directory
            print(f"Moved {filepath.name}")
        except Exception as e:
            print(f"Error moving file {filepath.name}: {e}")
file_in.close()
