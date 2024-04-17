import pathlib
from collections import Counter
from pprint import pprint

# Step 1: Define the path to your Desktop. Adjust this path as necessary.
desktop_path = pathlib.Path.home() / 'Desktop'

# Step 2: Create a Counter to hold the count of each file type.
file_type_counts = Counter()

# Step 3: Iterate over all files on the Desktop and update the counter based on file suffix.
for file_path in desktop_path.iterdir():
    if file_path.is_file():  # Make sure to count only files, not directories
        file_type_counts[file_path.suffix] += 1

# Step 4: Use pprint to print the file type counts nicely.
print("File type counts on your Desktop:")
pprint(dict(file_type_counts))
