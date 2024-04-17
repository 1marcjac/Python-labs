# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.
from pathlib import Path
import csv

# Define the directory to count files in, relative to this script's location
# Use an absolute path if preferred
directory_to_scan = Path(__file__).parent / 'C:\Users\1marc\OneDrive\Documents\'

# Define the CSV file path where results will be written
csv_file_path = Path(__file__).parent / "file_counts.csv"

# Function to count files
def count_files(directory):
    return sum(1 for _ in directory.rglob('*') if _.is_file())

# Count the files
file_count = count_files(directory_to_scan)

# Write the count to a CSV file
with csv_file_path.open(mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Directory', 'File Count'])
    csvwriter.writerow([str(directory_to_scan), file_count])

print(f"File count has been written to {csv_file_path}")
