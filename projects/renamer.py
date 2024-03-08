# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

from pathlib import Path
import shutil
from datetime import datetime

# Define the source directory (Desktop)
source_directory = Path(r'C:\Users\1marc\Desktop')

# Define the destination directory for the screenshots
destination_directory = source_directory / "Renamed_Screenshots"

# Ensure the destination directory exists
destination_directory.mkdir(exist_ok=True)

# Identify all .png files (screenshots) on the Desktop
png_files = list(source_directory.glob('*.png'))

# Move and rename all screenshots
for index, file_path in enumerate(png_files, start=1):
    # Define the new filename, e.g., "Screenshot_1.png", "Screenshot_2.png", etc.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"Screenshot_{index}_{timestamp}.png"
    
    # Define the new path for each file in the destination directory
    new_file_path = destination_directory / new_filename
    
    # Move and rename the screenshot
    shutil.move(str(file_path), str(new_file_path))
    print(f"Moved and renamed {file_path} to {new_file_path}")
