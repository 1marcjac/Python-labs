# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path("/Users/1marc/Desktop")

# List all the files on there
for filepath in desktop.iterdir():
    print(filepath.name)
# Filter for screenshots only
    if filepath.suffix == '.jpg':  # Filter for screenshots only
    

# Create a new folder
        new_path = pathlib.Path('Users/1marc/Desktop/screenshots')
        new_path.mkdir(exist_ok=True)
        #create a new path for each file 
        new_filepath = new_path.joinpath(filepath.name)
# Move the screenshots in there
        filepath.replace(new_filepath)
